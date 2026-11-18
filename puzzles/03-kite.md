# The Wind Is Free, the Field Is Not

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 4 &nbsp;&nbsp; **id** `5e32edb2fea6`

## Introduction

The Dunnage Kite Festival charges by the kite, which has produced some creative definitions of 'one kite'.
Four fliers are involved. Determine each flier's entry fee and kite.
- **Flier**: Ifeoma, Gunnar, Tansy and Kipling.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6 and $8.
- **Kite**: a delta wing, a paper sled kite, a rokkaku fighter and a box kite.
Every flier has a different entry fee and kite, so within each category every item is used exactly once.

## Clues

1. Kipling pays $4.
2. Tansy flies a box kite. The flier who flies a box kite pays $6.
3. The flier who flies a rokkaku fighter pays $4. The flier who flies a rokkaku fighter is cheaper than Gunnar in entry fee order.
4. The flier who flies a delta wing does not pay $2.

## Solving chart

*Entry fee vs Flier*

| | Ifeoma | Gunnar | Tansy | Kipling |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Entry fee vs Kite*

| | a delta wing | a paper sled kite | a rokkaku fighter | a box kite |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Flier vs Kite*

| | a delta wing | a paper sled kite | a rokkaku fighter | a box kite |
|---|---|---|---|---|
| **Ifeoma** | | | | |
| **Gunnar** | | | | |
| **Tansy** | | | | |
| **Kipling** | | | | |

## Solution

| Entry fee | Flier | Kite |
|---|---|---|
| $2 | Ifeoma | a paper sled kite |
| $4 | Kipling | a rokkaku fighter |
| $6 | Tansy | a box kite |
| $8 | Gunnar | a delta wing |

## How it falls out

1. [direct] from clue 6 kite:a box kite: ruled out position(s) 1,2,4
2. [direct] from clue 5 kite:a rokkaku fighter: ruled out position(s) 1,3,4
3. [direct] from clue 4 kite:a delta wing: ruled out position(s) 1
4. [direct] from clue 3 flier:Tansy: ruled out position(s) 1,2,4
5. [direct] from clue 1 flier:Kipling: ruled out position(s) 1,3,4
6. [bijection] flier:Ifeoma: ruled out position(s) 2,3
7. [bijection] flier:Gunnar: ruled out position(s) 2,3
8. [bijection] kite:a delta wing: ruled out position(s) 2,3
9. [bijection] kite:a paper sled kite: ruled out position(s) 2,3
10. [bijection] kite:a paper sled kite: ruled out position(s) 4
11. [order] from clue 2 flier:Gunnar: ruled out position(s) 1
12. [bijection] flier:Ifeoma: ruled out position(s) 4

---

<sub>seed `2026172599193` &middot; score 3.67 &middot; atoms 6 &middot; positives 4 &middot; solved by order</sub>
