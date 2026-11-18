"""Rendering: canonical puzzle text, solving charts and solution pages.

The *canonical* rendering is deliberately plain.  Its job is to be impossible to
misread, not to be charming -- phase 2 hands it to a narrator whose job is the
charm, and the round-trip gate compares meaning, not prose.  So where elegance
and precision conflict here, precision wins every time.

:func:`canonical_intro` is the one piece of flavour text that carries logical
weight, exactly as Penny Dell's own solving guide warns: "All the information you
need ... is given in the introduction and clues."  It states the cast, the
categories and the all-different conditions, and nothing else.
"""

from __future__ import annotations

from typing import Sequence

from .clues import Atom
from .model import Clue, Schema, Solution


def _listify(items: Sequence[str], conj: str = "and") -> str:
    """Join items, switching to semicolons when one of them contains "and".

    "tree fern fibre, coconut husk, perlite and charcoal and lava rock" has no
    unambiguous reading -- there is no telling where the fourth item starts.
    Semicolons give it one.
    """
    items = list(items)
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if any(f" {conj.split()[-1]} " in item or " and " in item for item in items):
        return "; ".join(items[:-1]) + f"; {conj} {items[-1]}"
    return ", ".join(items[:-1]) + f" {conj} {items[-1]}"


def clue_text(clue: Clue, schema: Schema) -> str:
    """Render one numbered clue as sentences.

    Atoms are joined as separate sentences rather than stitched with ", but ".
    Stitching meant lowercasing the second clause's first word, which quietly
    mangled proper nouns -- "but leocadia does not ...". The narrative pass is
    where clauses get combined gracefully; here, correctness wins.
    """
    return " ".join(a.render(schema) for a in clue.atoms)


COUNT_WORDS = {
    2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight",
}


def canonical_intro(puzzle) -> str:
    """The logically load-bearing introduction, written as a task.

    Everything a solver is entitled to assume before reading clue 1 -- how many
    entities there are, the categories, the items in play, the order of the
    ordered one, and that each item is used exactly once -- but phrased the way
    a printed puzzle phrases it: *who* is involved and *what to work out*,
    rather than a list of fields. Penny Dell's own guide is blunt that this
    paragraph carries logical weight, so none of it is decoration.
    """
    schema = puzzle.schema
    n = schema.size
    count = COUNT_WORDS.get(n, str(n))
    subject = next((c for c in schema.categories if c.subject), None)
    others = [c for c in schema.categories if c is not subject]
    lines: list[str] = []

    blurb = (getattr(puzzle, "blurb", "") or "").strip()
    if blurb:
        lines.append(blurb)

    nouns = [c.noun or c.label.casefold() for c in others]
    lines.append(
        f"{count} {schema.entity_noun_plural} are involved. Determine each "
        f"{schema.entity_noun}'s {_listify(nouns)}."
    )

    if subject is not None:
        lines.append(f"- **{subject.label}**: {_listify(list(subject.items))}.")
    for cat in others:
        order = ""
        if cat.ordered:
            # The items are already printed in order, so name the direction
            # rather than repeating the endpoints.
            low = cat.cmp_less or "lower"
            high = cat.cmp_more or "higher"
            order = f" (listed from {low} to {high})"
        lines.append(f"- **{cat.label}**{order}: {_listify(list(cat.items))}.")

    lines.append(
        f"Every {schema.entity_noun} has a different {_listify(nouns)}, so "
        f"within each category every item is used exactly once."
    )
    return "\n".join(lines)


def clue_glosses(puzzle) -> list[dict]:
    """Per-clue pedantic semantics, for a narrator that must not drift.

    Each entry pairs the canonical sentence with an explicit statement of what
    the clue does *and does not* assert -- the direction of an ordering, the
    symmetry of an adjacency, the exclusivity of a "between".
    """
    schema = puzzle.schema
    out = []
    for i, clue in enumerate(puzzle.clues, start=1):
        out.append(
            {
                "number": i,
                "canonical": clue_text(clue, schema),
                "atoms": [
                    {
                        "kind": a.kind,
                        "canonical": a.render(schema),
                        "gloss": a.gloss(schema),
                        "json": a.to_json(),
                    }
                    for a in clue.atoms
                ],
            }
        )
    return out


