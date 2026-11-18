"""Text blocks for the panels around the grid.

The grid itself is a Textual ``DataTable``; these are the read-only panels
(clues, answer sheet, help) rendered as plain strings so they are trivial to
assert on in tests.
"""

from __future__ import annotations

from textwrap import fill
from typing import Sequence

from logicgrid.model import Ref
from logicgrid.render import canonical_intro, clue_text

from .board import YES, Board

MARK_YES = "O"
MARK_NO = "x"
MARK_OPEN = "."

_ARTICLES = ("the ", "a ", "an ")


def _strip_article(item: str) -> str:
    low = item.casefold()
    for article in _ARTICLES:
        if low.startswith(article):
            return item[len(article) :]
    return item


def short_labels(items: Sequence[str], cap: int = 10, floor: int = 3) -> list[str]:
    """Shortest prefixes that still tell the items apart.

    Column headers have to name the cross category -- bare 1..N is unreadable --
    but full names do not fit a terminal. Leading articles are dropped first,
    since "a fluted rim" and "a fork-crimped edge" share nothing useful up
    front: stripped, three characters separate them.
    """
    bases = [_strip_article(i) for i in items]
    # A prefix every item shares carries no information: "slot one", "slot two"
    # become "one", "two" rather than "slot o", "slot tw".
    if len(bases) > 1:
        shared = 0
        shortest = min(len(b) for b in bases)
        while shared < shortest and len({b[shared].casefold() for b in bases}) == 1:
            shared += 1
        word = bases[0].rfind(" ", 0, shared + 1)
        if word > 0 and all(len(b) - word - 1 >= 2 for b in bases):
            bases = [b[word + 1 :] for b in bases]
    out = []
    for i, base in enumerate(bases):
        others = [b for j, b in enumerate(bases) if j != i]
        length = floor
        while length < min(cap, len(base)):
            prefix = base[:length].casefold()
            if not any(o.casefold().startswith(prefix) for o in others):
                break
            length += 1
        out.append(base[:length].strip())
    return out


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
                    1 - 9                  jump straight to a grid
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
