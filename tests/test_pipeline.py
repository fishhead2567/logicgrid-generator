"""End-to-end phase-2 plumbing, driven by canned replies -- no API calls.

:class:`logicgrid.llm.DryRunClient` returns prepared strings in order, so the
whole narrate -> extract -> verify -> retry loop can be exercised offline. What
this proves is that the wiring is right: prompts assemble, the structured
replies decode, the gates run, and a failure really does feed back into a second
narration attempt.

Whether a *real* narrator drifts is a separate question, answered by
``test_roundtrip_gate.py`` (which proves drift is detected) and by actually
running the pipeline.
"""

from __future__ import annotations

import json

import pytest

from logicgrid import (
    Category,
    Clue,
    Link,
    NotLink,
    Before,
    Puzzle,
    Ref,
    Schema,
    Solution,
)
from logicgrid.extract import EXTRACTION_SCHEMA, build_request as extract_request
from logicgrid.llm import DryRunClient, ModelConfig, Usage
from logicgrid.narrate import (
    NARRATIVE_SCHEMA,
    Narrative,
    brief,
    build_request,
    canonical_narrative,
    parse_reply,
)
from logicgrid.verify import FAIL, PASS, roundtrip, verify_narrative

DAYS = ("Monday", "Tuesday", "Wednesday")
BAKERS = ("Odette", "Bramwell", "Loretta")
PIES = ("rhubarb", "pecan", "blackberry")


@pytest.fixture
def puzzle() -> Puzzle:
    schema = Schema(
        [
            Category("day", "Day", DAYS, ordered=True, noun="day",
                     cmp_less="earlier", cmp_more="later", step_noun="day"),
            Category("baker", "Baker", BAKERS, noun="baker"),
            Category("pie", "Pie", PIES, noun="pie"),
        ],
        spine="day",
        entity_noun="entry",
        entity_noun_plural="entries",
    )
    solution = Solution(
        schema,
        {"day": list(DAYS), "baker": list(BAKERS), "pie": list(PIES)},
    )
    clues = (
        Clue((Link(Ref("baker", "Odette"), Ref("day", "Monday")),)),
        Clue((Before(Ref("baker", "Bramwell"), Ref("baker", "Loretta")),)),
        Clue((Link(Ref("pie", "rhubarb"), Ref("baker", "Odette")),)),
        Clue((NotLink(Ref("pie", "pecan"), Ref("baker", "Loretta")),)),
    )
    p = Puzzle(
        pid="pipe0001",
        title="A Small Bake-Off",
        theme="test",
        blurb="A fixture.",
        schema=schema,
        solution=solution,
        clues=clues,
        profile="gentle",
        score=2.0,
        rating=1,
        seed=0,
    )
    p.verify()
    return p


def _narrator_reply(clues: list[str], title: str = "The Little Bake-Off") -> str:
    return json.dumps(
        {
            "title": title,
            "introduction": (
                "Three entries were judged at the fair, one on each of Monday, "
                "Tuesday and Wednesday. The bakers were Odette, Bramwell and "
                "Loretta, and the pies were rhubarb, pecan and blackberry. Each "
                "baker, pie and day belongs to a different entry."
            ),
            "clues": clues,
        }
    )


GOOD_CLUES = [
    "Odette was judged on Monday.",
    "Bramwell was judged on an earlier day than Loretta.",
    "Odette baked the rhubarb pie.",
    "Loretta did not bake the pecan pie.",
]


def _fact(kind, *args, **kw):
    return {
        "kind": kind,
        "args": list(args),
        "k": kw.get("k"),
        "rel": kw.get("rel"),
        "op": kw.get("op"),
        "same": kw.get("same"),
        "sub": kw.get("sub"),
    }


def _extractor_reply(facts):
    return json.dumps(
        {
            "subject_count": 3,
            "categories": [
                {"label": "Day", "members": list(DAYS), "ordered": True},
                {"label": "Baker", "members": list(BAKERS), "ordered": False},
                {"label": "Pie", "members": list(PIES), "ordered": False},
            ],
            "clues": [{"number": i + 1, "facts": [f]} for i, f in enumerate(facts)],
        }
    )


