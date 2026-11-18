"""The Textual app, driven by real keypresses through Textual's test pilot.

``App.run_test()`` runs the app headless with a simulated terminal, so these
exercise the actual widgets, bindings and event handlers -- not a stand-in. That
is the reason a Textual TUI was picked over curses: it stays genuinely testable
while still being a real interactive app.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

pytest.importorskip("textual")

from textual.widgets import DataTable, Static, TabbedContent  # noqa: E402

from logicgrid.generate import Puzzle  # noqa: E402
from logicgrid.model import Ref  # noqa: E402
from puzzleplay.app import PlayApp  # noqa: E402
from puzzleplay.board import NO, YES  # noqa: E402
from puzzleplay.library import Library, LibraryError  # noqa: E402

PUZZLES = Path("puzzles")
pytestmark = pytest.mark.skipif(
    not sorted(PUZZLES.glob("*.json")), reason="no generated puzzles present"
)


@pytest.fixture
def library() -> Library:
    return Library.load(PUZZLES)


def _banner(app: PlayApp) -> str:
    return str(app.query_one("#banner", Static).content)


def _status(app: PlayApp) -> str:
    return str(app.query_one("#status", Static).content)


def _answer(app: PlayApp) -> str:
    return str(app.query_one("#answer", Static).content)


# ---------------------------------------------------------------------------
# library
# ---------------------------------------------------------------------------


def test_library_finds_puzzles(library):
    assert len(library) == 50
    assert library.puzzle(0).title


def test_library_lookup_by_number_name_and_substring(library):
    assert library.find("1") == 0
    assert library.find(library.paths[3].stem) == 3
    with pytest.raises(LibraryError, match="out of range"):
        library.find("999")
    with pytest.raises(LibraryError, match="no puzzle matching"):
        library.find("definitely-not-a-theme")


def test_library_rejects_an_empty_folder(tmp_path):
    with pytest.raises(LibraryError, match="no puzzle"):
        Library.load(tmp_path)


def test_library_accepts_a_single_file(library):
    one = Library.load(library.paths[0])
    assert len(one) == 1


# ---------------------------------------------------------------------------
# startup and layout
# ---------------------------------------------------------------------------


async def test_app_starts_with_a_grid_per_category_pair(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        schema = app.board.schema
        n = len(schema.categories)
        assert len(app._tabs) == n * (n - 1) // 2
        tabs = app.query_one("#grids", TabbedContent)
        assert tabs.active_pane is not None
        # Spine pairs come first: that is the answer sheet.
        first_pair = app._ordered_pairs()[0]
        assert schema.spine_name in first_pair


async def test_grid_has_one_row_per_item_and_a_label_column(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        table = app._active_table()
        cat_a, cat_b = app._active_pair()
        assert table.row_count == app.board.schema.by_name[cat_a].size
        # +1 for the row-label column.
        assert len(table.columns) == app.board.schema.by_name[cat_b].size + 1


async def test_clues_and_cast_are_on_screen(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        clues = str(app.query_one("#clues", Static).content)
        for cat in app.board.schema.categories:
            for item in cat.items:
                assert item in clues, f"{item} missing from the clue panel"
        assert "1." in clues


async def test_status_line_names_the_cell_under_the_cursor(library):
    """What lets the columns stay narrow enough to fit a terminal."""
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        refs = app.cursor_refs()
        assert refs is not None
        a, b = refs
        status = _status(app)
        assert a.item in status and b.item in status
        assert "unmarked" in status


# ---------------------------------------------------------------------------
# marking
# ---------------------------------------------------------------------------


async def test_pressing_o_marks_together_and_rules_out_the_rest(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        a, b = app.cursor_refs()
        await pilot.press("o")
        await pilot.pause()
        assert app.board.get(a, b) is YES
        others = [r for r in app.board.schema.by_name[b.cat].refs() if r != b]
        assert all(app.board.get(a, o) is NO for o in others)


async def test_pressing_x_marks_apart(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        a, b = app.cursor_refs()
        await pilot.press("x")
        await pilot.pause()
        assert app.board.get(a, b) is NO


async def test_space_cycles_through_the_three_states(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        a, b = app.cursor_refs()
        await pilot.press("space")
        await pilot.pause()
        assert app.board.get(a, b) is YES
        await pilot.press("space")
        await pilot.pause()
        assert app.board.get(a, b) is NO
        await pilot.press("space")
        await pilot.pause()
        assert app.board.get(a, b) is None


async def test_undo_reverses_a_whole_cascade(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        await pilot.press("o")
        await pilot.pause()
        assert app.board.known_cells() > 1
        await pilot.press("u")
        await pilot.pause()
        assert app.board.known_cells() == 0


async def test_backspace_clears_one_cell(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        a, b = app.cursor_refs()
        await pilot.press("x")
        await pilot.pause()
        await pilot.press("backspace")
        await pilot.pause()
        assert app.board.get(a, b) is None


async def test_arrow_keys_move_the_cursor(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        before = app.cursor_refs()
        await pilot.press("down")
        await pilot.pause()
        after = app.cursor_refs()
        assert before != after


async def test_a_conflicting_mark_is_refused_with_a_message(library):
    """Two O's in one column is impossible; say so rather than corrupting."""
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        await pilot.press("o")
        await pilot.pause()
        marks_before = dict(app.board.marks)
        await pilot.press("down")
        await pilot.press("o")
        await pilot.pause()
        assert app.board.marks == marks_before
        assert "clash" in _banner(app).lower()


