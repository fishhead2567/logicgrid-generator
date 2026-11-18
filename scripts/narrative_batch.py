"""Drive the narrative round-trip over several puzzles, in three file-based steps.

Lets any model sit in the middle -- subagents, a chat window, another provider --
while the gates stay in code. ``logicgrid narrate --no-dry-run`` does the same
thing against the API; this exists so the loop can be run and inspected without
a key.

    python scripts/narrative_batch.py prepare puzzles/04-pigeon.json ...
    #  -> narratives/work/<stem>/narrator_prompt.txt   for each puzzle
    python scripts/narrative_batch.py ingest
    #  -> narrative.md, and readers/prompt.txt in a directory of its own
    python scripts/narrative_batch.py judge
    #  -> roundtrip.json per puzzle, plus a summary table

The canonical puzzles in ``puzzles/`` are never written to. They are the
logical definition; a narrative is a derived artefact that has to be checked
back against them.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from logicgrid.extract import build_request as extract_request  # noqa: E402
from logicgrid.generate import Puzzle  # noqa: E402
from logicgrid.narrate import Narrative, build_request, parse_reply  # noqa: E402
from logicgrid.render import clue_text  # noqa: E402
from logicgrid.verify import (  # noqa: E402
    consensus_drift,
    failure_report,
    judge,
    verdict_for,
)

ROOT = Path("narratives")
WORK = ROOT / "work"


def _schema_note(request) -> str:
    return (
        f"\n\n{'=' * 70}\nReply with ONLY a JSON object matching this schema, "
        f"no prose and no code fence:\n{json.dumps(request.schema, indent=2)}\n"
    )


def _load(path: Path) -> Puzzle:
    return Puzzle.from_json(json.loads(path.read_text(encoding="utf-8")))


def cmd_prepare(args: argparse.Namespace) -> int:
    WORK.mkdir(parents=True, exist_ok=True)
    for raw in args.puzzles:
        path = Path(raw)
        puzzle = _load(path)
        cell = WORK / path.stem
        (cell / "readers").mkdir(parents=True, exist_ok=True)
        (cell / "replies").mkdir(parents=True, exist_ok=True)
        (cell / "puzzle.json").write_text(
            json.dumps(puzzle.to_json(), indent=2), encoding="utf-8"
        )
        request = build_request(puzzle)
        (cell / "narrator_prompt.txt").write_text(
            f"{request.system}\n\n{'=' * 70}\nTASK\n{'=' * 70}\n\n{request.user}"
            + _schema_note(request),
            encoding="utf-8",
        )
        print(
            f"{path.stem:22s} {puzzle.profile:9s} {puzzle.rating}/7 "
            f"{len(puzzle.schema.categories)}x{puzzle.schema.size} "
            f"{len(puzzle.clues):2d} clues -> {cell / 'narrator_prompt.txt'}"
        )
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    for cell in sorted(WORK.iterdir()):
        reply = cell / "narrator_reply.json"
        if not reply.exists():
            print(f"{cell.name:22s} no narrator_reply.json yet")
            continue
        puzzle = _load(cell / "puzzle.json")
        try:
            narrative = parse_reply(
                puzzle, reply.read_text(encoding="utf-8"), model=args.model
            )
        except ValueError as exc:
            print(f"{cell.name:22s} REJECTED: {exc}")
            continue
        (cell / "narrative.txt").write_text(narrative.to_text(), encoding="utf-8")
        (cell / "narrative.md").write_text(narrative.to_markdown(), encoding="utf-8")
        (cell / "narrative.json").write_text(
            json.dumps(narrative.to_json(), indent=2), encoding="utf-8"
        )
        request = extract_request(narrative.to_text())
        # The reader's directory holds this file and nothing else, so
        # "independent reader" is a fact rather than an instruction.
        (cell / "readers" / "prompt.txt").write_text(
            f"{request.system}\n\n{'=' * 70}\nTASK\n{'=' * 70}\n\n{request.user}"
            + _schema_note(request),
            encoding="utf-8",
        )
        print(
            f"{cell.name:22s} {len(narrative.clues):2d} clues "
            f"(from {len(puzzle.clues)} canonical), "
            f"{len(narrative.to_text()):5d} chars -> readers/prompt.txt"
        )
    return 0


def cmd_judge(args: argparse.Namespace) -> int:
    rows = []
    for cell in sorted(WORK.iterdir()):
        if not (cell / "puzzle.json").exists():
            continue
        puzzle = _load(cell / "puzzle.json")
        replies = sorted((cell / "replies").glob("reader*.json"))
        if not replies:
            print(f"{cell.name:22s} no reader replies yet")
            continue
        readings = [
            judge(
                i,
                p.read_text(encoding="utf-8"),
                puzzle.schema,
                puzzle.clues,
                puzzle.solution,
                model=p.stem,
            )
            for i, p in enumerate(replies)
        ]
        verdict = verdict_for(readings, required=min(args.required, len(readings)))
        missing, extra, disagree = consensus_drift(readings)
        (cell / "roundtrip.json").write_text(
            json.dumps(
                {
                    "pid": puzzle.pid,
                    "verdict": verdict,
                    "readers": len(readings),
                    "solution_ok": sum(1 for r in readings if r.solution_ok),
                    "ir_ok": sum(1 for r in readings if r.ir_ok),
                    "consensus_missing": [a.to_json() for a in missing],
                    "consensus_extra": [a.to_json() for a in extra],
                    "readers_disagree": disagree,
                    "readings": [r.to_json() for r in readings],
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        if verdict != "fail":
            # Publish only what verified. A narrative nobody has checked back
            # against the puzzle has no business being played.
            ROOT.mkdir(parents=True, exist_ok=True)
            narrative = Narrative.from_json(
                json.loads((cell / "narrative.json").read_text(encoding="utf-8"))
                if (cell / "narrative.json").exists()
                else {"title": "", "introduction": "", "clues": []}
            )
            (ROOT / f"{cell.name}.json").write_text(
                json.dumps(
                    {**narrative.to_json(), "verdict": verdict, "pid": puzzle.pid},
                    indent=2,
                ),
                encoding="utf-8",
            )
        rows.append((cell, puzzle, readings, verdict, missing, extra, disagree))

    if not rows:
        return 1
    print(
        f"{'puzzle':22s} {'profile':9s} {'verdict':16s} {'solved':>7s} "
        f"{'exact':>6s}  notes"
    )
    failures = 0
    for cell, puzzle, readings, verdict, missing, extra, disagree in rows:
        n = len(readings)
        notes = []
        if missing:
            notes.append(f"{len(missing)} fact(s) lost by all")
        if extra:
            notes.append(f"{len(extra)} invented by all")
        if disagree and not (missing or extra):
            notes.append("readers differed")
        print(
            f"{cell.name:22s} {puzzle.profile:9s} {verdict:16s} "
            f"{sum(1 for r in readings if r.solution_ok)}/{n:<5d} "
            f"{sum(1 for r in readings if r.ir_ok)}/{n:<4d}  {', '.join(notes)}"
        )
        if verdict == "fail":
            failures += 1
            if args.detail:
                print(failure_report(readings, puzzle.schema, puzzle.clues))
    passed = len(rows) - failures
    print(f"\n{passed}/{len(rows)} narratives verified")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("prepare", help="write a narrator prompt per puzzle")
    p.add_argument("puzzles", nargs="+")
    p.set_defaults(func=cmd_prepare)

    i = sub.add_parser("ingest", help="turn narrator replies into reader prompts")
    i.add_argument("--model", default="subagent")
    i.set_defaults(func=cmd_ingest)

    j = sub.add_parser("judge", help="run the gates over the reader replies")
    j.add_argument("--required", type=int, default=3)
    j.add_argument("--detail", action="store_true", help="print failure feedback")
    j.set_defaults(func=cmd_judge)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
