"""The round-trip gate: does the narrative still mean the puzzle?

Three independent extractors read the narrative back into formal clues.  Each
reading is then judged on four checks, in increasing order of what they prove:

1. **parse** -- the reading decodes, and every name it uses is part of the cast.
   A failure here means the narrative renamed or invented something.
2. **cast** -- the categories the reader found match the real ones.  This is
   what catches an introduction that dropped a member or mangled a spelling.
3. **solution** -- *the check that matters.* Feed the reader's clue set to the
   uniqueness oracle: it must yield exactly one solution, and that solution must
   be the original.  Pass this and the narrative is provably solvable to the
   right answer, which is the actual requirement.
4. **IR equality** -- the reader's clue set is identical to the original, atom
   for atom.  Stricter than necessary (a differently-shaped but logically
   equivalent reading is perfectly good), so failing this alone is a flag for a
   human, not a rejection.

Hence three verdicts: ``pass`` (every reader agrees down to the IR),
``pass_equivalent`` (every reader recovers the right unique solution, but some
phrased a clue differently) and ``fail``.

Why the solution check beats comparing clue text or clue IR: it is immune to
harmless rewording and fatal to actual drift.  Tighten "earlier" into "just
before" and the clue set usually goes to zero solutions; loosen "immediately
before" into "before" and it usually goes to several.  Either way the oracle
notices, and it notices for the right reason.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

from .clues import Atom
from .csp import Engine, flatten
from .extract import Extraction, ExtractionError, build_request as extract_request, parse_reply
from .llm import ModelConfig
from .model import Schema, Solution
from .narrate import Narrative, narrate

#: Verdicts.
PASS = "pass"
PASS_EQUIVALENT = "pass_equivalent"
FAIL = "fail"


@dataclass(slots=True)
class Check:
    name: str
    passed: bool
    detail: str = ""

    def __str__(self) -> str:  # pragma: no cover - display only
        mark = "ok" if self.passed else "FAIL"
        return f"[{mark}] {self.name}{': ' + self.detail if self.detail else ''}"


@dataclass(slots=True)
class Reading:
    """One extractor's reading, judged."""

    index: int
    model: str
    checks: list[Check] = field(default_factory=list)
    extraction: Extraction | None = None
    solutions: int = 0
    missing: tuple[Atom, ...] = ()
    extra: tuple[Atom, ...] = ()
    error: str = ""

    @property
    def solution_ok(self) -> bool:
        return all(c.passed for c in self.checks if c.name in ("parse", "solution"))

    @property
    def ir_ok(self) -> bool:
        return any(c.name == "ir" and c.passed for c in self.checks)

    @property
    def ok(self) -> bool:
        return all(c.passed for c in self.checks) and not self.error

    def to_json(self) -> dict:
        return {
            "index": self.index,
            "model": self.model,
            "solution_ok": self.solution_ok,
            "ir_ok": self.ir_ok,
            "solutions": self.solutions,
            "checks": [{"name": c.name, "passed": c.passed, "detail": c.detail} for c in self.checks],
            "missing": [a.to_json() for a in self.missing],
            "extra": [a.to_json() for a in self.extra],
            "error": self.error,
        }


@dataclass(slots=True)
class RoundTrip:
    """The verdict on one narrative."""

    pid: str
    verdict: str
    narrative: Narrative
    readings: list[Reading] = field(default_factory=list)
    attempt: int = 1
    required: int = 3

    @property
    def passed(self) -> bool:
        return self.verdict in (PASS, PASS_EQUIVALENT)

    def agreement(self) -> int:
        return sum(1 for r in self.readings if r.solution_ok)

    def drift(self) -> tuple[tuple[Atom, ...], tuple[Atom, ...], bool]:
        return consensus_drift(self.readings)

    def summary(self) -> str:
        n = len(self.readings)
        ir = sum(1 for r in self.readings if r.ir_ok)
        missing, extra, disagree = self.drift()
        bits = [
            f"{self.verdict} (attempt {self.attempt})",
            f"{self.agreement()}/{n} readers recovered the solution",
            f"{ir}/{n} matched the clue set exactly",
        ]
        if missing:
            bits.append(f"{len(missing)} fact(s) lost by EVERY reader")
        if extra:
            bits.append(f"{len(extra)} fact(s) invented by EVERY reader")
        if disagree and not (missing or extra):
            bits.append("readers disagreed with each other")
        return ": ".join(bits[:1]) + " " + ", ".join(bits[1:])

    def feedback(self, schema: Schema, original: Sequence) -> str:
        return failure_report(self.readings, schema, original)

    def to_json(self) -> dict:
        return {
            "pid": self.pid,
            "verdict": self.verdict,
            "attempt": self.attempt,
            "agreement": self.agreement(),
            "narrative": self.narrative.to_json(),
            "readings": [r.to_json() for r in self.readings],
        }


