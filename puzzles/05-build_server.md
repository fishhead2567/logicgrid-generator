# The Build Server Contest

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `9fc20fe8ba55`

## Introduction

A creative-mode server, one weekend, and a block limit everybody swore they would stay under.
Four builders are involved. Determine each builder's score and material.
- **Builder**: Keiko, Nadine, Thandiwe and Oscar Pell.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points and 70 points.
- **Material**: sea lantern, sandstone, quartz and copper.
Every builder has a different score and material, so within each category every item is used exactly once.

## Clues

1. The builder who builds it from sandstone scores 61 points.
2. The builder who builds it from quartz scores 70 points.
3. Keiko and 64 points are exactly one score step apart in score order, in one direction or the other. Keiko does not build it from copper.
4. Oscar Pell is exactly one score step lower than 67 points, with no score in between.
5. Thandiwe is lower than the builder who builds it from sea lantern in score order.

## Solving chart

*Score vs Builder*

| | Keiko | Nadine | Thandiwe | Oscar Pell |
|---|---|---|---|---|
| **61 points** | | | | |
| **64 points** | | | | |
| **67 points** | | | | |
| **70 points** | | | | |

*Score vs Material*

| | sea lantern | sandstone | quartz | copper |
|---|---|---|---|---|
| **61 points** | | | | |
| **64 points** | | | | |
| **67 points** | | | | |
| **70 points** | | | | |

*Builder vs Material*

| | sea lantern | sandstone | quartz | copper |
|---|---|---|---|---|
| **Keiko** | | | | |
| **Nadine** | | | | |
| **Thandiwe** | | | | |
| **Oscar Pell** | | | | |

## Solution

| Score | Builder | Material |
|---|---|---|
| 61 points | Thandiwe | sandstone |
| 64 points | Oscar Pell | copper |
| 67 points | Keiko | sea lantern |
| 70 points | Nadine | quartz |

## How it falls out

1. [direct] from clue 5 material:quartz: ruled out position(s) 1,2,3
2. [direct] from clue 2 material:sandstone: ruled out position(s) 2,3,4
3. [bijection] material:sea lantern: ruled out position(s) 1,4
4. [bijection] material:copper: ruled out position(s) 1,4
5. [order] from clue 6 builder:Keiko: ruled out position(s) 2,4
6. [order] from clue 4 builder:Oscar Pell: ruled out position(s) 1,3,4
7. [order] from clue 3 builder:Thandiwe: ruled out position(s) 3,4
8. [bijection] builder:Nadine: ruled out position(s) 2
9. [bijection] builder:Thandiwe: ruled out position(s) 2
10. [bijection] builder:Nadine: ruled out position(s) 1,3
11. [bijection] builder:Keiko: ruled out position(s) 1
12. [direct] from clue 1 material:copper: ruled out position(s) 3
13. [bijection] material:sea lantern: ruled out position(s) 2

---

<sub>seed `2026172815037` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
