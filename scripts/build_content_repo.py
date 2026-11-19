"""Build the puzzle *content* repo the Android app fetches from.

The content repo is a build artefact, not a second source of truth: this script
regenerates it from ``puzzles/`` and ``narratives/`` so it can always be
rebuilt, and so the generator repo stays the only place puzzles are authored.

    python scripts/build_content_repo.py --out ../logicgrid-puzzles

What it writes:

    manifest.json        everything the app needs to decide what to download
    puzzles/<id>.json    the canonical puzzle (schema, clues, solution)
    narratives/<id>.json the verified narrative, where one exists
    README.md            what the repo is, and the fetch contract

**The app should key progress on ``pid``, not on the filename.** A pid is a
hash of the puzzle's own content, so it survives regeneration and renumbering;
filenames do not. Regenerate the set with a different seed and ``01-kite.json``
may hold an entirely different puzzle, but a pid always means one puzzle.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from logicgrid import __version__  # noqa: E402
from logicgrid.generate import Puzzle  # noqa: E402
from logicgrid.render import canonical_intro, clue_text  # noqa: E402

SCHEMA = 1


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _entry(path: Path, data: bytes) -> dict:
    return {"path": path.as_posix(), "sha256": _sha256(data), "bytes": len(data)}


README = """\
# {name}

Puzzle content for the LogicGrid app. **Generated, not hand-edited** -- rebuilt
from the generator repo with `scripts/build_content_repo.py`.

{count} puzzles, ratings {lo}-{hi}, {narrated} with a verified narrative.
Generated {when} by logicgrid {version}.

## Fetch contract

The app needs no git client. Everything is plain HTTPS against the raw files:

1. `GET manifest.json`
2. Compare each entry's `sha256` with what you have cached.
3. Download only what changed, and verify the hash before replacing a cached
   file. A truncated download must never overwrite a good puzzle.
4. If any step fails, keep using the cache. The app ships an initial set in its
   assets so a first run works with no network at all.

## manifest.json

```json
{{
  "schema": {schema},
  "generated": "<ISO 8601 UTC>",
  "generator": "logicgrid <version>",
  "count": {count},
  "puzzles": [
    {{
      "pid": "<stable content hash -- key your progress on THIS>",
      "id": "<filename stem, NOT stable across regeneration>",
      "title": "...", "theme": "...", "profile": "gentle|easy|moderate|hard|expert",
      "rating": 1, "categories": 3, "items": 4, "clues": 5,
      "puzzle": {{"path": "puzzles/<id>.json", "sha256": "...", "bytes": 0}},
      "narrative": {{"path": "narratives/<id>.json", "sha256": "...", "bytes": 0}}
    }}
  ]
}}
```

`narrative` is absent when a puzzle has none; fall back to the canonical clues,
which every puzzle has.

### Key progress on `pid`

`id` is a filename and moves when the set is regenerated. `pid` is a hash of
the puzzle's content, so it identifies one puzzle for good. Keying completion
on `id` means a regeneration silently marks the wrong puzzles done.

## Puzzle format

`puzzles/<id>.json` carries `schema` (the categories and their items), `clues`
(typed clue atoms), `solution`, and `text` -- the canonical prose, pre-rendered.

**Use `text`.** Rendering a clue from the atoms means re-implementing ~375 lines
of English morphology (irregular verb stems, do-support negation, article
insertion, pluralisation, number words, per-spine comparatives). `text.intro`
and `text.clues` are exactly what the reference terminal player shows, so every
client reads identically. The atoms are there for anything that needs the
logic -- a hint engine, a solver -- not for display. Every puzzle in here has been verified to
have exactly one solution, reachable without guessing unless its profile says
otherwise.

Note that the solution ships with the puzzle, so the app can check answers and
reveal them offline. Anyone reading this repo can therefore read the answers --
a deliberate trade for offline play.

## Narrative format

`narratives/<id>.json` holds `title`, `introduction` and `clues` (prose). Each
one has been read back by three independent extractors and proved to yield the
same unique solution as the canonical clues. `verdict` is `pass`, or
`pass_equivalent` where the readers agreed on the answer by differently-shaped
routes.