# ---------------------------------------------------------------------------
# judging one reading
# ---------------------------------------------------------------------------


def _cast_check(extraction: Extraction, schema: Schema) -> Check:
    """Did the reader find the real cast?

    Compared through :meth:`Schema.try_resolve`, so a reader that drops a
    leading article -- which prose forces on it, and which every reader does --
    is not mistaken for one that lost a cast member.
    """

    def canon(name: str) -> str:
        ref = schema.try_resolve(name)
        return ref.item if ref else f"?{name}"

    want = {frozenset(c.items) for c in schema.categories}
    got = {frozenset(canon(m) for m in members) for _, members in extraction.categories}
    if want == got:
        return Check("cast", True)
    missing_groups = want - got
    detail_bits = []
    all_items = {i for c in schema.categories for i in c.items}
    found_items = {canon(m) for _, members in extraction.categories for m in members}
    lost = sorted(all_items - found_items)
    invented = sorted(x.lstrip("?") for x in found_items - all_items)
    if lost:
        detail_bits.append(f"members not mentioned: {', '.join(lost)}")
    if invented:
        detail_bits.append(f"members not in the puzzle: {', '.join(invented)}")
    if not detail_bits and missing_groups:
        detail_bits.append("categories were grouped differently")
    if extraction.subject_count and extraction.subject_count != schema.size:
        detail_bits.append(
            f"reader believed there were {extraction.subject_count} subjects, "
            f"not {schema.size}"
        )
    return Check("cast", False, "; ".join(detail_bits))


def judge(
    reading_index: int,
    text: str,
    schema: Schema,
    original: Sequence,
    solution: Solution,
    model: str = "",
) -> Reading:
    """Run all four checks on one extractor reply."""
    out = Reading(index=reading_index, model=model)
    try:
        extraction = parse_reply(text, schema, model=model)
    except ExtractionError as exc:
        out.error = str(exc)
        out.checks.append(Check("parse", False, str(exc)))
        return out
    out.extraction = extraction
    out.checks.append(Check("parse", True, f"{len(extraction.atoms)} facts"))
    out.checks.append(_cast_check(extraction, schema))

    atoms = extraction.atoms
    if not atoms:
        out.checks.append(Check("solution", False, "no facts were extracted"))
        out.checks.append(Check("ir", False, "no facts were extracted"))
        return out

    try:
        count, found = Engine(schema, atoms).count_solutions(limit=2)
    except Exception as exc:  # noqa: BLE001 - a malformed set must not crash a run
        out.checks.append(Check("solution", False, f"could not be solved: {exc}"))
        out.checks.append(Check("ir", False, "not compared"))
        return out
    out.solutions = count

    if count == 0:
        out.checks.append(
            Check(
                "solution",
                False,
                "the reader's clue set has NO solution -- a clue was read as "
                "stronger than it is",
            )
        )
    elif count > 1:
        out.checks.append(
            Check(
                "solution",
                False,
                f"the reader's clue set has {count}+ solutions -- a clue was read "
                "as weaker than it is, or one was lost",
            )
        )
    elif found != solution:
        out.checks.append(
            Check("solution", False, "unique, but it is a DIFFERENT answer")
        )
    else:
        out.checks.append(Check("solution", True, "unique, and the right answer"))

    want = set(flatten(original))
    got = set(atoms)
    out.missing = tuple(sorted(want - got, key=lambda a: repr(a.to_json())))
    out.extra = tuple(sorted(got - want, key=lambda a: repr(a.to_json())))
    if not out.missing and not out.extra:
        out.checks.append(Check("ir", True, "identical clue set"))
    else:
        out.checks.append(
            Check(
                "ir",
                False,
                f"{len(out.missing)} fact(s) not recovered, {len(out.extra)} added",
            )
        )
    return out


