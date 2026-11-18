"""Generator properties that must hold for every puzzle it emits."""

from __future__ import annotations

import json

import pytest

from logicgrid import (
    PROFILES,
    Puzzle,
    PuzzleSpec,
    count_solutions,
    generate,
    human_solve,
    is_unique,
    to_markdown,
    to_text,
)
from logicgrid.csp import flatten
from logicgrid.difficulty import rating, score
from logicgrid.themes import THEMES

SEEDS = (11, 23, 404)
PROFILE_NAMES = ("gentle", "easy", "moderate", "hard", "expert")

CASES = [(name, seed) for name in PROFILE_NAMES for seed in SEEDS]


@pytest.fixture(scope="module")
def generated() -> dict[tuple[str, int], Puzzle]:
    return {(n, s): generate(PuzzleSpec(difficulty=n, seed=s)) for n, s in CASES}


@pytest.mark.parametrize("name,seed", CASES)
def test_every_clue_is_true_of_the_solution(generated, name, seed):
    puzzle = generated[(name, seed)]
    for atom in puzzle.atoms():
        assert atom.holds(puzzle.solution), f"{atom!r} is false for its own solution"


@pytest.mark.parametrize("name,seed", CASES)
def test_exactly_one_solution(generated, name, seed):
    puzzle = generated[(name, seed)]
    assert count_solutions(puzzle.schema, puzzle.clues, limit=3) == 1


@pytest.mark.parametrize("name,seed", CASES)
def test_verify_passes(generated, name, seed):
    generated[(name, seed)].verify()


@pytest.mark.parametrize("name,seed", CASES)
def test_solvable_by_hand(generated, name, seed):
    """A puzzle a person cannot finish is not a puzzle."""
    puzzle = generated[(name, seed)]
    profile = PROFILES[puzzle.profile]
    report = human_solve(
        puzzle.schema,
        puzzle.clues,
        allow_trial=profile.allow_trial,
        subset_size=profile.subset_size,
    )
    assert report.solved, report.summary()
    assert report.solution == puzzle.solution


@pytest.mark.parametrize("name,seed", CASES)
def test_no_guessing_below_expert(generated, name, seed):
    """Only the expert profile is allowed to need trial and error."""
    puzzle = generated[(name, seed)]
    if PROFILES[puzzle.profile].allow_trial:
        pytest.skip("this profile permits trial and error")
    report = human_solve(puzzle.schema, puzzle.clues, allow_trial=False)
    assert report.solved
    assert report.trial_eliminations == 0


@pytest.mark.parametrize("name,seed", CASES)
def test_every_clue_is_load_bearing(generated, name, seed):
    """Minimality: drop any single clue and uniqueness must be lost.

    This is the property that separates a pleasant puzzle from a slog, and the
    minimiser's whole job.
    """
    puzzle = generated[(name, seed)]
    atoms = list(puzzle.atoms())
    for i, atom in enumerate(atoms):
        reduced = atoms[:i] + atoms[i + 1 :]
        assert not is_unique(puzzle.schema, reduced), (
            f"clue {atom!r} is redundant -- the minimiser left it in"
        )


@pytest.mark.parametrize("name,seed", CASES)
def test_rating_lands_in_the_profile_band(generated, name, seed):
    puzzle = generated[(name, seed)]
    lo, hi = PROFILES[name].band
    assert lo - 1 <= puzzle.rating <= hi + 1, (
        f"{name} seed {seed} rated {puzzle.rating}, band {(lo, hi)}"
    )


@pytest.mark.parametrize("name", PROFILE_NAMES)
def test_generation_is_deterministic(name):
    a = generate(PuzzleSpec(difficulty=name, seed=99))
    b = generate(PuzzleSpec(difficulty=name, seed=99))
    assert a.to_json() == b.to_json()


@pytest.mark.parametrize("name", PROFILE_NAMES)
def test_different_seeds_give_different_puzzles(name):
    a = generate(PuzzleSpec(difficulty=name, seed=1))
    b = generate(PuzzleSpec(difficulty=name, seed=2))
    assert a.solution.to_json() != b.solution.to_json() or a.theme != b.theme


@pytest.mark.parametrize("name,seed", CASES)
def test_json_round_trip(generated, name, seed):
    puzzle = generated[(name, seed)]
    clone = Puzzle.from_json(json.loads(json.dumps(puzzle.to_json())))
    assert clone.solution == puzzle.solution
    assert set(clone.atoms()) == set(puzzle.atoms())
    clone.verify()


@pytest.mark.parametrize("name,seed", CASES)
def test_renders_without_error(generated, name, seed):
    puzzle = generated[(name, seed)]
    md = to_markdown(puzzle, trace=True)
    assert puzzle.title in md
    for cat in puzzle.schema.categories:
        for item in cat.items:
            assert item in md, f"{item} missing from the rendered puzzle"
    assert to_text(puzzle, solution=True)


@pytest.mark.parametrize("name,seed", CASES)
def test_item_names_are_globally_unique(generated, name, seed):
    """What lets a clue name an item without naming its category."""
    puzzle = generated[(name, seed)]
    names = [i for c in puzzle.schema.categories for i in c.items]
    assert len(names) == len(set(names))


def test_ramp_covers_the_difficulty_range():
    from logicgrid.difficulty import ramp_sequence

    seq = ramp_sequence(50)
    assert len(seq) == 50
    assert set(seq) == set(PROFILE_NAMES)
    # Monotone non-decreasing difficulty across the set.
    order = {n: i for i, n in enumerate(PROFILE_NAMES)}
    levels = [order[n] for n in seq]
    assert levels == sorted(levels)


def test_all_themes_declare_enough_material():
    for theme in THEMES:
        assert theme.max_categories() >= 5, theme.slug
        assert theme.max_items() >= 6, theme.slug
        assert theme.blurb and theme.title and theme.entity_noun, theme.slug
