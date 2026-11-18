# logicgrid

Generator, solver and difficulty rater for **Penny Dell-style logic grid
puzzles** — the kind with a chatty introduction, a numbered clue list and a
solving chart — plus an LLM pipeline that turns each puzzle into a narrative and
then *proves the narrative still means the same puzzle*.

Zero runtime dependencies. Everything is deterministic in a single integer seed.

```bash
pip install -e .                      # extras: llm, play, dev
                                      # (quoting for extras differs by shell -- see Playing them)
logicgrid gen --count 50 --out puzzles
logicgrid stats puzzles
```

```python
from logicgrid import PuzzleSpec, generate, to_markdown

puzzle = generate(PuzzleSpec(difficulty="hard", seed=1234))
puzzle.verify()          # re-proves uniqueness from the clues alone
print(to_markdown(puzzle))
```

---

## Why this exists rather than an existing generator

I looked first. The honest summary of the field:

| Project | Why it didn't fit |
|---|---|
| [tuchandra/zebra](https://github.com/tuchandra/zebra) | MIT, Python, SAT-based — but author-declared unmaintained, capped at 3–5 houses, **no difficulty control**, not on PyPI |
| [quint-t/Puzzle-Generator-and-Solver](https://github.com/quint-t/Puzzle-Generator-and-Solver) | Best feature set found (20 constraint levels, minimisation) but **non-commercial licence only**, and a script rather than an API |
| [antonstefer/logic-grid](https://github.com/antonstefer/logic-grid) | Good design — difficulty modelled by named human techniques, an idea borrowed here. TypeScript |
| [joshhills](https://github.com/joshhills/logic-puzzle-generator), [alebrozzo](https://github.com/alebrozzo/puzzles) | TypeScript |
| [grilops](https://github.com/obijywk/grilops), [pynstein](https://github.com/dennistreysa/pynstein) | Solvers only, no generation |

PyPI has nothing (`logic-grid`, `zebra-puzzle`, `logic-puzzle-generator` all 404).
The academic state of the art is Shyne, Facey & Cooper,
*[Generating Solvable and Difficult Logic Grid Puzzles](https://www.researchgate.net/publication/382795361_Generating_Solvable_and_Difficult_Logic_Grid_Puzzles)*
(GECCO '24), which uses FI-2Pop to maximise difficulty on a 1–7 scale — the
same scale used here, so output is comparable.

The deciding factor was the narrative round-trip: verifying that an LLM's prose
still means the original puzzle needs a typed, machine-comparable clue
representation, and no existing project exposes one.

The format itself is copied from
[Penny Dell's own solving guide](https://www.pennydellpuzzles.com/wp-content/uploads/2019/03/How-to-Solve-Logic-Problems.pdf),
whose worked example is transcribed into `tests/test_penny_dell_sample.py` as a
correctness check: the engine agrees with the publisher's own stated answer and,
like their walkthrough, reaches it without guessing. Three details from that
guide shape the design:

1. **A numbered clue bundles several facts.** *"Anne was married on Monday, but
   not to Wally"* is two constraints under one number.
2. **The introduction carries logical weight.** Their guide says so outright:
   "All the information you need … is given in the introduction and clues." The
   all-different conditions live there, not in the clue list.
3. **Parenthetical embedding.** *"Vern (who married Fran) was married the day
   after Eve"* folds a pairing into the subject of an ordering clue.

"Penny Dell" is someone else's trademark; this package imitates the *format*,
not the brand.

---

## How generation works

The loop is deliberately boring, because the properties that matter are
**verified rather than argued for**:

1. invent a random solution;
2. enumerate a pool of clue atoms that are **all true of that solution** — so
   the clue set can never be self-contradictory, whatever subset is chosen;
3. add atoms until the uniqueness oracle reports exactly one solution;
4. repeatedly try to drop each atom, keeping only those whose removal costs
   uniqueness — so **every surviving clue is load-bearing**;
5. solve it the way a person would and *measure* the difficulty that falls out;
6. if that misses the requested band, discard the whole thing and retry.

Step 4 is what separates a pleasant puzzle from a slog: an unminimised clue set
is typically twice the size it needs to be and full of clues that do nothing.
`tests/test_generator.py` asserts minimality by brute force — for every
generated puzzle, dropping any single clue must lose uniqueness.

### The spine

One category is the **spine**, and it supplies the puzzle's index: entity *p* is
the one holding `spine.items[p]`. This kills the *M!* relabelling symmetry a
naive "entity id" model suffers from, and makes every positional clue trivial to
evaluate — an entity's position *is* its index. An ordered spine unlocks
before/adjacent/between clues; a spine carrying numeric values also unlocks
arithmetic ones.

### Item names are globally unique

Enforced by `Schema`. This is what lets a clue — and a narrative paragraph —
name an item without also naming its category, which removes a large class of
ambiguity from the LLM round-trip. An extractor can write `"Marigold"` and the
right category is recovered automatically.

---

## Difficulty is measured, not asserted

`human_solver.py` solves with a ladder of **named human techniques**, always
reaching for the cheapest rung that still makes progress, and reports the
highest rung it was forced onto:

| # | Technique | What it is |
|---|---|---|
| 1 | `direct` | a clue names a cell; equalities carry the fact around |
| 2 | `bijection` | one item per position, one position per item |
| 3 | `order` | positional and arithmetic reasoning |
| 4 | `disjunction` | resolving either/or, not-both and if-then clues |
| 5 | `subset` | naked and hidden pairs/triples |
| 6 | `trial` | assume a cell, hit a contradiction, rule it out |

A puzzle the ladder cannot finish is **discarded**, not shipped — solvable by
search is not the same as solvable by a person. Only the `expert` profile is
permitted to require guessing; a test asserts the rest never do.

The 1–7 rating comes from a weighted score (hardest technique required, how
often the expensive techniques were needed, how few cells are given away, grid
size, compound-clue count). The weights' units are arbitrary, so the cut points
are **calibrated from data**:

```bash
python scripts/calibrate.py --samples 24
```

The committed thresholds come from 24 samples per profile. Profile medians came
out at 3.97 / 4.93 / 5.51 / 9.51 / 16.09 for gentle → expert — monotonic, so the
score function ranks difficulty correctly and only the cut points needed
setting.

### Complexity knobs

```python
PuzzleSpec(
    difficulty="hard",      # gentle | easy | moderate | hard | expert
    seed=1234,
    categories=5, items=5,  # grid shape
    theme="county_fair",
    kinds=("link", "not_link", "before", "or"),   # allowed clue types
    max_positive=1,         # cap on free "X goes with Y" clues — the big dial
    allow_trial=False,      # may the puzzle need guessing?
    max_bundle=3,           # facts per numbered clue
)
```

`max_positive` is the most effective single knob: a puzzle whose clues are
mostly flat pairings is easy however large the grid.

The built-in 50-puzzle ramp is 8 gentle, 10 easy, 12 moderate, 12 hard, 8
expert, across 27 themes and grids from 3×4 to 5×6.

---

## Phase 2: narrative, and proving it survived

```
puzzle.json  ──▶ NARRATOR (context-free)  ──▶ narrative
                                                 │
                        ┌────────────────────────┼────────────────────────┐
                        ▼                        ▼                        ▼
                   EXTRACTOR 1             EXTRACTOR 2             EXTRACTOR 3
                        └────────────────────────┼────────────────────────┘
                                                 ▼
                                           four gates
```

Each extractor sees **only the narrative** — never the clue list, never the
solution, never the theme metadata — and must rebuild the formal clues from the
prose alone. The narrator is never shown the solution, so it cannot leak it.

Each reading faces four checks, in increasing order of what they prove:

1. **parse** — it decodes, and every name it uses is part of the cast.
2. **cast** — the categories it found match the real ones (catches an
   introduction that dropped a member or mangled a spelling).
3. **solution** — *the one that matters.* Feed the reading to the uniqueness
   oracle: exactly one solution, and it must be the original. Pass this and the
   narrative is **provably solvable to the right answer**.
4. **IR equality** — the reading is identical to the original, atom for atom.

Verdicts: `pass` (all readers agree down to the IR), `pass_equivalent` (all
readers recover the right unique solution by a differently-shaped but equivalent
route) and `fail`. On failure the diff is fed back to the narrator as prose
feedback — phrased in terms of meaning, since the narrator was never shown the
notation — and it tries again.

### The blind spot, stated honestly

The solution check catches drift **exactly when the drifted clue set no longer
has the original solution as its unique model**. That covers most real mistakes,
and it fires through three different symptoms — no solution, several solutions,
or one solution that is the wrong one.

It is **blind** to drift that leaves the original solution still unique. Two
cases do that:

- **tightening** a clue the answer happens to satisfy — narrate "earlier than"
  as "just before" when they really *are* adjacent;
- **loosening** a clue whose work the others already do — drop "immediately"
  from a chain that is pinned at both ends anyway.

Both leave a puzzle that is solvable to the right answer, so neither is
*broken* — but both are a different puzzle, usually an easier one. What catches
them is **agreement between independent readers**: if every reader missed the
same fact, or every reader invented the same fact, the narrative itself drifted,
and that is disqualifying. If the readers merely differ from one another, the
prose is ambiguous — also worth knowing, since a human solver could read it
either way.

Both cases are pinned down as tests in `tests/test_roundtrip_gate.py`, so the
blind spot cannot quietly widen.

### Anti-drift measures on the narrator

The pitfall is narration silently strengthening a constraint. Guards:

- every atom is handed over with a **gloss generated from the IR itself** that
  spells out what it does and does not assert — direction, symmetry,
  exclusivity;
- the system prompt lists the specific traps in the imperative: *"earlier"* is
  not *"just before"*; *"adjacent"* is symmetric; *"between"* is exclusive with
  unordered endpoints; a gap of N means positions **differ** by N, not N *in
  between* (that off-by-one is the single likeliest way to change a clue);
  *if-then* is not biconditional; *either/or* is inclusive; *not both* permits
  neither;
- the backstory must be **logically inert** — the introduction may state only
  the entity count, the categories with their full item lists, and the
  all-different conditions;
- gaps are only ever rendered as "N apart", never "N in between".

### Running it

Costs nothing and needs no key:

```bash
logicgrid narrate puzzles --dry-run --show      # assemble prompts, print one
```

Then, with `ANTHROPIC_API_KEY` set:

```bash
logicgrid narrate puzzles --no-dry-run --readers 3 --required 3
```

Both roles default to `claude-opus-5-5`. Extraction is the gate and 3 of every 4
calls, so it is the obvious place to trade accuracy for cost if you want to —
`--extractor-model claude-haiku-5-5` is ~40× cheaper per token. That is your
call, not a default. `llm.py` also exposes `complete_batch`, which runs a whole
set through the Batches API at half price.

---

## Playing them

```bash
logicgrid-play puzzles                 # start at the first puzzle
logicgrid-play puzzles --puzzle 34     # or by number, name or substring
logicgrid-play puzzles --list          # just list what is there
```

Installing the extra, which needs `textual`. The quotes are only there to stop
bash and zsh globbing `[play]`, so the right form depends on your shell:

```bash
pip install -e '.[play]'    # bash / zsh, including Git Bash
pip install -e ".[play]"    # PowerShell
pip install -e .[play]      # cmd.exe -- it treats ' as a literal character
```

A Textual TUI (`src/puzzleplay/`). **Chosen over a web app because it has to be
playable over SSH**: it runs in the session you are already in, with no port
forwarding, no firewall hole and nothing to reconnect for. Textual ships a test
pilot, so unlike curses it stays genuinely testable — `tests/test_play_app.py`
drives the real widgets with real keypresses.

Layout: a tab per pair of categories, each a grid with a cell cursor; the clue
list beside it; the answer sheet below. Column headers name the cross category
using the shortest prefixes that still tell its items apart — leading articles
and any shared prefix dropped first, so "a fluted rim" / "a fork-crimped edge"
become `flu` / `for`, and "slot one" / "slot two" become `one` / `two`. A legend
line spells them out, and the status line always names the exact cell you are
on.

| key | |
|---|---|
| arrows / mouse | move the cell cursor |
| `]` `[` | next / previous grid |
| `1`-`9` | jump straight to a grid |
| `o` | these two go together |
| `x` | these two do not |
| `space` | cycle `.` → `O` → `x` → `.` |
| `backspace` | clear the cell |
| `u` | undo |
| `c` | check my work so far |
| `a` | toggle assist |
| `n` `p` | next / previous puzzle |
| `s` | reveal the solution |
| `?` | help |

Finishing the answer sheet announces itself: **SOLVED** if every placing is
right, or *"not quite — N marks are wrong"* if not. `c` checks at any point and
names the offending cells.

### Only your own marks are stored

Circling a cell forces x's across its row and column, and assist can chain
further. None of that is stored as if you had marked it — the board keeps *your*
marks and recomputes the closure on every change. So changing your mind about a
cell withdraws everything that followed from it, rather than leaving behind x's
nothing supports any more. It also makes undo a snapshot and makes toggling
assist a pure recompute.

Assist is off by default. Row-and-column elimination is bookkeeping the rules
force, so that is always on; transitivity and last-cell-standing are real
deductions, so they stay opt-in — otherwise the program is solving the puzzle,
not you.

---

## CLI

| Command | What it does |
|---|---|
| `logicgrid gen --count 50 --out puzzles` | generate a set along the difficulty ramp |
| `logicgrid gen --difficulty expert --count 5` | one profile throughout |
| `logicgrid show P.json --trace` | print a puzzle, with the deduction walkthrough |
| `logicgrid solve P.json` | re-verify uniqueness and hand-solve |
| `logicgrid stats puzzles` | verify and summarise a folder |
| `logicgrid themes` | list the 27 theme packs |
| `logicgrid narrate puzzles --dry-run` | assemble phase-2 prompts without calling the API |

---

## Layout

```
src/logicgrid/
  model.py         Category / Ref / Schema / Solution / Clue
  clues.py         the clue IR: 14 atom types, JSON codec, prose + glosses
  csp.py           propagation and the uniqueness oracle
  human_solver.py  the technique ladder; difficulty's raw material
  difficulty.py    score, 1-7 rating, generation profiles
  generate.py      solution -> pool -> grow -> minimise -> rate
  themes.py        27 theme packs and 9 spines
  render.py        canonical text, solving charts, solution pages
  llm.py           Claude client: single, concurrent and batch
  narrate.py       narrator prompt and reply decoding
  extract.py       extractor prompt, schema and lenient decoding
  verify.py        the four gates, consensus drift, retry loop
  cli.py
src/puzzleplay/      the terminal player (Textual)
  board.py           the solving chart: your marks, plus what they force
  library.py         puzzle discovery
  render.py          clue / answer / help panels
  app.py             the app, bindings and layout
scripts/calibrate.py
tests/
puzzles/           50 generated puzzles + index.md
```

### Clue prose

A clue can only read well if the categories know what they *mean*, so each one
carries a third-person verb and both polarities are derived from it:

| | |
|---|---|
| `verb="harvests in"` | "Leocadia harvests in April" / "Leocadia does not harvest in April" |
| `verb="is troubled by"` | "Leocadia is troubled by thrips" / "... is not troubled by thrips" |

Negation is mechanical: an auxiliary takes `not` directly, anything else gets
do-support with the `-s` stripped. `tests/test_phrasing.py` runs every verb in
every theme pack through it, because a past-tense slip ships as *"does not
contained"* — which is exactly what that test caught.

Two further pieces make it work:

- **a subject.** One axis per theme holds the actors, and clues prefer it as the
  grammatical subject. `Link` normalises its arguments, so phrasing cannot
  depend on which way round the atom was built.
- **a descriptor** for when no name is involved: an entity can be named by any
  of its attributes — "the grower who is troubled by thrips" — so an
  attribute-to-attribute clue still gets a subject. Descriptors are
  possessive-free by construction, because "the grower who is troubled by
  thrips's month" is unparseable. The relative pronoun follows the entity:
  people get *who*, a clock gets *that*.

The introduction states a task rather than a schema — *"Four growers are
involved. Determine each grower's harvest month and pest."* — while still
carrying every condition a solver needs, which Penny Dell's guide is explicit
about.

`distinct` is excluded from generation: *"Leocadia, thrips and April are three
different growers"* is confusing when Grower is itself a category, and plain
negatives say the same thing clearly. The atom stays in the IR, since an
extractor may legitimately read one out of a narrative.

### The clue IR

Symmetric arguments are **normalised at construction**, so `Adjacent(a, b)` and
`Adjacent(b, a)` build the same object and ordinary `==` is already semantic
comparison — which is what the round-trip gate relies on.

| Tier | Kinds |
|---|---|
| A — pairing | `link`, `not_link` |
| B — structure | `distinct`, `before`, `immediately_before`, `adjacent`, `between`, `gap`, `parity`, `arith` |
| C — compound | `not`, `or`, `not_both`, `if_then` |

Atoms need only declare their refs and test one candidate tuple; propagation is
generalised arc consistency over the (tiny) product of their domains. Adding a
clue type therefore means writing `check()`, `render()` and `gloss()` — no
bespoke propagator.

---

## Tests

```bash
python -m pytest            # 462 passed, 3 skipped
```

- `test_penny_dell_sample.py` — the published sample puzzle: our engine finds
  the publisher's stated answer, confirms it is unique, and reaches it without
  guessing.
- `test_generator.py` — per-puzzle properties across 5 profiles × 3 seeds: every
  clue true of its own solution, exactly one solution, hand-solvable, no
  guessing below expert, **every clue load-bearing**, rating in band, JSON
  round-trip, globally unique item names, determinism.
- `test_roundtrip_gate.py` — the phase-2 gate against hand-written *drifted*
  extractions, **offline, no API calls**: loosening, reversal, contradictory
  tightening, dropped facts, the gap off-by-one, renamed cast, lost cast member,
  and the two consensus-only cases. These are what justify spending money on the
  pipeline.
- `test_board.py` / `test_play_app.py` — the player: forced bookkeeping,
  refused conflicts, editing a cell withdrawing what it forced, assist
  soundness, and a full playthrough of a real puzzle driven by nothing but
  cursor keys and `o`, ending in the solved banner.
- `test_pipeline.py` — the whole narrate → extract → verify → retry loop driven
  by canned replies, again offline: prompts assemble, the narrator prompt does
  not leak the solution, a wrong clue count is rejected, a failure really does
  feed back into a second attempt, one reader's error doesn't sink the run, and
  the extraction schema stays strict-structured-outputs-safe (no union types,
  every property required).

---

## Running one round-trip by hand

`scripts/demo_roundtrip.py` splits the pipeline into three file-based steps, so
the model in the middle can be anything that reads a prompt and returns JSON — a
subagent, a chat window, a different provider:

```bash
python scripts/demo_roundtrip.py --dir demo dump puzzles/42-regatta.json
#   -> demo/narrator_prompt.txt        hand to a narrator, save the reply
python scripts/demo_roundtrip.py --dir demo narrate --reply demo/narrator_reply.json
#   -> demo/narrative.txt, demo/extractor_prompt.txt
python scripts/demo_roundtrip.py --dir demo verify demo/replies/reader*.json
#   -> per-check results and the verdict
```

Give each reader the extractor prompt in a directory of its own. The prompt
contains the narrative and nothing else, and keeping it isolated is what makes
"independent reader" true rather than aspirational.

### What the first real round-trip found

Run on `42-regatta.json` (hard, 5/7, 7 clues covering 8 of the 14 atom types)
with one narrator and three genuinely isolated readers, the gate initially
rejected all three readings — and it was **wrong to**. Every reader had written
`Last Resort` where the item is called `the Last Resort`.

Unanimity is the tell. A single reader doing that is a quirk; all three doing it
means it is a fact about English rather than about the model: "The Last Resort
finished second" is the only way to start that sentence, and the article belongs
to the grammar, not to the name. So resolution is now tolerant of case,
whitespace and a leading `the`/`a`/`an` — and nothing else, so `Annie` still
fails to resolve to `Anne`. The tolerance only applies where the stripped form
stays unambiguous.

With that fixed, the same three readings pass all four checks: **3/3 recovered
the one true solution, 3/3 matched the clue set atom for atom.** Both the
resolver tolerance and its limits are now tests.

The lesson generalises: a gate this strict will produce false positives, and the
cheap way to find them is to run the loop once, by hand, before paying for 200
calls.

### A hazard worth knowing about

Some item names contain "and" — `lilac and bronze`, `mustard and black`,
`a bell and gong`. Rendered naively, "Lilac and bronze and fifth are next to
each other" is genuinely ambiguous prose, and that ambiguity is invisible in the
formal clue. A competent narrator disambiguates ("the entry **in** lilac and
bronze"), and the round-trip gate catches it when one doesn't — but if you add
themes, prefer item names that do not contain a conjunction.
