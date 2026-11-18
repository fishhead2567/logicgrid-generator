# The Wind Is Free, the Field Is Not

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `62c05f182b20`

## Introduction

The Dunnage Kite Festival charges by the kite, which has produced some creative definitions of 'one kite'.
Four fliers are involved. Determine each flier's entry fee and mishap.
- **Flier**: Blaise, Aurelio, Gunnar and Tansy.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6 and $8.
- **Mishap**: a power line scare, a snapped spar, a tangled line and a trespassing dog.
Every flier has a different entry fee and mishap, so within each category every item is used exactly once.

## Clues

1. Blaise pays $2.
2. Gunnar is undone by a snapped spar.
3. Blaise is undone by a tangled line.
4. The flier who is undone by a power line scare and $2 are exactly one fee step apart in entry fee order, in one direction or the other.
5. Tansy and $8 are exactly one fee step apart in entry fee order, in one direction or the other.

## Solving chart

*Entry fee vs Flier*

| | Blaise | Aurelio | Gunnar | Tansy |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Entry fee vs Mishap*

| | a power line scare | a snapped spar | a tangled line | a trespassing dog |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Flier vs Mishap*

| | a power line scare | a snapped spar | a tangled line | a trespassing dog |
|---|---|---|---|---|
| **Blaise** | | | | |
| **Aurelio** | | | | |
| **Gunnar** | | | | |
| **Tansy** | | | | |

## Solution

| Entry fee | Flier | Mishap |
|---|---|---|
| $2 | Blaise | a tangled line |
| $4 | Aurelio | a power line scare |
| $6 | Tansy | a trespassing dog |
| $8 | Gunnar | a snapped spar |

## How it falls out

1. [direct] from clue 4 flier:Blaise: ruled out position(s) 2,3,4
2. [direct] from clue 5 mishap:a tangled line: ruled out position(s) 2,3,4
3. [bijection] flier:Aurelio: ruled out position(s) 1
4. [bijection] flier:Gunnar: ruled out position(s) 1
5. [bijection] flier:Tansy: ruled out position(s) 1
6. [bijection] mishap:a power line scare: ruled out position(s) 1
7. [bijection] mishap:a snapped spar: ruled out position(s) 1
8. [bijection] mishap:a trespassing dog: ruled out position(s) 1
9. [order] from clue 3 flier:Tansy: ruled out position(s) 2,4
10. [order] from clue 1 mishap:a power line scare: ruled out position(s) 3,4
11. [bijection] flier:Aurelio: ruled out position(s) 3
12. [bijection] flier:Gunnar: ruled out position(s) 3
13. [bijection] mishap:a snapped spar: ruled out position(s) 2
14. [bijection] mishap:a trespassing dog: ruled out position(s) 2
15. [direct] from clue 2 flier:Gunnar: ruled out position(s) 2
16. [direct] from clue 2 mishap:a snapped spar: ruled out position(s) 3
17. [bijection] flier:Aurelio: ruled out position(s) 4
18. [bijection] mishap:a trespassing dog: ruled out position(s) 4

---

<sub>seed `2026172832408` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
