# The Clun Forest Trials

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `b30fe4d51b38`

## Introduction

A hillside, six handlers, and a judge who deducts for a wide outrun with the enthusiasm of a man settling an old score.
Five handlers are involved. Determine each handler's score, dog and flock.
- **Handler**: Idris, Huw Pryce, Nerys, Eiddwen and Constance.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Dog**: Tweed, Fly, Gyp, Bute and Moss.
- **Flock**: Herdwicks, Dalesbreds, Cheviots, Beulahs and Rough Fells.
Every handler has a different score, dog and flock, so within each category every item is used exactly once.

## Clues

1. The handler who gathers Beulahs scores 64 points.
2. Nerys falls somewhere between the handler who runs Tweed and 67 points in score order.
3. 67 points is exactly one score step lower than the handler who gathers Rough Fells, with no score in between.
4. The handler who gathers Cheviots falls somewhere between the handler who runs Bute and the handler who runs Tweed in score order.
5. Huw Pryce is exactly one score step lower than the handler who gathers Rough Fells, with no score in between.
6. The handler who runs Gyp is lower than the handler who gathers Beulahs in score order.
7. The handler who runs Gyp does not gather Herdwicks.
8. The handler who runs Fly and Idris are exactly one score step apart in score order, in one direction or the other.
9. The handler who gathers Cheviots and Constance are exactly one score step apart in score order, in one direction or the other.

## Solving chart

*Score vs Handler*

| | Idris | Huw Pryce | Nerys | Eiddwen | Constance |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Dog*

| | Tweed | Fly | Gyp | Bute | Moss |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Flock*

| | Herdwicks | Dalesbreds | Cheviots | Beulahs | Rough Fells |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Handler vs Dog*

| | Tweed | Fly | Gyp | Bute | Moss |
|---|---|---|---|---|---|
| **Idris** | | | | | |
| **Huw Pryce** | | | | | |
| **Nerys** | | | | | |
| **Eiddwen** | | | | | |
| **Constance** | | | | | |

*Handler vs Flock*

| | Herdwicks | Dalesbreds | Cheviots | Beulahs | Rough Fells |
|---|---|---|---|---|---|
| **Idris** | | | | | |
| **Huw Pryce** | | | | | |
| **Nerys** | | | | | |
| **Eiddwen** | | | | | |
| **Constance** | | | | | |

*Dog vs Flock*

| | Herdwicks | Dalesbreds | Cheviots | Beulahs | Rough Fells |
|---|---|---|---|---|---|
| **Tweed** | | | | | |
| **Fly** | | | | | |
| **Gyp** | | | | | |
| **Bute** | | | | | |
| **Moss** | | | | | |

## Solution

| Score | Handler | Dog | Flock |
|---|---|---|---|
| 61 points | Eiddwen | Gyp | Dalesbreds |
| 64 points | Constance | Bute | Beulahs |
| 67 points | Huw Pryce | Moss | Cheviots |
| 70 points | Nerys | Fly | Rough Fells |
| 73 points | Idris | Tweed | Herdwicks |

## How it falls out

1. [direct] from clue 3 flock:Beulahs: ruled out position(s) 1,3,4,5
2. [bijection] flock:Herdwicks: ruled out position(s) 2
3. [bijection] flock:Dalesbreds: ruled out position(s) 2
4. [bijection] flock:Cheviots: ruled out position(s) 2
5. [bijection] flock:Rough Fells: ruled out position(s) 2
6. [order] from clue 9 handler:Nerys: ruled out position(s) 1,3,5
7. [order] from clue 9 dog:Tweed: ruled out position(s) 2,3,4
8. [order] from clue 8 handler:Huw Pryce: ruled out position(s) 1,5
9. [order] from clue 8 flock:Rough Fells: ruled out position(s) 1
10. [order] from clue 7 flock:Cheviots: ruled out position(s) 1,5
11. [order] from clue 5 dog:Gyp: ruled out position(s) 2,3,4,5
12. [order] from clue 2 flock:Rough Fells: ruled out position(s) 3,5
13. [order] from clue 8 handler:Huw Pryce: ruled out position(s) 2,4
14. [order] from clue 1 handler:Constance: ruled out position(s) 1
15. [direct] from clue 4 flock:Herdwicks: ruled out position(s) 1
16. [bijection] dog:Tweed: ruled out position(s) 1
17. [bijection] dog:Fly: ruled out position(s) 1
18. [bijection] dog:Bute: ruled out position(s) 1
19. [bijection] dog:Moss: ruled out position(s) 1
20. [bijection] flock:Herdwicks: ruled out position(s) 4
21. [bijection] flock:Dalesbreds: ruled out position(s) 4
22. [bijection] flock:Cheviots: ruled out position(s) 4
23. [bijection] flock:Dalesbreds: ruled out position(s) 3,5
24. [bijection] handler:Idris: ruled out position(s) 3
25. [bijection] handler:Eiddwen: ruled out position(s) 3
26. [bijection] handler:Constance: ruled out position(s) 3
27. [order] from clue 1 handler:Constance: ruled out position(s) 5
28. [order] from clue 9 handler:Nerys: ruled out position(s) 2
29. [order] from clue 7 dog:Bute: ruled out position(s) 3,4,5
30. [bijection] dog:Fly: ruled out position(s) 2,5
31. [bijection] dog:Moss: ruled out position(s) 2,5
32. [bijection] flock:Herdwicks: ruled out position(s) 3
33. [bijection] handler:Idris: ruled out position(s) 4
34. [bijection] handler:Eiddwen: ruled out position(s) 4
35. [bijection] handler:Constance: ruled out position(s) 4
36. [order] from clue 6 handler:Idris: ruled out position(s) 1
37. [bijection] handler:Idris: ruled out position(s) 2
38. [bijection] handler:Eiddwen: ruled out position(s) 2
39. [bijection] handler:Eiddwen: ruled out position(s) 5
40. [order] from clue 6 dog:Fly: ruled out position(s) 3
_... and 1 further steps._

---

<sub>seed `2026172825900` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
