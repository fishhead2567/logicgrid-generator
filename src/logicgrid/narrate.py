"""Turn a formal puzzle into a Penny Dell-style narrative.

The hard part is not writing nice prose -- it is writing nice prose that means
*exactly* what the clue meant.  Natural language loves to tighten a constraint:
"earlier than" drifts into "just before", "next to" acquires a direction,
"two apart" becomes "two in between".  Every one of those silently changes the
puzzle, usually into one with no solution or several.

Three things guard against that:

* the narrator is given a **gloss** per atom that spells out what the clue does
  and does not assert, generated from the IR itself (see
  :meth:`logicgrid.clues.Atom.gloss`);
* it is given an explicit list of the specific traps, in the imperative;
* nothing it writes is trusted -- :mod:`logicgrid.verify` reads the narrative
  back with independent extractors and re-proves the puzzle.

The narrator never sees the solution.  It cannot leak what it does not know.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .llm import ModelConfig, Request
from .render import canonical_intro, clue_glosses, clue_text

SYSTEM = """\
You are a puzzle editor for a logic-problem magazine in the Penny Dell tradition.

You will be given a logic grid puzzle in formal notation. Your job is to dress
it as a magazine problem: a short, characterful introduction followed by a
numbered clue list. A solver should be able to solve your version using only
what you write, and should arrive at exactly the same answer as the formal
version.

THE ONE RULE THAT MATTERS: you are rewriting, not editing. Every clue must
assert precisely what the formal clue asserts -- no stronger, no weaker, nothing
added, nothing dropped. Charm is welcome in the introduction and in word choice.
It is never welcome in the logical content.

INTRODUCTION REQUIREMENTS

The introduction carries logical weight. It must state, in flowing prose:
  - how many subjects there are;
  - every category, with its complete list of members, spelled exactly as
    given;
  - that within each category every member belongs to a different subject
    (each is used exactly once);
  - for any category marked as ordered, the order its members are listed in.
Anything else in the introduction must be pure scene-setting that constrains
nothing. If a solver could deduce a single cell from your backstory, the
backstory is wrong.

CLUE REQUIREMENTS

  - Produce exactly as many numbered clues as you are given, in the same order.
  - Each numbered clue expresses exactly the facts listed under it -- all of
    them, and nothing more. Where a clue bundles several facts, keep them
    together in one numbered clue, as printed puzzles do.
  - Use the member names exactly as spelled in the category lists. Do not
    shorten, pluralise, re-case, translate or nickname them. "Mrs Abernathy"
    does not become "Abernathy".
  - Never reveal or hint at the answer. Never write a clue that explains a
    deduction ("so X must be Y"). Never cross-reference clue numbers.
  - Do not number facts within a clue or add parenthetical notes to the solver.

TRAPS -- these are the specific ways narration goes wrong. Read the gloss under
each clue and obey it:

  - "earlier/before" means STRICTLY earlier by any amount. Do NOT write
    "just before", "right before", "immediately", or "the next".
  - "immediately before" means exactly one step, in that direction only. Do not
    reverse the two subjects.
  - "next to / adjacent" is SYMMETRIC: one step apart, direction unspecified.
    Do not write "just after", which picks a direction.
  - "between" is exclusive and the two outer subjects are UNORDERED. Do not
    imply which of them comes first, and do not make the gaps definite.
  - a gap of N means the positions DIFFER by N -- "N apart", "N later". It does
    NOT mean "N in between", which would be N+1. This off-by-one is the single
    most common mistake. Prefer the words "apart" or "later".
  - "if X then Y" asserts nothing when X is false, and does NOT assert the
    converse. Do not write it as "X exactly when Y".
  - "either X or Y" is INCLUSIVE -- possibly both. Do not write "but not both".
  - "not both X and Y" permits neither. Do not write it as "exactly one of".
  - a negative clue stays negative. "A is not with B" must not become "A is
    with someone else, perhaps C".

Return your answer in the required JSON format.\
"""

RETRY_PREFIX = """\
A previous attempt at this narrative FAILED verification. Independent readers
converted your prose back into formal clues and did not recover the original
puzzle. The specific problems are listed below. Write a fresh narrative that
fixes them, keeping everything else about the brief the same.

PROBLEMS WITH THE PREVIOUS ATTEMPT:
{report}

PREVIOUS ATTEMPT (for reference -- do not simply repeat it):
{previous}

