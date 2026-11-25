"""Read a narrative back into formal clues.

This is the other half of the round-trip.  An extractor sees **only** the
narrative -- never the original clue list, never the solution, never the theme
metadata -- and must rebuild the formal clue set from the prose alone.  Several
extractors run independently, so agreement between them is evidence rather than
luck.

Two details make the comparison tractable:

* **Items are named, not categorised.** Item names are globally unique within a
  puzzle (enforced by :class:`logicgrid.model.Schema`), so an extractor can write
  ``"Marigold"`` and we resolve it to the right category ourselves.  That removes
  a whole class of disagreement about what to call the categories.
* **Compound clues nest exactly one level.** The generator never builds an
  either/or of an either/or, so the output schema needs no recursion -- which
  keeps it compatible with strict structured outputs.

An item name that does not resolve is itself a finding: it means the narrative
renamed part of the cast.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from .clues import (
    Adjacent,
    Arith,
    Atom,
    Before,
    Between,
    Distinct,
    Gap,
    IfThen,
    ImmediatelyBefore,
    Link,
    Not,
    NotBoth,
    NotLink,
    Or,
    Parity,
)
from .llm import ModelConfig, Request
from .model import PuzzleError, Ref, Schema

SIMPLE_KINDS = (
    "link",
    "not_link",
    "distinct",
    "before",
    "immediately_before",
    "adjacent",
    "between",
    "gap",
    "parity",
    "arith",
)
COMPOUND_KINDS = ("not", "or", "not_both", "if_then")


class ExtractionError(ValueError):
    """The reply did not describe a clue set we can use."""


# ---------------------------------------------------------------------------
# prompt
# ---------------------------------------------------------------------------

SYSTEM = """\
You convert logic-grid puzzles written as prose into formal notation.

You will be given a puzzle: an introduction and a numbered clue list. Translate
it literally into the fact types below. You are a translator, not a solver.