## Licence

MIT -- see [LICENSE](LICENSE). That covers the puzzle content here as well as
the manifest.

Logic grid puzzles of this shape are a long-standing magazine format. These are
written in the style of Penny Dell's "Logic Problems", but "Penny Dell" is
someone else's trademark and nothing here is affiliated with or endorsed by
them.
"""


def build(out: Path, puzzles: Path, narratives: Path, init_git: bool) -> int:
    if out.exists():
        for sub in ("puzzles", "narratives"):
            shutil.rmtree(out / sub, ignore_errors=True)
    (out / "puzzles").mkdir(parents=True, exist_ok=True)
    (out / "narratives").mkdir(parents=True, exist_ok=True)

    entries = []
    ratings = []
    narrated = 0
    for path in sorted(puzzles.glob("*.json")):
        raw = path.read_bytes()
        puzzle = Puzzle.from_json(json.loads(raw.decode("utf-8")))
        stem = path.stem

        # Ship the canonical prose alongside the clue IR.
        #
        # Without this a client has to re-implement the renderer to show a
        # puzzle at all -- and that is ~375 lines of English morphology:
        # irregular verb stems, do-support negation, article insertion,
        # -ies/-ves/-es pluralisation, number words, per-spine comparatives.
        # Only 5 of 50 puzzles have a narrative, so the canonical text is the
        # *common* path, not a fallback. Pre-rendering it here keeps that
        # subsystem in one language and guarantees every client shows byte
        # identical wording.
        data = json.loads(raw.decode("utf-8"))
        data["text"] = {
            "intro": canonical_intro(puzzle),
            "clues": [clue_text(clue, puzzle.schema) for clue in puzzle.clues],
        }
        raw = (json.dumps(data, indent=2) + "\n").encode("utf-8")

        dest = out / "puzzles" / f"{stem}.json"
        dest.write_bytes(raw)
        entry = {
            "pid": puzzle.pid,
            "id": stem,
            "title": puzzle.title,
            "theme": puzzle.theme,
            "profile": puzzle.profile,
            "rating": puzzle.rating,
            "categories": len(puzzle.schema.categories),
            "items": puzzle.schema.size,
            "clues": len(puzzle.clues),
            "puzzle": _entry(Path("puzzles") / f"{stem}.json", raw),
        }
        nar = narratives / f"{stem}.json"
        if nar.exists():
            nraw = nar.read_bytes()
            (out / "narratives" / f"{stem}.json").write_bytes(nraw)
            entry["narrative"] = _entry(Path("narratives") / f"{stem}.json", nraw)
            narrated += 1
        entries.append(entry)
        ratings.append(puzzle.rating)

    if not entries:
        print(f"error: no puzzles in {puzzles}", file=sys.stderr)
        return 1

    when = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    manifest = {
        "schema": SCHEMA,
        "generated": when,
        "generator": f"logicgrid {__version__}",
        "count": len(entries),
        "narrated": narrated,
        "puzzles": entries,
    }
    (out / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    (out / "README.md").write_text(
        README.format(
            name=out.name,
            count=len(entries),
            lo=min(ratings),
            hi=max(ratings),
            narrated=narrated,
            when=when,
            version=__version__,
            schema=SCHEMA,
        ),
        encoding="utf-8",
    )

    if init_git and not (out / ".git").exists():
        subprocess.run(["git", "init", "-q"], cwd=out, check=True)

    size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
    print(f"{out}")
    print(f"  {len(entries)} puzzles, {narrated} narrated, ratings "
          f"{min(ratings)}-{max(ratings)}")
    print(f"  manifest.json + {len(entries)} puzzle files + {narrated} narratives")
    print(f"  {size / 1024:.0f} KiB total")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="../logicgrid-puzzles")
    ap.add_argument("--puzzles", default="puzzles")
    ap.add_argument("--narratives", default="narratives")
    ap.add_argument("--no-git", action="store_true")
    args = ap.parse_args()
    return build(
        Path(args.out), Path(args.puzzles), Path(args.narratives), not args.no_git
    )


if __name__ == "__main__":
    raise SystemExit(main())