def consensus_drift(
    readings: Sequence[Reading],
) -> tuple[tuple[Atom, ...], tuple[Atom, ...], bool]:
    """Drift every reader shares, plus whether the readers disagree.

    The solution check has one blind spot: *tightening* a clue in a way the
    answer happens to satisfy.  Narrate "Cathy is earlier than Eve" as "Cathy is
    just before Eve" and, if they really are adjacent, the clue set still has
    exactly one solution and it is still the right one -- so the oracle is
    happy, while the puzzle has quietly become a different (easier) puzzle.

    What catches it is agreement between independent readers.  If every reader
    missed the same fact, or every reader invented the same fact, the narrative
    itself drifted; that is systematic and disqualifying.  If the readers merely
    differ from each other, the prose is ambiguous -- also worth knowing, since a
    human solver could read it either way.
    """
    usable = [r for r in readings if r.extraction is not None]
    if not usable:
        return (), (), True
    missing = set(usable[0].missing)
    extra = set(usable[0].extra)
    for r in usable[1:]:
        missing &= set(r.missing)
        extra &= set(r.extra)
    sets = [frozenset(r.extraction.atoms) for r in usable]  # type: ignore[union-attr]
    disagree = len(set(sets)) > 1
    key = lambda a: repr(a.to_json())  # noqa: E731
    return tuple(sorted(missing, key=key)), tuple(sorted(extra, key=key)), disagree


def verdict_for(
    readings: Sequence[Reading],
    required: int = 3,
    require_exact_ir: bool = False,
) -> str:
    """Combine readings into a verdict.

    ``fail`` unless every reader parses the narrative, finds the real cast, and
    recovers the one true solution -- *and* no drift is shared by all readers.
    ``pass`` when the readers additionally agree with the original clue set atom
    for atom; ``pass_equivalent`` when they recover the right puzzle by a
    differently-shaped but equivalent route.
    """
    agreeing = sum(1 for r in readings if r.solution_ok)
    if agreeing < required:
        return FAIL
    if any(not c.passed for r in readings for c in r.checks if c.name == "cast"):
        return FAIL
    missing, extra, _disagree = consensus_drift(readings)
    if missing or extra:
        return FAIL
    if all(r.ok for r in readings):
        return PASS
    return FAIL if require_exact_ir else PASS_EQUIVALENT


# ---------------------------------------------------------------------------
# feedback for the narrator
# ---------------------------------------------------------------------------


def _clue_of(atom: Atom, clues: Sequence) -> int | None:
    for i, clue in enumerate(clues):
        if atom in getattr(clue, "atoms", ()):
            return i + 1
    return None