"""

#: Structured output schema: lets us check the clue count mechanically rather
#: than parsing prose headings.
NARRATIVE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "A short, inviting title for the puzzle.",
        },
        "introduction": {
            "type": "string",
            "description": (
                "One or two paragraphs. Must name the subject count, every "
                "category with its full member list, and the one-each "
                "condition. Scene-setting must constrain nothing."
            ),
        },
        "clues": {
            "type": "array",
            "description": (
                "The numbered clues as plain sentences, in the given order, "
                "without leading numbers."
            ),
            "items": {"type": "string"},
        },
    },
    "required": ["title", "introduction", "clues"],
    "additionalProperties": False,
}


@dataclass(slots=True)
class Narrative:
    """A narrated puzzle: what the solver (and the extractor) gets to see."""

    pid: str
    title: str
    introduction: str
    clues: tuple[str, ...]
    model: str = ""
    attempt: int = 1

    def to_text(self) -> str:
        """The full narrative, exactly as handed to the extractors."""
        lines = [self.title, "", self.introduction.strip(), "", "Clues:"]
        for i, clue in enumerate(self.clues, start=1):
            lines.append(f"{i}. {clue.strip()}")
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", "", self.introduction.strip(), "", "## Clues", ""]
        for i, clue in enumerate(self.clues, start=1):
            lines.append(f"{i}. {clue.strip()}")
        return "\n".join(lines)

    def to_json(self) -> dict:
        return {
            "pid": self.pid,
            "title": self.title,
            "introduction": self.introduction,
            "clues": list(self.clues),
            "model": self.model,
            "attempt": self.attempt,
        }

    @classmethod
    def from_json(cls, data: Mapping) -> "Narrative":
        return cls(
            pid=data.get("pid", ""),
            title=data["title"],
            introduction=data["introduction"],
            clues=tuple(data["clues"]),
            model=data.get("model", ""),
            attempt=int(data.get("attempt", 1)),
        )


def brief(puzzle) -> str:
    """The narrator's brief: cast, categories, and glossed clues."""
    schema = puzzle.schema
    out: list[str] = []
    out.append(f"SETTING (raw material -- rewrite freely): {puzzle.blurb}")
    out.append(f"WORKING TITLE: {puzzle.title}")
    out.append("")
    out.append(
        f"SUBJECTS: {schema.size} {schema.entity_noun_plural}. Each has exactly one "
        f"member of every category below, and within a category each member "
        f"belongs to a different {schema.entity_noun}."
    )
    out.append("")
    out.append("CATEGORIES (use these spellings verbatim):")
    for cat in schema.categories:
        tag = ""
        if cat.ordered:
            tag = f"  [ORDERED, listed {cat.cmp_less or 'lowest'} to {cat.cmp_more or 'highest'}]"
        out.append(f"  {cat.label}{tag}")
        out.append(f"    {', '.join(cat.items)}")
    if schema.ordered:
        out.append("")
        out.append(
            f"The ordered category is '{schema.spine.label}'. Positional clues refer "
            f"to it. Its {schema.size} values are the only positions that exist."
        )
    out.append("")
    out.append(f"CLUES -- produce exactly {len(puzzle.clues)} numbered clues:")
    for entry in clue_glosses(puzzle):
        out.append("")
        out.append(f"  Clue {entry['number']}:")
        for atom in entry["atoms"]:
            out.append(f"    FACT [{atom['kind']}]: {atom['canonical']}")
            out.append(f"      MEANS EXACTLY: {atom['gloss']}")
    return "\n".join(out)


def build_request(
    puzzle,
    previous: Narrative | None = None,
    failure_report: str = "",
) -> Request:
    """Assemble the narrator prompt, optionally with repair feedback."""
    user = brief(puzzle)
    if previous is not None and failure_report:
        user = RETRY_PREFIX.format(
            report=failure_report, previous=previous.to_text()
        ) + user
    return Request(system=SYSTEM, user=user, schema=NARRATIVE_SCHEMA, key=puzzle.pid)


def parse_reply(puzzle, text: str, model: str = "", attempt: int = 1) -> Narrative:
    """Decode the narrator's structured reply, checking the clue count."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"narrator reply was not valid JSON: {exc}") from exc
    for field in ("title", "introduction", "clues"):
        if field not in data:
            raise ValueError(f"narrator reply is missing {field!r}")
    clues = [str(c) for c in data["clues"]]
    if len(clues) != len(puzzle.clues):
        raise ValueError(
            f"narrator produced {len(clues)} clues, expected {len(puzzle.clues)}"
        )
    return Narrative(
        pid=puzzle.pid,
        title=str(data["title"]),
        introduction=str(data["introduction"]),
        clues=tuple(clues),
        model=model,
        attempt=attempt,
    )


def narrate(
    puzzle,
    client,
    config: ModelConfig | None = None,
    previous: Narrative | None = None,
    failure_report: str = "",
    attempt: int = 1,
) -> Narrative:
    """One narration pass."""
    request = build_request(puzzle, previous, failure_report)
    text = client.complete(request, config)
    model = (config or getattr(client, "config", ModelConfig())).model
    return parse_reply(puzzle, text, model=model, attempt=attempt)


def canonical_narrative(puzzle) -> Narrative:
    """The canonical text dressed as a :class:`Narrative`.

    Not a narration -- it is the plain rendering.  Useful as a control: it must
    pass the round-trip gate trivially, so if it ever fails, the fault is in the
    extractor or the gate rather than in the narrator.
    """
    intro = canonical_intro(puzzle).replace("**", "").replace("\n- ", " ")
    return Narrative(
        pid=puzzle.pid,
        title=puzzle.title,
        introduction=intro,
        clues=tuple(clue_text(c, puzzle.schema) for c in puzzle.clues),
        model="canonical",
    )
