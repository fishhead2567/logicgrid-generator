"""A solver restricted to techniques a person would actually use.

The uniqueness oracle in :mod:`logicgrid.csp` can crack anything by searching,
which tells us nothing about how hard a puzzle *feels*.  This module instead
climbs a ladder of named techniques, always reaching for the cheapest one that
still makes progress, and reports which rung it had to stand on:

1. **direct** -- a clue names a cell; equalities carry the fact around
2. **bijection** -- one item per position and one position per item
3. **order** -- positional and arithmetic reasoning
4. **disjunction** -- resolving either/or, not-both and if-then clues
5. **subset** -- naked and hidden pairs/triples
6. **trial** -- assume a cell, hit a contradiction, rule it out

Difficulty then falls out of observation rather than assertion: the highest rung
required, how often the expensive rungs were needed, and how much of the grid
was left to deduce.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Iterable, Sequence

from .clues import Atom
from .csp import (
    ALL_TIERS,
    Contradiction,
    Engine,
    Grid,
    Step,
    T_BIJECTION,
    T_DIRECT,
    T_SUBSET,
    T_TRIAL,
    TIER_NAMES,
    clue_index_map,
)
from .model import Schema, Solution


@dataclass(slots=True)
class SolveReport:
    """What the human-style solver managed, and how hard it had to work."""

    solved: bool
    solution: Solution | None
    max_tier: int
    tier_counts: dict[int, int] = field(default_factory=dict)
    steps: int = 0
    trial_eliminations: int = 0
    unknown_cells: int = 0
    deduced_cells: int = 0
    trace: list[Step] = field(default_factory=list)
    contradiction: bool = False

    @property
    def max_technique(self) -> str:
        return TIER_NAMES.get(self.max_tier, "none")

    def hard_steps(self) -> int:
        """Steps that needed disjunction, subset or trial reasoning."""
        return sum(n for t, n in self.tier_counts.items() if t >= 4)

    def summary(self) -> str:
        bits = ", ".join(
            f"{TIER_NAMES[t]}={self.tier_counts[t]}" for t in sorted(self.tier_counts)
        )
        state = "solved" if self.solved else "stuck"
        return f"{state} via {self.max_technique} ({self.steps} steps: {bits})"

    def to_json(self) -> dict:
        return {
            "solved": self.solved,
            "max_tier": self.max_tier,
            "max_technique": self.max_technique,
            "steps": self.steps,
            "tier_counts": {TIER_NAMES[t]: n for t, n in sorted(self.tier_counts.items())},
            "trial_eliminations": self.trial_eliminations,
            "unknown_cells": self.unknown_cells,
        }


def _trial_pass(
    engine: Engine,
    grid: Grid,
    tiers: Iterable[int],
    trace: list[Step],
) -> int:
    """Assume-and-refute over open cells. Returns how many values were ruled out.

    Stops at the first successful refutation so the solver can drop back to
    cheaper techniques, which is what a person does.
    """
    tiers = frozenset(tiers)
    for ref in sorted(grid.open_refs(), key=lambda r: (len(grid.dom[r]), r.key)):
        for value in sorted(grid.dom[ref]):
            probe = grid.copy()
            probe.assign(ref, value)
            try:
                engine.propagate(probe, tiers=tiers)
            except Contradiction:
                grid.dom[ref] = grid.dom[ref] - {value}
                trace.append(Step(T_TRIAL, TIER_NAMES[T_TRIAL], ref, (value,)))
                return 1
    return 0


def human_solve(
    schema: Schema,
    clues: Sequence,
    *,
    allow_trial: bool = True,
    max_tier: int = T_TRIAL,
    subset_size: int = 3,
) -> SolveReport:
    """Solve with human techniques, escalating only as far as necessary."""
    atoms, owners = clue_index_map(clues)
    engine = Engine(schema, atoms, owners)
    grid = Grid(schema)
    trace: list[Step] = []
    counts: Counter[int] = Counter()

    ceiling = min(max_tier, T_TRIAL if allow_trial else T_SUBSET)
    unknown = (len(schema.categories) - 1) * schema.size
    enabled = T_DIRECT

    while True:
        before = grid.remaining()
        batch: list[Step] = []
        try:
            engine.propagate(
                grid,
                tiers=range(T_DIRECT, min(enabled, T_SUBSET) + 1),
                trace=batch,
                subset_size=subset_size,
            )
        except Contradiction:
            trace.extend(batch)
            return SolveReport(
                solved=False,
                solution=None,
                max_tier=max((s.tier for s in trace), default=0),
                tier_counts=dict(counts),
                steps=len(trace),
                unknown_cells=unknown,
                trace=trace,
                contradiction=True,
            )
        trace.extend(batch)
        for s in batch:
            counts[s.tier] += 1

        if grid.solved:
            break

        if grid.remaining() < before:
            # Progress was made; fall back to the cheapest techniques again.
            enabled = T_DIRECT
            continue

        if enabled < min(ceiling, T_SUBSET):
            enabled += 1
            continue

        if ceiling >= T_TRIAL:
            gained = _trial_pass(engine, grid, range(T_DIRECT, T_SUBSET + 1), trace)
            if gained:
                counts[T_TRIAL] += gained
                enabled = T_DIRECT
                continue

        break

    solved = grid.solved
    deduced = sum(
        1
        for r, d in grid.dom.items()
        if len(d) == 1 and not schema.is_spine(r)
    )
    return SolveReport(
        solved=solved,
        solution=grid.to_solution() if solved else None,
        max_tier=max((s.tier for s in trace), default=0),
        tier_counts=dict(counts),
        steps=len(trace),
        trial_eliminations=counts.get(T_TRIAL, 0),
        unknown_cells=unknown,
        deduced_cells=deduced,
        trace=trace,
    )


def explain(schema: Schema, clues: Sequence, limit: int | None = None) -> list[str]:
    """Human-readable walkthrough of the deductions, for solution pages."""
    report = human_solve(schema, clues)
    lines = [s.describe(schema) for s in report.trace]
    if limit is not None:
        lines = lines[:limit]
    return lines