def failure_report(
    readings: Sequence[Reading] | RoundTrip, schema: Schema, original: Sequence
) -> str:
    """A description of what went wrong, written for the narrator to act on.

    Deliberately phrased in terms of meaning rather than notation: the narrator
    was never shown the notation, so telling it that ``before`` became
    ``immediately_before`` would be useless.  It is told which clue drifted and
    in which direction.
    """
    if isinstance(readings, RoundTrip):
        readings = readings.readings
    lines: list[str] = []

    # Lead with drift every reader shares: that is the narrative's own fault and
    # the most actionable thing the narrator can be told.
    missing, extra, disagree = consensus_drift(readings)
    for atom in missing:
        num = _clue_of(atom, original)
        where = f"clue {num}" if num else "a clue"
        lines.append(
            f"- EVERY reader failed to get this fact out of {where}. Your wording "
            f"did not convey it. State it plainly: {atom.gloss(schema)}"
        )
    for atom in extra:
        lines.append(
            f"- EVERY reader read a fact out of your prose that the puzzle does "
            f"NOT contain: {atom.render(schema)} You made a clue stronger or more "
            f"specific than it is. Loosen that wording."
        )
    if disagree and not (missing or extra):
        lines.append(
            "- the readers disagreed with each other about what some clue meant, "
            "so the prose is ambiguous. Make every clue admit one reading only."
        )

    for reading in readings:
        if reading.ok:
            continue
        label = f"Reader {reading.index + 1}"
        if reading.error:
            lines.append(f"- {label} could not even read the puzzle: {reading.error}")
            continue
        for check in reading.checks:
            if not check.passed and check.name in ("cast", "solution"):
                lines.append(f"- {label}: {check.detail}")
        for atom in reading.missing:
            num = _clue_of(atom, original)
            where = f"clue {num}" if num else "a clue"
            lines.append(
                f"- {label} did not get this fact out of {where}. It must be "
                f"unmistakable: {atom.gloss(schema)}"
            )
        for atom in reading.extra:
            lines.append(
                f"- {label} read a fact out of your prose that is NOT in the "
                f"puzzle: {atom.render(schema)} Your wording implied something "
                f"stronger or different than intended."
            )
    if not lines:
        lines.append("- the readings disagreed with each other; make each clue blunter.")
    # Keep the report bounded; a wall of text makes the retry worse, not better.
    if len(lines) > 24:
        lines = lines[:24] + [f"- ... and {len(lines) - 24} further problems."]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# the round trip
# ---------------------------------------------------------------------------


def verify_narrative(
    puzzle,
    narrative: Narrative,
    client,
    *,
    readers: int = 3,
    required: int = 3,
    config: ModelConfig | None = None,
    attempt: int = 1,
    max_workers: int = 3,
    require_exact_ir: bool = False,
) -> RoundTrip:
    """Read one narrative back with ``readers`` independent extractors."""
    text = narrative.to_text()
    requests = [extract_request(text) for _ in range(readers)]
    replies = client.complete_many(requests, config, max_workers=max_workers)
    model = (config or getattr(client, "config", ModelConfig())).model

    readings: list[Reading] = []
    for i, reply in enumerate(replies):
        if isinstance(reply, Exception):
            r = Reading(index=i, model=model, error=str(reply))
            r.checks.append(Check("parse", False, str(reply)))
            readings.append(r)
            continue
        readings.append(
            judge(i, reply, puzzle.schema, puzzle.clues, puzzle.solution, model=model)
        )

    return RoundTrip(
        pid=puzzle.pid,
        verdict=verdict_for(readings, required, require_exact_ir),
        narrative=narrative,
        readings=readings,
        attempt=attempt,
        required=required,
    )


def roundtrip(
    puzzle,
    client,
    *,
    readers: int = 3,
    required: int = 3,
    max_attempts: int = 3,
    narrator_config: ModelConfig | None = None,
    extractor_config: ModelConfig | None = None,
    require_exact_ir: bool = False,
    on_attempt=None,
) -> RoundTrip:
    """Narrate, verify, and retry with feedback until the narrative holds.

    Returns the first passing round trip, or the last failure if none pass.
    """
    previous: Narrative | None = None
    report = ""
    last: RoundTrip | None = None

    for attempt in range(1, max_attempts + 1):
        narrative = narrate(
            puzzle,
            client,
            config=narrator_config,
            previous=previous,
            failure_report=report,
            attempt=attempt,
        )
        result = verify_narrative(
            puzzle,
            narrative,
            client,
            readers=readers,
            required=required,
            config=extractor_config,
            attempt=attempt,
            require_exact_ir=require_exact_ir,
        )
        if on_attempt is not None:
            on_attempt(result)
        last = result
        if result.passed:
            return result
        previous = narrative
        report = failure_report(result.readings, puzzle.schema, puzzle.clues)

    assert last is not None
    return last
