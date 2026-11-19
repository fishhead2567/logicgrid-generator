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


# ---------------------------------------------------------------------------
# clue balance: a puzzle can be correct and still tedious
# ---------------------------------------------------------------------------


def _toy_schema():
    """A 3x3 grid with an ordered spine, built by hand so the balance tests
    describe exactly the clue sets they care about."""
    from logicgrid.model import Category, Schema

    place = Category(
        name="place",
        label="Placing",
        items=("first", "second", "third"),
        ordered=True,
        noun="placing",
        cmp_less="better",
        cmp_more="worse",
        step_noun="place",
        verb="places",
    )
    baker = Category(
        name="baker", label="Baker", items=("Ada", "Bram", "Cleo"),
        noun="baker", subject=True,
    )
    pie = Category(
        name="pie", label="Pie", items=("rhubarb", "pecan", "mincemeat"),
        noun="pie", verb="bakes",
    )
    return Schema([place, baker, pie], "place")


def test_clue_balance_counts_an_uncovered_pair():
    """The defect this gate exists for: with three categories, pinning
    place-baker and place-pie leaves baker-pie derivable, so the generator
    will happily never mention it."""
    from logicgrid.clues import Link
    from logicgrid.difficulty import clue_balance
    from logicgrid.model import Clue, Ref

    schema = _toy_schema()
    atoms = (
        Link(Ref("place", "first"), Ref("baker", "Ada")),
        Link(Ref("place", "second"), Ref("baker", "Bram")),
        Link(Ref("place", "first"), Ref("pie", "rhubarb")),
        Link(Ref("place", "third"), Ref("pie", "pecan")),
    )
    bal = clue_balance(schema, [Clue((a,)) for a in atoms])
    assert bal["pairs"] == 3
    assert bal["pairs_covered"] == 2
    assert bal["pair_coverage"] == pytest.approx(2 / 3)
    # Every atom is a flat link, which is the other half of the same complaint.
    assert bal["positive_share"] == 1.0
    assert bal["degenerate"] == 0


def test_clue_balance_flags_a_compound_whose_refs_are_already_pinned():
    """"The baker who bakes rhubarb places better than Bram" carries nothing
    once another clue says Ada bakes rhubarb: the solver substitutes and the
    indirection was decoration."""
    from logicgrid.clues import Before, Link
    from logicgrid.difficulty import clue_balance
    from logicgrid.model import Clue, Ref

    schema = _toy_schema()
    pinned = (
        Link(Ref("baker", "Ada"), Ref("pie", "rhubarb")),
        Link(Ref("baker", "Bram"), Ref("pie", "pecan")),
    )
    leaning = Before(Ref("pie", "rhubarb"), Ref("baker", "Bram"))
    bal = clue_balance(schema, [Clue((a,)) for a in pinned + (leaning,)])
    assert bal["degenerate"] == 1

    # Swap one pinning link for a negative and the indirection is real again.
    loose = (
        Link(Ref("baker", "Ada"), Ref("pie", "rhubarb")),
        Before(Ref("pie", "rhubarb"), Ref("baker", "Bram")),
    )
    assert clue_balance(schema, [Clue((a,)) for a in loose])["degenerate"] == 0


def test_balance_ok_rejects_the_uncovered_pair_and_the_crowded_pair():
    from logicgrid.clues import Link, NotLink
    from logicgrid.generate import balance_ok
    from logicgrid.model import Ref

    schema = _toy_schema()
    prof = PROFILES["gentle"]

    uncovered = [
        Link(Ref("place", "first"), Ref("baker", "Ada")),
        NotLink(Ref("place", "second"), Ref("baker", "Bram")),
        Link(Ref("place", "first"), Ref("pie", "rhubarb")),
    ]
    assert not balance_ok(schema, uncovered, prof)

    crowded = [
        NotLink(Ref("place", "first"), Ref("baker", "Ada")),
        NotLink(Ref("place", "second"), Ref("baker", "Bram")),
        NotLink(Ref("place", "third"), Ref("baker", "Cleo")),
        NotLink(Ref("place", "first"), Ref("baker", "Bram")),
        Link(Ref("baker", "Ada"), Ref("pie", "rhubarb")),
        Link(Ref("place", "second"), Ref("pie", "pecan")),
    ]
    assert not balance_ok(schema, crowded, prof)


