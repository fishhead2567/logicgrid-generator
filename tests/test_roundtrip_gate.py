"""Prove the round-trip gate catches semantic drift -- offline, no API calls.

These are the tests that justify spending money on the pipeline.  Each one
hand-writes what an extractor would return for a *drifted* narrative and asserts
the gate rejects it, naming the kind of drift.  If these pass, the gate works;
whether a given narrative drifts is then just a question of what the model
writes.

The honest division of labour between the gates:

**The oracle catches drift exactly when the drifted clue set no longer has the
original solution as its unique model.** In practice that covers most real
mistakes, and it fires through three different symptoms -- no solution, several
solutions, or one solution that is the wrong one. Which symptom appears depends
on the puzzle, not on the kind of drift, so these tests assert "rejected" rather
than predicting the symptom.

**The oracle is blind to drift that leaves the original solution still unique.**
Two cases do that:

* tightening a clue the answer happens to satisfy ("earlier than" -> "just
  before", where they really are adjacent);
* loosening a clue whose work is already done by the others (dropping
  "immediately" from a chain that is pinned at both ends anyway).

Both leave a puzzle that is solvable to the right answer -- so they are not
*broken* -- but they are a different puzzle, usually an easier one. Only
agreement between independent readers reveals them, which is what
:func:`consensus_drift` is for.

Both of those cases are pinned down below, so the blind spot cannot quietly
widen.
"""

from __future__ import annotations

import json

import pytest

from logicgrid import (
    Adjacent,
    Before,
    Category,
    Clue,
    ImmediatelyBefore,
    Link,
    NotLink,
    Puzzle,
    Ref,
    Schema,
    Solution,
    count_solutions,
)
from logicgrid.verify import (
    FAIL,
    PASS,
    PASS_EQUIVALENT,
    consensus_drift,
    failure_report,
    judge,
    prose_problems,
    verdict_for,
)
from logicgrid.clues import Between, link_closure, normalise_set
from logicgrid.narrate import Narrative

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday")
WOMEN = ("Anne", "Cathy", "Eve", "Fran")
MEN = ("Paul", "Rob", "Stan", "Vern")


def _ref(item: str) -> Ref:
    for cat, items in (("day", DAYS), ("woman", WOMEN), ("man", MEN)):
        if item in items:
            return Ref(cat, item)
    raise KeyError(item)


@pytest.fixture
def puzzle() -> Puzzle:
    schema = Schema(
        [
            Category("day", "Day", DAYS, ordered=True, noun="day",
                     cmp_less="earlier", cmp_more="later", step_noun="day"),
            Category("woman", "Woman", WOMEN, noun="woman"),
            Category("man", "Man", MEN, noun="man"),
        ],
        spine="day",
        entity_noun="couple",
    )
    solution = Solution(
        schema,
        {
            "day": list(DAYS),
            "woman": ["Anne", "Cathy", "Eve", "Fran"],
            "man": ["Paul", "Rob", "Stan", "Vern"],
        },
    )
    clues = (
        Clue((Link(_ref("Anne"), _ref("Monday")),)),
        Clue((Before(_ref("Cathy"), _ref("Eve")),)),
        Clue((ImmediatelyBefore(_ref("Eve"), _ref("Fran")),)),
        Clue((Link(_ref("Paul"), _ref("Anne")),)),
        Clue((Adjacent(_ref("Rob"), _ref("Stan")),)),
        Clue((Link(_ref("Vern"), _ref("Thursday")),)),
        Clue((NotLink(_ref("Rob"), _ref("Wednesday")),)),
    )
    p = Puzzle(
        pid="test0001",
        title="A Test Of Weddings",
        theme="test",
        blurb="A fixture.",
        schema=schema,
        solution=solution,
        clues=clues,
        profile="moderate",
        score=5.0,
        rating=4,
        seed=0,
    )
    p.verify()  # the fixture really is a valid, uniquely-solvable puzzle
    return p


# ---------------------------------------------------------------------------
# helpers to fabricate what an extractor would return
# ---------------------------------------------------------------------------


def _fact(kind: str, *args: str, **kw) -> dict:
    return {
        "kind": kind,
        "args": list(args),
        "k": kw.get("k"),
        "rel": kw.get("rel"),
        "op": kw.get("op"),
        "same": kw.get("same"),
        "sub": kw.get("sub"),
    }


