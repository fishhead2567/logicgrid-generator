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
from .csp import flatten
from .render import canonical_intro, canonical_preamble, clue_text

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

Write TWO OR THREE SENTENCES of scene-setting. Be funny where the subject lets
you; dry is worse than silly. This is the only part of the puzzle where you
have a free hand, so use it.

DO NOT list the cast, the categories, the members, the count of subjects, the
one-each condition, or the order of the ordered category. Those are printed
separately, above your text and on the solver's chart, exactly as given. Say
them again and you have written a worse copy of something already on the page.

Your sentences must constrain NOTHING. If a solver could deduce a single cell
from your scene, the scene is wrong. Mention a member name only in passing
colour that carries no fact: "the judges have not spoken to each other since
the incident" is fine, "the judges arrived in order of seniority" is not.

ONE EXTRA SENTENCE -- a fourth -- is allowed, and only for this: when the
subject matter is one a reader may simply not know. Sheepdog trials, change
ringing, drystone walling, a hell-box, pomace, the heavy events. Say plainly
what the thing is, in passing, as a magazine would: "Change ringing is bells
rung in strict mathematical sequences, by teams who care about this far more
than you are about to." Do
not take the extra sentence for a subject that explains itself -- a food court,
a karaoke night and a school bake sale need no gloss, and padding them reads
as condescension.

CLUE REQUIREMENTS

You are given a flat list of numbered FACTS. That numbering is bookkeeping, not
a template: what has to survive is the set of facts, not its arrangement.

  - Every fact must appear somewhere in your clue list. Losing one makes the
    puzzle unsolvable, and is the worst thing you can do.
  - Add nothing. A fact a solver could read out of your prose that is not in
    the list is just as damaging as a missing one.
  - GROUP THEM AS A MAGAZINE WOULD. Combine facts that share a subject into one
    numbered clue, and order the clues however reads best. Printed puzzles
    routinely carry two or three facts under one number -- "Anne was married on
    Monday, but not to Wally" is one clue holding two facts. Use that freedom;
    a clue list that flows is the point of the exercise.
  - Do not over-merge. Two or three facts to a clue reads well; six becomes a
    paragraph the solver has to parse twice. Keep each numbered clue to about
    one or two sentences.
  - REARRANGE FREELY, so long as the set of facts is identical. The test is
    always the same: could a solver deduce something from your version that
    the fact list does not support, or fail to deduce something it does? If
    no, the rearrangement is yours to make. Specifically, all of these are
    yours:
      * the order of the numbered clues;
      * which facts share a clue, regardless of how the list numbers them;
      * the order of facts within one clue -- lead with whichever reads
        better, and name a shared subject once rather than twice ("Rose
        places third and uses the cake server", never "Rose places third.
        The builder who places third uses the cake server.");
      * either side of a SYMMETRIC fact: "A and B are one apart" is the same
        fact as "B and A are one apart", and for "between", which of the two
        outer points you name first is not specified, so pick the one that
        reads better;
      * turning a comparison round WHEN THE COMPARATIVE TURNS WITH IT: "A is
        earlier than B" and "B is later than A" are one fact said two ways.
    These are NOT yours, because they change the fact:
      * reversing a directional fact without reversing the comparative. "A is
        immediately before B" is not "B is immediately before A".
      * implying an order between the two outer points of a "between". They
        are unordered; naming one first is prose, saying one is earlier is a
        new fact.
      * merging two facts into a claim stronger than either, such as turning
        "A is earlier than B" and "B is earlier than C" into "A, B and C in
        that order" when nothing rules out gaps you have not been told about.
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
                "Two or three sentences of scene-setting, funny where the "
                "subject allows. A fourth is permitted only to say plainly "
                "what an unfamiliar activity is. Never list the cast, the "
                "categories, the members, the subject count, the one-each "
                "condition or the ordering -- those are printed separately. "
                "Must constrain nothing."
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


def clue_count_range(facts: int) -> tuple[int, int]:
    """How many numbered clues a narrative holding ``facts`` facts should have.

    Wide on purpose. The floor stops everything being crushed into three
    paragraph-long clues; the ceiling is one clue per fact, which is what the
    old one-to-one rule forced and what made the prose read like a list.
    """
    return max(1, (facts + 2) // 3), facts


@dataclass(slots=True)
class Narrative:
    """A narrated puzzle: what the solver (and the extractor) gets to see."""

    pid: str
    title: str
    #: The narrator's scene: two or three sentences, and no cast list.
    introduction: str
    clues: tuple[str, ...]
    model: str = ""
    attempt: int = 1
    #: The canonical preamble -- count, task, categories, members, ordering,
    #: one-each -- printed verbatim between the scene and the clues.
    #:
    #: Not narrated, deliberately. The narrator used to be required to restate
    #: all of it in prose, which produced a longer and less scannable copy of a
    #: list the solver is looking at on the chart anyway, and left no room in
    #: the paragraph for anything else.
    #:
    #: It still has to be part of the text. The extractors read the cast out of
    #: what they are given, and the whole claim of the round trip is that they
    #: see exactly what a solver sees. Drop it and every reading fails its cast
    #: check for want of a list nobody was shown.
    preamble: str = ""

    def to_text(self) -> str:
        """The full narrative, exactly as handed to the extractors."""
        lines = [self.title, "", self.introduction.strip()]
        if self.preamble.strip():
            lines += ["", self.preamble.strip()]
        lines += ["", "Clues:"]
        for i, clue in enumerate(self.clues, start=1):
            lines.append(f"{i}. {clue.strip()}")
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", "", self.introduction.strip()]
        if self.preamble.strip():
            lines += ["", self.preamble.strip()]
        lines += ["", "## Clues", ""]
        for i, clue in enumerate(self.clues, start=1):
            lines.append(f"{i}. {clue.strip()}")
        return "\n".join(lines)

    def to_json(self) -> dict:
        return {
            "pid": self.pid,
            "title": self.title,
            "introduction": self.introduction,
            "preamble": self.preamble,
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
            preamble=data.get("preamble", ""),
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
    atoms = flatten(puzzle.clues)
    low, high = clue_count_range(len(atoms))
    out.append(
        f"FACTS -- all {len(atoms)} of these must appear. Group them into "
        f"roughly {low} to {high} numbered clues, however reads best:"
    )
    for i, atom in enumerate(atoms, start=1):
        out.append("")
        out.append(f"  FACT {i} [{atom.kind}]: {atom.render(schema)}")
        out.append(f"    MEANS EXACTLY: {atom.gloss(schema)}")
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
    clues = [str(c).strip() for c in data["clues"] if str(c).strip()]
    # The clue count is deliberately NOT pinned to the original. The gate
    # compares the fact set the readers recover, not its arrangement, so the
    # narrator is free to merge facts into clues that flow -- which is what
    # makes a clue list read like a magazine rather than a constraint dump.
    # Only the absurd is rejected: no clues at all, or more clues than there
    # are facts to put in them.
    facts = len(flatten(puzzle.clues))
    if not clues:
        raise ValueError("narrator produced no clues")
    if len(clues) > facts:
        raise ValueError(
            f"narrator produced {len(clues)} clues for only {facts} facts, so "
            "at least one must be empty or invented"
        )
    return Narrative(
        pid=puzzle.pid,
        title=str(data["title"]),
        introduction=str(data["introduction"]),
        # Attached here rather than asked of the narrator, so that it is the
        # canonical text character for character and cannot drift.
        preamble=canonical_preamble(puzzle),
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