ABSOLUTE RULES

  - Do NOT solve the puzzle. Do not combine clues, infer anything, or add facts
    that the text does not state. One stated fact becomes one output fact.
  - Do NOT drop anything. A numbered clue often carries several facts ("X is on
    Monday, but not with Y" is two). List every one, under that clue's number.
  - Record what the text says, not the strongest reading of it. If a clue says
    "earlier", use `before`, NOT `immediately_before`, however natural the
    tighter reading feels.
  - Name subjects by the exact member names from the introduction's lists. Copy
    the spelling character for character.
  - Facts stated in the INTRODUCTION about counts, category membership, or
    "each is used once" are structural -- do NOT output them as facts. Only the
    numbered clues become facts.
  - If a clue is genuinely ambiguous, choose the WEAKER reading (the one that
    rules out less).

FACT TYPES

Pairing:
  link(A, B)              A and B belong to the same subject.
  not_link(A, B)          A and B belong to different subjects.
  distinct(A, B, C, ...)  All named are different subjects (pairwise). Use for
                          "three different people" phrasing.

Position (these compare positions in the ordered category):

  The ordered category supplies the positions, but EVERY subject sits at one of
  them, so these facts take ANY members as arguments -- not only members of the
  ordered category. "Constance scores lower than the handler who runs Bute" is
  before(Constance, Bute): neither names a score, and the fact is still about
  the scores they hold. Never leave a comparison out for want of a way to name
  an unnamed subject's position. If you can name the subject, you can compare
  it.

  before(A, B)                A is strictly earlier than B, by any amount.
  immediately_before(A, B)    B is exactly one step after A. Direction matters.
  adjacent(A, B)              One step apart, direction unspecified. ALWAYS use
                              this for "exactly one apart", never gap with k=1:
                              the two say the same thing, and this is the one
                              to say it with.
  between(A, B, C)            A is strictly between B and C; B and C are in no
                              particular order. A is the MIDDLE one -- put it
                              first.
  gap(A, B, k, rel)           The positions differ by k. rel is "eq" (exactly),
                              "ge" (at least) or "le" (at most). "three apart"
                              and "three later" are both k=3. "three in
                              between" is k=4.
  parity(A, B, same)          same=true: both at odd-numbered or both at
                              even-numbered positions. same=false: one of each.
  arith(A, B, k, op)          Numeric: op="add" means A's value = B's value + k
                              (A is larger). op="mul" means A's value = B's
                              value x k.

Compound (each holds simple facts only, never another compound):
  not(F)                  F is false. Prefer not_link over not(link(...)).
  or(F1, F2, ...)         At least one holds. Inclusive -- possibly several.
  not_both(F1, F2)        At most one holds. Neither holding is allowed too.
  if_then(F1, F2)         If F1 holds then F2 holds. Says nothing when F1 is
                          false. Does NOT assert the converse. Put the
                          condition first.

OUTPUT

Fill `args` with the member names in the order shown above. Use `sub` for the
facts inside a compound, and `[]` otherwise. Where a fact type does not use
`k`, `rel`, `op` or `same`, write that field's "unused" sentinel -- 0, "none",
"none" and false, as each field's own description says. Every field is always
present; nothing is omitted, and nothing is null.

Report EVERY category the introduction lists, with its members exactly as
written there, INCLUDING the one that names the subjects themselves. If the
introduction says the archivists are Dr Mwangi, Mr Pelletier and Ms Castellano,
then "archivist" is a category with those three members, exactly like the
shelves and the decades. Leaving it out is the commonest way this reply goes
wrong: the names are a category, even though they are also what every other
category is about.

That is a separate matter from the rule about facts. Counts and membership are
structural and are never emitted as *facts* -- but every category must still be
reported here.\
"""

# Strict structured outputs want ``additionalProperties: false`` with every
# property required, which rules out simply omitting the fields a given fact
# type does not use.  Rather than rely on nullable union types, every field is
# always present with an explicit "unused" sentinel ("none", 0, false, []).
# Simple and compound facts are two separate types rather than one recursive
# one, which is possible because the generator never nests a compound inside a
# compound -- so the schema needs no ``$ref``.
_UNUSED_NOTE = ' Write "none" when this fact type does not use it.'

_SIMPLE_ATOM_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "kind": {"type": "string", "enum": list(SIMPLE_KINDS)},
        "args": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Member names, in the order the fact type specifies.",
        },
        "k": {"type": "number", "description": "Used by gap and arith; else 0."},
        "rel": {"type": "string", "enum": ["eq", "ge", "le", "none"],
                "description": "Used by gap." + _UNUSED_NOTE},
        "op": {"type": "string", "enum": ["add", "mul", "none"],
               "description": "Used by arith." + _UNUSED_NOTE},
        "same": {"type": "boolean", "description": "Used by parity; else false."},
    },
    "required": ["kind", "args", "k", "rel", "op", "same"],
    "additionalProperties": False,
}

_ATOM_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "kind": {"type": "string", "enum": list(SIMPLE_KINDS) + list(COMPOUND_KINDS)},
        "args": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Member names; empty for a compound fact.",
        },
        "k": {"type": "number", "description": "Used by gap and arith; else 0."},
        "rel": {"type": "string", "enum": ["eq", "ge", "le", "none"],
                "description": "Used by gap." + _UNUSED_NOTE},
        "op": {"type": "string", "enum": ["add", "mul", "none"],
               "description": "Used by arith." + _UNUSED_NOTE},
        "same": {"type": "boolean", "description": "Used by parity; else false."},
        "sub": {
            "type": "array",
            "items": _SIMPLE_ATOM_SCHEMA,
            "description": "The facts inside a compound fact; empty otherwise.",
        },
    },
    "required": ["kind", "args", "k", "rel", "op", "same", "sub"],
    "additionalProperties": False,
}

EXTRACTION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "subject_count": {"type": "integer"},
        "categories": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "label": {"type": "string"},
                    "members": {"type": "array", "items": {"type": "string"}},
                    "ordered": {"type": "boolean"},
                },
                "required": ["label", "members", "ordered"],
                "additionalProperties": False,
            },
        },
        "clues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "number": {"type": "integer"},
                    "facts": {"type": "array", "items": _ATOM_SCHEMA},
                },
                "required": ["number", "facts"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["subject_count", "categories", "clues"],
    "additionalProperties": False,
}


def build_request(narrative_text: str) -> Request:
    """The extractor prompt. Carries the narrative and nothing else."""
    return Request(
        system=SYSTEM,
        user=f"Convert this puzzle into formal notation.\n\n{narrative_text}",
        schema=EXTRACTION_SCHEMA,
    )


# ---------------------------------------------------------------------------
# decoding
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class Extraction:
    """One extractor's reading of a narrative."""

    atoms: tuple[Atom, ...]
    clue_atoms: tuple[tuple[Atom, ...], ...]
    subject_count: int
    categories: tuple[tuple[str, tuple[str, ...]], ...]
    model: str = ""
    raw: dict = field(default_factory=dict)

    def to_json(self) -> dict:
        return {
            "model": self.model,
            "subject_count": self.subject_count,
            "categories": [
                {"label": label, "members": list(members)}
                for label, members in self.categories
            ],
            "clues": [[a.to_json() for a in group] for group in self.clue_atoms],
        }


def _resolve(schema: Schema, name: str, kind: str) -> Ref:
    ref = schema.try_resolve(str(name).strip())
    if ref is None:
        raise ExtractionError(
            f"{kind}: no member named {name!r} exists in this puzzle "
            "(the narrative renamed or invented part of the cast)"
        )
    return ref


def _need(args: Sequence[Ref], n: int, kind: str) -> None:
    if len(args) != n:
        raise ExtractionError(f"{kind} needs {n} members, got {len(args)}")


def _build_atom(data: Mapping, schema: Schema, allow_compound: bool = True) -> Atom:
    kind = str(data.get("kind", "")).strip()
    raw_args = data.get("args") or []
    if not isinstance(raw_args, Sequence) or isinstance(raw_args, str):
        raise ExtractionError(f"{kind}: 'args' must be a list of member names")
    args = [_resolve(schema, a, kind) for a in raw_args]

    def opt(field: str):
        """Read a field, treating the "unused" sentinels as absent."""
        value = data.get(field)
        if value is None or value == "none" or value == "":
            return None
        return value

    k = opt("k")
    rel = opt("rel") or "eq"
    op = opt("op") or "add"
    same = data.get("same")
    sub_raw = data.get("sub") or []

    if kind == "link":
        _need(args, 2, kind)
        return Link(args[0], args[1])
    if kind == "not_link":
        _need(args, 2, kind)
        return NotLink(args[0], args[1])
    if kind == "distinct":
        if len(args) < 2:
            raise ExtractionError("distinct needs at least two members")
        return Distinct(tuple(args))
    if kind == "before":
        _need(args, 2, kind)
        return Before(args[0], args[1])
    if kind == "immediately_before":
        _need(args, 2, kind)
        return ImmediatelyBefore(args[0], args[1])
    if kind == "adjacent":
        _need(args, 2, kind)
        return Adjacent(args[0], args[1])
    if kind == "between":
        _need(args, 3, kind)
        return Between(args[0], args[1], args[2])
    if kind == "gap":
        _need(args, 2, kind)
        if k is None:
            raise ExtractionError("gap needs a numeric 'k'")
        return Gap(args[0], args[1], int(k), str(rel))
    if kind == "parity":
        _need(args, 2, kind)
        if same is None:
            raise ExtractionError("parity needs 'same' to be true or false")
        return Parity(args[0], args[1], bool(same))
    if kind == "arith":
        _need(args, 2, kind)
        if k is None:
            raise ExtractionError("arith needs a numeric 'k'")
        return Arith(args[0], args[1], float(k), str(op))

    if kind not in COMPOUND_KINDS:
        raise ExtractionError(f"unknown fact type {kind!r}")
    if not allow_compound:
        raise ExtractionError(f"{kind}: compound facts may not nest inside one another")

    subs = [_build_atom(s, schema, allow_compound=False) for s in sub_raw]
    if kind == "not":
        if len(subs) != 1:
            raise ExtractionError("not needs exactly one inner fact")
        return Not(subs[0])
    if kind == "or":
        if len(subs) < 2:
            raise ExtractionError("or needs at least two inner facts")
        return Or(tuple(subs))
    if kind == "not_both":
        if len(subs) != 2:
            raise ExtractionError("not_both needs exactly two inner facts")
        return NotBoth(subs[0], subs[1])
    if len(subs) != 2:
        raise ExtractionError("if_then needs exactly two inner facts")
    return IfThen(subs[0], subs[1])


def loads_lenient(text: str) -> Any:
    """Parse JSON that may have arrived wrapped in prose or a code fence.

    ``output_config.format`` should make the reply bare JSON, but a model that
    adds a sentence or fences it as Markdown should not cost us a whole retry.
    """
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    if text.startswith("```"):
        body = text.split("```")[1] if text.count("```") >= 2 else text[3:]
        body = body.removeprefix("json").strip()
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            pass
    start, end = text.find("{"), text.rfind("}")
    if 0 <= start < end:
        return json.loads(text[start : end + 1])
    raise json.JSONDecodeError("no JSON object found", text, 0)


def parse_reply(text: str, schema: Schema, model: str = "") -> Extraction:
    """Decode an extractor reply against the original puzzle's schema."""
    try:
        data = loads_lenient(text)
    except json.JSONDecodeError as exc:
        raise ExtractionError(f"extractor reply was not valid JSON: {exc}") from exc
    if not isinstance(data, Mapping):
        raise ExtractionError("extractor reply was not a JSON object")

    clue_groups: list[tuple[Atom, ...]] = []
    flat: list[Atom] = []
    clues = data.get("clues")
    if not isinstance(clues, Sequence) or isinstance(clues, str):
        raise ExtractionError("extractor reply has no 'clues' list")
    for entry in clues:
        facts = entry.get("facts") or [] if isinstance(entry, Mapping) else []
        group: list[Atom] = []
        for fact in facts:
            try:
                atom = _build_atom(fact, schema)
            except PuzzleError as exc:
                raise ExtractionError(str(exc)) from exc
            group.append(atom)
            flat.append(atom)
        clue_groups.append(tuple(group))

    cats_raw = data.get("categories") or []
    cats: list[tuple[str, tuple[str, ...]]] = []
    for c in cats_raw:
        if isinstance(c, Mapping):
            cats.append(
                (str(c.get("label", "")), tuple(str(m) for m in c.get("members", [])))
            )

    return Extraction(
        atoms=tuple(flat),
        clue_atoms=tuple(clue_groups),
        subject_count=int(data.get("subject_count", 0) or 0),
        categories=tuple(cats),
        model=model,
        raw=dict(data),
    )


def extract(narrative_text: str, schema: Schema, client, config: ModelConfig | None = None) -> Extraction:
    """One extraction pass."""
    text = client.complete(build_request(narrative_text), config)
    model = (config or getattr(client, "config", ModelConfig())).model
    return parse_reply(text, schema, model=model)