def _reply(facts: list[dict], *, cast: bool = True) -> str:
    cats = (
        [
            {"label": "Day", "members": list(DAYS), "ordered": True},
            {"label": "Woman", "members": list(WOMEN), "ordered": False},
            {"label": "Man", "members": list(MEN), "ordered": False},
        ]
        if cast
        else [
            {"label": "Day", "members": list(DAYS), "ordered": True},
            {"label": "Woman", "members": ["Anne", "Cathy", "Eve"], "ordered": False},
            {"label": "Man", "members": list(MEN), "ordered": False},
        ]
    )
    return json.dumps(
        {
            "subject_count": 4,
            "categories": cats,
            "clues": [{"number": i + 1, "facts": [f]} for i, f in enumerate(facts)],
        }
    )


FAITHFUL = [
    _fact("link", "Anne", "Monday"),
    _fact("before", "Cathy", "Eve"),
    _fact("immediately_before", "Eve", "Fran"),
    _fact("link", "Paul", "Anne"),
    _fact("adjacent", "Rob", "Stan"),
    _fact("link", "Vern", "Thursday"),
    _fact("not_link", "Rob", "Wednesday"),
]


def _judge(puzzle, facts, index=0, cast=True):
    return judge(
        index,
        _reply(facts, cast=cast),
        puzzle.schema,
        puzzle.clues,
        puzzle.solution,
        model="test",
    )


# ---------------------------------------------------------------------------
# the happy path
# ---------------------------------------------------------------------------


def test_faithful_reading_passes_every_check(puzzle):
    reading = _judge(puzzle, FAITHFUL)
    assert reading.error == ""
    assert reading.solution_ok
    assert reading.ir_ok
    assert reading.ok, [str(c) for c in reading.checks]
    assert reading.solutions == 1


def test_three_faithful_readings_give_a_clean_pass(puzzle):
    readings = [_judge(puzzle, FAITHFUL, i) for i in range(3)]
    assert verdict_for(readings, required=3) == PASS


# ---------------------------------------------------------------------------
# drift the solution gate catches
# ---------------------------------------------------------------------------


def test_loosening_is_rejected_even_when_it_stays_unique(puzzle):
    """'immediately before' narrated as plain 'before' -- the classic loosening.

    Note what actually happens here: ``Cathy < Eve`` and ``Eve < Fran`` already
    pin the three women to positions 1, 2, 3, so dropping "immediately" leaves
    the puzzle *still* uniquely solvable with the same answer. The oracle has
    nothing to complain about. The clue set is nonetheless different, and
    consensus between readers is what rejects it.
    """
    drifted = list(FAITHFUL)
    drifted[2] = _fact("before", "Eve", "Fran")
    reading = _judge(puzzle, drifted)
    assert reading.solutions == 1
    assert reading.solution_ok, "the oracle cannot see this one"
    assert not reading.ir_ok

    readings = [_judge(puzzle, drifted, i) for i in range(3)]
    missing, extra, _ = consensus_drift(readings)
    assert any(a.kind == "immediately_before" for a in missing)
    assert any(a.kind == "before" for a in extra)
    assert verdict_for(readings, required=3) == FAIL


def test_swapping_a_clue_for_a_weaker_one_is_rejected(puzzle):
    """Replacing an ordering clue with a bare negative is rejected.

    The symptom here is "unique but different answer" rather than "several
    answers" -- which is the point of not asserting on the symptom. What matters
    is that the reading does not pass.
    """
    drifted = list(FAITHFUL)
    drifted[1] = _fact("not_link", "Cathy", "Tuesday")  # weaker than Cathy < Eve
    reading = _judge(puzzle, drifted)
    assert not reading.solution_ok
    assert verdict_for([reading] * 3, required=3) == FAIL


def test_reversing_a_direction_is_caught(puzzle):
    """'the day after Eve' reversed into 'the day before Eve'."""
    drifted = list(FAITHFUL)
    drifted[2] = _fact("immediately_before", "Fran", "Eve")
    reading = _judge(puzzle, drifted)
    assert not reading.solution_ok
    assert verdict_for([reading] * 3, required=3) == FAIL