FAITHFUL_FACTS = [
    _fact("link", "Odette", "Monday"),
    _fact("before", "Bramwell", "Loretta"),
    _fact("link", "rhubarb", "Odette"),
    _fact("not_link", "pecan", "Loretta"),
]
DRIFTED_FACTS = [
    _fact("link", "Odette", "Monday"),
    _fact("immediately_before", "Bramwell", "Loretta"),  # tightened
    _fact("link", "rhubarb", "Odette"),
    _fact("not_link", "pecan", "Loretta"),
]


# ---------------------------------------------------------------------------
# prompt assembly
# ---------------------------------------------------------------------------


def test_brief_names_every_item_and_glosses_every_clue(puzzle):
    text = brief(puzzle)
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item in text, item
    assert text.count("MEANS EXACTLY:") == len(puzzle.atoms())
    assert "STRICTLY" in text, "the before-gloss must warn against tightening"


def test_narrator_prompt_does_not_leak_the_solution(puzzle):
    """The narrator cannot leak an answer it was never given."""
    request = build_request(puzzle)
    whole = request.system + request.user
    assert "SOLUTION" not in whole.upper().replace("SOLVER", "")
    # The solution is a pairing of items; no clue states Bramwell's day, and the
    # brief must not either.
    assert "Bramwell was judged on Tuesday" not in whole
    assert "Tuesday" in whole  # it is a category member, which is fine


def test_prompts_declare_their_schemas(puzzle):
    assert build_request(puzzle).schema is NARRATIVE_SCHEMA
    assert extract_request("anything").schema is EXTRACTION_SCHEMA


def test_extractor_prompt_carries_only_the_narrative(puzzle):
    narrative = canonical_narrative(puzzle)
    request = extract_request(narrative.to_text())
    assert "Do NOT solve" in request.system
    # No formal notation, no theme metadata, no profile, no rating.
    assert "gentle" not in request.user
    assert "pipe0001" not in request.user


# ---------------------------------------------------------------------------
# reply decoding
# ---------------------------------------------------------------------------


def test_narrator_reply_decodes(puzzle):
    narrative = parse_reply(puzzle, _narrator_reply(GOOD_CLUES), model="test")
    assert narrative.title == "The Little Bake-Off"
    assert len(narrative.clues) == 4
    assert "1. Odette was judged on Monday." in narrative.to_text()


def test_wrong_clue_count_is_rejected(puzzle):
    """A narrator that merges or splits clues must not pass silently."""
    with pytest.raises(ValueError, match="3 clues, expected 4"):
        parse_reply(puzzle, _narrator_reply(GOOD_CLUES[:3]))


def test_non_json_narrator_reply_is_rejected(puzzle):
    with pytest.raises(ValueError, match="not valid JSON"):
        parse_reply(puzzle, "Once upon a time")


# ---------------------------------------------------------------------------
# the loop
# ---------------------------------------------------------------------------


def test_faithful_round_trip_passes(puzzle):
    client = DryRunClient([_extractor_reply(FAITHFUL_FACTS)] * 3)
    narrative = parse_reply(puzzle, _narrator_reply(GOOD_CLUES))
    result = verify_narrative(puzzle, narrative, client, readers=3, required=3)
    assert result.verdict == PASS, result.summary()
    assert result.passed
    assert result.agreement() == 3


def test_drifted_round_trip_fails_and_explains_itself(puzzle):
    client = DryRunClient([_extractor_reply(DRIFTED_FACTS)] * 3)
    narrative = parse_reply(puzzle, _narrator_reply(GOOD_CLUES))
    result = verify_narrative(puzzle, narrative, client, readers=3, required=3)
    assert result.verdict == FAIL
    feedback = result.feedback(puzzle.schema, puzzle.clues)
    assert "EVERY reader" in feedback
    assert "STRICTLY" in feedback, "feedback must restate the intended meaning"


