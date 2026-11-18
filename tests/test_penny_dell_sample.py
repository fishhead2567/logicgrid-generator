"""Validate the engine against Penny Dell's own published sample problem.

Transcribed from "How to Solve Logic Problems" (Penny Publications, 2008), the
worked example in their solving guide.  If our clue IR and solver agree with a
puzzle the publisher themselves walked through, the semantics are right.

    Five couples were married last week, each on a different weekday. From the
    information provided, determine the woman (one is Cathy) and man (one is
    Paul) who make up each couple, as well as the day on which each couple was
    married.

      1. Anne was married on Monday, but not to Wally.
      2. Stan's wedding was on Wednesday. Rob was married on Friday,
         but not to Ida.
      3. Vern (who married Fran) was married the day after Eve.

Their stated answer: Anne and Paul, Mon.; Cathy and Rob, Fri.; Eve and Stan,
Wed.; Fran and Vern, Thu.; Ida and Wally, Tue.
"""

from __future__ import annotations

import pytest

from logicgrid import (
    Category,
    Clue,
    ImmediatelyBefore,
    Link,
    NotLink,
    Ref,
    Schema,
    Solution,
    count_solutions,
    human_solve,
    solve,
)

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
WOMEN = ("Anne", "Cathy", "Eve", "Fran", "Ida")
MEN = ("Paul", "Rob", "Stan", "Vern", "Wally")


@pytest.fixture
def schema() -> Schema:
    return Schema(
        [
            Category("day", "Day", DAYS, ordered=True, noun="day",
                     cmp_less="earlier", cmp_more="later", step_noun="day"),
            Category("woman", "Woman", WOMEN, noun="woman"),
            Category("man", "Man", MEN, noun="man"),
        ],
        spine="day",
        entity_noun="couple",
    )


def _r(item: str) -> Ref:
    for cat, items in (("day", DAYS), ("woman", WOMEN), ("man", MEN)):
        if item in items:
            return Ref(cat, item)
    raise KeyError(item)


@pytest.fixture
def clues() -> tuple[Clue, ...]:
    return (
        # 1. Anne was married on Monday, but not to Wally.
        Clue((Link(_r("Anne"), _r("Monday")), NotLink(_r("Anne"), _r("Wally"))), "but_not"),
        # 2. Stan's wedding was on Wednesday. Rob was married on Friday, but not to Ida.
        Clue(
            (
                Link(_r("Stan"), _r("Wednesday")),
                Link(_r("Rob"), _r("Friday")),
                NotLink(_r("Rob"), _r("Ida")),
            ),
            "sentences",
        ),
        # 3. Vern (who married Fran) was married the day after Eve.
        Clue(
            (
                Link(_r("Vern"), _r("Fran")),
                ImmediatelyBefore(_r("Eve"), _r("Vern")),
            ),
            "parenthetical",
        ),
    )


PUBLISHED = {
    "day": list(DAYS),
    "woman": ["Anne", "Ida", "Eve", "Fran", "Cathy"],
    "man": ["Paul", "Wally", "Stan", "Vern", "Rob"],
}


def test_published_solution_satisfies_every_clue(schema, clues):
    solution = Solution(schema, PUBLISHED)
    for clue in clues:
        for atom in clue.atoms:
            assert atom.holds(solution), f"{atom!r} is false for the published answer"


def test_puzzle_has_exactly_one_solution(schema, clues):
    assert count_solutions(schema, clues, limit=3) == 1


def test_oracle_finds_the_published_solution(schema, clues):
    assert solve(schema, clues) == Solution(schema, PUBLISHED)


def test_solvable_without_trial_and_error(schema, clues):
    """Penny Dell's walkthrough uses no guessing, so neither should we."""
    report = human_solve(schema, clues, allow_trial=False)
    assert report.solved
    assert report.trial_eliminations == 0
    assert report.solution == Solution(schema, PUBLISHED)


def test_dropping_any_clue_loses_uniqueness(schema, clues):
    """The published clue set is minimal -- a good check on our minimiser's goal."""
    for i in range(len(clues)):
        reduced = clues[:i] + clues[i + 1 :]
        assert count_solutions(schema, reduced, limit=2) > 1, (
            f"clue {i + 1} turned out to be redundant"
        )


def test_immediately_before_is_directional(schema):
    """'the day after Eve' must not be reversible."""
    solution = Solution(schema, PUBLISHED)
    assert ImmediatelyBefore(_r("Eve"), _r("Vern")).holds(solution)
    assert not ImmediatelyBefore(_r("Vern"), _r("Eve")).holds(solution)


def test_intro_facts_are_implicit(schema, clues):
    """Nobody had to state 'each couple married on a different day'.

    The all-different condition lives in the model, not in the clue list, which
    is exactly how the printed puzzles work -- and why the narrative step must
    keep stating it in the introduction.
    """
    solution = solve(schema, clues)
    assert solution is not None
    for cat in schema.categories:
        row = solution.table[cat.name]
        assert len(set(row)) == len(row)
