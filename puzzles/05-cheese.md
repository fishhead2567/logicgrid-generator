# The Cheesemongers' Standoff

*A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.*

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 4 &nbsp;&nbsp; **id** `f136fe730fc1`

## Introduction

There are 4 wheels. Each has exactly one price and one item from every other category below, and within each category every item belongs to a different wheel.
- **Price** (listed in order): $3, $5, $7 and $9.
- **Cheese**: Saltpans, Oakmoss, Bellringer and Winter Tarn.
- **Rind**: a cloth-bound rind, a natural rind, a washed rind and a waxed rind.
The price steps above are listed in order, from $3 to $9.

## Clues

1. Saltpans goes with $7. $7 goes with a natural rind.
2. Winter Tarn goes with a waxed rind. Winter Tarn goes with $3.
3. Bellringer goes with a cloth-bound rind.
4. $5 does not go with a washed rind.

## Solving chart

*Price vs Cheese*

| | Saltpans | Oakmoss | Bellringer | Winter Tarn |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Price vs Rind*

| | a cloth-bound rind | a natural rind | a washed rind | a waxed rind |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Cheese vs Rind*

| | a cloth-bound rind | a natural rind | a washed rind | a waxed rind |
|---|---|---|---|---|
| **Saltpans** | | | | |
| **Oakmoss** | | | | |
| **Bellringer** | | | | |
| **Winter Tarn** | | | | |

## Solution

| Price | Cheese | Rind |
|---|---|---|
| $3 | Winter Tarn | a waxed rind |
| $5 | Bellringer | a cloth-bound rind |
| $7 | Saltpans | a natural rind |
| $9 | Oakmoss | a washed rind |

## How it falls out

1. [direct] from clue 6 rind:a natural rind: ruled out position(s) 1,2,4
2. [direct] from clue 5 rind:a washed rind: ruled out position(s) 2
3. [direct] from clue 4 cheese:Winter Tarn: ruled out position(s) 2,3,4
4. [direct] from clue 3 rind:a waxed rind: ruled out position(s) 2,3,4
5. [direct] from clue 1 cheese:Saltpans: ruled out position(s) 1,2,4
6. [bijection] cheese:Oakmoss: ruled out position(s) 1,3
7. [bijection] cheese:Bellringer: ruled out position(s) 1,3
8. [bijection] rind:a cloth-bound rind: ruled out position(s) 1,3
9. [bijection] rind:a washed rind: ruled out position(s) 1,3
10. [bijection] rind:a cloth-bound rind: ruled out position(s) 4
11. [direct] from clue 2 cheese:Bellringer: ruled out position(s) 4
12. [bijection] cheese:Oakmoss: ruled out position(s) 2

---

<sub>seed `2026172615031` &middot; score 2.285 &middot; atoms 6 &middot; positives 5 &middot; solved by bijection</sub>