def test_tightening_into_a_contradiction_is_caught(puzzle):
    """'earlier than' narrated as 'immediately before' where they are not adjacent."""
    drifted = list(FAITHFUL)
    # Anne is Monday and Vern is Thursday: three apart, so adjacency is false.
    drifted[0] = _fact("adjacent", "Anne", "Vern")
    reading = _judge(puzzle, drifted)
    assert not reading.solution_ok
    assert reading.solutions == 0
    detail = next(c.detail for c in reading.checks if c.name == "solution")
    assert "NO solution" in detail


def test_dropping_a_fact_is_caught(puzzle):
    drifted = [f for f in FAITHFUL if f["kind"] != "not_link"]
    reading = _judge(puzzle, drifted)
    assert not reading.solution_ok
    assert reading.solutions > 1


def test_the_off_by_one_gap_trap_is_caught(puzzle):
    """'one day apart' (k=1) vs 'one day between them' (k=2).

    The drifted version turns out to still have exactly one solution -- but a
    different one (Cathy on Thursday, Eve on Tuesday, Fran on Wednesday). The
    gate rejects it on the "unique, but it is a DIFFERENT answer" branch, which
    is why that branch exists at all.
    """
    base = list(FAITHFUL)
    base[1] = _fact("gap", "Cathy", "Eve", k=1, rel="eq")
    truthful = _judge(puzzle, base)
    assert truthful.solutions == 1  # Cathy and Eve really are one apart
    assert truthful.solution_ok

    base[1] = _fact("gap", "Cathy", "Eve", k=2, rel="eq")
    drifted = _judge(puzzle, base)
    assert not drifted.solution_ok
    assert "DIFFERENT answer" in next(
        c.detail for c in drifted.checks if c.name == "solution"
    )
    assert verdict_for([drifted] * 3, required=3) == FAIL


def test_renaming_the_cast_fails_to_parse(puzzle):
    drifted = list(FAITHFUL)
    drifted[0] = _fact("link", "Annie", "Monday")  # Anne -> Annie
    reading = _judge(puzzle, drifted)
    assert not reading.solution_ok
    assert "Annie" in reading.error
    assert verdict_for([reading] * 3, required=3) == FAIL


def test_losing_a_cast_member_fails_the_cast_check(puzzle):
    reading = _judge(puzzle, FAITHFUL, cast=False)
    cast = next(c for c in reading.checks if c.name == "cast")
    assert not cast.passed
    assert "Fran" in cast.detail
    # Solvable or not, a narrative that hides a cast member is rejected.
    assert verdict_for([reading] * 3, required=3) == FAIL


# ---------------------------------------------------------------------------
# drift ONLY consensus catches -- the oracle's blind spot
# ---------------------------------------------------------------------------


def test_consistent_tightening_slips_past_the_solution_gate(puzzle):
    """The blind spot, stated as a test so it cannot regress unnoticed.

    Cathy and Eve happen to be adjacent, so narrating "Cathy is earlier than
    Eve" as "Cathy is just before Eve" leaves the puzzle uniquely solvable with
    the same answer. The oracle cannot see the difference.
    """
    drifted = list(FAITHFUL)
    drifted[1] = _fact("immediately_before", "Cathy", "Eve")
    reading = _judge(puzzle, drifted)
    assert reading.solutions == 1
    assert reading.solution_ok, "the oracle genuinely cannot catch this one"
    assert not reading.ir_ok, "but the clue set is demonstrably different"


def test_consensus_catches_what_the_oracle_cannot(puzzle):
    """All three readers tighten the same clue -> systematic drift -> fail."""
    drifted = list(FAITHFUL)
    drifted[1] = _fact("immediately_before", "Cathy", "Eve")
    readings = [_judge(puzzle, drifted, i) for i in range(3)]
    missing, extra, _ = consensus_drift(readings)
    assert any(a.kind == "before" for a in missing)
    assert any(a.kind == "immediately_before" for a in extra)
    assert verdict_for(readings, required=3) == FAIL


def test_reader_disagreement_is_reported_but_not_fatal(puzzle):
    """Two readers agree, one phrases a clue equivalently -- still solvable.

    ``not_link(Rob, Wednesday)`` and ``not_link(Wednesday, Rob)`` are the same
    atom after normalisation, so to get genuine shape variance we use a
    different-but-equivalent encoding of an adjacency.
    """
    variant = list(FAITHFUL)
    variant[4] = _fact("gap", "Rob", "Stan", k=1, rel="eq")  # == adjacent
    readings = [_judge(puzzle, FAITHFUL, 0), _judge(puzzle, FAITHFUL, 1), _judge(puzzle, variant, 2)]
    missing, extra, disagree = consensus_drift(readings)
    assert disagree
    assert not missing and not extra, "no drift is shared by all three"
    assert all(r.solution_ok for r in readings)
    assert verdict_for(readings, required=3) == PASS_EQUIVALENT
    assert verdict_for(readings, required=3, require_exact_ir=True) == FAIL


