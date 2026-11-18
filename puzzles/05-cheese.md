# The Cheesemongers' Standoff

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `4c437f283d38`

## Introduction

A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.
Four cheeses are involved. Determine each cheese's price and rind.
- **Cheese**: Oakmoss, Saltpans, Old Thrashing and Bellringer.
- **Price** (listed from cheaper to dearer): $3, $5, $7 and $9.
- **Rind**: an ash-coated rind, a cloth-bound rind, a washed rind and a waxed rind.
Every cheese has a different price and rind, so within each category every item is used exactly once.

## Clues

1. Oakmoss sells for $7.
2. Old Thrashing sells for $5.
3. Saltpans sells for $9.
4. The cheese that has a washed rind sells for $9.
5. The cheese that has a cloth-bound rind does not sell for $3.
6. $3 is exactly one price step cheaper than the cheese that has an ash-coated rind, with no price in between.

## Solving chart

*Price vs Cheese*

| | Oakmoss | Saltpans | Old Thrashing | Bellringer |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Price vs Rind*

| | an ash-coated rind | a cloth-bound rind | a washed rind | a waxed rind |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Cheese vs Rind*

| | an ash-coated rind | a cloth-bound rind | a washed rind | a waxed rind |
|---|---|---|---|---|
| **Oakmoss** | | | | |
| **Saltpans** | | | | |
| **Old Thrashing** | | | | |
| **Bellringer** | | | | |

## Solution

| Price | Cheese | Rind |
|---|---|---|
| $3 | Bellringer | a waxed rind |
| $5 | Old Thrashing | an ash-coated rind |
| $7 | Oakmoss | a cloth-bound rind |
| $9 | Saltpans | a washed rind |

## How it falls out

1. [direct] from clue 6 cheese:Old Thrashing: ruled out position(s) 1,3,4
2. [direct] from clue 5 cheese:Oakmoss: ruled out position(s) 1,2,4
3. [direct] from clue 3 rind:a cloth-bound rind: ruled out position(s) 1
4. [direct] from clue 2 cheese:Saltpans: ruled out position(s) 1,2,3
5. [direct] from clue 1 rind:a washed rind: ruled out position(s) 1,2,3
6. [bijection] cheese:Bellringer: ruled out position(s) 2,3,4
7. [bijection] rind:an ash-coated rind: ruled out position(s) 4
8. [bijection] rind:a cloth-bound rind: ruled out position(s) 4
9. [bijection] rind:a waxed rind: ruled out position(s) 4
10. [order] from clue 4 rind:an ash-coated rind: ruled out position(s) 1,3
11. [bijection] rind:a cloth-bound rind: ruled out position(s) 2
12. [bijection] rind:a waxed rind: ruled out position(s) 2
13. [bijection] rind:a waxed rind: ruled out position(s) 3

---

<sub>seed `2026172615031` &middot; score 3.67 &middot; atoms 6 &middot; positives 4 &middot; solved by order</sub>