@pytest.mark.parametrize("name,seed", CASES)
def test_generated_clues_mention_every_pair_of_categories(generated, name, seed):
    """Every sub-grid gets said something about, so no block of the chart is
    reachable only by transitivity."""
    from logicgrid.difficulty import clue_balance

    puzzle = generated[(name, seed)]
    bal = clue_balance(puzzle.schema, puzzle.clues)
    assert bal["pair_coverage"] == 1.0, (
        f"{bal['pairs_covered']}/{bal['pairs']} category pairs mentioned"
    )


@pytest.mark.parametrize("name,seed", CASES)
def test_generated_clues_are_not_crowded_onto_one_pair(generated, name, seed):
    from logicgrid.difficulty import clue_balance

    puzzle = generated[(name, seed)]
    prof = PROFILES[name]
    bal = clue_balance(puzzle.schema, puzzle.clues)
    assert bal["top_pair_share"] <= prof.max_pair_share
    assert bal["positive_share"] <= prof.max_positive_share
    assert bal["degenerate"] == 0


@pytest.mark.parametrize("name,seed", CASES)
def test_no_numbered_clue_answers_its_own_riddle(generated, name, seed):
    """A clue may point at an entity by descriptor, and another clue may name
    that entity -- that connection is the solver's job.  What it may not do is
    both inside one numbered clue: "The grower who pots in perlite is earlier
    than Taavi.  Rowena pots in perlite."
    """
    from logicgrid.generate import _described_refs, _named_refs

    puzzle = generated[(name, seed)]
    for i, clue in enumerate(puzzle.clues, 1):
        named: set = set()
        described: set = set()
        for atom in clue.atoms:
            named |= _named_refs(atom)
            described |= _described_refs(atom, puzzle.schema)
        overlap = named & described
        assert not overlap, (
            f"clue {i} of {name}/{seed} names and describes {sorted(r.key for r in overlap)}: "
            f"{clue.render(puzzle.schema) if hasattr(clue, 'render') else clue}"
        )


def test_bundles_cleanly_rejects_the_shape_it_exists_for():
    """Measured at 14% of puzzles before the guard, but none of the seeds in
    ``CASES`` happen to hit it -- so the property test above is not on its own
    a regression guard.  This pins the exact shape.
    """
    from logicgrid.clues import Before, Link, NotLink
    from logicgrid.generate import _bundles_cleanly
    from logicgrid.model import Ref

    schema = _toy_schema()
    # "The baker who bakes rhubarb places better than Bram. Ada bakes rhubarb."
    riddle = Before(Ref("pie", "rhubarb"), Ref("baker", "Bram"))
    answer = Link(Ref("baker", "Ada"), Ref("pie", "rhubarb"))
    assert not _bundles_cleanly([riddle], answer, schema)
    assert not _bundles_cleanly([answer], riddle, schema)

    # A link naming an unrelated item is fine beside the same comparison.
    elsewhere = Link(Ref("baker", "Cleo"), Ref("pie", "pecan"))
    assert _bundles_cleanly([riddle], elsewhere, schema)

    # The house style survives: two statements about one baker still bundle.
    assert _bundles_cleanly(
        [Link(Ref("baker", "Ada"), Ref("place", "first"))],
        NotLink(Ref("baker", "Ada"), Ref("pie", "pecan")),
        schema,
    )

    # A spine value is its own label, never a riddle, so a comparison against
    # one bundles with a link that mentions it.
    assert _bundles_cleanly(
        [Before(Ref("baker", "Ada"), Ref("place", "third"))],
        Link(Ref("place", "third"), Ref("pie", "pecan")),
        schema,
    )