def test_symmetric_atoms_normalise_so_argument_order_is_not_drift(puzzle):
    """A reader naming an adjacency the other way round must not be a finding."""
    swapped = list(FAITHFUL)
    swapped[4] = _fact("adjacent", "Stan", "Rob")
    reading = _judge(puzzle, swapped)
    assert reading.ir_ok, "Adjacent(a,b) and Adjacent(b,a) are the same clue"
    assert verdict_for([reading] * 3, required=3) == PASS


# ---------------------------------------------------------------------------
# article tolerance -- normalisation, not drift
# ---------------------------------------------------------------------------


def test_dropped_leading_articles_resolve(puzzle):
    """Prose forces this, so it must not read as a renamed cast.

    An item called "the Last Resort" cannot be written any other way at the
    start of a sentence, and in practice every reader names it without the
    article. That is normalisation; refusing it would burn retries on perfectly
    good narratives.
    """
    schema = Schema(
        [
            Category("place", "Placing", ("first", "second"), ordered=True,
                     noun="placing"),
            Category("boat", "Boat", ("the Last Resort", "the Wet Hen")),
        ],
        spine="place",
    )
    assert schema.try_resolve("Last Resort") == Ref("boat", "the Last Resort")
    assert schema.try_resolve("the Last Resort") == Ref("boat", "the Last Resort")
    assert schema.try_resolve("  LAST RESORT ") == Ref("boat", "the Last Resort")
    assert schema.try_resolve("wet hen") == Ref("boat", "the Wet Hen")


def test_tolerance_does_not_extend_to_real_misnaming(puzzle):
    """The whole point of the parse gate is to catch an invented name."""
    schema = puzzle.schema
    assert schema.try_resolve("Anne") == Ref("woman", "Anne")
    for wrong in ("Annie", "Ann", "Anne-Marie", "Anna", "Wallace", ""):
        assert schema.try_resolve(wrong) is None, wrong


def test_ambiguous_article_stripping_falls_back_to_exact():
    """If two items collide once stripped, neither gets the loose treatment."""
    schema = Schema(
        [
            Category("slot", "Slot", ("one", "two"), ordered=True, noun="slot"),
            Category("horse", "Horse", ("Hen", "the Hen")),
        ],
        spine="slot",
    )
    assert schema.try_resolve("Hen") == Ref("horse", "Hen")
    assert schema.try_resolve("the Hen") == Ref("horse", "the Hen")
    # The colliding loose key resolves to neither rather than guessing.
    assert schema.try_resolve("HEN") is None


def test_cast_check_tolerates_dropped_articles():
    """The cast comparison must use the same tolerance as resolution."""
    schema = Schema(
        [
            Category("place", "Placing", ("first", "second"), ordered=True,
                     noun="placing"),
            Category("boat", "Boat", ("the Last Resort", "the Wet Hen")),
        ],
        spine="place",
    )
    solution = Solution(
        schema,
        {"place": ["first", "second"], "boat": ["the Last Resort", "the Wet Hen"]},
    )
    clues = (Clue((Link(Ref("boat", "the Last Resort"), Ref("place", "first")),)),)
    reply = json.dumps(
        {
            "subject_count": 2,
            "categories": [
                {"label": "Placing", "members": ["first", "second"], "ordered": True},
                # Articles dropped, exactly as the readers did.
                {"label": "Boat", "members": ["Last Resort", "Wet Hen"],
                 "ordered": False},
            ],
            "clues": [
                {
                    "number": 1,
                    "facts": [_fact("link", "Last Resort", "first")],
                }
            ],
        }
    )
    reading = judge(0, reply, schema, clues, solution)
    assert reading.ok, [str(c) for c in reading.checks]


def test_empty_extraction_fails(puzzle):
    reading = _judge(puzzle, [])
    assert not reading.solution_ok
    assert verdict_for([reading] * 3, required=3) == FAIL


