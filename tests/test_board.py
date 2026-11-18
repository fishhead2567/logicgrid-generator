"""The solving chart: marks, forced bookkeeping, conflicts, undo, completion."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from logicgrid import Category, Clue, Link, Puzzle, Ref, Schema, Solution
from logicgrid.generate import Puzzle as GPuzzle
from puzzleplay.board import NO, YES, Board, Conflict, cell

DAYS = ("Monday", "Tuesday", "Wednesday")
BAKERS = ("Odette", "Bramwell", "Loretta")
PIES = ("rhubarb", "pecan", "blackberry")


@pytest.fixture
def puzzle() -> Puzzle:
    schema = Schema(
        [
            Category("day", "Day", DAYS, ordered=True, noun="day",
                     cmp_less="earlier", cmp_more="later", step_noun="day"),
            Category("baker", "Baker", BAKERS, noun="baker"),
            Category("pie", "Pie", PIES, noun="pie"),
        ],
        spine="day",
        entity_noun="entry",
        entity_noun_plural="entries",
    )
    solution = Solution(
        schema, {"day": list(DAYS), "baker": list(BAKERS), "pie": list(PIES)}
    )
    return Puzzle(
        pid="board001",
        title="Board Fixture",
        theme="test",
        blurb="A fixture.",
        schema=schema,
        solution=solution,
        clues=(Clue((Link(Ref("baker", "Odette"), Ref("day", "Monday")),)),),
        profile="gentle",
        score=1.0,
        rating=1,
        seed=0,
    )


def R(item: str) -> Ref:
    for cat, items in (("day", DAYS), ("baker", BAKERS), ("pie", PIES)):
        if item in items:
            return Ref(cat, item)
    raise KeyError(item)


def test_cell_key_is_order_independent():
    a, b = R("Odette"), R("Monday")
    assert cell(a, b) == cell(b, a)


def test_a_yes_rules_out_its_row_and_column(puzzle):
    """Forced bookkeeping, not deduction: one O empties a row and a column."""
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.get(R("Odette"), R("Monday")) is YES
    # Odette cannot also be Tuesday or Wednesday.
    assert board.get(R("Odette"), R("Tuesday")) is NO
    assert board.get(R("Odette"), R("Wednesday")) is NO
    # Monday cannot also be Bramwell or Loretta.
    assert board.get(R("Bramwell"), R("Monday")) is NO
    assert board.get(R("Loretta"), R("Monday")) is NO
    # Nothing else was touched.
    assert board.get(R("Bramwell"), R("Tuesday")) is None


def test_a_no_does_not_cascade(puzzle):
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), NO)
    assert board.get(R("Odette"), R("Monday")) is NO
    assert board.known_cells() == 1


def test_conflicting_mark_is_refused_and_changes_nothing(puzzle):
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), YES)
    before = dict(board.marks)
    with pytest.raises(Conflict, match="clashes"):
        board.set_mark(R("Bramwell"), R("Monday"), YES)
    assert board.marks == before, "a refused mark must leave the board alone"


def test_same_category_pairing_is_refused(puzzle):
    board = Board(puzzle)
    with pytest.raises(Conflict, match="both"):
        board.set_mark(R("Odette"), R("Bramwell"), YES)


def test_undo_restores_the_whole_cascade(puzzle):
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.known_cells() == 5
    assert board.undo()
    assert board.known_cells() == 0
    assert not board.undo()


def test_clearing_a_mark_also_withdraws_what_it_forced(puzzle):
    """Change your mind and the consequences go with it.

    This is why only the player's own marks are stored: leaving behind x's that
    nothing supports any more would quietly corrupt the board.
    """
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.get(R("Odette"), R("Tuesday")) is NO
    assert board.clear_mark(R("Odette"), R("Monday"))
    assert board.get(R("Odette"), R("Monday")) is None
    assert board.get(R("Odette"), R("Tuesday")) is None, "forced x should go too"
    assert board.known_cells() == 0
    assert not board.clear_mark(R("Odette"), R("Monday"))


def test_a_forced_mark_is_not_the_players_to_clear(puzzle):
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.is_own(R("Odette"), R("Monday"))
    assert not board.is_own(R("Odette"), R("Tuesday"))
    assert not board.clear_mark(R("Odette"), R("Tuesday"))


def test_changing_your_mind_about_a_cell_is_allowed(puzzle):
    """O -> x on the same cell is an edit, not a contradiction."""
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Monday"), YES)
    board.set_mark(R("Odette"), R("Monday"), NO)  # must not raise
    assert board.get(R("Odette"), R("Monday")) is NO
    # The x's the circle forced are gone, since nothing forces them now.
    assert board.get(R("Odette"), R("Tuesday")) is None
    assert board.get(R("Bramwell"), R("Monday")) is None


def test_mistakes_are_detected_both_ways(puzzle):
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Tuesday"), YES)  # wrong: Odette is Monday
    wrong = board.mistakes()
    kinds = {(m.a.item, m.b.item, m.value) for m in wrong}
    assert ("Odette", "Tuesday", YES) in kinds or ("Tuesday", "Odette", YES) in kinds
    # The forced x on Odette/Monday is also a mistake, since they do pair up.
    assert any(m.value is NO for m in wrong)


def test_answer_sheet_fills_in_as_you_place(puzzle):
    board = Board(puzzle)
    assert board.answer()["baker"] == [None, None, None]
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.answer()["baker"] == ["Odette", None, None]
    assert board.answer()["day"] == list(DAYS)


def test_progress_counts_the_answer_sheet_not_the_chart(puzzle):
    board = Board(puzzle)
    assert board.progress() == (0, 6)  # 2 non-spine categories x 3 items
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.progress() == (1, 6)


def test_solved_requires_complete_and_correct(puzzle):
    board = Board(puzzle)
    board.fill_from_solution()
    assert board.answer_complete()
    assert board.solved()
    assert board.mistakes() == []


def test_a_full_but_wrong_sheet_is_complete_not_solved(puzzle):
    """The distinction the app needs to tell you 'not quite' rather than nothing."""
    board = Board(puzzle)
    board.set_mark(R("Odette"), R("Tuesday"), YES)
    board.set_mark(R("Bramwell"), R("Monday"), YES)
    board.set_mark(R("Loretta"), R("Wednesday"), YES)
    board.set_mark(R("rhubarb"), R("Monday"), YES)
    board.set_mark(R("pecan"), R("Tuesday"), YES)
    board.set_mark(R("blackberry"), R("Wednesday"), YES)
    assert board.answer_complete()
    assert not board.solved()
    assert board.mistakes()


def test_assist_chains_transitivity(puzzle):
    """With assist on, a cross-link plus a spine link places the third item."""
    board = Board(puzzle, assist=True)
    board.set_mark(R("Odette"), R("rhubarb"), YES)
    board.set_mark(R("Odette"), R("Monday"), YES)
    assert board.get(R("rhubarb"), R("Monday")) is YES, "transitivity should fire"


def test_assist_finishes_a_last_cell(puzzle):
    board = Board(puzzle, assist=True)
    board.set_mark(R("Odette"), R("Monday"), NO)
    board.set_mark(R("Odette"), R("Tuesday"), NO)
    assert board.get(R("Odette"), R("Wednesday")) is YES, "only cell left"


def test_assist_off_leaves_deductions_alone(puzzle):
    board = Board(puzzle, assist=False)
    board.set_mark(R("Odette"), R("Monday"), NO)
    board.set_mark(R("Odette"), R("Tuesday"), NO)
    assert board.get(R("Odette"), R("Wednesday")) is None


def test_assist_never_introduces_a_mistake(puzzle):
    """Chained deductions must stay sound, or assist is worse than useless."""
    board = Board(puzzle, assist=True)
    board.set_mark(R("Odette"), R("Monday"), YES)
    board.set_mark(R("Bramwell"), R("Tuesday"), YES)
    assert board.mistakes() == []
    # Two of three bakers placed forces the third, and assist should take it.
    assert board.get(R("Loretta"), R("Wednesday")) is YES
    assert board.answer()["baker"] == ["Odette", "Bramwell", "Loretta"]
    # The pies are untouched by those marks, so the puzzle is not finished --
    # assist deduces, it does not invent.
    assert board.answer()["pie"] == [None, None, None]
    assert not board.solved()


# ---------------------------------------------------------------------------
# against the real generated set
# ---------------------------------------------------------------------------

PUZZLE_FILES = sorted(Path("puzzles").glob("*.json"))


@pytest.mark.skipif(not PUZZLE_FILES, reason="no generated puzzles present")
@pytest.mark.parametrize("path", PUZZLE_FILES[::7], ids=lambda p: p.stem)
def test_real_puzzles_can_be_played_to_a_win(path):
    """Fill a real board from its solution: it must end solved and clean."""
    puzzle = GPuzzle.from_json(json.loads(path.read_text(encoding="utf-8")))
    board = Board(puzzle)
    schema = puzzle.schema
    spine = schema.spine
    for cat in schema.other_categories():
        for ref in cat.refs():
            position = puzzle.solution.position(ref)
            board.set_mark(ref, Ref(spine.name, spine.items[position]), YES)
    assert board.mistakes() == []
    assert board.answer_complete()
    assert board.solved()


@pytest.mark.skipif(not PUZZLE_FILES, reason="no generated puzzles present")
@pytest.mark.parametrize("path", PUZZLE_FILES[::11], ids=lambda p: p.stem)
def test_assist_on_real_puzzles_stays_sound(path):
    """Assist is a deduction engine; it must never contradict the truth."""
    puzzle = GPuzzle.from_json(json.loads(path.read_text(encoding="utf-8")))
    board = Board(puzzle, assist=True)
    schema = puzzle.schema
    spine = schema.spine
    for cat in schema.other_categories():
        for ref in cat.refs():
            position = puzzle.solution.position(ref)
            target = Ref(spine.name, spine.items[position])
            if board.get(ref, target) is not YES:
                board.set_mark(ref, target, YES)
            assert board.mistakes() == [], f"assist went wrong after {ref.item}"
    assert board.solved()
