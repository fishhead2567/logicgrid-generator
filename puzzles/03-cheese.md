# The Cheesemongers' Standoff

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `187d63d44cfc`

## Introduction

A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.
Four cheeses are involved. Determine each cheese's price and maker.
- **Cheese**: Old Thrashing, Saltpans, Winter Tarn and Bellringer.
- **Price** (listed from cheaper to dearer): $3, $5, $7 and $9.
- **Maker**: Lachlan, Ambrose, Perdita and Hepzibah.
Every cheese has a different price and maker, so within each category every item is used exactly once.

## Clues

1. Saltpans sells for $3.
2. The cheese that was made by Lachlan sells for $7.
3. Winter Tarn does not sell for $9.
4. Winter Tarn was not made by Ambrose.
5. Old Thrashing is exactly one price step cheaper than the cheese that was made by Hepzibah, with no price in between.

## Solving chart

*Price vs Cheese*

| | Old Thrashing | Saltpans | Winter Tarn | Bellringer |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Price vs Maker*

| | Lachlan | Ambrose | Perdita | Hepzibah |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Cheese vs Maker*

| | Lachlan | Ambrose | Perdita | Hepzibah |
|---|---|---|---|---|
| **Old Thrashing** | | | | |
| **Saltpans** | | | | |
| **Winter Tarn** | | | | |
| **Bellringer** | | | | |

## Solution

| Price | Cheese | Maker |
|---|---|---|
| $3 | Saltpans | Ambrose |
| $5 | Winter Tarn | Perdita |
| $7 | Old Thrashing | Lachlan |
| $9 | Bellringer | Hepzibah |

## How it falls out

1. [direct] from clue 5 maker:Lachlan: ruled out position(s) 1,2,4
2. [direct] from clue 3 cheese:Winter Tarn: ruled out position(s) 4
3. [direct] from clue 1 cheese:Saltpans: ruled out position(s) 2,3,4
4. [bijection] cheese:Old Thrashing: ruled out position(s) 1
5. [bijection] cheese:Winter Tarn: ruled out position(s) 1
6. [bijection] cheese:Bellringer: ruled out position(s) 1
7. [bijection] maker:Ambrose: ruled out position(s) 3
8. [bijection] maker:Perdita: ruled out position(s) 3
9. [bijection] maker:Hepzibah: ruled out position(s) 3
10. [order] from clue 4 cheese:Old Thrashing: ruled out position(s) 2,4
11. [order] from clue 4 maker:Hepzibah: ruled out position(s) 1,2
12. [bijection] cheese:Winter Tarn: ruled out position(s) 3
13. [bijection] cheese:Bellringer: ruled out position(s) 3
14. [bijection] cheese:Bellringer: ruled out position(s) 2
15. [bijection] maker:Ambrose: ruled out position(s) 4
16. [bijection] maker:Perdita: ruled out position(s) 4
17. [direct] from clue 2 maker:Ambrose: ruled out position(s) 2
18. [bijection] maker:Perdita: ruled out position(s) 1

---

<sub>seed `2026172899202` &middot; score 4.27 &middot; atoms 5 &middot; positives 2 &middot; solved by order</sub>