def test_malformed_json_fails_to_parse(puzzle):
    reading = judge(0, "not json at all", puzzle.schema, puzzle.clues, puzzle.solution)
    assert not reading.solution_ok
    assert "JSON" in reading.error


# ---------------------------------------------------------------------------
# normalisations the *renderer* makes necessary
#
# Both of these undo a shape difference the renderer introduced, not one the
# reader invented. Without them the gate fails narratives that are perfectly
# faithful, which is exactly what it did: nine of ten narratives in one run
# were rejected for prose the renderer itself had asked for.
# ---------------------------------------------------------------------------


def test_a_pinned_clue_is_compared_as_the_position_it_pins(puzzle):
    """"One day earlier than Wednesday" is rendered "on Tuesday", so a reader
    writes a link. The canonical atom is still an immediately_before, and
    comparing the two shapes directly reports a fact lost and a fact invented
    -- the same fact, twice, in two shapes.
    """
    schema = puzzle.schema
    pinned = ImmediatelyBefore(_ref("Cathy"), _ref("Wednesday"))
    assert normalise_set(schema, [pinned]) == {Link(_ref("Cathy"), _ref("Tuesday"))}
    # Non-vacuity: an entity-to-entity step pins nothing and is left alone.
    plain = ImmediatelyBefore(_ref("Eve"), _ref("Fran"))
    assert normalise_set(schema, [plain]) == {plain}


def test_the_exclusivity_a_between_spells_out_is_dropped(puzzle):
    """[Between.render] ends "matching neither", and some readers write that
    down as its own pair of facts while others treat it as already covered.
    Both are right, so the pair is dropped from whichever side holds it.
    """
    schema = puzzle.schema
    span = Between(_ref("Cathy"), _ref("Monday"), _ref("Thursday"))
    spelled = [span, NotLink(_ref("Cathy"), _ref("Monday")),
               NotLink(_ref("Cathy"), _ref("Thursday"))]
    assert normalise_set(schema, spelled) == normalise_set(schema, [span])


def test_a_not_link_no_between_implies_is_kept(puzzle):
    """Non-vacuity: only the entailment of a between that is actually present
    is dropped. A free-standing negative is a fact in its own right.
    """
    schema = puzzle.schema
    loose = NotLink(_ref("Cathy"), _ref("Monday"))
    assert normalise_set(schema, [loose]) == {loose}
    # ... and the pair is only dropped for the between that implies it, not for
    # any between at all.
    other = Between(_ref("Eve"), _ref("Monday"), _ref("Thursday"))
    assert normalise_set(schema, [other, loose]) == {other, loose}


def test_a_pinned_reading_is_not_reported_as_drift():
    """End to end: a puzzle holding a pinned clue, read exactly as rendered.

    The reader is handed "Eve meets on Wednesday" and writes a link, because
    that is what the sentence says. Before the normalisation this scored 3/3 on
    the solution check and 0/3 on the IR, and the shared shape difference was
    counted as consensus drift -- a fail.
    """
    schema = Schema(
        [
            Category("day", "Day", DAYS, ordered=True, noun="day",
                     cmp_less="earlier", cmp_more="later", step_noun="day"),
            Category("woman", "Woman", WOMEN, noun="woman"),
            Category("man", "Man", MEN, noun="man"),
        ],
        spine="day",
        entity_noun="couple",
    )
    solution = Solution(
        schema,
        {"day": list(DAYS), "woman": list(WOMEN), "man": list(MEN)},
    )
    clues = (
        Clue((Link(_ref("Anne"), _ref("Monday")),)),
        Clue((Before(_ref("Cathy"), _ref("Eve")),)),
        # The pinned clue: Eve sits one day before Thursday, i.e. Wednesday.
        Clue((ImmediatelyBefore(_ref("Eve"), _ref("Thursday")),)),
        Clue((Link(_ref("Paul"), _ref("Anne")),)),
        Clue((Adjacent(_ref("Rob"), _ref("Stan")),)),
        Clue((Link(_ref("Vern"), _ref("Thursday")),)),
        Clue((NotLink(_ref("Rob"), _ref("Wednesday")),)),
    )
    p = Puzzle(
        pid="test0002", title="A Pinned Test", theme="test", blurb="A fixture.",
        schema=schema, solution=solution, clues=clues, profile="moderate",
        score=5.0, rating=4, seed=0,
    )
    p.verify()

    facts = list(FAITHFUL)
    facts[2] = _fact("link", "Eve", "Wednesday")   # what the prose says
    readings = [_judge(p, facts, index=i) for i in range(3)]
    for r in readings:
        assert r.solution_ok, r.checks
        assert not r.missing and not r.extra, (r.missing, r.extra)
    assert verdict_for(readings, required=3) == "pass"