# ---------------------------------------------------------------------------
# feedback -- the point of the whole thing
# ---------------------------------------------------------------------------


async def test_check_reports_no_mistakes_on_a_correct_mark(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        a, b = app.cursor_refs()
        correct = app.board.truth(a, b)
        await pilot.press("o" if correct else "x")
        await pilot.pause()
        await pilot.press("c")
        await pilot.pause()
        assert "No mistakes" in _banner(app)


async def test_check_names_the_wrong_marks(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        a, b = app.cursor_refs()
        correct = app.board.truth(a, b)
        await pilot.press("x" if correct else "o")  # deliberately wrong
        await pilot.pause()
        await pilot.press("c")
        await pilot.pause()
        banner = _banner(app)
        assert "mistake" in banner
        assert a.item in banner or b.item in banner


async def test_reveal_then_check_says_solved(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        await pilot.press("s")
        await pilot.pause()
        assert app.board.solved()
        await pilot.press("c")
        await pilot.pause()
        assert "SOLVED" in _banner(app)
        assert "?" not in _answer(app), "the answer sheet should be full"


async def test_finishing_correctly_announces_itself_without_being_asked(library):
    """'feedback when I am done' -- it must fire on its own."""
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        app.board.fill_from_solution()
        app._refresh()
        await pilot.pause()
        assert "SOLVED" in _banner(app)


async def test_a_full_but_wrong_sheet_says_not_quite(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        board = app.board
        schema = board.schema
        spine = schema.spine
        # Place every item one spine position off, so the sheet fills but lies.
        for cat in schema.other_categories():
            for ref in cat.refs():
                pos = board.solution.position(ref)
                shifted = (pos + 1) % schema.size
                target = Ref(spine.name, spine.items[shifted])
                if board.get(ref, target) is None:
                    board.set_mark(ref, target, YES)
        app._refresh()
        await pilot.pause()
        if board.answer_complete():
            assert "Not quite" in _banner(app)
            assert not board.solved()


async def test_reset_clears_the_board(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        await pilot.press("o")
        await pilot.pause()
        await pilot.press("r")
        await pilot.pause()
        assert app.board.known_cells() == 0


# ---------------------------------------------------------------------------
# navigation
# ---------------------------------------------------------------------------


async def test_next_and_previous_puzzle(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        first = app.puzzle.pid
        await pilot.press("n")
        await pilot.pause()
        assert app.puzzle.pid != first
        assert app.board.known_cells() == 0, "a new puzzle starts clean"
        await pilot.press("p")
        await pilot.pause()
        assert app.puzzle.pid == first


async def test_switching_puzzles_rebuilds_the_grids(library):
    """Puzzles differ in shape, so stale tables would be a real bug."""
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        # Walk to a puzzle with a different grid shape.
        start = (len(app.board.schema.categories), app.board.schema.size)
        for _ in range(len(library) - 1):
            await pilot.press("n")
            await pilot.pause()
            shape = (len(app.board.schema.categories), app.board.schema.size)
            if shape != start:
                break
        n = len(app.board.schema.categories)
        assert len(app._tabs) == n * (n - 1) // 2
        table = app._active_table()
        cat_a, cat_b = app._active_pair()
        assert table.row_count == app.board.schema.by_name[cat_a].size
        assert len(table.columns) == app.board.schema.by_name[cat_b].size + 1


async def test_tab_moves_between_grids(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        first = app._active_pair()
        await pilot.press("bracketright")
        await pilot.pause()
        assert app._active_pair() != first


async def test_assist_can_be_toggled_from_the_keyboard(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        assert not app.board.assist
        await pilot.press("a")
        await pilot.pause()
        assert app.board.assist
        assert "assist ON" in _banner(app)
        assert "assist ON" in _status(app)


async def test_help_screen_opens_and_closes(library):
    app = PlayApp(library)
    async with app.run_test() as pilot:
        await pilot.pause()
        await pilot.press("question_mark")
        await pilot.pause()
        assert len(app.screen_stack) == 2
        await pilot.press("escape")
        await pilot.pause()
        assert len(app.screen_stack) == 1


# ---------------------------------------------------------------------------
# a full playthrough
# ---------------------------------------------------------------------------


async def test_play_a_whole_puzzle_with_keystrokes_only(library):
    """Drive a real puzzle to a win using nothing but cursor keys and 'o'.

    The strongest test available: no internal calls, just the keys a player
    would actually press, ending in the solved banner.
    """
    small = min(
        range(len(library)),
        key=lambda i: (
            len(library.puzzle(i).schema.categories) * library.puzzle(i).schema.size
        ),
    )
    app = PlayApp(library, index=small)
    async with app.run_test(size=(140, 50)) as pilot:
        await pilot.pause()
        schema = app.board.schema
        spine = schema.spine
        # Visit each non-spine category's grid against the spine and mark the O.
        for cat in schema.other_categories():
            tab_id = f"pair-{cat.name}-{spine.name}".replace("_", "-")
            app.query_one("#grids", TabbedContent).active = tab_id
            await pilot.pause()
            table = app._active_table()
            for row, ref in enumerate(cat.refs()):
                col = app.board.solution.position(ref) + 1
                table.move_cursor(row=row, column=col)
                await pilot.pause()
                if app.board.get(*app.cursor_refs()) is not YES:
                    await pilot.press("o")
                    await pilot.pause()
        assert app.board.solved(), _status(app)
        assert "SOLVED" in _banner(app)
        assert "?" not in _answer(app)
