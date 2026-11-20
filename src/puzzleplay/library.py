"""Finding and loading puzzles from a folder."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from logicgrid.generate import Puzzle


class LibraryError(RuntimeError):
    pass


@dataclass(slots=True)
class Narration:
    """A verified narrative version of a puzzle, for reading in place of clues."""

    title: str
    introduction: str
    clues: tuple[str, ...]
    verdict: str = ""

    @property
    def flagged(self) -> bool:
        """True when the readers recovered the puzzle by differing routes."""
        return self.verdict == "pass_equivalent"


@dataclass(slots=True)
class Library:
    """The puzzle files in a directory, in filename order.

    Optionally paired with a narratives directory. A narrative is only looked
    for by stem, and only ``judge`` writes one there, so anything the player
    offers has already been read back and verified against its puzzle.
    """

    root: Path
    paths: list[Path]
    narratives: Path | None = None

    @classmethod
    def load(
        cls, root: str | Path, narratives: str | Path | None = None
    ) -> "Library":
        root = Path(root)
        if root.is_file():
            paths, base = [root], root.parent
        else:
            if not root.is_dir():
                raise LibraryError(f"no such puzzle folder: {root}")
            paths = sorted(
                p for p in root.glob("*.json") if not p.name.startswith("_")
            )
            if not paths:
                raise LibraryError(
                    f"no puzzle .json files in {root} -- run 'logicgrid gen' first"
                )
            base = root
        if narratives is None:
            guess = base.parent / "narratives"
            narratives = guess if guess.is_dir() else None
        elif narratives is not None:
            narratives = Path(narratives)
            if not narratives.is_dir():
                raise LibraryError(f"no such narratives folder: {narratives}")
        return cls(base, paths, narratives)

    def narration(self, index: int) -> Narration | None:
        """The verified narrative for a puzzle, if one has been published.

        Found by stem, then **confirmed by pid**. The stem alone is not an
        identity: ``45-jam.json`` and ``45-mushroom.json`` are both the
        forty-fifth puzzle of some set, and a reseed reuses the numbers. Pair
        on the filename and a narrative eventually gets served for a puzzle it
        does not describe -- prose about clues that are not on the chart,
        silently, because nothing else would disagree.

        ``scripts/build_content_repo.py`` already refuses that pairing when it
        assembles the content repo. This is the same check on the way in to the
        terminal player, which had been matching on the stem alone.
        """
        if self.narratives is None:
            return None
        path = self.narratives / f"{self.label(index)}.json"
        if not path.exists():
            return None
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("pid") != self.puzzle(index).pid:
                return None
            return Narration(
                title=str(data["title"]),
                introduction=str(data["introduction"]),
                clues=tuple(str(c) for c in data["clues"]),
                verdict=str(data.get("verdict", "")),
            )
        except (OSError, ValueError, KeyError, LibraryError):
            # A malformed narrative is not worth failing a game over; the
            # canonical clues are always there.
            return None

    def narrated_count(self) -> int:
        return sum(1 for i in range(len(self)) if self.narration(i) is not None)

    def __len__(self) -> int:
        return len(self.paths)

    def puzzle(self, index: int) -> Puzzle:
        path = self.paths[index % len(self.paths)]
        try:
            return Puzzle.from_json(json.loads(path.read_text(encoding="utf-8")))
        except (OSError, ValueError, KeyError) as exc:
            raise LibraryError(f"{path.name} is not a readable puzzle: {exc}") from exc

    def find(self, needle: str) -> int:
        """Index by 1-based number, filename stem, or substring of either."""
        if needle.isdigit():
            n = int(needle) - 1
            if not 0 <= n < len(self.paths):
                raise LibraryError(f"puzzle {needle} is out of range (1-{len(self.paths)})")
            return n
        low = needle.casefold()
        for i, path in enumerate(self.paths):
            if path.stem.casefold() == low:
                return i
        hits = [i for i, p in enumerate(self.paths) if low in p.stem.casefold()]
        if len(hits) == 1:
            return hits[0]
        if not hits:
            raise LibraryError(f"no puzzle matching {needle!r}")
        names = ", ".join(self.paths[i].stem for i in hits[:6])
        raise LibraryError(f"{needle!r} matches several puzzles: {names}")

    def label(self, index: int) -> str:
        return self.paths[index % len(self.paths)].stem
