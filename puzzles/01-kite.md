# The Wind Is Free, the Field Is Not

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 3 &nbsp;&nbsp; **id** `89f5280affb0`

## Introduction

The Dunnage Kite Festival charges by the kite, which has produced some creative definitions of 'one kite'.
Four fliers are involved. Determine each flier's entry fee and mishap.
- **Flier**: Ifeoma, Blaise, Tansy and Kipling.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6 and $8.
- **Mishap**: a snapped spar, a trespassing dog, a sudden lull and a power line scare.
Every flier has a different entry fee and mishap, so within each category every item is used exactly once.

## Clues

1. The flier who is undone by a power line scare pays $6. Tansy is undone by a power line scare.
2. Kipling is not undone by a snapped spar. The flier who is undone by a snapped spar is exactly one fee step cheaper than $6, with no entry fee in between.
3. Blaise is not undone by a trespassing dog. Kipling is cheaper than the flier who is undone by a trespassing dog in entry fee order.

## Solving chart

*Entry fee vs Flier*

| | Ifeoma | Blaise | Tansy | Kipling |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Entry fee vs Mishap*

| | a snapped spar | a trespassing dog | a sudden lull | a power line scare |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Flier vs Mishap*

| | a snapped spar | a trespassing dog | a sudden lull | a power line scare |
|---|---|---|---|---|
| **Ifeoma** | | | | |
| **Blaise** | | | | |
| **Tansy** | | | | |
| **Kipling** | | | | |

## Solution

| Entry fee | Flier | Mishap |
|---|---|---|
| $2 | Kipling | a sudden lull |
| $4 | Blaise | a snapped spar |
| $6 | Tansy | a power line scare |
| $8 | Ifeoma | a trespassing dog |

## How it falls out

1. [direct] from clue 5 mishap:a power line scare: ruled out position(s) 1,2,4
2. [direct] from clue 4 flier:Tansy: ruled out position(s) 1,2,4
3. [bijection] flier:Ifeoma: ruled out position(s) 3
4. [bijection] flier:Blaise: ruled out position(s) 3
5. [bijection] flier:Kipling: ruled out position(s) 3
6. [bijection] mishap:a snapped spar: ruled out position(s) 3
7. [bijection] mishap:a trespassing dog: ruled out position(s) 3
8. [bijection] mishap:a sudden lull: ruled out position(s) 3
9. [order] from clue 3 mishap:a snapped spar: ruled out position(s) 1,4
10. [order] from clue 2 flier:Kipling: ruled out position(s) 4
11. [order] from clue 2 mishap:a trespassing dog: ruled out position(s) 1
12. [direct] from clue 1 flier:Kipling: ruled out position(s) 2
13. [bijection] flier:Ifeoma: ruled out position(s) 1
14. [bijection] flier:Blaise: ruled out position(s) 1
15. [bijection] mishap:a trespassing dog: ruled out position(s) 2
16. [bijection] mishap:a sudden lull: ruled out position(s) 2
17. [bijection] mishap:a sudden lull: ruled out position(s) 4
18. [direct] from clue 6 flier:Blaise: ruled out position(s) 4
19. [bijection] flier:Ifeoma: ruled out position(s) 2

---

<sub>seed `2026172583355` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
