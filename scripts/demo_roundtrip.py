"""Drive one round-trip by hand, so the loop can be run with any LLM.

Splits the pipeline into three file-based steps.  Useful for proving the design
works before wiring up an API key -- the model in the middle can be a subagent,
a chat window, or anything else that can read a prompt and return JSON.

    python scripts/demo_roundtrip.py dump   puzzles/35-x.json --dir demo
    #  -> demo/narrator_prompt.txt   (hand to a narrator, save reply)
    python scripts/demo_roundtrip.py narrate --dir demo --reply demo/narrator_reply.json
    #  -> demo/narrative.txt, demo/extractor_prompt.txt
    python scripts/demo_roundtrip.py verify --dir demo demo/reader*.json
    #  -> the verdict

``logicgrid narrate --no-dry-run`` does all of this automatically; this script
exists to make each step inspectable.
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
from logicgrid.verify import failure_report, judge, verdict_for  # noqa: E402

PUZZLE = "puzzle.json"
NARRATIVE = "narrative.txt"


def _load_puzzle(path: Path) -> Puzzle:
    return Puzzle.from_json(json.loads(path.read_text(encoding="utf-8")))


def cmd_dump(args: argparse.Namespace) -> int:
    out = Path(args.dir)
    out.mkdir(parents=True, exist_ok=True)
    puzzle = _load_puzzle(Path(args.puzzle))
    (out / PUZZLE).write_text(
        json.dumps(puzzle.to_json(), indent=2), encoding="utf-8"
    )
    request = build_request(puzzle)
    (out / "narrator_prompt.txt").write_text(
        f"{request.system}\n\n{'=' * 70}\nTASK\n{'=' * 70}\n\n{request.user}\n\n"
        f"{'=' * 70}\nReply with ONLY a JSON object matching this schema:\n"
        f"{json.dumps(request.schema, indent=2)}\n",
        encoding="utf-8",
    )
    print(f"{puzzle.title}  ({puzzle.profile}, {puzzle.rating}/7, "
          f"{len(puzzle.clues)} clues)")
    print(f"wrote {out / 'narrator_prompt.txt'}")
    return 0


def cmd_narrate(args: argparse.Namespace) -> int:
    out = Path(args.dir)
    puzzle = _load_puzzle(out / PUZZLE)
    reply = Path(args.reply).read_text(encoding="utf-8")
    narrative = parse_reply(puzzle, reply, model=args.model)
    (out / NARRATIVE).write_text(narrative.to_text(), encoding="utf-8")
    (out / "narrative.md").write_text(narrative.to_markdown(), encoding="utf-8")
    request = extract_request(narrative.to_text())
    (out / "extractor_prompt.txt").write_text(
        f"{request.system}\n\n{'=' * 70}\nTASK\n{'=' * 70}\n\n{request.user}\n\n"
        f"{'=' * 70}\nReply with ONLY a JSON object matching this schema:\n"
        f"{json.dumps(request.schema, indent=2)}\n",
        encoding="utf-8",
    )
    print(f"narrative: {len(narrative.clues)} clues, "
          f"{len(narrative.to_text())} chars -> {out / NARRATIVE}")
    print(f"wrote {out / 'extractor_prompt.txt'}")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    out = Path(args.dir)
    puzzle = _load_puzzle(out / PUZZLE)
    readings = []
    for i, path in enumerate(args.replies):
        text = Path(path).read_text(encoding="utf-8")
        readings.append(
            judge(i, text, puzzle.schema, puzzle.clues, puzzle.solution,
                  model=Path(path).stem)
        )

    for reading in readings:
        print(f"\nreader {reading.index + 1} ({reading.model}):")
        for check in reading.checks:
            print(f"  {check}")
        for atom in reading.missing:
            print(f"  - not recovered: {atom.render(puzzle.schema)}")
        for atom in reading.extra:
            print(f"  + invented:      {atom.render(puzzle.schema)}")

    verdict = verdict_for(readings, required=args.required)
    print(f"\n{'=' * 70}")
    print(f"VERDICT: {verdict}")
    agree = sum(1 for r in readings if r.solution_ok)
    exact = sum(1 for r in readings if r.ir_ok)
    print(f"  {agree}/{len(readings)} readers recovered the one true solution")
    print(f"  {exact}/{len(readings)} matched the clue set atom for atom")
    if verdict == "fail":
        print("\nfeedback that would go back to the narrator:")
        print(failure_report(readings, puzzle.schema, puzzle.clues))
    return 0 if verdict != "fail" else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", default="demo", help="working directory")
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("dump", help="write the narrator prompt")
    d.add_argument("puzzle")
    d.set_defaults(func=cmd_dump)

    n = sub.add_parser("narrate", help="ingest the narrator reply")
    n.add_argument("--reply", required=True)
    n.add_argument("--model", default="subagent")
    n.set_defaults(func=cmd_narrate)

    v = sub.add_parser("verify", help="judge the extractor replies")
    v.add_argument("replies", nargs="+")
    v.add_argument("--required", type=int, default=3)
    v.set_defaults(func=cmd_verify)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
