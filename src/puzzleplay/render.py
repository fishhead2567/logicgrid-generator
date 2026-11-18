"""Text blocks for the panels around the grid.

The grid itself is a Textual ``DataTable``; these are the read-only panels
(clues, answer sheet, help) rendered as plain strings so they are trivial to
assert on in tests.
"""

from __future__ import annotations

from textwrap import fill

from logicgrid.model import Ref
from logicgrid.render import canonical_intro, clue_text

from .board import YES, Board

MARK_YES = "O"
MARK_NO = "x"
MARK_OPEN = "."


def clue_block(puzzle, width: int = 52) -> str:
    """Introduction plus the numbered clues, wrapped for a side panel."""
    out: list[str] = []
    intro = canonical_intro(puzzle).replace("**", "")
    for line in intro.splitlines():
        if line.startswith("- "):
            out += fill(line[2:], width=width, initial_indent="  - ",
                        subsequent_indent="    ").splitlines()
        else:
            out += fill(line, width=width).splitlines()
    out.append("")
    for i, clue in enumerate(puzzle.clues, start=1):
        out += fill(
            clue_text(clue, puzzle.schema),
            width=width,
            initial_indent=f"{i:>2}. ",
            subsequent_indent="    ",
        ).splitlines()
        out.append("")
    return "\n".join(out).rstrip()


def answer_block(board: Board) -> str:
    """The answer sheet: one row per spine position, '?' where unplaced."""
    schema = board.schema
    answer = board.answer()
    cats = list(schema.categories)
    widths = []
    for cat in cats:
        values = [str(v) if v else "?" for v in answer[cat.name]]
        widths.append(min(18, max(len(cat.label), *(len(v) for v in values))))
    rows = [" ".join(f"{c.label[:w]:<{w}}" for c, w in zip(cats, widths))]
    rows.append(" ".join("-" * w for w in widths))
    for i in range(schema.size):
        cells = []
        for cat, w in zip(cats, widths):
            value = answer[cat.name][i]
            cells.append(f"{(str(value) if value else '?')[:w]:<{w}}")
        rows.append(" ".join(cells))
    return "\n".join(rows)


def cell_label(board: Board, a: Ref, b: Ref) -> str:
    """What the cursor is sitting on, for the status line."""
    value = board.get(a, b)
    mark = {None: "unmarked", YES: "marked O (together)", False: "marked x (apart)"}[value]
    return f"{a.item}  /  {b.item}   -- {mark}"


def progress_label(board: Board) -> str:
    placed, total = board.progress()
    return f"{placed}/{total} placed"


HELP = """\
  MOVING            arrows or h/j/k/l      move the cell cursor
                    ] and [                next / previous grid
                    mouse click            jump to a cell

  MARKING           o                      these two go together
                    x                      these two do not
                    space                  cycle  .  ->  O  ->  x  ->  .
                    backspace              clear the cell
                    u                      undo

  PLAYING           c                      check my work so far
                    a                      toggle assist (auto-deduce)
                    r                      reset this puzzle
                    n / p                  next / previous puzzle
                    s                      reveal the solution
                    ?                      this help
                    q                      quit

  Marking a cell O automatically rules out the rest of its row and column --
  that is bookkeeping the rules force, not a deduction. Assist goes further
  and chains deductions for you; it is off by default so the puzzle stays
  yours to solve.
"""
