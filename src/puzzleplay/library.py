"""Finding and loading puzzles from a folder."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from logicgrid.generate import Puzzle


class LibraryError(RuntimeError):
    pass


@dataclass(slots=True)
class Library:
    """The puzzle files in a directory, in filename order."""

    root: Path
    paths: list[Path]

    @classmethod
    def load(cls, root: str | Path) -> "Library":
        root = Path(root)
        if root.is_file():
            return cls(root.parent, [root])
        if not root.is_dir():
            raise LibraryError(f"no such puzzle folder: {root}")
        paths = sorted(p for p in root.glob("*.json") if not p.name.startswith("_"))
        if not paths:
            raise LibraryError(
                f"no puzzle .json files in {root} -- run 'logicgrid gen' first"
            )
        return cls(root, paths)

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