# ---------------------------------------------------------------------------
# a clue that claims two subjects where the grid allows one
# ---------------------------------------------------------------------------
#
# The defect no reading can report. "Haskell presses in January, as does the
# maker accused of acetification" extracts as the two links it is built from,
# so three readers recover the one true solution and the round trip is happy.
# A human reads "as does" as introducing somebody else, rules out the identity
# the clue exists to establish, and hits a contradiction. It shipped once.


def _narrative(*clues: str) -> Narrative:
    return Narrative(
        pid="test0001",
        title="A Test",
        introduction="A scene that constrains nothing.",
        clues=tuple(clues),
    )


@pytest.mark.parametrize(
    "clue",
    [
        "Anne marries on Monday, as does the woman who marries Paul.",
        "Anne marries on Monday, and so does the woman who marries Paul.",
        "Anne marries on Monday. So does the woman who marries Paul.",
        "Anne marries on Monday; likewise the woman who marries Paul.",
        "Anne marries on Monday, and the woman who marries Paul, too.",
        "Anne marries on Monday, and the woman who marries Paul, as well.",
        "Anne marries on Monday, and the same goes for the woman who marries Paul.",
        "Anne marries on Monday. Ditto the woman who marries Paul.",
    ],
)
def test_a_clue_claiming_two_subjects_for_one_is_refused(clue):
    problems = prose_problems(_narrative(clue))
    assert len(problems) == 1, problems
    assert "clue 1" in problems[0]
    assert clue in problems[0]       # the narrator is shown its own sentence


def test_the_merge_a_magazine_wants_is_accepted():
    """The honest merge names the one subject, and must not be flagged.

    This is the phrasing the fix asks the narrator for, so if the check
    rejected it there would be nothing left to write.
    """
    assert prose_problems(_narrative(
        "Anne, who marries Paul, marries on Monday.",
        "Cathy marries earlier than Eve.",
    )) == ()


def test_separate_clues_about_one_item_are_accepted():
    """Two plain facts that pin the same day: the canonical shape.

    No distinctness is claimed, because nothing joins them.
    """
    assert prose_problems(_narrative(
        "Anne marries on Monday.",
        "The woman who marries Paul marries on Monday.",
    )) == ()


def test_also_about_one_subject_is_left_alone():
    """The word "also" is not in the ban list, and must not creep into it.

    Its common use attaches a second fact to the subject already named, which
    is exactly the merge the narrator is told to write.
    """
    assert prose_problems(
        _narrative("Anne marries on Monday, and also marries Paul.")
    ) == ()


def test_the_introduction_is_not_searched():
    """The scene constrains nothing, so a shared predicate there asserts
    nothing that could be wrong."""
    n = Narrative(
        pid="test0001",
        title="A Test",
        introduction="Anne has not spoken to the caterer since the incident, "
        "and neither has the florist; likewise the vicar.",
        clues=("Anne marries on Monday.",),
    )
    assert prose_problems(n) == ()


def test_a_prose_defect_fails_a_narrative_the_readers_approved(puzzle):
    """Every reader passes; the verdict is still fail.

    Both halves matter. If the readings did not pass on their own, this would
    prove nothing about the prose check.
    """
    readings = [_judge(puzzle, FAITHFUL, index=i) for i in range(3)]
    assert verdict_for(readings, required=3) == PASS

    bad = _narrative("Anne marries on Monday, as does the woman who marries Paul.")
    assert prose_problems(bad)

    # What verify_narrative does with the two, minus the API calls.
    verdict = FAIL if prose_problems(bad) else verdict_for(readings, required=3)
    assert verdict == FAIL


def test_the_narrator_is_told_what_to_write_instead(puzzle):
    """The feedback has to carry the remedy, or the retry repeats the mistake."""
    report = failure_report(
        [_judge(puzzle, FAITHFUL, index=i) for i in range(3)],
        puzzle.schema,
        puzzle.clues,
        prose=prose_problems(
            _narrative("Anne marries on Monday, as does the woman who marries Paul.")
        ),
    )
    assert "Name that subject" in report
    assert "separate clues" in report