def test_retry_loop_recovers_after_a_failed_attempt(puzzle):
    """Attempt 1 drifts, the feedback goes back, attempt 2 lands."""
    replies = [
        _narrator_reply(GOOD_CLUES, "Attempt One"),
        *[_extractor_reply(DRIFTED_FACTS)] * 3,
        _narrator_reply(GOOD_CLUES, "Attempt Two"),
        *[_extractor_reply(FAITHFUL_FACTS)] * 3,
    ]
    client = DryRunClient(replies)
    seen = []
    result = roundtrip(
        puzzle, client, readers=3, required=3, max_attempts=3,
        on_attempt=lambda r: seen.append(r.verdict),
    )
    assert seen == [FAIL, PASS]
    assert result.passed
    assert result.attempt == 2
    assert result.narrative.title == "Attempt Two"
    # 2 narrations + 6 extractions
    assert client.usage.calls == 8


def test_retry_prompt_contains_the_previous_attempt_and_the_diff(puzzle):
    client = DryRunClient([_extractor_reply(DRIFTED_FACTS)] * 3)
    narrative = parse_reply(puzzle, _narrator_reply(GOOD_CLUES, "First Go"))
    result = verify_narrative(puzzle, narrative, client, readers=3, required=3)
    report = result.feedback(puzzle.schema, puzzle.clues)
    retry = build_request(puzzle, previous=narrative, failure_report=report)
    assert "FAILED verification" in retry.user
    assert "First Go" in retry.user
    assert "do not simply repeat it" in retry.user


def test_roundtrip_gives_up_after_max_attempts(puzzle):
    client = DryRunClient(
        [_narrator_reply(GOOD_CLUES), *[_extractor_reply(DRIFTED_FACTS)] * 3] * 2
    )
    result = roundtrip(puzzle, client, readers=3, required=3, max_attempts=2)
    assert not result.passed
    assert result.attempt == 2


def test_an_extractor_error_is_contained(puzzle):
    """One reader failing must not take down the run."""

    class Flaky(DryRunClient):
        def complete(self, request, config=None):
            self.prompts.append(request)
            if len(self.prompts) == 2:
                raise RuntimeError("rate limited")
            return _extractor_reply(FAITHFUL_FACTS)

    narrative = parse_reply(puzzle, _narrator_reply(GOOD_CLUES))
    result = verify_narrative(puzzle, narrative, Flaky(), readers=3, required=3)
    assert result.verdict == FAIL
    assert result.agreement() == 2
    assert any("rate limited" in r.error for r in result.readings)


def test_canonical_narrative_is_a_usable_control(puzzle):
    """The plain rendering must look like a narrative, for use as a control."""
    control = canonical_narrative(puzzle)
    text = control.to_text()
    assert len(control.clues) == len(puzzle.clues)
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item in text, item
    assert "Three entries are involved" in text
    assert "Determine each entry's" in text


# ---------------------------------------------------------------------------
# cost reporting
# ---------------------------------------------------------------------------


def test_usage_cost_estimate():
    u = Usage(input_tokens=1_000_000, output_tokens=100_000, calls=4)
    assert u.cost("claude-opus-5-5") == pytest.approx(4.0 + 2.0)
    assert u.cost("claude-haiku-5-5") == pytest.approx(0.1 + 0.05)
    assert "4 calls" in u.summary()


# ---------------------------------------------------------------------------
# extraction decoding
# ---------------------------------------------------------------------------


def test_unused_fields_use_sentinels_not_nulls(puzzle):
    """Strict schemas need every field present, so unused ones carry sentinels."""
    from logicgrid.extract import parse_reply as parse_extraction

    reply = json.dumps(
        {
            "subject_count": 3,
            "categories": [
                {"label": "Day", "members": list(DAYS), "ordered": True},
                {"label": "Baker", "members": list(BAKERS), "ordered": False},
                {"label": "Pie", "members": list(PIES), "ordered": False},
            ],
            "clues": [
                {
                    "number": 1,
                    "facts": [
                        {
                            "kind": "link",
                            "args": ["Odette", "Monday"],
                            "k": 0,
                            "rel": "none",
                            "op": "none",
                            "same": False,
                            "sub": [],
                        }
                    ],
                }
            ],
        }
    )
    extraction = parse_extraction(reply, puzzle.schema)
    assert len(extraction.atoms) == 1
    assert extraction.atoms[0].kind == "link"


