"""Difficulty: measured from a solve, not asserted by a flag.

:func:`score` turns a :class:`~logicgrid.human_solver.SolveReport` plus the clue
set into a single number, and :func:`rating` buckets that number into 1-7 (the
same scale the GECCO '24 logic-grid generation work uses, which makes the output
comparable to published work).

The weights below say what we believe makes a logic problem hard:

* the most advanced technique the solver was *forced* to use, which dominates;
* how often it had to use the expensive techniques, rather than once by luck;
* how few cells are handed over for free -- a puzzle whose clues are mostly
  flat "X goes with Y" statements is easy however big the grid is;
* raw grid size, which matters but much less than the above;
* compound (either/or, if-then) clues, which cost working memory even when the
  deduction they enable is cheap.

:data:`THRESHOLDS` is calibrated empirically -- see ``scripts/calibrate.py``.
"""

from __future__ import annotations

import bisect
import math
from dataclasses import dataclass, field
from itertools import combinations
from typing import Mapping, Sequence

from .clues import (
    ALL_KINDS,
    Atom,
    TIER_A_KINDS,
    TIER_B_KINDS,
    TIER_C_KINDS,
)
from .csp import flatten
from .human_solver import SolveReport
from .model import Schema

#: How much each top technique contributes.  The jump from "order" to
#: "disjunction" is where puzzles stop being mechanical.
TIER_WEIGHT = {0: 0.0, 1: 0.0, 2: 0.3, 3: 1.0, 4: 2.4, 5: 3.4, 6: 5.2}

W_TIER = 1.55
W_HARD_STEPS = 0.95
W_SPARSITY = 2.40
W_SIZE = 0.115
W_TRIAL = 0.55
W_COMPOUND = 0.34

#: Upper bounds of ratings 1..6; anything above the last is a 7.
#:
#: Calibrated from 24 samples per profile (``scripts/calibrate.py --samples 24``,
#: seed 20261118).  The profile medians came out at 3.97 / 4.93 / 5.51 / 9.51 /
#: 16.09 for gentle / easy / moderate / hard / expert -- monotonic, so the score
#: function ranks difficulty correctly and only the cut points needed fixing.
#: Thresholds sit at the boundaries between adjacent profiles' distributions.
THRESHOLDS: tuple[float, ...] = (4.03, 4.50, 5.44, 7.32, 9.28, 11.24)

#: Kinds the generator may emit. ``distinct`` is excluded: "Leocadia,
#: thrips and April are three different growers" is confusing when Grower
#: is itself a category, and plain negatives say the same thing clearly.
#: The atom stays in the IR, since an extractor may legitimately read one
#: out of a narrative.
EXCLUDED_FROM_GENERATION = ("distinct",)
GEN_B_KINDS = tuple(k for k in TIER_B_KINDS if k not in EXCLUDED_FROM_GENERATION)
GEN_ALL_KINDS = tuple(k for k in ALL_KINDS if k not in EXCLUDED_FROM_GENERATION)

RATING_NAMES = {
    1: "gentle",
    2: "easy",
    3: "moderate",
    4: "tricky",
    5: "hard",
    6: "very hard",
    7: "diabolical",
}


def clue_stats(schema: Schema, clues: Sequence) -> dict:
    """Shape of a clue set: counts by kind, positives, compounds."""
    atoms = flatten(clues)
    kinds: dict[str, int] = {}
    positives = 0
    compounds = 0
    for atom in atoms:
        kinds[atom.kind] = kinds.get(atom.kind, 0) + 1
        if atom.is_positive_link():
            positives += 1
        if atom.kind in TIER_C_KINDS:
            compounds += 1
    return {
        "atoms": len(atoms),
        "numbered_clues": len(clues),
        "kinds": kinds,
        "positives": positives,
        "compounds": compounds,
    }


