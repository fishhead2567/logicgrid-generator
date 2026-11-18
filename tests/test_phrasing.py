"""Clue prose: real sentences rather than "X goes with Y".

A clue only reads well if the categories know what they mean, so each one
carries a third-person verb and both polarities are derived from it. These
tests guard the derivation -- an irregular or past-tense verb slipping into a
theme pack would otherwise ship as "does not contained".
"""

from __future__ import annotations

import pytest

from logicgrid import (
    Adjacent,
    Before,
    Between,
    Category,
    Gap,
    ImmediatelyBefore,
    Link,
    NotLink,
    PuzzleSpec,
    Ref,
    Schema,
    Solution,
    canonical_intro,
    clue_text,
    generate,
)
from logicgrid.model import _AUX, negate_verb, third_person_stem
from logicgrid.themes import THEMES

ALL_VERBS = sorted(
    {t.spine_verb for t in THEMES if t.spine_verb}
    | {a.verb for t in THEMES for a in t.axes if a.verb}
)


# ---------------------------------------------------------------------------
# the verb machinery
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("verb", ALL_VERBS)
def test_every_theme_verb_is_third_person(verb):
    """The negator needs a third-person head: an auxiliary, or something -s.

    "contained" would quietly become "does not contained"; this is the check
    that caught exactly that.
    """
    head = verb.split()[0]
    assert head.casefold() in _AUX or head.endswith("s"), (
        f"{verb!r} is not third-person singular, so it cannot be negated"
    )


@pytest.mark.parametrize("verb", ALL_VERBS)
def test_every_theme_verb_negates_cleanly(verb):
    negative = negate_verb(verb)
    assert negative != verb
    if negative.startswith("does not "):
        stem = negative[len("does not ") :].split()[0]
        assert not stem.endswith("s"), f"{verb!r} -> {negative!r} kept the -s"
        assert stem, f"{verb!r} negated to an empty stem"
    else:
        assert negative.split()[1] == "not", f"{verb!r} -> {negative!r}"


@pytest.mark.parametrize(
    "verb,expected",
    [
        ("harvests in", "does not harvest in"),
        ("is troubled by", "is not troubled by"),
        ("was bought by", "was not bought by"),
        ("flies", "does not fly"),
        ("watches", "does not watch"),
        ("has", "does not have"),
        ("goes with", "does not go with"),
        ("passes", "does not pass"),
    ],
)
def test_negation_examples(verb, expected):
    assert negate_verb(verb) == expected


def test_stem_handles_the_awkward_endings():
    assert third_person_stem("flies") == "fly"
    assert third_person_stem("watches") == "watch"
    assert third_person_stem("passes") == "pass"
    assert third_person_stem("has") == "have"
    assert third_person_stem("is") == "be"


# ---------------------------------------------------------------------------
# clue sentences
# ---------------------------------------------------------------------------

MONTHS = ("January", "February", "March", "April")
GROWERS = ("Leocadia", "Ambrose", "Rowena", "Taavi")
PESTS = ("thrips", "mealybug", "scale insects", "fungus gnats")


@pytest.fixture
def schema() -> Schema:
    return Schema(
        [
            Category("month", "Harvest month", MONTHS, ordered=True, noun="month",
                     cmp_less="earlier", cmp_more="later", step_noun="month",
                     verb="harvests in"),
            Category("grower", "Grower", GROWERS, noun="grower", subject=True),
            Category("pest", "Pest", PESTS, noun="pest", verb="is troubled by"),
        ],
        spine="month",
        entity_noun="grower",
        entity_noun_plural="growers",
    )


def R(item: str) -> Ref:
    for cat, items in (("month", MONTHS), ("grower", GROWERS), ("pest", PESTS)):
        if item in items:
            return Ref(cat, item)
    raise KeyError(item)


def test_a_name_and_a_month_read_as_a_sentence(schema):
    """The complaint that started this: not 'Leocadia goes with April'."""
    assert Link(R("Leocadia"), R("April")).render(schema) == (
        "Leocadia harvests in April."
    )
    assert NotLink(R("Leocadia"), R("April")).render(schema) == (
        "Leocadia does not harvest in April."
    )


def test_the_name_is_the_subject_whichever_way_round_the_atom_is(schema):
    """Link normalises its arguments, so phrasing must not depend on order."""
    forward = Link(R("Leocadia"), R("thrips")).render(schema)
    backward = Link(R("thrips"), R("Leocadia")).render(schema)
    assert forward == backward == "Leocadia is troubled by thrips."


def test_two_attributes_get_a_descriptor_subject(schema):
    """No name in sight, so one attribute names the entity."""
    rendered = Link(R("April"), R("thrips")).render(schema)
    assert rendered == "The grower who is troubled by thrips harvests in April."
    negative = NotLink(R("April"), R("thrips")).render(schema)
    assert negative == (
        "The grower who is troubled by thrips does not harvest in April."
    )