# ---------------------------------------------------------------------------
# closing the triangle, so the honest merge survives the gate
# ---------------------------------------------------------------------------


def test_the_honest_merge_is_not_reported_as_drift(puzzle):
    """A reader of the merged clue writes the identity and the day.

    The fixture holds "Anne marries on Monday" and "Paul marries Anne". A
    magazine prints those as one clue -- "Anne, who marries Paul, marries on
    Monday" -- and a reader may write the day against Paul rather than Anne.
    Same triangle, different two sides. Without the closure every reader
    differs from the puzzle the same way, and the gate calls that systematic
    drift: a fail earned by writing the clue correctly.
    """
    facts = list(FAITHFUL)
    facts[0] = _fact("link", "Paul", "Monday")   # instead of Anne-Monday
    readings = [_judge(puzzle, facts, index=i) for i in range(3)]
    for r in readings:
        assert r.solution_ok, r.checks
        assert not r.missing and not r.extra, (r.missing, r.extra)
    assert verdict_for(readings, required=3) == PASS


def test_closure_does_not_excuse_a_lost_fact(puzzle):
    """The guard on the test above: closure must not swallow real loss.

    A reader that keeps the day and drops the couple leaves the triangle with
    one side, which implies nothing. The fact is still missing and must be
    reported as missing -- otherwise "it was implied" would excuse anything.
    """
    facts = [
        f for f in FAITHFUL
        if not (f["kind"] == "link" and f["args"] == ["Paul", "Anne"])
    ]
    reading = _judge(puzzle, facts)
    assert any(
        a.kind == "link" and "Paul" in {r.item for r in a.refs()}
        for a in reading.missing
    ), reading.missing


def test_closure_adds_the_third_side_and_nothing_else():
    links = {Link(_ref("Anne"), _ref("Monday")), Link(_ref("Paul"), _ref("Anne"))}
    assert link_closure(links) == links | {Link(_ref("Paul"), _ref("Monday"))}


def test_closure_never_links_two_items_of_one_category():
    """No entity holds two days, so such a link is a contradiction rather than
    an implication -- and inventing one would hand the solver a fact that
    cannot be true. The solver is what should report the contradiction."""
    links = {Link(_ref("Anne"), _ref("Monday")), Link(_ref("Anne"), _ref("Tuesday"))}
    closed = link_closure(links)
    assert Link(Ref("day", "Monday"), Ref("day", "Tuesday")) not in closed
    assert closed == links


def test_closure_leaves_unrelated_links_alone():
    links = {Link(_ref("Anne"), _ref("Monday")), Link(_ref("Rob"), _ref("Tuesday"))}
    assert link_closure(links) == links


def test_closure_does_not_touch_negatives():
    """Deliberately narrow: positive links only.

    A not_link is implied by the triangle too, but widening the closure widens
    what the drift check can no longer see, and nothing needs it.
    """
    atoms = {Link(_ref("Anne"), _ref("Monday")), NotLink(_ref("Paul"), _ref("Tuesday"))}
    assert link_closure(atoms) == atoms


def test_normalise_set_closes_the_triangle(puzzle):
    """Through the function the gate actually calls."""
    two_days = {Link(_ref("Anne"), _ref("Monday")), Link(_ref("Paul"), _ref("Monday"))}
    identity = {Link(_ref("Anne"), _ref("Monday")), Link(_ref("Paul"), _ref("Anne"))}
    assert normalise_set(puzzle.schema, two_days) == normalise_set(
        puzzle.schema, identity
    )


def test_no_published_narrative_claims_two_subjects_for_one():
    """The guard on the shelf, not on the pipeline.

    The gate now refuses these, but the gate only runs when something is
    narrated. Four clues across three published narratives had already got
    past it, and a player found them before any test did. This reads what is
    actually on disk, so a bad clue cannot sit in the repository unnoticed
    however it arrived there.
    """
    import pathlib

    root = pathlib.Path(__file__).resolve().parent.parent / "narratives"
    files = sorted(root.glob("*.json")) if root.is_dir() else []
    if not files:
        pytest.skip("no published narratives in this checkout")

    problems: list[str] = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        for problem in prose_problems(Narrative.from_json(data)):
            problems.append(f"{path.name}: {problem}")
    assert not problems, "\n".join(problems)
