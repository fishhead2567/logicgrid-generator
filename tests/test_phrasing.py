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
        head = verb.split()[0]
        stem = negative[len("does not ") :].split()[0]
        assert stem, f"{verb!r} negated to an empty stem"
        # The defect this guards is do-support applied to a head that was never
        # stripped: "contained" -> "does not contained".  Testing that the stem
        # *changed* catches that, where testing that it does not end in -s
        # also rejects honest stems like "press", "pass", "toss" and "cross".
        assert stem != head, f"{verb!r} -> {negative!r} kept the third-person head"
    else:
        assert negative.split()[1] == "not", f"{verb!r} -> {negative!r}"


@pytest.mark.parametrize(
    "verb,expected",
    [
        ("harvests in", "does not harvest in"),
        ("presses in", "does not press in"),
        ("crosses", "does not cross"),
        ("has grown", "has not grown"),
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
    """The old bundling lowercased the second clause: 'but leocadia does not'.

    That is the invariant, and it still holds. What changed is the count: the
    clue used to be two sentences naming Leocadia twice, and the repeat is now
    dropped in favour of ", and". The old assertion said `count == 2`, which
    pinned the rendering rather than the rule it was there to protect.

    The two are easy to confuse and pull in opposite directions, so both are
    asserted here: the name appears exactly once, in its proper case, and
    nothing anywhere in the clue is a recased version of it.
    """
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
    assert text.count("Leocadia") == 1, text
    assert text == "Leocadia harvests in April, and is not troubled by thrips.", text


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


# ---------------------------------------------------------------------------
# compound clues must offer a real choice
# ---------------------------------------------------------------------------


def test_impossible_disjuncts_are_not_generated():
    """A branch that can never hold is not a choice, it is padding.

    Found by reading a narrated puzzle: "Either the jewel orchid grower
    harvests later than May, or Columbine pots in tree fern fibre" -- where May
    is the last month, so the first branch is unsatisfiable and the clue just
    asserts the second one at twice the length.
    """
    from logicgrid.clues import IfThen, NotBoth, Not, Or
    from logicgrid.generate import is_vacuous

    for difficulty in ("hard", "expert"):
        for seed in (3, 11, 42):
            puzzle = generate(PuzzleSpec(difficulty=difficulty, seed=seed))
            for atom in puzzle.atoms():
                if isinstance(atom, (Or, NotBoth, IfThen)):
                    for part in atom.subatoms():
                        assert not is_vacuous(part, puzzle.schema), (
                            f"{difficulty}/{seed}: {part!r} can never hold"
                        )
                elif isinstance(atom, Not):
                    assert not is_vacuous(atom.inner, puzzle.schema)


def test_is_vacuous_spots_the_endpoint_cases():
    from logicgrid.clues import Adjacent, Before, Gap, ImmediatelyBefore
    from logicgrid.generate import is_vacuous

    schema = Schema(
        [
            Category("month", "Month", MONTHS, ordered=True, noun="month",
                     cmp_less="earlier", cmp_more="later", step_noun="month"),
            Category("grower", "Grower", GROWERS, noun="grower", subject=True),
        ],
        spine="month",
        entity_noun="grower",
    )
    last, first = Ref("month", MONTHS[-1]), Ref("month", MONTHS[0])
    who = Ref("grower", GROWERS[0])
    assert is_vacuous(Before(last, who), schema), "nothing is after the last month"
    assert is_vacuous(ImmediatelyBefore(last, who), schema)
    assert is_vacuous(Gap(who, last, len(MONTHS)), schema), "gap wider than the grid"
    # And the satisfiable ones are left alone.
    assert not is_vacuous(Before(first, who), schema)
    assert not is_vacuous(Adjacent(who, last), schema)
    assert not is_vacuous(Gap(who, last, 2), schema)


def test_no_blurb_counts_the_cast():
    """A blurb must not say how many there are, because it cannot know.

    A blurb is authored once; the puzzle is built at 4, 5 or 6 items.  So
    "six builders" is wrong two times in three, and wrong in the worst way:
    the solver reads "six builders", then reads "Five builders are involved",
    and goes hunting for a builder who was never there.  The intro states the
    cast size already, computed from the schema.

    Counts that are not the cast are fine -- an altitude, a time, people
    writing letters -- so this allows a number word only when the words after
    it make it something other than a tally of the puzzle's actors.
    """
    import re

    from logicgrid.themes import THEMES

    number = re.compile(
        # \S+ rather than \w+: \w stops at the apostrophe, which turns
        # "four o'clock" into the bare token "o".
        r"\b(two|three|four|five|six|seven|eight|nine|ten)\b\s+(\S+)",
        re.I,
    )
    allowed = {
        "thousand",  # "two thousand feet" -- an altitude
        "hundred",
        "o'clock",  # "four o'clock" -- a time
        "people",  # "at least two people are writing letters" -- not the cast
    }
    offenders = []
    for theme in THEMES:
        for count, nxt in number.findall(theme.blurb):
            if nxt.casefold().strip(".,;:!?\"'") not in allowed:
                offenders.append(f"{theme.slug}: {count!r} {nxt!r}")
    assert not offenders, "blurbs that count the cast: " + "; ".join(offenders)


def test_between_names_its_outer_points_in_spine_order():
    """"Between fifth and second" is right, and reads backwards.

    Between's two outer points are unordered and the solver is told so, so
    either arrangement is correct. But `Between.__post_init__` canonicalises
    them by sorting Refs, which is alphabetical -- "fifth" sorts before
    "second" -- and a reader who has just been told the placings run from
    better to worse then has to stop and re-sort the sentence.

    Rendering only. The atom is untouched, so no pid moves.
    """
    import pathlib
    from logicgrid.cli import _load
    from logicgrid.csp import flatten
    from logicgrid.model import Ref
    from logicgrid.render import clue_text

    offenders = []
    checked = 0
    for path in sorted(pathlib.Path("puzzles").glob("*.json")):
        puzzle = _load(path)
        spine = puzzle.schema.spine
        for n, clue in enumerate(puzzle.clues, 1):
            text = clue_text(clue, puzzle.schema)
            for atom in flatten([clue]):
                data = atom.to_json()
                if data["kind"] != "between":
                    continue
                b = Ref(*data["b"].split(":", 1))
                c = Ref(*data["c"].split(":", 1))
                if b.cat != spine.name or c.cat != spine.name:
                    continue  # position is what the solver is working out
                checked += 1
                lo, hi = spine.index(b.item), spine.index(c.item)
                first, second = (b.item, c.item) if lo < hi else (c.item, b.item)
                # Match the between phrase itself, not the two item names
                # anywhere in the clue. A clue carries several facts, and an
                # earlier one routinely mentions the same spine point -- which
                # made the first version of this test report a false offender
                # in 22-fast_food, where "$9" appears in the preceding sentence.
                if f"between {first} and {second} in" not in text:
                    offenders.append(f"{path.stem} c{n}: {text}")
    assert checked >= 3, f"only {checked} spine-to-spine between clues to check"
    assert not offenders, "between reads backwards:\n  " + "\n  ".join(offenders)


def test_between_says_it_is_exclusive():
    """The shipped wording has to settle the reading, because it decides the puzzle.

    "Hartley falls somewhere between first and fourth" invites the inclusive
    reading, and the solver is given no way to tell. It matters more than a
    wording quibble: relax `between` to inclusive and 33 of the 35 puzzles
    that use it stop having a unique solution. A solver who reads it the wrong
    way does not hit a contradiction and back up -- they finish, are told they
    are wrong, and cannot see why.

    The gloss has always said "'Between' is exclusive", but the gloss is
    internal: it feeds the narrator brief and the verifier's feedback, and no
    player ever sees it.
    """
    import pathlib
    from logicgrid.cli import _load
    from logicgrid.csp import flatten
    from logicgrid.render import clue_text

    checked, offenders = 0, []
    for path in sorted(pathlib.Path("puzzles").glob("*.json")):
        puzzle = _load(path)
        for n, clue in enumerate(puzzle.clues, 1):
            if not any(a.to_json()["kind"] == "between" for a in flatten([clue])):
                continue
            checked += 1
            text = clue_text(clue, puzzle.schema)
            if "matching neither" not in text:
                offenders.append(f"{path.stem} c{n}: {text}")
    assert checked >= 20, f"only {checked} between clues found"
    assert not offenders, (
        "between clues that do not say they are exclusive:\n  "
        + "\n  ".join(offenders[:5])
    )


def test_no_clue_names_its_own_subject_twice():
    """"Rose is third. The person in third place does X" is two facts and bad prose.

    Every multi-fact clue in the set shares a referent between its facts, and
    the renderer used to name it once per sentence. Where the shared referent
    opens both sentences, the repeat is dropped and the clauses are joined.

    The guard is deliberately not "no sentence opening repeats", because a
    clue may legitimately carry two facts about two different members of the
    same category -- "The kid who wears snowflake pajamas ... The kid who
    leaves out gingerbread ..." opens twice with "The kid who" and must stay
    two sentences. Only a shared *ref* licenses the join.
    """
    import pathlib
    from logicgrid.cli import _load
    from logicgrid.clues import shared_opening
    from logicgrid.render import clue_text

    offenders, multi = [], 0
    for path in sorted(pathlib.Path("puzzles").glob("*.json")):
        puzzle = _load(path)
        for n, clue in enumerate(puzzle.clues, 1):
            atoms = list(clue.atoms)
            if len(atoms) < 2:
                continue
            multi += 1
            text = clue_text(clue, puzzle.schema)
            for prev, atom in zip(atoms, atoms[1:]):
                a, b = prev.render(puzzle.schema), atom.render(puzzle.schema)
                lead = shared_opening(puzzle.schema, a, prev, b, atom)
                # If the two facts share an opening subject, the rendered clue
                # must not contain that subject followed by a sentence break.
                if lead and f". {lead}" in text:
                    offenders.append(f"{path.stem} c{n}: {text[:120]}")
    assert multi >= 30, f"only {multi} multi-fact clues to check"
    assert not offenders, "clues repeating their own subject:\n  " + "\n  ".join(
        offenders[:5]
    )


def test_a_two_link_chain_is_said_from_the_entity_side(schema):
    """"X is third. The third-place one does Y" becomes "X is third and does Y"."""
    from logicgrid.model import Clue

    # link(flaw, point) and link(name, point): two links meeting at one point.
    clue = Clue((Link(R("thrips"), R("April")), Link(R("Leocadia"), R("April"))), "chain")
    text = clue_text(clue, schema)

    assert text.count("April") == 1, text
    assert text.startswith("Leocadia"), f"should lead with the name: {text}"
    assert ", and " in text, text
    # Both facts still there.
    assert "April" in text and "thrips" in text, text


def test_two_links_that_share_nothing_stay_two_sentences(schema):
    """The rewrite needs a shared point; without one the facts are unrelated."""
    from logicgrid.model import Clue

    clue = Clue((Link(R("Leocadia"), R("April")), Link(R("Ambrose"), R("March"))), "pair")
    text = clue_text(clue, schema)
    assert text.count(".") == 2, text
    assert ", and " not in text, text


def test_the_link_chain_rewrite_keeps_the_same_facts():
    """Equivalence, checked by solving rather than by reading.

    link(S,Y) and link(X,S) is rewritten to link(X,S) and link(X,Y). That is
    sound -- all three refs are one entity either way -- but it is a rewrite
    of a puzzle's clues, so it is worth proving rather than arguing. Every
    puzzle in the set still has exactly one solution, and it is the recorded
    one.
    """
    import pathlib
    from logicgrid.cli import _load
    from logicgrid.clues import rephrase_link_chain
    from logicgrid.csp import count_solutions

    touched = 0
    for path in sorted(pathlib.Path("puzzles").glob("*.json")):
        puzzle = _load(path)
        rewritten = []
        for clue in puzzle.clues:
            atoms = rephrase_link_chain(puzzle.schema, list(clue.atoms))
            if list(atoms) != list(clue.atoms):
                touched += 1
            rewritten.extend(atoms)
        if not rewritten:
            continue
        assert count_solutions(puzzle.schema, rewritten, limit=2) == 1, path.stem
    assert touched >= 2, f"the rewrite fired on {touched} clues, so this proves little"


# ---------------------------------------------------------------------------
# a relation to a literal spine item is a direct fact in disguise
# ---------------------------------------------------------------------------


def test_one_step_from_a_named_month_states_the_month(schema):
    """"Exactly one month earlier than February" is January, said the long way.

    Both ends of an ``immediately_before`` carry a position, so naming one of
    them with a literal spine item fixes the other outright. Rendering that as
    arithmetic makes the solver compute what the clue could have stated -- the
    same defect as a clue naming its subject twice, one layer down.
    """
    assert ImmediatelyBefore(R("Leocadia"), R("February")).render(schema) == (
        "Leocadia harvests in January."
    )
    # And the other way round: the spine item leads, so the entity is after it.
    assert ImmediatelyBefore(R("February"), R("Leocadia")).render(schema) == (
        "Leocadia harvests in March."
    )


def test_the_gloss_describes_the_sentence_the_narrator_is_handed(schema):
    """A gloss contradicting its own sentence is worse than no gloss.

    The narrator gets both, so the gloss for a pinned fact has to talk about
    the position, not about consecutiveness the sentence no longer mentions.
    """
    atom = ImmediatelyBefore(R("Leocadia"), R("February"))
    assert "January" in atom.gloss(schema)
    assert "consecutive" not in atom.gloss(schema)
    # The unpinned case still explains the direction, which is the whole risk.
    plain = ImmediatelyBefore(R("Leocadia"), R("Taavi"))
    assert "do not reverse it" in plain.gloss(schema).casefold()


def test_an_entity_to_entity_step_keeps_its_relation(schema):
    """Non-vacuity: the rewrite must not swallow the ordinary case."""
    text = ImmediatelyBefore(R("Leocadia"), R("Taavi")).render(schema)
    assert "exactly one month earlier" in text
    assert "with no month in between" in text


def test_a_step_off_the_end_of_the_spine_keeps_its_relation(schema):
    """Nothing sits one month before January, so there is no position to state.

    The atom is unsatisfiable, which is the generator's business rather than
    the renderer's; what matters here is that the renderer does not invent a
    month outside the spine.
    """
    text = ImmediatelyBefore(R("Leocadia"), R("January")).render(schema)
    assert "exactly one month earlier" in text
    for month in MONTHS:
        assert f"harvests in {month}" not in text


@pytest.mark.parametrize("month", MONTHS)
def test_an_adjacent_is_never_rewritten_into_a_position(schema, month):
    """Deliberately left alone: the edge is a real, if small, deduction.

    "Leocadia and January are one month apart" pins February just as firmly,
    but only once the solver notices there is no month before January, and
    that noticing is worth keeping.

    Every month is checked, because only three of the four are load-bearing
    and the vacuous one is the tempting case to write. Wiring the pinning
    helper into [Adjacent] leaves "Leocadia and January" alone -- the helper
    reads ``immediately_before``, so January takes it one step off the bottom
    of the spine and it declines. A test using January alone therefore passes
    whether ``adjacent`` is rewritten or not; it was written that way first,
    and the probe that was supposed to break it did not. February and March
    would be rewritten outright *wrongly* -- "one month apart from March" is
    February or April, not February -- and April would be rewritten correctly
    but unwantedly.
    """
    text = Adjacent(R("Leocadia"), R(month)).render(schema)
    assert "exactly one month apart" in text
    assert "in one direction or the other" in text
    for other in MONTHS:
        assert f"harvests in {other}" not in text


@pytest.mark.parametrize("seed", [11, 12, 13, 14, 15, 16])
def test_a_pinned_clue_states_the_position_the_solution_has(seed):
    """The rewrite has to be *right*, not merely plausible.

    Easy to get backwards: ``immediately_before(a, b)`` puts ``b`` after
    ``a``, so a named spine item on the right means the entity sits one step
    *lower*, and on the left one step higher. This checks the rendered
    sentence against the recorded solution, which is the only authority on
    where the entity actually is.
    """
    puzzle = generate(PuzzleSpec(difficulty="easy", seed=seed, strict_band=False))
    schema = puzzle.schema
    checked = 0
    for clue in puzzle.clues:
        for atom in clue.atoms:
            if atom.kind != "immediately_before":
                continue
            refs = atom.refs()
            spine = [r for r in refs if schema.is_spine(r)]
            other = [r for r in refs if not schema.is_spine(r)]
            if len(spine) != 1 or not other:
                continue
            position = puzzle.solution.position(other[0])
            item = schema.spine.items[position]
            assert item in atom.render(schema), (
                f"{atom.render(schema)!r} does not name {item!r}, where the "
                f"solution puts {other[0].key!r}"
            )
            checked += 1
    if checked == 0:
        pytest.skip("this seed produced no clue pinned by a named spine item")
