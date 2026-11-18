"""The player's solving chart.

This is the Penny Dell grid as a data structure: for every pair of distinct
categories, an M x M matrix of marks, each ``True`` (these two go together),
``False`` (they do not) or absent (not yet known).

Deliberately *not* the representation :mod:`logicgrid.csp` uses. That one maps
each item to the spine positions it could occupy, which is ideal for solving but
cannot express "I know the Mudlark is the Seminary crew's boat, but not yet
which placing they got" -- a state a human passes through constantly. Pairwise
marks can.

**Only the player's own marks are stored.** Everything else -- the x's a circled
cell forces across its row and column, and anything assist deduces -- is
recomputed from them on every change by :meth:`Board._closure`. Keeping the two
separate is what makes editing sound: change your mind about a cell and the
consequences of the old answer vanish with it, rather than lingering as x's
nothing supports any more. It also makes undo a one-line snapshot and makes
toggling assist a pure recompute.

Two levels of inference:

* **always on** -- a circled cell rules out the rest of its row and column. That
  is not deduction, it is the pencil-work the rules force.
* **assist, off by default** -- transitivity (A=B and B=C so A=C) and
  last-cell-standing. Those *are* deductions, so doing them for the player
  changes the puzzle; available, but opt-in.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from logicgrid.model import Ref, Schema, Solution

YES = True
NO = False

Cell = tuple[Ref, Ref]


class Conflict(ValueError):
    """The requested mark contradicts what the player has already said."""


def cell(a: Ref, b: Ref) -> Cell:
    """Canonical key for an unordered pair of refs."""
    return (a, b) if a <= b else (b, a)


@dataclass(slots=True)
class Mistake:
    a: Ref
    b: Ref
    value: bool


class Board:
    """Mark state for one puzzle, with undo."""

    def __init__(self, puzzle, assist: bool = False) -> None:
        self.puzzle = puzzle
        self.schema: Schema = puzzle.schema
        self.solution: Solution = puzzle.solution
        self._assist = assist
        #: What the player explicitly marked.
        self.user_marks: dict[Cell, bool] = {}
        #: Those plus everything they force. Rebuilt on every change.
        self.marks: dict[Cell, bool] = {}
        self._history: list[dict[Cell, bool]] = []
        self.pairs: tuple[tuple[str, str], ...] = tuple(
            (a.name, b.name) for a, b in combinations(self.schema.categories, 2)
        )

    # -- assist ----------------------------------------------------------
    @property
    def assist(self) -> bool:
        return self._assist

    @assist.setter
    def assist(self, value: bool) -> None:
        self._assist = value
        self.marks = self._closure(self.user_marks)

    # -- queries ---------------------------------------------------------
    def get(self, a: Ref, b: Ref) -> bool | None:
        return self.marks.get(cell(a, b))

    def is_own(self, a: Ref, b: Ref) -> bool:
        """Did the player mark this cell themselves, or did it follow?"""
        return cell(a, b) in self.user_marks

    def total_cells(self) -> int:
        m = self.schema.size
        return len(self.pairs) * m * m

    def known_cells(self) -> int:
        return len(self.marks)

    def truth(self, a: Ref, b: Ref) -> bool:
        return self.solution.position(a) == self.solution.position(b)

    def mistakes(self) -> list[Mistake]:
        """Marks that contradict the real solution."""
        return [
            Mistake(a, b, value)
            for (a, b), value in sorted(self.marks.items())
            if value != self.truth(a, b)
        ]

    def links_for(self, ref: Ref, cat_name: str) -> tuple[list[Ref], list[Ref]]:
        """``(confirmed, ruled_out)`` for ``ref`` against one category."""
        yes, no = [], []
        for other in self.schema.by_name[cat_name].refs():
            value = self.get(ref, other)
            if value is YES:
                yes.append(other)
            elif value is NO:
                no.append(other)
        return yes, no

    def answer(self) -> dict[str, list[str | None]]:
        """The player's answer so far, as spine-indexed rows."""
        spine = self.schema.spine
        rows: dict[str, list[str | None]] = {spine.name: list(spine.items)}
        for cat in self.schema.other_categories():
            row: list[str | None] = [None] * self.schema.size
            for ref in cat.refs():
                yes, _ = self.links_for(ref, spine.name)
                if len(yes) == 1:
                    row[spine.index(yes[0].item)] = ref.item
            rows[cat.name] = row
        return rows

    def answer_complete(self) -> bool:
        """Every item placed against the spine -- right or wrong."""
        return all(None not in row for row in self.answer().values())

    def solved(self) -> bool:
        """Every item placed against the spine, and all of it correct."""
        return self.answer_complete() and not self.mistakes()

    def progress(self) -> tuple[int, int]:
        """``(placed, total)`` cells of the answer sheet, not the whole chart."""
        answer = self.answer()
        cats = [c.name for c in self.schema.other_categories()]
        placed = sum(1 for c in cats for v in answer[c] if v is not None)
        return placed, len(cats) * self.schema.size

    # -- inference -------------------------------------------------------
    def _closure(self, user: dict[Cell, bool]) -> dict[Cell, bool]:
        """Everything that follows from ``user``. Raises on a contradiction."""
        marks: dict[Cell, bool] = {}
        queue: list[Cell] = []

        def put(key: Cell, value: bool) -> None:
            previous = marks.get(key)
            if previous is None:
                marks[key] = value
                queue.append(key)
            elif previous != value:
                a, b = key
                held = "go together" if previous else "do not go together"
                raise Conflict(
                    f"that clashes with the board: {a.item} and {b.item} "
                    f"already {held}"
                )

        for key, value in user.items():
            put(key, value)

        by_name = self.schema.by_name

        def propagate_forced() -> None:
            while queue:
                key = queue.pop()
                if marks[key] is not YES:
                    continue
                a, b = key
                for other in by_name[b.cat].refs():
                    if other != b:
                        put(cell(a, other), NO)
                for other in by_name[a.cat].refs():
                    if other != a:
                        put(cell(other, b), NO)

        propagate_forced()
        if not self._assist:
            return marks

        def value_of(a: Ref, b: Ref) -> bool | None:
            return marks.get(cell(a, b))

        changed = True
        while changed:
            changed = False
            # Transitivity: a fact about one item is a fact about its partner.
            for (a, b), value in list(marks.items()):
                if value is not YES:
                    continue
                for cat in self.schema.categories:
                    if cat.name in (a.cat, b.cat):
                        continue
                    for c in cat.refs():
                        va, vb = value_of(a, c), value_of(b, c)
                        if va is not None and vb is None:
                            put(cell(b, c), va)
                            changed = True
                        elif vb is not None and va is None:
                            put(cell(a, c), vb)
                            changed = True
            propagate_forced()
            # Last cell standing in a row.
            for cat_a, cat_b in self.pairs:
                for first, second in ((cat_a, cat_b), (cat_b, cat_a)):
                    for ref in by_name[first].refs():
                        yes, no = [], []
                        for other in by_name[second].refs():
                            v = value_of(ref, other)
                            if v is YES:
                                yes.append(other)
                            elif v is NO:
                                no.append(other)
                        if yes:
                            continue
                        open_cells = [
                            o for o in by_name[second].refs() if o not in no
                        ]
                        if len(open_cells) == 1:
                            put(cell(ref, open_cells[0]), YES)
                            changed = True
            propagate_forced()
        return marks

    # -- mutation --------------------------------------------------------
    def set_mark(self, a: Ref, b: Ref, value: bool) -> None:
        """Mark a cell. Raises :class:`Conflict` and changes nothing on a clash.

        The targeted cell is always overwritable -- changing your own answer is
        an edit, not a contradiction. Only a *forced* consequence clashing with
        another of your marks is a conflict.
        """
        if a.cat == b.cat:
            raise Conflict(
                f"{a.item} and {b.item} are both "
                f"{self.schema.by_name[a.cat].label} -- a grid only pairs "
                f"different categories"
            )
        trial = dict(self.user_marks)
        trial[cell(a, b)] = value
        derived = self._closure(trial)  # raises before anything is committed
        self._history.append(dict(self.user_marks))
        self.user_marks = trial
        self.marks = derived

    def clear_mark(self, a: Ref, b: Ref) -> bool:
        """Erase one of the player's own marks, and whatever it forced."""
        key = cell(a, b)
        if key not in self.user_marks:
            return False
        trial = dict(self.user_marks)
        del trial[key]
        derived = self._closure(trial)
        self._history.append(dict(self.user_marks))
        self.user_marks = trial
        self.marks = derived
        return True

    def undo(self) -> bool:
        if not self._history:
            return False
        self.user_marks = self._history.pop()
        self.marks = self._closure(self.user_marks)
        return True

    def reset(self) -> None:
        if not self.user_marks:
            return
        self._history.append(dict(self.user_marks))
        self.user_marks = {}
        self.marks = {}

    def fill_from_solution(self) -> None:
        """Fill the whole chart correctly. For ``reveal`` and for tests."""
        self._history.append(dict(self.user_marks))
        marks: dict[Cell, bool] = {}
        for cat_a, cat_b in self.pairs:
            for a in self.schema.by_name[cat_a].refs():
                for b in self.schema.by_name[cat_b].refs():
                    marks[cell(a, b)] = self.truth(a, b)
        self.user_marks = marks
        self.marks = dict(marks)