def clue_balance(schema: Schema, clues: Sequence) -> dict:
    """How evenly a clue set spreads over the grid's category pairs.

    A clue set can be minimal, unique and solvable while still being tedious to
    read, because nothing in the uniqueness oracle cares *where* the information
    sits.  With three categories, pinning A-B and A-C leaves B-C derivable by
    transitivity, so the generator will happily ship a puzzle in which one
    sub-grid is never mentioned and four of five clues are flat "X is Y".
    That puzzle is correct and dull.

    Three numbers, measured on the flat atom set:

    ``pair_coverage``
        fraction of category pairs that at least one atom touches.
    ``top_pair_share``
        fraction of atoms crowded onto the single busiest pair.
    ``positive_share``
        fraction of atoms that are flat positive links -- the ones that hand a
        cell over rather than asking for a deduction.

    ``degenerate`` counts a different defect: a positional or compound atom
    every one of whose refs is *also* pinned outright by a flat link elsewhere
    in the set.  "The crew who rows the Last Resort is better than the Tannery
    crew" is such a clue when another line already says the Almshouse crew rows
    the Last Resort -- the solver substitutes and the indirection was theatre.
    """
    atoms = flatten(clues)
    if not atoms:
        return {
            "pair_coverage": 0.0,
            "top_pair_share": 0.0,
            "positive_share": 0.0,
            "degenerate": 0,
            "pairs": 0,
            "pairs_covered": 0,
        }

    names = [c.name for c in schema.categories]
    all_pairs = {frozenset(p) for p in combinations(names, 2)}
    counts: dict[frozenset, int] = {}
    pinned: set = set()
    positives = 0
    for atom in atoms:
        cats = {r.cat for r in atom.refs()}
        for pair in combinations(sorted(cats), 2):
            key = frozenset(pair)
            counts[key] = counts.get(key, 0) + 1
        if atom.is_positive_link():
            positives += 1
            pinned |= set(atom.refs())

    degenerate = 0
    for atom in atoms:
        if atom.is_positive_link():
            continue
        refs = set(atom.refs())
        if refs and refs <= pinned:
            degenerate += 1

    total = sum(counts.values()) or 1
    return {
        "pair_coverage": len(set(counts) & all_pairs) / max(1, len(all_pairs)),
        "top_pair_share": max(counts.values()) / total,
        "positive_share": positives / len(atoms),
        "degenerate": degenerate,
        "pairs": len(all_pairs),
        "pairs_covered": len(set(counts) & all_pairs),
    }


def score(schema: Schema, clues: Sequence, report: SolveReport) -> float:
    """A continuous difficulty score. Higher is harder."""
    stats = clue_stats(schema, clues)
    unknown = max(1, (len(schema.categories) - 1) * schema.size)

    # Fraction of the unknown cells that were *not* handed over as free links.
    sparsity = max(0.0, 1.0 - stats["positives"] / unknown)

    value = (
        W_TIER * TIER_WEIGHT.get(report.max_tier, 5.2)
        + W_HARD_STEPS * math.log1p(report.hard_steps())
        + W_SPARSITY * sparsity
        + W_SIZE * unknown
        + W_TRIAL * math.log1p(report.trial_eliminations)
        + W_COMPOUND * math.log1p(stats["compounds"])
    )
    return round(value, 4)


def rating(value: float) -> int:
    """Bucket a score into 1-7."""
    return bisect.bisect_left(THRESHOLDS, value) + 1


def rate(schema: Schema, clues: Sequence, report: SolveReport) -> tuple[float, int]:
    s = score(schema, clues, report)
    return s, rating(s)


# ---------------------------------------------------------------------------
# generation profiles
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Profile:
    """A complexity preset: what the generator may build and what to aim for."""

    name: str
    band: tuple[int, int]
    shapes: tuple[tuple[int, int], ...]
    kinds: tuple[str, ...]
    weights: Mapping[str, float] = field(default_factory=dict)
    #: Hard cap on free "X goes with Y" atoms. ``None`` means no cap.
    max_positive: int | None = None
    allow_trial: bool = False
    subset_size: int = 2
    #: Require an ordered spine (positional clues need one).
    require_ordered: bool = True
    #: Require numeric spine values (arithmetic clues need them).
    require_numeric: bool = False
    #: Maximum atoms bundled under one numbered clue.
    max_bundle: int = 2
    #: Reject a clue set that crowds more than this share of its atoms onto a
    #: single category pair.  ``1.0`` disables the check.
    max_pair_share: float = 0.45
    #: Reject a clue set that leaves this fraction of the grid's category pairs
    #: unmentioned, whenever there are at least as many atoms as pairs.
    min_pair_coverage: float = 1.0
    #: Reject a clue set in which more than this share of atoms are flat
    #: positive links.  Distinct from :attr:`max_positive`, which is a hard
    #: count applied while growing; this is a ratio applied after minimising,
    #: when the final clue count is known.
    max_positive_share: float = 0.5

    def weight(self, kind: str) -> float:
        return self.weights.get(kind, 1.0)

    def target(self) -> range:
        return range(self.band[0], self.band[1] + 1)


