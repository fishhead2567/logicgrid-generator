"""Generate cross-implementation conformance fixtures for the Kotlin Board port.

Re-writing ``tests/test_board.py`` in Kotlin would test my re-reading of those
tests, not the faithfulness of the port. Instead this walks the real puzzles
through a deterministic sequence of marks and records the *exact* state after
every step. A Kotlin test replays the same sequence and asserts identical
state, so a divergence in forced elimination, in assist, or in conflict
detection is caught at the step it first appears.

    python scripts/board_fixtures.py --out ../logicgrid-android/core/src/test/resources/fixtures

Encoding
--------
Refs are numbered in **schema order** -- ``for cat in categories: for item in
cat.items`` -- so the Kotlin side can rebuild the same indices from the puzzle
JSON alone, with nothing extra to keep in sync. A cell is the single integer
``min*R + max`` over its two ref indices, which makes a whole closure two
sorted int arrays and keeps the fixtures small enough to commit.

Both ``assist`` settings get a trace, because assist is the subtle half: it is
where a fixpoint loop, transitivity and last-cell-standing can all go
quietly wrong.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from logicgrid.generate import Puzzle  # noqa: E402
from logicgrid.model import Ref  # noqa: E402
from puzzleplay.board import NO, YES, Board, Conflict  # noqa: E402

VERSION = 1


def ref_index(puzzle) -> dict[Ref, int]:
    """Refs numbered in schema order. The Kotlin side must match exactly."""
    return {ref: i for i, ref in enumerate(puzzle.schema.all_refs)}


def encode_marks(marks, index: dict[Ref, int], size: int) -> dict:
    yes, no = [], []
    for (a, b), value in marks.items():
        i, j = index[a], index[b]
        cell = min(i, j) * size + max(i, j)
        (yes if value is YES else no).append(cell)
    return {"yes": sorted(yes), "no": sorted(no)}


def trace(puzzle, assist: bool, steps: int, seed: int) -> dict:
    """One deterministic walk, recording full state after every step."""
    board = Board(puzzle, assist=assist)
    index = ref_index(puzzle)
    refs = list(puzzle.schema.all_refs)
    size = len(refs)
    rng = random.Random(seed)

    # Only cross-category pairs are legal cells.
    cells = [
        (a, b)
        for n, a in enumerate(refs)
        for b in refs[n + 1 :]
        if a.cat != b.cat
    ]

    out = []
    for step in range(steps):
        a, b = cells[rng.randrange(len(cells))]
        action = rng.choice(["yes", "yes", "no", "no", "clear"])
        conflict = ""
        try:
            if action == "clear":
                cleared = board.clear_mark(a, b)
                if not cleared:
                    action = "clear_noop"
            else:
                board.set_mark(a, b, YES if action == "yes" else NO)
        except Conflict as exc:
            conflict = str(exc)

        answer = board.answer()
        out.append(
            {
                "step": step,
                "action": action,
                "a": index[a],
                "b": index[b],
                # A conflict must be rejected *and change nothing*, so the
                # state recorded after it is as load-bearing as any other.
                "conflict": bool(conflict),
                "user": encode_marks(board.user_marks, index, size),
                "closure": encode_marks(board.marks, index, size),
                "mistakes": len(board.mistakes()),
                "answerComplete": board.answer_complete(),
                "solved": board.solved(),
                "answer": {k: list(v) for k, v in answer.items()},
            }
        )

    return {"assist": assist, "seed": seed, "steps": out}


def build(puzzles: Path, out: Path, steps: int, limit: int | None) -> int:
    out.mkdir(parents=True, exist_ok=True)
    paths = sorted(puzzles.glob("*.json"))
    if limit:
        # Keep one of every grid shape rather than the first N, so the shapes
        # with the most cells are not the ones left out.
        by_shape: dict[tuple[int, int], Path] = {}
        for path in paths:
            p = Puzzle.from_json(json.loads(path.read_text(encoding="utf-8")))
            by_shape.setdefault((len(p.schema.categories), p.schema.size), path)
        chosen = list(by_shape.values())
        chosen += [p for p in paths if p not in chosen][: max(0, limit - len(chosen))]
        paths = sorted(chosen)

    index_rows = []
    total_bytes = 0
    for path in paths:
        puzzle = Puzzle.from_json(json.loads(path.read_text(encoding="utf-8")))
        seed = int(puzzle.pid[:8], 16)
        fixture = {
            "version": VERSION,
            "pid": puzzle.pid,
            "id": path.stem,
            # The puzzle travels with its own fixture. Self-contained means the
            # Kotlin side cannot be replaying one puzzle against another's
            # trace after a regeneration, and the fixtures stay a fixed
            # contract rather than something that drifts with puzzles/.
            "puzzle": json.loads(path.read_text(encoding="utf-8")),
            "refs": [r.key for r in puzzle.schema.all_refs],
            "solution": puzzle.solution.to_json(),
            "traces": [
                trace(puzzle, False, steps, seed),
                trace(puzzle, True, steps, seed),
            ],
        }
        dest = out / f"{path.stem}.board.json"
        blob = json.dumps(fixture, separators=(",", ":")) + "\n"
        dest.write_text(blob, encoding="utf-8")
        total_bytes += len(blob)
        index_rows.append(
            {
                "file": dest.name,
                "pid": puzzle.pid,
                "categories": len(puzzle.schema.categories),
                "items": puzzle.schema.size,
            }
        )

    (out / "index.json").write_text(
        json.dumps(
            {"version": VERSION, "steps": steps, "fixtures": index_rows}, indent=2
        )
        + "\n",
        encoding="utf-8",
    )

    shapes = sorted({(r["categories"], r["items"]) for r in index_rows})
    print(f"{len(index_rows)} fixtures, {steps} steps x 2 assist modes each")
    print(f"  shapes covered: {', '.join(f'{c}x{i}' for c, i in shapes)}")
    print(f"  {total_bytes / 1024:.0f} KiB -> {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--puzzles", default="puzzles")
    ap.add_argument(
        "--out",
        default="../logicgrid-android/core/src/test/resources/fixtures",
    )
    ap.add_argument("--steps", type=int, default=30)
    ap.add_argument(
        "--limit",
        type=int,
        default=12,
        help="how many puzzles to trace (0 = all); every grid shape is kept",
    )
    args = ap.parse_args()
    return build(
        Path(args.puzzles), Path(args.out), args.steps, args.limit or None
    )


if __name__ == "__main__":
    raise SystemExit(main())
