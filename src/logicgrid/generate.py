"""Puzzle generation.

The loop is deliberately boring, because the interesting property -- that the
puzzle has exactly one solution and is solvable by hand -- is *verified* rather
than argued for:

1. invent a random solution;
2. enumerate a pool of clue atoms that are **all true of that solution**, so the
   clue set can never be self-contradictory no matter what we pick;
3. keep adding atoms until the uniqueness oracle says exactly one solution;
4. repeatedly try to drop each atom, keeping only those whose removal would
   lose uniqueness -- so every surviving clue is load-bearing;
5. solve it the way a person would, and measure the difficulty that falls out;
6. if that misses the requested band, throw the whole thing away and retry.

Step 4 is what separates a pleasant puzzle from a slog: a grown-but-unminimised
clue set is typically twice the size it needs to be and full of clues that do
nothing.

Everything is driven from one integer seed, so ``generate(spec)`` with the same
spec always returns byte-identical output.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, replace
from itertools import combinations, permutations
from random import Random
from typing import Iterable, Mapping, Sequence

from .clues import (
    ALL_KINDS,
    TIER_C_KINDS,
    Adjacent,
    Arith,
    Atom,
    Before,
    Between,
    Distinct,
    Gap,
    IfThen,
    ImmediatelyBefore,
    Link,
    Not,
    NotBoth,
    NotLink,
    Or,
    Parity,
    atom_from_json,
    is_trivial,
    make_not,
)
from .csp import Engine, flatten, is_unique
from .difficulty import Profile, clue_stats, profile as get_profile, ramp_sequence, rate
from .human_solver import SolveReport, human_solve
from .model import Clue, PuzzleError, Ref, Schema, Solution
from .themes import THEMES, Theme, theme as get_theme, themes_for

#: Sentinel for "inherit from the profile" on an int override.
INHERIT = -1


@dataclass(frozen=True, slots=True)
class PuzzleSpec:
    """What to generate. Anything left ``None`` is taken from the profile.

    ``seed`` alone determines the result: same spec, same puzzle, always.
    """

    difficulty: str = "moderate"
    seed: int = 0
    categories: int | None = None
    items: int | None = None
    theme: str | None = None
    kinds: tuple[str, ...] | None = None
    max_positive: int = INHERIT
    allow_trial: bool | None = None
    max_bundle: int | None = None
    subset_size: int | None = None
    #: Reject puzzles whose measured rating misses the profile's band.
    strict_band: bool = True
    max_attempts: int = 80

    def resolved(self) -> Profile:
        prof = get_profile(self.difficulty)
        changes: dict = {}
        if self.kinds is not None:
            unknown = set(self.kinds) - set(ALL_KINDS)
            if unknown:
                raise PuzzleError(f"unknown clue kinds: {sorted(unknown)}")
            changes["kinds"] = tuple(self.kinds)
        if self.max_positive != INHERIT:
            changes["max_positive"] = self.max_positive
        if self.allow_trial is not None:
            changes["allow_trial"] = self.allow_trial
        if self.max_bundle is not None:
            changes["max_bundle"] = self.max_bundle
        if self.subset_size is not None:
            changes["subset_size"] = self.subset_size
        if self.categories is not None or self.items is not None:
            shapes = []
            for c, i in prof.shapes:
                shapes.append((self.categories or c, self.items or i))
            changes["shapes"] = tuple(dict.fromkeys(shapes))
        return replace(prof, **changes) if changes else prof

    def to_json(self) -> dict:
        return {
            "difficulty": self.difficulty,
            "seed": self.seed,
            **({"categories": self.categories} if self.categories else {}),
            **({"items": self.items} if self.items else {}),
            **({"theme": self.theme} if self.theme else {}),
            **({"kinds": list(self.kinds)} if self.kinds else {}),
            **({"max_positive": self.max_positive} if self.max_positive != INHERIT else {}),
        }


@dataclass(slots=True)
class Puzzle:
    """A finished puzzle: schema, clues, solution and provenance."""

    pid: str
    title: str
    theme: str
    blurb: str
    schema: Schema
    solution: Solution
    clues: tuple[Clue, ...]
    profile: str
    score: float
    rating: int
    seed: int
    spec: dict = field(default_factory=dict)
    report: SolveReport | None = None
    attempts: int = 1

    def atoms(self) -> tuple[Atom, ...]:
        return flatten(self.clues)

    @property
    def size(self) -> int:
        return self.schema.size

    def verify(self) -> None:
        """Re-prove the two properties that matter. Raises on failure."""
        atoms = self.atoms()
        for atom in atoms:
            atom.validate(self.schema)
            if not atom.holds(self.solution):
                raise PuzzleError(f"clue is false for the stated solution: {atom!r}")
        engine = Engine(self.schema, atoms)
        count, sol = engine.count_solutions(limit=2)
        if count != 1:
            raise PuzzleError(f"puzzle has {count} solutions, expected exactly 1")
        if sol != self.solution:
            raise PuzzleError("unique solution does not match the recorded solution")

    def stats(self) -> dict:
        return clue_stats(self.schema, self.clues)

    def to_json(self) -> dict:
        return {
            "pid": self.pid,
            "title": self.title,
            "theme": self.theme,
            "blurb": self.blurb,
            "profile": self.profile,
            "rating": self.rating,
            "score": self.score,
            "seed": self.seed,
            "spec": self.spec,
            "schema": self.schema.to_json(),
            "clues": [
                {"style": c.style, "atoms": [a.to_json() for a in c.atoms]}
                for c in self.clues
            ],
            "solution": self.solution.to_json(),
            "stats": self.stats(),
            "solve": self.report.to_json() if self.report else None,
        }

    @classmethod
    def from_json(cls, data: Mapping) -> "Puzzle":
        schema = Schema.from_json(data["schema"])
        clues = tuple(
            Clue(tuple(atom_from_json(a) for a in c["atoms"]), c.get("style", "sentences"))
            for c in data["clues"]
        )
        return cls(
            pid=data["pid"],
            title=data["title"],
            theme=data["theme"],
            blurb=data.get("blurb", ""),
            schema=schema,
            solution=Solution(schema, data["solution"]),
            clues=clues,
            profile=data.get("profile", ""),
            score=float(data.get("score", 0.0)),
            rating=int(data.get("rating", 0)),
            seed=int(data.get("seed", 0)),
            spec=dict(data.get("spec", {})),
        )


# ---------------------------------------------------------------------------
# solution + pool
# ---------------------------------------------------------------------------


def random_solution(schema: Schema, rng: Random) -> Solution:
    """A uniformly random solution (the spine row is fixed by construction)."""
    table: dict[str, list[str]] = {schema.spine_name: list(schema.spine.items)}
    for cat in schema.other_categories():
        row = list(cat.items)
        rng.shuffle(row)
        table[cat.name] = row
    return Solution(schema, table)


def _pairs(schema: Schema) -> list[tuple[Ref, Ref]]:
    """Every ref pair drawn from two different categories."""
    out = []
    cats = schema.categories
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            for a in cats[i].refs():
                for b in cats[j].refs():
                    out.append((a, b))
    return out


def _cap(items: list, limit: int, rng: Random) -> list:
    if len(items) <= limit:
        return items
    return rng.sample(items, limit)


def build_pool(
    schema: Schema,
    solution: Solution,
    prof: Profile,
    rng: Random,
    *,
    allow_gap: bool = True,
    allow_parity: bool = True,
) -> dict[str, list[Atom]]:
    """All non-trivial atoms of the allowed kinds that are TRUE of ``solution``.

    Generating only true atoms is what makes the clue set unconditionally
    consistent: any subset of a set of true statements is still satisfied by the
    solution we started from, so the only question left for the oracle is
    whether that subset pins the solution *uniquely*.
    """
    kinds = set(prof.kinds)
    if not schema.ordered:
        kinds -= {
            "before", "immediately_before", "adjacent", "between", "gap",
            "parity", "arith",
        }
    if not allow_gap:
        kinds.discard("gap")
    if not allow_parity:
        kinds.discard("parity")
    if not schema.numeric:
        kinds.discard("arith")

    pos = solution.position
    pool: dict[str, list[Atom]] = {}
    pairs = _pairs(schema)
    size = schema.size
    budget = 24 * size

    def add(kind: str, atoms: Iterable[Atom]) -> None:
        kept = []
        seen = set()
        for atom in atoms:
            if atom in seen or is_trivial(atom, schema):
                continue
            if not atom.holds(solution):
                continue
            seen.add(atom)
            kept.append(atom)
        if kept:
            pool[kind] = _cap(kept, budget, rng)

    if "link" in kinds:
        add("link", (Link(a, b) for a, b in pairs))
    if "not_link" in kinds:
        add("not_link", (NotLink(a, b) for a, b in pairs))
    ordered_pairs = [(x, y) for a, b in pairs for x, y in ((a, b), (b, a))]
    if "before" in kinds:
        add("before", (Before(x, y) for x, y in ordered_pairs))
    if "immediately_before" in kinds:
        add("immediately_before", (ImmediatelyBefore(x, y) for x, y in ordered_pairs))
    if "adjacent" in kinds:
        add("adjacent", (Adjacent(a, b) for a, b in pairs))
    if "gap" in kinds:
        add(
            "gap",
            (
                Gap(a, b, k, "eq")
                for a, b in pairs
                for k in range(2, size)
            ),
        )
    if "parity" in kinds:
        add("parity", (Parity(a, b, same) for a, b in pairs for same in (True, False)))
    if "arith" in kinds and schema.numeric:
        vals = schema.spine.values or ()
        steps = sorted({abs(x - y) for x in vals for y in vals if x != y})
        factors = sorted({2, 3} | {
            round(x / y, 6) for x in vals for y in vals if y and (x / y).is_integer()
        })
        add(
            "arith",
            [Arith(a, b, k, "add") for a, b in pairs for k in steps]
            + [Arith(a, b, float(k), "mul") for a, b in pairs for k in factors if k > 1],
        )
    if "between" in kinds:
        triples = []
        all_refs = list(schema.all_refs)
        for a in all_refs:
            others = [r for r in all_refs if r.cat != a.cat]
            for b, c in combinations(others, 2):
                if b.cat == c.cat and b.item == c.item:
                    continue
                triples.append(Between(a, b, c))
        add("between", triples)
    if "distinct" in kinds:
        groups = []
        all_refs = list(schema.all_refs)
        for combo in combinations(all_refs, 3):
            if len({r.cat for r in combo}) < 2:
                continue
            groups.append(Distinct(combo))
        rng.shuffle(groups)
        add("distinct", groups[: budget * 2])

    # -- compound clues, built from the simple pool ----------------------
    simple = [a for k, lst in pool.items() if k in ("link", "not_link") for a in lst]
    simple += [
        a
        for k in ("before", "adjacent", "immediately_before", "gap", "parity")
        for a in pool.get(k, ())
    ]
    # False counterparts, needed for disjunctions to carry information.
    false_atoms: list[Atom] = []
    for a, b in pairs:
        if pos(a) != pos(b):
            false_atoms.append(Link(a, b))
        else:
            false_atoms.append(NotLink(a, b))
    if schema.ordered:
        for a, b in pairs:
            if pos(a) >= pos(b):
                false_atoms.append(Before(a, b))
            if abs(pos(a) - pos(b)) != 1:
                false_atoms.append(Adjacent(a, b))
    false_atoms = [a for a in false_atoms if not is_trivial(a, schema)]
    rng.shuffle(false_atoms)
    rng.shuffle(simple)

    def refs_ok(*atoms: Atom) -> bool:
        seen: set[Ref] = set()
        for at in atoms:
            seen |= set(at.refs())
        return len(seen) <= 4

    if "not" in kinds:
        add("not", [make_not(a) for a in false_atoms[: budget * 2]])
    if "or" in kinds:
        # Exactly one true disjunct: the clue tells you "one of these two", and
        # the solver must refute the other.
        cands = []
        for t in simple[: budget * 2]:
            negation = make_not(t)
            for f in false_atoms[:40]:
                # "X or not-X" is a tautology carrying no information.  The
                # minimiser would drop it anyway, but skipping it here keeps the
                # pool honest and the search cheaper.
                if t != f and f != negation and refs_ok(t, f):
                    cands.append(Or((t, f)))
        rng.shuffle(cands)
        add("or", cands[: budget * 2])
    if "not_both" in kinds:
        cands = []
        for f1, f2 in combinations(false_atoms[:60], 2):
            if refs_ok(f1, f2):
                cands.append(NotBoth(f1, f2))
        for t in simple[:40]:
            for f in false_atoms[:40]:
                if refs_ok(t, f):
                    cands.append(NotBoth(t, f))
        rng.shuffle(cands)
        add("not_both", cands[: budget * 2])
    if "if_then" in kinds:
        cands = []
        for x in false_atoms[:60]:
            for y in false_atoms[:60]:
                if x != y and refs_ok(x, y):
                    cands.append(IfThen(x, y))
        for x in simple[:40]:
            for y in simple[:40]:
                if x != y and refs_ok(x, y):
                    cands.append(IfThen(x, y))
        rng.shuffle(cands)
        add("if_then", cands[: budget * 2])

    return {k: v for k, v in pool.items() if v}


def weighted_order(pool: Mapping[str, Sequence[Atom]], prof: Profile, rng: Random) -> list[Atom]:
    """Interleave the per-kind pools according to the profile's weights."""
    buckets = {k: list(v) for k, v in pool.items() if v}
    for lst in buckets.values():
        rng.shuffle(lst)
    out: list[Atom] = []
    while buckets:
        kinds = list(buckets)
        weights = [max(prof.weight(k), 1e-6) for k in kinds]
        kind = rng.choices(kinds, weights=weights, k=1)[0]
        out.append(buckets[kind].pop())
        if not buckets[kind]:
            del buckets[kind]
    return out