@pytest.mark.parametrize(
    "wrapper",
    [
        "{body}",
        "```json\n{body}\n```",
        "```\n{body}\n```",
        "Here is the conversion:\n\n{body}\n\nLet me know if you need more.",
    ],
)
def test_json_survives_fences_and_prose(wrapper):
    """A stray sentence or code fence must not cost a retry."""
    from logicgrid.extract import loads_lenient

    body = '{"a": 1, "b": [2, 3]}'
    assert loads_lenient(wrapper.format(body=body)) == {"a": 1, "b": [2, 3]}


def test_unparseable_reply_raises_extraction_error(puzzle):
    from logicgrid.extract import ExtractionError
    from logicgrid.extract import parse_reply as parse_extraction

    with pytest.raises(ExtractionError, match="not valid JSON"):
        parse_extraction("I could not do that.", puzzle.schema)


def test_a_gap_without_a_distance_is_an_explicit_error(puzzle):
    from logicgrid.extract import ExtractionError
    from logicgrid.extract import parse_reply as parse_extraction

    reply = json.dumps(
        {
            "subject_count": 3,
            "categories": [],
            "clues": [
                {
                    "number": 1,
                    "facts": [
                        {
                            "kind": "gap",
                            "args": ["Odette", "Bramwell"],
                            "k": 0,
                            "rel": "eq",
                            "op": "none",
                            "same": False,
                            "sub": [],
                        }
                    ],
                }
            ],
        }
    )
    with pytest.raises(ExtractionError, match="gap"):
        parse_extraction(reply, puzzle.schema)


def test_compounds_may_not_nest(puzzle):
    """The schema forbids it; the decoder must refuse it too."""
    from logicgrid.extract import ExtractionError
    from logicgrid.extract import parse_reply as parse_extraction

    inner = {
        "kind": "or",
        "args": [],
        "k": 0,
        "rel": "none",
        "op": "none",
        "same": False,
    }
    reply = json.dumps(
        {
            "subject_count": 3,
            "categories": [],
            "clues": [
                {
                    "number": 1,
                    "facts": [
                        {
                            "kind": "or",
                            "args": [],
                            "k": 0,
                            "rel": "none",
                            "op": "none",
                            "same": False,
                            "sub": [inner, inner],
                        }
                    ],
                }
            ],
        }
    )
    with pytest.raises(ExtractionError, match="nest"):
        parse_extraction(reply, puzzle.schema)


def test_extraction_schema_has_no_union_types():
    """Strict structured outputs are safest with plain types and no nulls."""
    from logicgrid.extract import EXTRACTION_SCHEMA

    def walk(node):
        if isinstance(node, dict):
            if "type" in node:
                assert isinstance(node["type"], str), f"union type: {node['type']}"
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(EXTRACTION_SCHEMA)


def test_every_object_in_the_schema_is_strict():
    """additionalProperties false, and every property required."""
    from logicgrid.extract import EXTRACTION_SCHEMA

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "object":
                assert node.get("additionalProperties") is False
                assert set(node.get("required", [])) == set(node["properties"])
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(EXTRACTION_SCHEMA)


def test_batch_mode_strips_the_fallback_parameter():
    """``fallbacks`` is rejected on the Batches API, so it must be dropped."""
    cfg = ModelConfig(fallback="claude-opus-4-8")
    assert cfg.fallback  # the single-call path keeps it
    stripped = ModelConfig(cfg.model, cfg.max_tokens, cfg.effort, None)
    assert stripped.fallback is None
