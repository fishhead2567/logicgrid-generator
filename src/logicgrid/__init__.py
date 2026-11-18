"""logicgrid -- Penny Dell-style logic grid puzzles, generated and verified.

Quick start::

    from logicgrid import PuzzleSpec, generate, to_markdown

    puzzle = generate(PuzzleSpec(difficulty="hard", seed=1234))
    puzzle.verify()                 # re-proves uniqueness from the clues alone
    print(to_markdown(puzzle))

Everything is deterministic in the seed.  Difficulty is *measured* by solving
the puzzle with human techniques only (see :mod:`logicgrid.human_solver`), not
asserted by the generator, so a puzzle labelled 6/7 really did need the
techniques that make a 6.
"""

from .clues import (
    ALL_KINDS,
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
    TIER_A_KINDS,
    TIER_B_KINDS,
    TIER_C_KINDS,
    atom_from_json,
    atoms_from_json,
)
from .csp import Engine, Grid, count_solutions, is_unique, solve
from .difficulty import (
    PROFILES,
    RAMP,
    Profile,
    clue_stats,
    rate,
    rating,
    score,
)
from .extract import Extraction, ExtractionError, extract
from .generate import Puzzle, PuzzleSpec, generate, generate_many
from .human_solver import SolveReport, explain, human_solve
from .llm import Client, DryRunClient, LLMError, ModelConfig, Request, Usage
from .narrate import Narrative, canonical_narrative, narrate
from .model import Category, Clue, PuzzleError, Ref, Schema, Solution
from .render import (
    canonical_intro,
    clue_glosses,
    clue_text,
    solution_table,
    solving_chart,
    to_markdown,
    to_text,
    walkthrough,
)
from .themes import THEMES, Theme, theme, themes_for
from .verify import FAIL, PASS, PASS_EQUIVALENT, RoundTrip, roundtrip, verify_narrative

__version__ = "0.1.0"

__all__ = [
    "ALL_KINDS",
    "Adjacent",
    "Arith",
    "Atom",
    "Before",
    "Between",
    "Category",
    "Client",
    "Clue",
    "Distinct",
    "DryRunClient",
    "Engine",
    "Extraction",
    "ExtractionError",
    "FAIL",
    "LLMError",
    "ModelConfig",
    "Narrative",
    "PASS",
    "PASS_EQUIVALENT",
    "Request",
    "RoundTrip",
    "Usage",
    "canonical_narrative",
    "extract",
    "narrate",
    "roundtrip",
    "verify_narrative",
    "Gap",
    "Grid",
    "IfThen",
    "ImmediatelyBefore",
    "Link",
    "Not",
    "NotBoth",
    "NotLink",
    "Or",
    "PROFILES",
    "Parity",
    "Profile",
    "Puzzle",
    "PuzzleError",
    "PuzzleSpec",
    "RAMP",
    "Ref",
    "Schema",
    "SolveReport",
    "Solution",
    "THEMES",
    "TIER_A_KINDS",
    "TIER_B_KINDS",
    "TIER_C_KINDS",
    "Theme",
    "atom_from_json",
    "atoms_from_json",
    "canonical_intro",
    "clue_glosses",
    "clue_stats",
    "clue_text",
    "count_solutions",
    "explain",
    "generate",
    "generate_many",
    "human_solve",
    "is_unique",
    "rate",
    "rating",
    "score",
    "solution_table",
    "solve",
    "solving_chart",
    "theme",
    "themes_for",
    "to_markdown",
    "to_text",
    "walkthrough",
    "__version__",
]