def solving_chart(puzzle, pairs: bool = True) -> str:
    """Blank pairwise grids, the Penny Dell way: `.` for yes, `X` for no."""
    schema = puzzle.schema
    cats = schema.categories
    blocks: list[str] = []
    todo = []
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            todo.append((cats[i], cats[j]))
            if not pairs:
                break
    for left, right in todo:
        header = "| | " + " | ".join(right.items) + " |"
        sep = "|---" * (len(right.items) + 1) + "|"
        rows = [f"| **{item}** |" + " |" * len(right.items) for item in left.items]
        blocks.append(
            f"*{left.label} vs {right.label}*\n\n"
            + "\n".join([header, sep, *rows])
        )
    return "\n\n".join(blocks)


def solution_table(puzzle) -> str:
    schema = puzzle.schema
    cats = schema.categories
    header = "| " + " | ".join(c.label for c in cats) + " |"
    sep = "|---" * len(cats) + "|"
    rows = []
    for p in schema.positions:
        entity = puzzle.solution.entity(p)
        rows.append("| " + " | ".join(entity[c.name] for c in cats) + " |")
    return "\n".join([header, sep, *rows])


def walkthrough(puzzle, limit: int = 40) -> str:
    """The deduction trace, as a numbered explanation."""
    if puzzle.report is None:
        return "_(no solve trace recorded)_"
    lines = []
    for i, step in enumerate(puzzle.report.trace[:limit], start=1):
        lines.append(f"{i}. {step.describe(puzzle.schema)}")
    if len(puzzle.report.trace) > limit:
        lines.append(f"_... and {len(puzzle.report.trace) - limit} further steps._")
    return "\n".join(lines)


def to_markdown(
    puzzle,
    *,
    solution: bool = True,
    chart: bool = True,
    trace: bool = False,
) -> str:
    """A complete puzzle page."""
    schema = puzzle.schema
    stats = puzzle.stats()
    head = [
        f"# {puzzle.title}",
        "",
        f"**Difficulty** {puzzle.rating}/7 ({puzzle.profile}) &nbsp;&nbsp; "
        f"**Grid** {len(schema.categories)} x {schema.size} &nbsp;&nbsp; "
        f"**Clues** {len(puzzle.clues)} &nbsp;&nbsp; "
        f"**id** `{puzzle.pid}`",
        "",
        "## Introduction",
        "",
        canonical_intro(puzzle),
        "",
        "## Clues",
        "",
    ]
    for i, clue in enumerate(puzzle.clues, start=1):
        head.append(f"{i}. {clue_text(clue, schema)}")
    if chart:
        head += ["", "## Solving chart", "", solving_chart(puzzle)]
    if solution:
        head += ["", "## Solution", "", solution_table(puzzle)]
    if trace:
        head += ["", "## How it falls out", "", walkthrough(puzzle)]
    head += [
        "",
        "---",
        "",
        f"<sub>seed `{puzzle.seed}` &middot; score {puzzle.score} &middot; "
        f"atoms {stats['atoms']} &middot; positives {stats['positives']} &middot; "
        f"solved by {puzzle.report.max_technique if puzzle.report else 'n/a'}</sub>",
    ]
    return "\n".join(head)


def to_text(puzzle, *, solution: bool = False) -> str:
    """Plain text, for terminals and for feeding to an LLM."""
    schema = puzzle.schema
    out = [puzzle.title, "=" * len(puzzle.title), "", puzzle.blurb, ""]
    intro = canonical_intro(puzzle).replace("**", "").replace("- ", "  - ")
    out += [intro, "", "CLUES", "-----"]
    for i, clue in enumerate(puzzle.clues, start=1):
        out.append(f"{i:>2}. {clue_text(clue, schema)}")
    if solution:
        out += ["", "SOLUTION", "--------"]
        for p in schema.positions:
            entity = puzzle.solution.entity(p)
            bits = ", ".join(f"{c.label}: {entity[c.name]}" for c in schema.categories)
            out.append(f"  {bits}")
    return "\n".join(out)