def test_no_theme_pack_collides_with_itself():
    """Item names must be globally unique inside a built puzzle, and
    ``Schema`` enforces that -- but only for the shape that happened to be
    sampled.  A pack that repeats a name across two axes ships fine until the
    seed that draws both, so check the pools themselves.

    This is the check that makes authoring packs in bulk safe: two axes both
    offering "the Peregrine" is the easy mistake, and it would otherwise
    surface as an intermittent generation failure.
    """
    import collections

    from logicgrid.themes import THEMES

    for theme in THEMES:
        names = [i for axis in theme.axes for i in axis.pool] + list(theme.spine.items)
        dupes = [n for n, c in collections.Counter(names).items() if c > 1]
        assert not dupes, f"theme {theme.slug!r} repeats {dupes}"


def test_every_theme_builds_at_every_shape_it_claims():
    """``max_categories``/``max_items`` are promises ``themes_for`` relies on."""
    from random import Random

    from logicgrid.themes import THEMES

    for theme in THEMES:
        for cats in range(3, theme.max_categories() + 1):
            for items in range(3, theme.max_items() + 1):
                schema = theme.build(cats, items, Random(7))
                assert len(schema.categories) == cats
                assert schema.size == items
                assert any(c.subject for c in schema.categories), (
                    f"{theme.slug} at {cats}x{items} lost its names axis"
                )


@pytest.mark.parametrize("name,seed", [("easy", 23)])
def test_plain_text_states_the_blurb_once(generated, name, seed):
    """``canonical_intro`` opens with the blurb, so ``to_text`` must not."""
    puzzle = generated[(name, seed)]
    blurb = puzzle.blurb.strip()
    assert blurb
    assert to_text(puzzle).count(blurb) == 1


# ---------------------------------------------------------------------------
# theme spread
# ---------------------------------------------------------------------------


def test_deal_exhausts_the_deck_before_repeating():
    """The property the old spread lacked.  Rejecting a theme that matched one
    of the last four sampled *with replacement*, so over 50 puzzles a 27-theme
    pool repeated heavily while never repeating back to back."""
    import collections
    from random import Random

    from logicgrid.generate import Deal

    slugs = [f"t{i}" for i in range(7)]
    deck = Deal(slugs, Random(1))
    drawn = []
    for _ in range(21):
        slug = deck.hand(3)[0]
        deck.take(slug)
        drawn.append(slug)

    # Every card appears before any appears a fourth time.
    counts = collections.Counter(drawn)
    assert set(counts) == set(slugs), f"never dealt: {set(slugs) - set(counts)}"
    assert max(counts.values()) - min(counts.values()) <= 2


def test_a_pack_spreads_its_themes():
    """Eight puzzles from 37 packs should be eight different packs."""
    from logicgrid import generate_many

    pack = generate_many(8, seed=3)
    slugs = [p.theme for p in pack]
    assert len(set(slugs)) == len(slugs), f"repeated inside one pack: {slugs}"
    assert len(pack) == 8


def test_a_reused_theme_gets_a_different_grid():
    """Over a run longer than the deck, a pack may come round again -- but not
    at the same shape, or the two puzzles read as the same puzzle twice."""
    from logicgrid import generate_many
    from logicgrid.themes import THEMES

    # Long enough to force reuse without being slow: one more than the deck.
    pack = generate_many(len(THEMES) + 3, seed=11, difficulty="gentle")
    seen: dict[str, set[tuple[int, int]]] = {}
    for p in pack:
        shape = (len(p.schema.categories), p.schema.size)
        assert shape not in seen.get(p.theme, set()), (
            f"{p.theme} reused at the same {shape[0]}x{shape[1]} grid"
        )
        seen.setdefault(p.theme, set()).add(shape)