# ---------------------------------------------------------------------------
# grow / minimise / bundle
# ---------------------------------------------------------------------------


def grow(
    schema: Schema,
    pool: Mapping[str, Sequence[Atom]],
    prof: Profile,
    rng: Random,
    *,
    batch: int = 2,
) -> list[Atom] | None:
    """Add atoms until the clue set has exactly one solution."""
    order = weighted_order(pool, prof, rng)
    chosen: list[Atom] = []
    positives = 0
    floor = max(3, (len(schema.categories) - 1) * schema.size // 3)
    for atom in order:
        if atom.is_positive_link() and prof.max_positive is not None:
            if positives >= prof.max_positive:
                continue
        chosen.append(atom)
        if atom.is_positive_link():
            positives += 1
        if len(chosen) >= floor and len(chosen) % batch == 0:
            if is_unique(schema, chosen):
                return chosen
    return chosen if is_unique(schema, chosen) else None


def minimize(schema: Schema, atoms: Sequence[Atom], rng: Random, max_passes: int = 6) -> list[Atom]:
    """Drop every atom whose removal keeps the solution unique.

    Repeated shuffled passes, because minimality is order-dependent: the result
    is a *locally* minimal set, which is what hand-written puzzles are too.
    """
    current = list(atoms)
    for _ in range(max_passes):
        order = list(range(len(current)))
        rng.shuffle(order)
        dropped = False
        for idx in order:
            if idx >= len(current):
                continue
            trial = current[:idx] + current[idx + 1 :]
            if not trial:
                continue
            if is_unique(schema, trial):
                current = trial
                dropped = True
        if not dropped:
            break
    return current


def _style_for(group: Sequence[Atom]) -> str:
    if len(group) == 1:
        return "sentences"
    kinds = [a.kind for a in group]
    if len(group) == 2 and "link" in kinds and "not_link" in kinds:
        return "but_not"
    if all(k == "not_link" for k in kinds):
        return "and"
    return "sentences"


def bundle(
    atoms: Sequence[Atom],
    schema: Schema,
    prof: Profile,
    rng: Random,
) -> tuple[Clue, ...]:
    """Group atoms into numbered clues that share a subject.

    Purely presentational -- the logical content is the flat union -- but it is
    what makes a clue list read like Penny Dell rather than like a constraint
    dump.  "Anne was married on Monday, but not to Wally" is one clue carrying
    two facts, and that is the house style.
    """
    remaining = list(atoms)
    rng.shuffle(remaining)
    clues: list[Clue] = []
    while remaining:
        head = remaining.pop()
        group = [head]
        # A compound clue stands alone. Either/or and if-then clauses already
        # carry labelled sub-parts, so bundling anything beside them produces a
        # paragraph the solver has to parse twice -- printed puzzles give them
        # their own number, and so do we.
        compound = head.kind in TIER_C_KINDS
        if prof.max_bundle > 1 and not compound and rng.random() < 0.55:
            shared = set(head.refs())
            for other in list(remaining):
                if len(group) >= prof.max_bundle:
                    break
                if other.kind in TIER_C_KINDS:
                    continue
                if set(other.refs()) & shared:
                    group.append(other)
                    remaining.remove(other)
                    shared |= set(other.refs())
        clues.append(Clue(tuple(group), _style_for(group)))

    # A gentle bias towards opening with concrete anchors, as printed puzzles do.
    def anchor_score(clue: Clue) -> tuple:
        spine_refs = sum(
            1 for a in clue.atoms for r in a.refs() if schema.is_spine(r)
        )
        has_link = any(a.is_positive_link() for a in clue.atoms)
        return (-int(has_link), -spine_refs, rng.random())

    clues.sort(key=anchor_score)
    return tuple(clues)


# ---------------------------------------------------------------------------
# the generator
# ---------------------------------------------------------------------------


def _pid(spec: PuzzleSpec, schema: Schema, solution: Solution) -> str:
    blob = json.dumps(
        {"s": spec.to_json(), "k": schema.to_json(), "v": solution.to_json()},
        sort_keys=True,
    )
    return hashlib.sha256(blob.encode()).hexdigest()[:12]


def _choose_theme(spec: PuzzleSpec, prof: Profile, cats: int, items: int, rng: Random) -> Theme:
    if spec.theme:
        th = get_theme(spec.theme)
        if th.max_categories() < cats or th.max_items() < items:
            raise PuzzleError(
                f"theme {spec.theme!r} cannot supply {cats} categories x {items} items"
            )
        return th
    needs_numeric = "arith" in prof.kinds
    options = themes_for(cats, items)
    if needs_numeric:
        numeric = [t for t in options if t.spine.values is not None]
        if numeric and rng.random() < 0.45:
            options = numeric
    if not options:
        raise PuzzleError(f"no theme supports {cats} categories x {items} items")
    return rng.choice(options)


def attempt_once(
    spec: PuzzleSpec, prof: Profile, rng: Random, attempt: int = 0
) -> Puzzle | None:
    """One full generate-grow-minimise-rate cycle. ``None`` if it came out unusable.

    Exposed separately so that calibration can sample the *natural* score
    distribution of a profile without the band filter rejecting most of it.
    """
    cats, items = rng.choice(prof.shapes)
    try:
        theme = _choose_theme(spec, prof, cats, items, rng)
    except PuzzleError:
        return None
    schema = theme.build(cats, items, rng)
    solution = random_solution(schema, rng)
    pool = build_pool(
        schema,
        solution,
        prof,
        rng,
        allow_gap=theme.spine.allow_gap,
        allow_parity=theme.spine.allow_parity,
    )
    if not pool:
        return None
    grown = grow(schema, pool, prof, rng)
    if grown is None:
        return None
    atoms = minimize(schema, grown, rng)
    if len(atoms) < 3:
        return None
    report = human_solve(
        schema,
        atoms,
        allow_trial=prof.allow_trial,
        subset_size=prof.subset_size,
    )
    if not report.solved:
        # Solvable by search but not by our technique ladder: too hard to be
        # fair, so discard it rather than ship a puzzle nobody can finish.
        return None
    score, rating = rate(schema, atoms, report)
    clues = bundle(atoms, schema, prof, rng)
    return Puzzle(
        pid=_pid(spec, schema, solution),
        title=theme.title,
        theme=theme.slug,
        blurb=theme.blurb,
        schema=schema,
        solution=solution,
        clues=clues,
        profile=prof.name,
        score=score,
        rating=rating,
        seed=spec.seed,
        spec=spec.to_json(),
        report=report,
        attempts=attempt + 1,
    )


def generate(spec: PuzzleSpec | None = None, **kwargs) -> Puzzle:
    """Generate one puzzle. Deterministic in ``spec.seed``.

    Retries until the *measured* rating lands in the profile's band, then
    re-proves uniqueness before returning.  If no attempt lands in band, the
    closest near-miss is returned (and still verified).
    """
    if spec is None:
        spec = PuzzleSpec(**kwargs)
    elif kwargs:
        spec = replace(spec, **kwargs)
    prof = spec.resolved()
    rng = Random(spec.seed)
    best: Puzzle | None = None
    best_miss = 10**9
    lo, hi = prof.band

    for attempt in range(spec.max_attempts):
        puzzle = attempt_once(spec, prof, rng, attempt)
        if puzzle is None:
            continue
        if lo <= puzzle.rating <= hi:
            puzzle.verify()
            return puzzle
        miss = lo - puzzle.rating if puzzle.rating < lo else puzzle.rating - hi
        if miss < best_miss:
            best, best_miss = puzzle, miss

    if best is None:
        raise PuzzleError(
            f"could not generate a puzzle for {spec!r} in {spec.max_attempts} attempts"
        )
    if spec.strict_band and best_miss > 1:
        raise PuzzleError(
            f"closest puzzle for {spec.difficulty!r} rated {best.rating}, "
            f"outside band {prof.band} by {best_miss}"
        )
    best.verify()
    return best


def generate_many(
    count: int = 50,
    seed: int = 0,
    curve: Sequence[str] | None = None,
    difficulty: str | None = None,
    **kwargs,
) -> list[Puzzle]:
    """Generate ``count`` puzzles, by default along the built-in ramp.

    Themes are spread so that consecutive puzzles differ, and each puzzle gets
    its own derived seed so that regenerating any single one is cheap.
    """
    if curve is None:
        names = [difficulty] * count if difficulty else ramp_sequence(count)
    else:
        names = list(curve)[:count]
        while len(names) < count:
            names.append(names[-1])

    out: list[Puzzle] = []
    used_recent: list[str] = []
    for i, name in enumerate(names):
        sub = seed * 100003 + i * 7919 + 1
        for bump in range(24):
            spec = PuzzleSpec(difficulty=name, seed=sub + bump * 104729, **kwargs)
            puzzle = generate(spec)
            if puzzle.theme not in used_recent[-4:]:
                break
        out.append(puzzle)
        used_recent.append(puzzle.theme)
    return out