GENTLE = Profile(
    name="gentle",
    band=(1, 2),
    shapes=((3, 4), (3, 4), (3, 5)),
    kinds=TIER_A_KINDS + ("before", "adjacent", "immediately_before"),
    weights={"link": 2.2, "not_link": 2.4, "before": 1.2, "adjacent": 0.9,
             "immediately_before": 0.9},
    max_positive=4,
    allow_trial=False,
    subset_size=2,
    max_bundle=2,
    # A gentle puzzle is allowed to be generous with flat links -- that is what
    # makes it gentle -- but not to be nothing else.
    max_pair_share=0.5,
    max_positive_share=0.62,
)

EASY = Profile(
    name="easy",
    band=(2, 3),
    shapes=((3, 5), (4, 4), (4, 5)),
    kinds=TIER_A_KINDS + ("before", "adjacent", "immediately_before", "between"),
    weights={"link": 1.8, "not_link": 2.6, "before": 1.3, "adjacent": 1.0,
             "immediately_before": 1.0, "between": 0.8, "distinct": 0.5},
    max_positive=3,
    allow_trial=False,
    subset_size=2,
    max_bundle=2,
    max_pair_share=0.5,
    max_positive_share=0.45,
)

MODERATE = Profile(
    name="moderate",
    band=(3, 4),
    shapes=((4, 5), (4, 5), (5, 5)),
    kinds=TIER_A_KINDS + GEN_B_KINDS[:-1],  # everything positional but arith
    weights={"link": 1.0, "not_link": 2.6, "before": 1.5, "adjacent": 1.2,
             "immediately_before": 1.2, "between": 1.1, "gap": 0.9,
             "parity": 0.4, "distinct": 0.6},
    max_positive=2,
    allow_trial=False,
    subset_size=3,
    max_bundle=3,
)

HARD = Profile(
    name="hard",
    band=(5, 6),
    shapes=((4, 5), (5, 5), (5, 5)),
    kinds=TIER_A_KINDS + GEN_B_KINDS[:-1] + ("or", "not_both"),
    weights={"link": 0.5, "not_link": 2.2, "before": 1.5, "adjacent": 1.2,
             "immediately_before": 1.0, "between": 1.2, "gap": 1.0,
             "parity": 0.6, "distinct": 0.7, "or": 1.6, "not_both": 1.0},
    max_positive=1,
    allow_trial=False,
    subset_size=3,
    max_bundle=3,
)

EXPERT = Profile(
    name="expert",
    band=(6, 7),
    shapes=((5, 5), (5, 6), (5, 6)),
    kinds=GEN_ALL_KINDS,
    weights={"link": 0.25, "not_link": 1.9, "before": 1.4, "adjacent": 1.1,
             "immediately_before": 0.9, "between": 1.2, "gap": 1.1,
             "parity": 0.8, "distinct": 0.7, "or": 1.9, "not_both": 1.3,
             "if_then": 1.3, "not": 0.6, "arith": 0.9},
    max_positive=0,
    allow_trial=True,
    subset_size=3,
    max_bundle=3,
)

PROFILES: dict[str, Profile] = {
    p.name: p for p in (GENTLE, EASY, MODERATE, HARD, EXPERT)
}

#: The 50-puzzle ramp used by ``logicgrid gen --curve ramp``.
RAMP: tuple[tuple[str, int], ...] = (
    ("gentle", 8),
    ("easy", 10),
    ("moderate", 12),
    ("hard", 12),
    ("expert", 8),
)


def profile(name: str) -> Profile:
    try:
        return PROFILES[name]
    except KeyError:
        raise KeyError(
            f"unknown profile {name!r}; choose from {sorted(PROFILES)}"
        ) from None


def ramp_sequence(total: int = 50, curve: Sequence[tuple[str, int]] = RAMP) -> list[str]:
    """Expand a curve into one profile name per puzzle, scaled to ``total``."""
    weights = [n for _, n in curve]
    base = sum(weights)
    out: list[str] = []
    for (name, n), _ in zip(curve, weights):
        count = max(1, round(total * n / base))
        out.extend([name] * count)
    # Trim or pad to land exactly on ``total``.
    while len(out) > total:
        out.pop()
    while len(out) < total:
        out.append(curve[-1][0])
    return out
