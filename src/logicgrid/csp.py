"""Constraint propagation and the uniqueness oracle.

Because the spine fixes the puzzle's indexing, every unknown in the grid has the
same shape: "which spine position does this item belong to?"  So a partial state
is just a map ``Ref -> set[int]`` of candidate positions, and a solved state is
one where every set is a singleton.  Spine items are singletons from the start.

Propagation has two ingredients:

* **Generalised arc consistency** per atom.  Each atom declares its refs and can
  test one candidate tuple, so we can brute-force the (tiny) product of its
  refs' domains and keep only values that take part in some supported tuple.
  Atoms never need bespoke propagators, which is what keeps the clue IR cheap to
  extend.
* **Bijection reasoning** per category: an item with one candidate position
  claims it, and a position wanted by only one item is claimed by it.

The search on top is plain DFS over the smallest remaining domain.  The oracle
counts solutions but stops at ``limit``, because the only question generation
ever asks is "is this exactly one?".
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations, product
from typing import Iterable, Iterator, Mapping, Sequence

from .clues import Atom, Link, NotLink
from .model import Ref, Schema, Solution

# Technique tiers (the human-solving ladder).
T_DIRECT = 1       # a clue naming a cell, propagated through equalities
T_BIJECTION = 2    # one-per-row / one-per-column within a category
T_ORDER = 3        # positional and arithmetic reasoning
T_DISJUNCTION = 4  # resolving either/or, not-both and if-then clues
T_SUBSET = 5       # naked and hidden pairs/triples
T_TRIAL = 6        # assume-and-refute (trial and error)

TIER_NAMES = {
    T_DIRECT: "direct",
    T_BIJECTION: "bijection",
    T_ORDER: "order",
    T_DISJUNCTION: "disjunction",
    T_SUBSET: "subset",
    T_TRIAL: "trial",
}

ALL_TIERS = frozenset(TIER_NAMES)

#: Tiers the uniqueness oracle propagates with.  Subset reasoning is deliberately
#: left out: it can only re-derive what the search already covers, so for a
#: complete solution count it is pure overhead.
ORACLE_TIERS = frozenset({T_DIRECT, T_BIJECTION, T_ORDER, T_DISJUNCTION})


class Contradiction(Exception):
    """Raised internally when a domain empties."""


@dataclass(slots=True)
class Step:
    """One recorded deduction, for explanations and difficulty rating."""

    tier: int
    technique: str
    ref: Ref | None
    removed: tuple[int, ...]
    clue: int | None = None

    def describe(self, schema: Schema) -> str:
        where = self.ref.key if self.ref else "-"
        src = f" from clue {self.clue + 1}" if self.clue is not None else ""
        vals = ",".join(str(v + 1) for v in self.removed)
        return f"[{self.technique}]{src} {where}: ruled out position(s) {vals}"


class Grid:
    """Mutable candidate-position state for every ref in the puzzle."""

    __slots__ = ("schema", "dom", "_cats")

    def __init__(self, schema: Schema, dom: dict[Ref, set[int]] | None = None) -> None:
        self.schema = schema
        if dom is not None:
            self.dom = dom
        else:
            positions = set(schema.positions)
            self.dom = {}
            for cat in schema.categories:
                for ref in cat.refs():
                    if schema.is_spine(ref):
                        self.dom[ref] = {schema.spine_position(ref)}
                    else:
                        self.dom[ref] = set(positions)
        self._cats = schema.categories

    def copy(self) -> "Grid":
        return Grid(self.schema, {r: set(v) for r, v in self.dom.items()})

    # -- state queries ---------------------------------------------------
    @property
    def solved(self) -> bool:
        return all(len(v) == 1 for v in self.dom.values())

    @property
    def broken(self) -> bool:
        return any(not v for v in self.dom.values())

    def remaining(self) -> int:
        """Total candidates still open -- a progress measure."""
        return sum(len(v) for v in self.dom.values())

    def open_refs(self) -> list[Ref]:
        return [r for r, v in self.dom.items() if len(v) > 1]

    def to_solution(self) -> Solution:
        if not self.solved:
            raise ValueError("grid is not fully determined")
        table: dict[str, list[str]] = {
            c.name: [""] * self.schema.size for c in self._cats
        }
        for ref, vals in self.dom.items():
            table[ref.cat][next(iter(vals))] = ref.item
        return Solution(self.schema, table)

    def assign(self, ref: Ref, value: int) -> None:
        self.dom[ref] = {value}

    def __repr__(self) -> str:  # pragma: no cover - debug aid
        return f"Grid(open={len(self.open_refs())}, remaining={self.remaining()})"


# ---------------------------------------------------------------------------
# propagation
# ---------------------------------------------------------------------------


def _tuple_ok(refs: Sequence[Ref], values: Sequence[int]) -> bool:
    """Reject tuples that put two items of one category in the same position."""
    n = len(refs)
    for i in range(n):
        for j in range(i + 1, n):
            if refs[i].cat == refs[j].cat and values[i] == values[j]:
                return False
    return True


def _revise_link(atom: Link, grid: Grid) -> list[tuple[Ref, tuple[int, ...]]]:
    """Fast path: linked refs must share a position, so intersect the domains."""
    da, db = grid.dom[atom.a], grid.dom[atom.b]
    if atom.a == atom.b:
        return []
    shared = da & db
    out = []
    if shared != da:
        out.append((atom.a, tuple(sorted(da - shared))))
        grid.dom[atom.a] = set(shared)
    if shared != db:
        out.append((atom.b, tuple(sorted(db - shared))))
        grid.dom[atom.b] = set(shared)
    return out


def _revise_not_link(atom: NotLink, grid: Grid) -> list[tuple[Ref, tuple[int, ...]]]:
    """Fast path: a pinned ref forbids its position to the other."""
    out = []
    for x, y in ((atom.a, atom.b), (atom.b, atom.a)):
        dx = grid.dom[x]
        if len(dx) == 1:
            v = next(iter(dx))
            if v in grid.dom[y]:
                grid.dom[y] = grid.dom[y] - {v}
                out.append((y, (v,)))
    return out


def _revise_generic(
    atom: Atom,
    grid: Grid,
    refs: tuple[Ref, ...] | None = None,
    check_tuple: bool = True,
) -> list[tuple[Ref, tuple[int, ...]]]:
    """Generalised arc consistency by enumerating supported tuples.

    ``refs`` and ``check_tuple`` are precomputed by :class:`Engine`: most atoms
    relate refs from different categories, in which case no tuple can violate a
    category's bijection and the per-tuple check can be skipped outright.
    """
    if refs is None:
        refs = atom.refs()
    doms = [sorted(grid.dom[r]) for r in refs]
    if any(not d for d in doms):
        raise Contradiction
    # Fully pinned: one check instead of a product enumeration.  This is the
    # common case deep in the search tree, where it saves a great deal.
    if all(len(d) == 1 for d in doms):
        values = [d[0] for d in doms]
        if check_tuple and not _tuple_ok(refs, values):
            raise Contradiction
        if not atom.check(dict(zip(refs, values)), grid.schema):
            raise Contradiction
        return []
    support: list[set[int]] = [set() for _ in refs]
    schema = grid.schema
    check = atom.check
    for values in product(*doms):
        if check_tuple and not _tuple_ok(refs, values):
            continue
        if check(dict(zip(refs, values)), schema):
            for i, v in enumerate(values):
                support[i].add(v)
    out = []
    for i, ref in enumerate(refs):
        old = grid.dom[ref]
        keep = support[i]
        if keep != old:
            out.append((ref, tuple(sorted(old - keep))))
            grid.dom[ref] = keep
            if not keep:
                raise Contradiction
    return out


def revise_atom(
    atom: Atom,
    grid: Grid,
    refs: tuple[Ref, ...] | None = None,
    check_tuple: bool = True,
) -> list[tuple[Ref, tuple[int, ...]]]:
    """Prune domains using one atom. Returns ``(ref, removed_values)`` pairs."""
    if isinstance(atom, Link):
        out = _revise_link(atom, grid)
    elif isinstance(atom, NotLink):
        out = _revise_not_link(atom, grid)
    else:
        return _revise_generic(atom, grid, refs, check_tuple)
    for ref, _ in out:
        if not grid.dom[ref]:
            raise Contradiction
    return out


def revise_bijection(cat_name: str, grid: Grid) -> list[tuple[Ref, tuple[int, ...]]]:
    """One item per position and one position per item, within one category."""
    refs = grid.schema.by_name[cat_name].refs()
    dom = grid.dom
    out: list[tuple[Ref, tuple[int, ...]]] = []

    # A pinned item owns its position outright.
    pinned: dict[int, Ref] = {}
    for ref in refs:
        d = dom[ref]
        if len(d) == 1:
            v = next(iter(d))
            if v in pinned:
                # Two items of one category cannot share a position.
                raise Contradiction
            pinned[v] = ref
    if pinned:
        taken = pinned.keys()
        for ref in refs:
            d = dom[ref]
            if len(d) == 1:
                continue
            clash = d & taken
            if clash:
                nd = d - clash
                if not nd:
                    raise Contradiction
                dom[ref] = nd
                out.append((ref, tuple(sorted(clash))))

    # A position only one item can take belongs to that item.
    holders: dict[int, list[Ref]] = {}
    for ref in refs:
        for v in dom[ref]:
            holders.setdefault(v, []).append(ref)
    for v in grid.schema.positions:
        hs = holders.get(v)
        if not hs:
            raise Contradiction
        if len(hs) == 1:
            ref = hs[0]
            d = dom[ref]
            if len(d) > 1:
                out.append((ref, tuple(sorted(d - {v}))))
                dom[ref] = {v}
    return out


def revise_subsets(cat_name: str, grid: Grid, max_size: int = 3) -> list[tuple[Ref, tuple[int, ...]]]:
    """Naked and hidden subsets within one category."""
    cat = grid.schema.by_name[cat_name]
    refs = [r for r in cat.refs() if len(grid.dom[r]) > 1]
    out: list[tuple[Ref, tuple[int, ...]]] = []
    if len(refs) < 2:
        return out

    for size in range(2, min(max_size, len(refs) - 1) + 1):
        # Naked: k items sharing k positions lock those positions away.
        for group in combinations(refs, size):
            union: set[int] = set()
            for r in group:
                union |= grid.dom[r]
            if len(union) != size:
                continue
            for other in cat.refs():
                if other in group:
                    continue
                overlap = grid.dom[other] & union
                if overlap:
                    grid.dom[other] = grid.dom[other] - union
                    out.append((other, tuple(sorted(overlap))))
                    if not grid.dom[other]:
                        raise Contradiction

        # Hidden: k positions available only to k items lock those items in.
        for positions in combinations(grid.schema.positions, size):
            pset = set(positions)
            holders = [r for r in cat.refs() if grid.dom[r] & pset]
            if len(holders) != size:
                continue
            for r in holders:
                extra = grid.dom[r] - pset
                if extra:
                    grid.dom[r] = grid.dom[r] & pset
                    out.append((r, tuple(sorted(extra))))
                    if not grid.dom[r]:
                        raise Contradiction
    return out


class Engine:
    """Propagation driver shared by the oracle and the human-style solver."""

    def __init__(self, schema: Schema, atoms: Sequence[Atom], clue_of: Sequence[int | None] | None = None) -> None:
        self.schema = schema
        self.atoms = tuple(atoms)
        self.clue_of = tuple(clue_of) if clue_of is not None else tuple([None] * len(atoms))
        # ref -> indices of atoms mentioning it, for wake-up on change
        # Precomputed per-atom metadata.  ``refs()`` builds a fresh tuple on
        # every call and propagation calls it tens of thousands of times, so it
        # is worth hoisting; ``needs_tuple_check`` records whether an atom can
        # even violate a category bijection, which most cannot.
        self.atom_refs: tuple[tuple[Ref, ...], ...] = tuple(a.refs() for a in self.atoms)
        self.needs_tuple_check: tuple[bool, ...] = tuple(
            len({r.cat for r in refs}) < len(refs) for refs in self.atom_refs
        )
        self.watchers: dict[Ref, list[int]] = {r: [] for r in schema.all_refs}
        for i, refs in enumerate(self.atom_refs):
            for r in refs:
                self.watchers.setdefault(r, []).append(i)
        self.by_tier: dict[int, list[int]] = {}
        for i, atom in enumerate(self.atoms):
            self.by_tier.setdefault(atom.tier, []).append(i)

    def propagate(
        self,
        grid: Grid,
        tiers: Iterable[int] = ALL_TIERS,
        trace: list[Step] | None = None,
        subset_size: int = 3,
        seed_refs: Iterable[Ref] | None = None,
    ) -> int:
        """Run propagation to a fixpoint. Returns the highest tier that fired.

        ``seed_refs`` restricts the initial work queue to constraints touching
        those refs.  The search uses it after assigning a single cell: without
        it, every node would re-revise every clue from scratch, which dominates
        the cost of a uniqueness check on a large grid.

        Raises :class:`Contradiction` if any domain empties.
        """
        tiers = frozenset(tiers)
        if seed_refs is None:
            queue: list[int] = [
                i for t in sorted(self.by_tier) if t in tiers for i in self.by_tier[t]
            ]
            cats_dirty: set[str] = {c.name for c in self.schema.categories}
        else:
            seeds = list(seed_refs)
            queue = [
                i
                for r in seeds
                for i in self.watchers.get(r, ())
                if self.atoms[i].tier in tiers
            ]
            cats_dirty = {r.cat for r in seeds}
        in_queue = set(queue)
        top_tier = 0

        while True:
            progressed = False

            while queue:
                i = queue.pop()
                in_queue.discard(i)
                atom = self.atoms[i]
                changes = revise_atom(
                    atom, grid, self.atom_refs[i], self.needs_tuple_check[i]
                )
                if changes:
                    progressed = True
                    top_tier = max(top_tier, atom.tier)
                    if trace is not None:
                        for ref, removed in changes:
                            trace.append(
                                Step(
                                    atom.tier,
                                    TIER_NAMES[atom.tier],
                                    ref,
                                    removed,
                                    self.clue_of[i],
                                )
                            )
                    for ref, _ in changes:
                        cats_dirty.add(ref.cat)
                        for j in self.watchers.get(ref, ()):
                            if j != i and j not in in_queue and self.atoms[j].tier in tiers:
                                queue.append(j)
                                in_queue.add(j)

            if T_BIJECTION in tiers and cats_dirty:
                todo, cats_dirty = cats_dirty, set()
                for cat in sorted(todo):
                    changes = revise_bijection(cat, grid)
                    if changes:
                        progressed = True
                        top_tier = max(top_tier, T_BIJECTION)
                        if trace is not None:
                            for ref, removed in changes:
                                trace.append(
                                    Step(T_BIJECTION, TIER_NAMES[T_BIJECTION], ref, removed)
                                )
                        for ref, _ in changes:
                            cats_dirty.add(ref.cat)
                            for j in self.watchers.get(ref, ()):
                                if j not in in_queue and self.atoms[j].tier in tiers:
                                    queue.append(j)
                                    in_queue.add(j)
                if queue or cats_dirty:
                    continue

            if not progressed and T_SUBSET in tiers:
                for cat in (c.name for c in self.schema.categories):
                    changes = revise_subsets(cat, grid, subset_size)
                    if changes:
                        progressed = True
                        top_tier = max(top_tier, T_SUBSET)
                        if trace is not None:
                            for ref, removed in changes:
                                trace.append(
                                    Step(T_SUBSET, TIER_NAMES[T_SUBSET], ref, removed)
                                )
                        for ref, _ in changes:
                            cats_dirty.add(ref.cat)
                            for j in self.watchers.get(ref, ()):
                                if j not in in_queue and self.atoms[j].tier in tiers:
                                    queue.append(j)
                                    in_queue.add(j)
                        break

            if not progressed:
                return top_tier

    # -- search ----------------------------------------------------------
    def count_solutions(
        self, limit: int = 2, grid: Grid | None = None
    ) -> tuple[int, Solution | None]:
        """Count solutions, stopping once ``limit`` have been found.

        Returns ``(count, first_solution)``.
        """
        root = grid.copy() if grid is not None else Grid(self.schema)
        found: list[Solution] = []
        try:
            self.propagate(root, tiers=ORACLE_TIERS)
        except Contradiction:
            return 0, None
        self._search(root, limit, found)
        return len(found), found[0] if found else None

    def _search(self, grid: Grid, limit: int, found: list[Solution]) -> None:
        if len(found) >= limit:
            return
        if grid.solved:
            found.append(grid.to_solution())
            return
        ref = min(grid.open_refs(), key=lambda r: (len(grid.dom[r]), r.key))
        for value in sorted(grid.dom[ref]):
            child = grid.copy()
            child.assign(ref, value)
            try:
                # Only constraints touching the cell we just fixed can have
                # become unsatisfied, so seed the queue with those.
                self.propagate(child, tiers=ORACLE_TIERS, seed_refs=(ref,))
            except Contradiction:
                continue
            self._search(child, limit, found)
            if len(found) >= limit:
                return

    def unique_solution(self) -> Solution | None:
        """The solution, if there is exactly one; otherwise ``None``."""
        count, sol = self.count_solutions(limit=2)
        return sol if count == 1 else None


# ---------------------------------------------------------------------------
# convenience
# ---------------------------------------------------------------------------


def flatten(clues: Iterable) -> tuple[Atom, ...]:
    """Flatten ``Clue`` bundles (or a bare atom iterable) into atoms."""
    out: list[Atom] = []
    for item in clues:
        if isinstance(item, Atom):
            out.append(item)
        else:
            out.extend(item.atoms)
    return tuple(out)


def clue_index_map(clues: Iterable) -> tuple[tuple[Atom, ...], tuple[int | None, ...]]:
    """Flatten clues while remembering which numbered clue each atom came from."""
    atoms: list[Atom] = []
    owners: list[int | None] = []
    for i, item in enumerate(clues):
        if isinstance(item, Atom):
            atoms.append(item)
            owners.append(i)
        else:
            for at in item.atoms:
                atoms.append(at)
                owners.append(i)
    return tuple(atoms), tuple(owners)


def count_solutions(schema: Schema, clues: Iterable, limit: int = 2) -> int:
    return Engine(schema, flatten(clues)).count_solutions(limit=limit)[0]


def is_unique(schema: Schema, clues: Iterable) -> bool:
    return count_solutions(schema, clues, limit=2) == 1


def solve(schema: Schema, clues: Iterable) -> Solution | None:
    return Engine(schema, flatten(clues)).unique_solution()
