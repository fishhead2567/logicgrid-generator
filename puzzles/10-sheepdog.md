# The Clun Forest Trials

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `18d702673a4e`

## Introduction

A hillside, a flock with its own ideas, and a judge who deducts for a wide outrun with the enthusiasm of someone settling an old score.
Five handlers are involved. Determine each handler's score and dog.
- **Handler**: Constance, Eiddwen, Marged, Huw Pryce and Tarrant.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Dog**: Bute, Gyp, Fly, Nell and Craig.
Every handler has a different score and dog, so within each category every item is used exactly once.

## Clues

1. The handler who runs Gyp scores 73 points.
2. The handler who runs Bute is lower than Constance in score order. The handler who runs Bute falls somewhere between 61 points and 67 points in score order.
3. Tarrant is higher than 70 points in score order.
4. The handler who runs Fly and 67 points are exactly one score step apart in score order, in one direction or the other.
5. Huw Pryce is exactly one score step lower than 70 points, with no score in between.
6. The handler who runs Craig is lower than Marged in score order.

## Solving chart

*Score vs Handler*

| | Constance | Eiddwen | Marged | Huw Pryce | Tarrant |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Dog*

| | Bute | Gyp | Fly | Nell | Craig |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Handler vs Dog*

| | Bute | Gyp | Fly | Nell | Craig |
|---|---|---|---|---|---|
| **Constance** | | | | | |
| **Eiddwen** | | | | | |
| **Marged** | | | | | |
| **Huw Pryce** | | | | | |
| **Tarrant** | | | | | |

## Solution

| Score | Handler | Dog |
|---|---|---|
| 61 points | Eiddwen | Craig |
| 64 points | Marged | Bute |
| 67 points | Huw Pryce | Nell |
| 70 points | Constance | Fly |
| 73 points | Tarrant | Gyp |

## How it falls out

1. [direct] from clue 1 dog:Gyp: ruled out position(s) 1,2,3,4
2. [bijection] dog:Bute: ruled out position(s) 5
3. [bijection] dog:Fly: ruled out position(s) 5
4. [bijection] dog:Nell: ruled out position(s) 5
5. [bijection] dog:Craig: ruled out position(s) 5
6. [order] from clue 7 handler:Tarrant: ruled out position(s) 1,2,3,4
7. [order] from clue 6 dog:Fly: ruled out position(s) 1,3
8. [order] from clue 5 dog:Bute: ruled out position(s) 1,3,4
9. [order] from clue 4 handler:Huw Pryce: ruled out position(s) 1,2,4,5
10. [order] from clue 3 handler:Constance: ruled out position(s) 1,2
11. [order] from clue 2 handler:Marged: ruled out position(s) 1
12. [bijection] dog:Fly: ruled out position(s) 2
13. [bijection] dog:Nell: ruled out position(s) 2
14. [bijection] dog:Craig: ruled out position(s) 2
15. [bijection] handler:Constance: ruled out position(s) 3,5
16. [bijection] handler:Eiddwen: ruled out position(s) 3,5
17. [bijection] handler:Marged: ruled out position(s) 3,5
18. [bijection] handler:Eiddwen: ruled out position(s) 2,4
19. [order] from clue 2 dog:Craig: ruled out position(s) 4
20. [bijection] dog:Nell: ruled out position(s) 4
21. [bijection] handler:Marged: ruled out position(s) 4
22. [order] from clue 2 dog:Craig: ruled out position(s) 3
23. [bijection] dog:Nell: ruled out position(s) 1

---

<sub>seed `2026172954635` &middot; score 4.86 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
