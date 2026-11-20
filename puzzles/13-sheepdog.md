# The Clun Forest Trials

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `fdaf2f3e832b`

## Introduction

A hillside, a flock with its own ideas, and a judge who deducts for a wide outrun with the enthusiasm of someone settling an old score.
Five handlers are involved. Determine each handler's score and dog.
- **Handler**: Idris, Nerys, Tarrant, Eiddwen and Huw Pryce.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Dog**: Gyp, Moss, Tweed, Nell and Craig.
Every handler has a different score and dog, so within each category every item is used exactly once.

## Clues

1. The handler who runs Moss scores 70 points. The handler who runs Nell falls somewhere between 61 points and 70 points in score order.
2. The handler who runs Gyp scores 73 points.
3. Huw Pryce does not score 73 points. Huw Pryce does not score 61 points.
4. 64 points is exactly one score step lower than Tarrant, with no score in between.
5. The handler who runs Craig falls somewhere between Idris and Nerys in score order. The handler who runs Craig is exactly one score step lower than Nerys, with no score in between.

## Solving chart

*Score vs Handler*

| | Idris | Nerys | Tarrant | Eiddwen | Huw Pryce |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Dog*

| | Gyp | Moss | Tweed | Nell | Craig |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Handler vs Dog*

| | Gyp | Moss | Tweed | Nell | Craig |
|---|---|---|---|---|---|
| **Idris** | | | | | |
| **Nerys** | | | | | |
| **Tarrant** | | | | | |
| **Eiddwen** | | | | | |
| **Huw Pryce** | | | | | |

## Solution

| Score | Handler | Dog |
|---|---|---|
| 61 points | Idris | Tweed |
| 64 points | Huw Pryce | Nell |
| 67 points | Tarrant | Craig |
| 70 points | Nerys | Moss |
| 73 points | Eiddwen | Gyp |

## How it falls out

1. [direct] from clue 8 dog:Moss: ruled out position(s) 1,2,3,5
2. [direct] from clue 6 dog:Gyp: ruled out position(s) 1,2,3,4
3. [direct] from clue 5 handler:Huw Pryce: ruled out position(s) 1
4. [direct] from clue 1 handler:Huw Pryce: ruled out position(s) 5
5. [bijection] dog:Tweed: ruled out position(s) 4,5
6. [bijection] dog:Nell: ruled out position(s) 4,5
7. [bijection] dog:Craig: ruled out position(s) 4,5
8. [order] from clue 7 dog:Craig: ruled out position(s) 1
9. [order] from clue 4 handler:Tarrant: ruled out position(s) 1,2,4,5
10. [order] from clue 3 dog:Nell: ruled out position(s) 1
11. [order] from clue 2 handler:Nerys: ruled out position(s) 1,2,5
12. [order] from clue 7 handler:Idris: ruled out position(s) 3,4,5
13. [bijection] dog:Tweed: ruled out position(s) 2,3
14. [bijection] handler:Nerys: ruled out position(s) 3
15. [bijection] handler:Eiddwen: ruled out position(s) 3
16. [bijection] handler:Huw Pryce: ruled out position(s) 3
17. [bijection] handler:Eiddwen: ruled out position(s) 1,2,4
18. [order] from clue 2 dog:Craig: ruled out position(s) 2
19. [bijection] dog:Nell: ruled out position(s) 3
20. [bijection] handler:Huw Pryce: ruled out position(s) 4
21. [bijection] handler:Idris: ruled out position(s) 2

---

<sub>seed `2026172878389` &middot; score 4.62 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