def test_no_clue_uses_a_possessive_on_a_descriptor(schema):
    """'the grower who is troubled by thrips's month' must never appear."""
    atoms = [
        Link(R("April"), R("thrips")),
        NotLink(R("April"), R("thrips")),
        Before(R("thrips"), R("mealybug")),
        ImmediatelyBefore(R("thrips"), R("mealybug")),
        Adjacent(R("thrips"), R("mealybug")),
        Between(R("thrips"), R("mealybug"), R("scale insects")),
        Gap(R("thrips"), R("mealybug"), 2, "eq"),
    ]
    for atom in atoms:
        text = atom.render(schema)
        assert "by's" not in text and "by' " not in text, text
        assert "thrips's" not in text, text


def test_positional_clues_compare_entities(schema):
    assert Before(R("Leocadia"), R("Taavi")).render(schema) == (
        "Leocadia is earlier than Taavi in month order."
    )
    # A spine item on the right is the natural yardstick.
    assert Before(R("Leocadia"), R("April")).render(schema) == (
        "Leocadia is earlier than April in month order."
    )
    # On the left it is flipped so the entity still leads.
    assert Before(R("January"), R("Leocadia")).render(schema) == (
        "Leocadia is later than January in month order."
    )


def test_immediately_before_keeps_its_direction_and_says_so(schema):
    text = ImmediatelyBefore(R("Leocadia"), R("Taavi")).render(schema)
    assert text == (
        "Leocadia is exactly one month earlier than Taavi, "
        "with no month in between."
    )


def test_adjacent_stays_symmetric_in_words(schema):
    text = Adjacent(R("Leocadia"), R("Taavi")).render(schema)
    assert "in one direction or the other" in text
    assert "exactly one month apart" in text


def test_proper_nouns_are_never_recased(schema):
    """The old bundling lowercased the second clause: 'but leocadia does not'."""
    from logicgrid.model import Clue

    clue = Clue(
        (
            Link(R("Leocadia"), R("April")),
            NotLink(R("Leocadia"), R("thrips")),
        ),
        "but_not",
    )
    text = clue_text(clue, schema)
    assert "leocadia" not in text, text
    assert text.count("Leocadia") == 2


# ---------------------------------------------------------------------------
# the introduction
# ---------------------------------------------------------------------------


def test_intro_sets_up_a_task_not_a_schema(schema):
    """It should read like a puzzle, and still carry every condition."""

    class Stub:
        pass

    puzzle = Stub()
    puzzle.schema = schema
    puzzle.blurb = "The orchid house at Fenn Park is a battleground."
    intro = canonical_intro(puzzle)

    assert "Four growers" in intro, intro
    assert "Determine" in intro, intro
    # Every item is still listed.
    for cat in schema.categories:
        for item in cat.items:
            assert item in intro, item
    # The all-different condition and the spine order are still stated.
    assert "different" in intro
    assert "January" in intro and "April" in intro
    assert "There are 4 entries" not in intro


def test_generated_puzzles_read_as_sentences():
    """End to end: no generated clue may fall back to the old phrasing."""
    for difficulty in ("gentle", "moderate", "expert"):
        puzzle = generate(PuzzleSpec(difficulty=difficulty, seed=5))
        intro = canonical_intro(puzzle)
        assert "Determine" in intro
        assert "entries" not in intro or puzzle.schema.entity_noun == "entry"
        for i, clue in enumerate(puzzle.clues, start=1):
            text = clue_text(clue, puzzle.schema)
            assert "goes with" not in text, f"{puzzle.theme} clue {i}: {text}"
            assert "'s's" not in text, f"{puzzle.theme} clue {i}: {text}"
            # A spine value can lead: "300 miles is exactly one hundred ..."
            assert text[0].isupper() or text[0].isdigit() or text[0] in "$([", (
                f"clue {i}: {text}"
            )
            assert text.rstrip().endswith((".", "!")), f"clue {i}: {text}"


def test_distinct_is_not_generated_any_more():
    """Its phrasing collides with the entity noun, so plain negatives do the job.

    "Leocadia, thrips and April are three different growers" is confusing when
    Grower is also a category. The atom stays in the IR -- an extractor may
    legitimately produce it -- but the generator no longer emits it.
    """
    for difficulty in ("easy", "moderate", "hard", "expert"):
        for seed in (1, 2, 3):
            puzzle = generate(PuzzleSpec(difficulty=difficulty, seed=seed))
            kinds = {a.kind for a in puzzle.atoms()}
            assert "distinct" not in kinds, f"{difficulty}/{seed}"


def test_every_shape_keeps_the_names():
    """A puzzle with no subject axis reads entirely in descriptors.

    Axes are sampled, so a 3-category puzzle drawn from a 5-axis theme could
    pick two attributes and leave the names out -- which happened to 7 of the
    first 50 generated puzzles.
    """
    from random import Random

    for theme_pack in THEMES:
        for cats in range(3, theme_pack.max_categories() + 1):
            for seed in range(4):
                schema = theme_pack.build(cats, 4, Random(seed))
                assert any(c.subject for c in schema.categories), (
                    f"{theme_pack.slug} at {cats} categories lost its names"
                )
