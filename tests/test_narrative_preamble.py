"""The cast list survives the split between scene and preamble.

The narrator used to be required to restate the whole cast in prose. It is now
required *not* to, and to write two or three sentences of scene instead. That
moved a load-bearing piece of text out of the one field that carried it, and
two things downstream read that field:

  - the extractors, whose cast check is the thing that failed every puzzle in
    the first trial run;
  - the terminal player, which would otherwise show a joke followed by clues
    naming people nobody introduced.

Both read it through ``Narrative.to_text`` / ``Narration.preamble``, so these
are tests that the preamble is actually in there.
"""

from __future__ import annotations

import json
import pathlib

import pytest

from logicgrid.cli import _load
from logicgrid.narrate import Narrative, parse_reply
from logicgrid.render import canonical_intro, canonical_preamble

PUZZLES = pathlib.Path("puzzles")


@pytest.fixture(scope="module")
def puzzle():
    paths = sorted(PUZZLES.glob("*.json"))
    assert paths, "no puzzles to test against"
    return _load(paths[0])


def test_the_preamble_is_the_intro_without_the_blurb(puzzle):
    full = canonical_intro(puzzle)
    bare = canonical_preamble(puzzle)
    assert bare in full
    # The blurb is the scene the narrator replaces; everything else is the
    # part that carries logical weight and must be printed verbatim.
    assert full.removesuffix(bare).strip() == (puzzle.blurb or "").strip()
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item in bare, f"{item!r} missing from the preamble"


def test_a_parsed_narrative_carries_the_cast(puzzle):
    reply = json.dumps(
        {
            "title": "A Title",
            "introduction": "Two sentences of scene. No cast list at all.",
            "clues": ["One clue."],
        }
    )
    narrative = parse_reply(puzzle, reply)

    # The scene names nobody...
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item not in narrative.introduction

    # ...but the text handed to an extractor names everybody.
    text = narrative.to_text()
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item in text, f"{item!r} is not in the extractor's text"


def test_the_preamble_is_canonical_character_for_character(puzzle):
    """Attached from the puzzle, never asked of the narrator, so it cannot drift."""
    narrative = parse_reply(
        puzzle,
        json.dumps({"title": "T", "introduction": "Scene.", "clues": ["c"]}),
    )
    assert narrative.preamble == canonical_preamble(puzzle)


def test_the_preamble_round_trips_through_json(puzzle):
    narrative = parse_reply(
        puzzle,
        json.dumps({"title": "T", "introduction": "Scene.", "clues": ["c"]}),
    )
    again = Narrative.from_json(narrative.to_json())
    assert again.preamble == narrative.preamble
    assert again.to_text() == narrative.to_text()


def test_an_older_narrative_without_a_preamble_still_loads(puzzle):
    """Narratives published before the split have no preamble field."""
    old = Narrative.from_json(
        {"pid": puzzle.pid, "title": "T", "introduction": "Old style.", "clues": ["c"]}
    )
    assert old.preamble == ""
    assert "Old style." in old.to_text()


def test_the_player_shows_the_cast_under_a_narrative(tmp_path, puzzle):
    from puzzleplay.library import Library
    from puzzleplay.render import narrative_block

    puzzles = tmp_path / "puzzles"
    puzzles.mkdir()
    (puzzles / "01.json").write_text(
        json.dumps(puzzle.to_json()), encoding="utf-8"
    )
    narratives = tmp_path / "narratives"
    narratives.mkdir()
    (narratives / "01.json").write_text(
        json.dumps(
            {
                "pid": puzzle.pid,
                "title": "A Title",
                "introduction": "A scene, naming nobody.",
                "preamble": canonical_preamble(puzzle),
                "clues": ["One clue."],
                "verdict": "pass",
            }
        ),
        encoding="utf-8",
    )

    narration = Library.load(puzzles, narratives).narration(0)
    assert narration is not None
    # Whitespace-normalised: the block is hard-wrapped to a panel width, so a
    # long item name is routinely split across two lines. That is correct
    # rendering, and searching the raw text for the name would fail on it.
    block = " ".join(narrative_block(narration, width=72).split())

    assert "A scene, naming nobody." in block
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item in block, f"{item!r} is not shown to the player"
