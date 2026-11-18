"""The playable Textual app.

Layout: a tab per pair of categories, each a ``DataTable`` with a cell cursor,
the clue list beside it, the answer sheet below, and a status line that always
names the cell you are on -- which is what lets the columns stay narrow enough
to fit a terminal.

Chosen over a web app because this has to be played over SSH: it runs in the
session you are already in, with no port forwarding. Textual's ``run_test``
pilot keeps it testable anyway, which is what ``tests/test_play_app.py`` uses.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.coordinate import Coordinate
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.widgets import (
    DataTable,
    Footer,
    Header,
    Label,
    Static,
    TabbedContent,
    TabPane,
)

from logicgrid.model import Ref

from .board import NO, YES, Board, Conflict
from .library import Library, LibraryError
from .render import (
    HELP,
    answer_block,
    cell_label,
    clue_block,
    progress_label,
    short_labels,
)

CELL_YES = Text("O", style="bold green")
CELL_NO = Text("x", style="red")
CELL_OPEN = Text(".", style="dim")
CELL_STYLES = {YES: CELL_YES, NO: CELL_NO, None: CELL_OPEN}


def _tab_id(cat_a: str, cat_b: str) -> str:
    return f"pair-{cat_a}-{cat_b}".replace("_", "-")


class HelpScreen(ModalScreen[None]):
    """Key bindings, over the top of the game."""

    BINDINGS = [("escape,q,question_mark", "dismiss", "Close")]

    def compose(self) -> ComposeResult:
        with Vertical(id="help-box"):
            yield Label("How to play", id="help-title")
            yield Static(HELP)
            yield Label("[dim]press escape to go back[/dim]")


class PlayApp(App[None]):
    """Play the puzzles in a folder."""

    CSS = """
    Screen { layout: vertical; }
    #body { height: 1fr; }
    #left { width: 1fr; min-width: 46; }
    #right { width: 1fr; border-left: solid $panel; padding-left: 1; }
    #clues { padding: 0 1; }
    TabbedContent { height: 1fr; }
    DataTable { height: auto; max-height: 100%; }
    #legend { height: auto; padding: 0 1; color: $text-muted; }
    #answer { height: auto; border-top: solid $panel; padding: 0 1; color: $text; }
    #status { height: auto; padding: 0 1; background: $panel; }
    #banner { height: auto; padding: 0 1; }
    #help-box {
        width: 80; height: auto; padding: 1 2;
        background: $surface; border: thick $accent;
    }
    #help-title { text-style: bold; }
    """

    BINDINGS = [
        ("o", "mark_yes", "O together"),
        ("x", "mark_no", "x apart"),
        ("space", "cycle", "cycle"),
        ("backspace,delete", "clear_cell", "clear"),
        ("u", "undo", "undo"),
        ("c", "check", "check"),
        Binding("bracketright,ctrl+right", "next_grid", "next grid", key_display="]"),
        Binding("bracketleft,ctrl+left", "prev_grid", "prev grid", key_display="["),
        *(
            Binding(str(d), f"goto_grid({d})", f"grid {d}", show=False)
            for d in range(1, 10)
        ),
        ("a", "assist", "assist"),
        ("r", "reset", "reset"),
        ("n", "next_puzzle", "next"),
        ("p", "prev_puzzle", "prev"),
        ("s", "reveal", "reveal"),
        ("question_mark", "help", "help"),
        ("q", "quit", "quit"),
    ]

    def __init__(self, library: Library, index: int = 0, assist: bool = False) -> None:
        super().__init__()
        self.library = library
        self.index = index % len(library)
        self.start_assist = assist
        self.puzzle = library.puzzle(self.index)
        self.board = Board(self.puzzle, assist=assist)
        self._tabs: dict[str, tuple[str, str]] = {}
        self._announced = False

    # -- layout ----------------------------------------------------------
    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with Horizontal(id="body"):
            with Vertical(id="left"):
                yield TabbedContent(id="grids")
                yield Static(id="legend")
                yield Static(id="answer")
            with VerticalScroll(id="right"):
                yield Static(id="clues")
        yield Static(id="banner")
        yield Static(id="status")
        yield Footer()

    async def on_mount(self) -> None:
        await self._load_puzzle()

    # -- puzzle loading --------------------------------------------------
    def _ordered_pairs(self) -> list[tuple[str, str]]:
        """Spine pairs first -- those are the answer sheet -- then the rest."""
        spine = self.board.schema.spine_name
        with_spine, cross = [], []
        for a, b in self.board.pairs:
            (with_spine if spine in (a, b) else cross).append(
                (b, a) if a == spine else (a, b)
            )
        return with_spine + cross

    async def _load_puzzle(self) -> None:
        """Rebuild everything for the current puzzle.

        ``clear_panes`` and ``add_pane`` are awaitable; not awaiting them races
        the teardown of the old panes against the creation of the new ones,
        which left the tab bar and the grids disagreeing about what exists.
        """
        self.puzzle = self.library.puzzle(self.index)
        self.board = Board(self.puzzle, assist=self.start_assist)
        self._announced = False
        schema = self.board.schema
        self.title = self.puzzle.title
        self.sub_title = (
            f"{self.index + 1}/{len(self.library)} - {self.puzzle.profile} "
            f"{self.puzzle.rating}/7 - {len(schema.categories)}x{schema.size}"
        )

        tabs = self.query_one("#grids", TabbedContent)
        await tabs.clear_panes()
        self._tabs = {}
        for cat_a, cat_b in self._ordered_pairs():
            rows = schema.by_name[cat_a]
            cols = schema.by_name[cat_b]
            tab_id = _tab_id(cat_a, cat_b)
            self._tabs[tab_id] = (cat_a, cat_b)
            table: DataTable = DataTable(cursor_type="cell", zebra_stripes=True)
            table.add_column(
                rows.label,
                key="__label__",
                width=max(10, min(22, max(len(i) for i in rows.items))),
            )
            # Name the cross category in the headers. Bare 1..N was the single
            # most confusing thing about the first version.
            for item, short in zip(cols.items, short_labels(cols.items)):
                table.add_column(short, key=item, width=max(3, len(short)))
            for item in rows.items:
                table.add_row(item, *([CELL_OPEN] * cols.size), key=item)
            title = (
                rows.label
                if cat_b == schema.spine_name
                else f"{rows.label[:7]}/{cols.label[:7]}"
            )
            pane = TabPane(title, table, id=tab_id)
            await tabs.add_pane(pane)
        first = next(iter(self._tabs), None)
        if first is not None:
            tabs.active = first

        self.query_one("#clues", Static).update(clue_block(self.puzzle, width=56))
        self._refresh()
        self.call_after_refresh(self._focus_table)

    def _focus_table(self) -> None:
        table = self._active_table()
        if table is not None:
            table.focus()

    # -- state -----------------------------------------------------------
    def _active_table(self) -> DataTable | None:
        tabs = self.query_one("#grids", TabbedContent)
        pane = tabs.active_pane
        if pane is None:
            return None
        try:
            return pane.query_one(DataTable)
        except Exception:  # pragma: no cover - pane not yet mounted
            return None

    def _active_pair(self) -> tuple[str, str] | None:
        tabs = self.query_one("#grids", TabbedContent)
        return self._tabs.get(tabs.active)

    def cursor_refs(self) -> tuple[Ref, Ref] | None:
        """The two items the cell cursor is on."""
        table = self._active_table()
        pair = self._active_pair()
        if table is None or pair is None or not table.row_count:
            return None
        cat_a, cat_b = pair
        coord = table.cursor_coordinate
        col = coord.column - 1  # column 0 is the row label
        if col < 0:
            col = 0
        rows = self.board.schema.by_name[cat_a].refs()
        cols = self.board.schema.by_name[cat_b].refs()
        if not (0 <= coord.row < len(rows)) or not (0 <= col < len(cols)):
            return None
        return rows[coord.row], cols[col]

    def _refresh(self) -> None:
        """Repaint every grid, the answer sheet and the status line.

        Marks cascade across grids (an O rules out a row and column, and assist
        chains further), so repainting everything is both simplest and correct.
        """
        tabs = self.query_one("#grids", TabbedContent)
        for tab_id, (cat_a, cat_b) in self._tabs.items():
            try:
                pane = tabs.get_pane(tab_id)
                table = pane.query_one(DataTable)
            except Exception:  # pragma: no cover - during teardown
                continue
            rows = self.board.schema.by_name[cat_a].refs()
            cols = self.board.schema.by_name[cat_b].refs()
            for r, a in enumerate(rows):
                for c, b in enumerate(cols):
                    table.update_cell_at(
                        Coordinate(r, c + 1), CELL_STYLES[self.board.get(a, b)]
                    )
        self.query_one("#answer", Static).update(answer_block(self.board))
        self._refresh_legend()
        self._refresh_status()
        self._check_completion()

    def _refresh_legend(self) -> None:
        """Spell out the abbreviated column headers, and number the grids."""
        pair = self._active_pair()
        if pair is None:
            return
        _cat_a, cat_b = pair
        cols = self.board.schema.by_name[cat_b]
        pairs = [
            f"{short}={item}"
            for short, item in zip(short_labels(cols.items), cols.items)
        ]
        ids = list(self._tabs)
        try:
            number = ids.index(self.query_one("#grids", TabbedContent).active) + 1
        except ValueError:
            number = 0
        head = f"grid {number}/{len(ids)}  " if number else ""
        self.query_one("#legend", Static).update(head + "   ".join(pairs))

    def _refresh_status(self, message: str = "") -> None:
        refs = self.cursor_refs()
        where = cell_label(self.board, *refs) if refs else "-"
        bits = [progress_label(self.board), where]
        if self.board.assist:
            bits.append("assist ON")
        line = "   ".join(bits)
        self.query_one("#status", Static).update(line)
        if message:
            self.query_one("#banner", Static).update(message)

    def _banner(self, message: str) -> None:
        self.query_one("#banner", Static).update(message)

    def _check_completion(self) -> None:
        if not self.board.answer_complete():
            self._announced = False
            return
        if self._announced:
            return
        self._announced = True
        wrong = self.board.mistakes()
        if not wrong:
            self._banner(
                "[bold green]SOLVED[/bold green] - every placing correct. "
                "'n' for the next puzzle."
            )
        else:
            self._banner(
                f"[bold red]Not quite[/bold red] - the sheet is full but "
                f"{len(wrong)} mark(s) are wrong. 'enter' to check, 'u' to undo."
            )

    # -- actions ---------------------------------------------------------
    def _set(self, value: bool | None) -> None:
        refs = self.cursor_refs()
        if refs is None:
            return
        a, b = refs
        try:
            if value is None:
                if not self.board.clear_mark(a, b):
                    self._refresh_status("nothing to clear there")
                    return
            else:
                self.board.set_mark(a, b, value)
        except Conflict as exc:
            self._banner(f"[yellow]{exc}[/yellow]")
            return
        self._banner("")
        self._refresh()

    def action_mark_yes(self) -> None:
        self._set(YES)

    def action_mark_no(self) -> None:
        self._set(NO)

    def action_clear_cell(self) -> None:
        self._set(None)

    def action_cycle(self) -> None:
        refs = self.cursor_refs()
        if refs is None:
            return
        current = self.board.get(*refs)
        self._set({None: YES, YES: NO, NO: None}[current])

    def action_undo(self) -> None:
        if self.board.undo():
            self._banner("")
            self._refresh()
        else:
            self._refresh_status("nothing to undo")

    def action_reset(self) -> None:
        self.board.reset()
        self._banner("board cleared")
        self._refresh()

    def action_assist(self) -> None:
        try:
            self.board.assist = not self.board.assist
        except Conflict as exc:
            self.board.assist = False
            self._banner(f"[yellow]assist found a contradiction: {exc}[/yellow]")
            return
        self._banner(
            "assist ON - deductions will be chained for you"
            if self.board.assist
            else "assist OFF"
        )
        self._refresh()

    def action_check(self) -> None:
        wrong = self.board.mistakes()
        placed, total = self.board.progress()
        if not wrong:
            if self.board.solved():
                self._banner("[bold green]SOLVED[/bold green] - all correct.")
            else:
                self._banner(
                    f"[green]No mistakes so far[/green] - {placed}/{total} placed."
                )
            return
        lines = [
            f"[red]{len(wrong)} mistake(s)[/red]:",
            *(
                f"  {m.a.item} / {m.b.item} is marked "
                f"{'O' if m.value else 'x'} but should be "
                f"{'x' if m.value else 'O'}"
                for m in wrong[:5]
            ),
        ]
        if len(wrong) > 5:
            lines.append(f"  ... and {len(wrong) - 5} more")
        self._banner("\n".join(lines))

    def action_reveal(self) -> None:
        self.board.fill_from_solution()
        self._announced = True
        self._banner("[yellow]solution revealed[/yellow] - 'u' to undo it")
        self._refresh()

    async def action_next_puzzle(self) -> None:
        self.index = (self.index + 1) % len(self.library)
        await self._load_puzzle()

    async def action_prev_puzzle(self) -> None:
        self.index = (self.index - 1) % len(self.library)
        await self._load_puzzle()

    def _step_grid(self, delta: int) -> None:
        ids = list(self._tabs)
        if not ids:
            return
        tabs = self.query_one("#grids", TabbedContent)
        try:
            i = ids.index(tabs.active)
        except ValueError:
            i = 0
        tabs.active = ids[(i + delta) % len(ids)]

    def action_goto_grid(self, number: int) -> None:
        """Jump straight to a grid. Cycling through ten of them was tedious."""
        ids = list(self._tabs)
        if 1 <= number <= len(ids):
            self.query_one("#grids", TabbedContent).active = ids[number - 1]
        else:
            self._refresh_status(f"there is no grid {number}")

    def action_next_grid(self) -> None:
        self._step_grid(1)

    def action_prev_grid(self) -> None:
        self._step_grid(-1)

    def action_help(self) -> None:
        self.push_screen(HelpScreen())

    # -- events ----------------------------------------------------------
    @on(DataTable.CellHighlighted)
    def _cursor_moved(self) -> None:
        self._refresh_status()

    @on(TabbedContent.TabActivated)
    def _tab_changed(self) -> None:
        self.call_after_refresh(self._focus_table)
        self._refresh_legend()
        self._refresh_status()


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="logicgrid-play",
        description="Play logic grid puzzles in the terminal.",
    )
    ap.add_argument(
        "path",
        nargs="?",
        default="puzzles",
        help="puzzle folder or a single puzzle .json (default: puzzles)",
    )
    ap.add_argument("--puzzle", help="start on this puzzle (number, name or substring)")
    ap.add_argument(
        "--assist",
        action="store_true",
        help="chain deductions automatically from the start",
    )
    ap.add_argument("--list", action="store_true", help="list the puzzles and exit")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        library = Library.load(args.path)
        index = library.find(args.puzzle) if args.puzzle else 0
    except LibraryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if args.list:
        for i, path in enumerate(library.paths, start=1):
            puzzle = library.puzzle(i - 1)
            print(
                f"{i:>3}. {path.stem:<22} {puzzle.profile:<9} {puzzle.rating}/7  "
                f"{len(puzzle.schema.categories)}x{puzzle.schema.size}  "
                f"{puzzle.title}"
            )
        return 0
    PlayApp(library, index=index, assist=args.assist).run()
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
