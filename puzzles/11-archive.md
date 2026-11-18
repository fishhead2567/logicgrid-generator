# The Mislabelled Drawers

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `9982911f3c1e`

## Introduction

The Vance Municipal Archive was reorganised in 1974 by somebody who has since left no forwarding address.
Five archivists are involved. Determine each archivist's shelf and decade.
- **Archivist**: Mr Ravensworth, Ms Okafor, Mr Pelletier, Ms Castellano and Ms Bhattacharya.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Decade**: the 1950s, the 1890s, the 1830s, the 1970s and the 1940s.
Every archivist has a different shelf and decade, so within each category every item is used exactly once.

## Clues

1. Mr Pelletier is lower than the third shelf in shelf order. Mr Pelletier covers the 1830s.
2. Ms Castellano does not file on the fifth shelf.
3. The third shelf is exactly one shelf lower than Ms Bhattacharya, with no shelf in between.
4. The second shelf falls somewhere between Ms Bhattacharya and Ms Okafor in shelf order.
5. Ms Bhattacharya and the archivist who covers the 1940s are exactly one shelf apart in shelf order, in one direction or the other.
6. Mr Pelletier is exactly one shelf lower than the archivist who covers the 1950s, with no shelf in between.
7. Ms Okafor does not cover the 1970s.

## Solving chart

*Shelf vs Archivist*

| | Mr Ravensworth | Ms Okafor | Mr Pelletier | Ms Castellano | Ms Bhattacharya |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Decade*

| | the 1950s | the 1890s | the 1830s | the 1970s | the 1940s |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Archivist vs Decade*

| | the 1950s | the 1890s | the 1830s | the 1970s | the 1940s |
|---|---|---|---|---|---|
| **Mr Ravensworth** | | | | | |
| **Ms Okafor** | | | | | |
| **Mr Pelletier** | | | | | |
| **Ms Castellano** | | | | | |
| **Ms Bhattacharya** | | | | | |

## Solution

| Shelf | Archivist | Decade |
|---|---|---|
| the bottom shelf | Ms Okafor | the 1890s |
| the second shelf | Mr Pelletier | the 1830s |
| the third shelf | Ms Castellano | the 1950s |
| the fourth shelf | Ms Bhattacharya | the 1970s |
| the fifth shelf | Mr Ravensworth | the 1940s |

## How it falls out

1. [direct] from clue 8 archivist:Ms Castellano: ruled out position(s) 5
2. [order] from clue 7 archivist:Ms Bhattacharya: ruled out position(s) 2
3. [order] from clue 7 archivist:Ms Okafor: ruled out position(s) 2
4. [order] from clue 6 archivist:Ms Bhattacharya: ruled out position(s) 1,3,5
5. [order] from clue 7 archivist:Ms Okafor: ruled out position(s) 3,4,5
6. [order] from clue 5 decade:the 1940s: ruled out position(s) 1,2,4
7. [order] from clue 3 archivist:Mr Pelletier: ruled out position(s) 5
8. [order] from clue 3 decade:the 1950s: ruled out position(s) 1
9. [order] from clue 1 archivist:Mr Pelletier: ruled out position(s) 3,4
10. [order] from clue 3 decade:the 1950s: ruled out position(s) 4,5
11. [direct] from clue 4 decade:the 1970s: ruled out position(s) 1
12. [direct] from clue 2 decade:the 1830s: ruled out position(s) 3,4,5
13. [bijection] archivist:Mr Ravensworth: ruled out position(s) 1,4
14. [bijection] archivist:Mr Pelletier: ruled out position(s) 1
15. [bijection] archivist:Ms Castellano: ruled out position(s) 1,4
16. [bijection] archivist:Mr Ravensworth: ruled out position(s) 2,3
17. [order] from clue 3 decade:the 1950s: ruled out position(s) 2
18. [direct] from clue 2 decade:the 1830s: ruled out position(s) 1
19. [bijection] archivist:Ms Castellano: ruled out position(s) 2
20. [bijection] decade:the 1890s: ruled out position(s) 2,3
21. [bijection] decade:the 1970s: ruled out position(s) 2,3
22. [bijection] decade:the 1940s: ruled out position(s) 3
23. [bijection] decade:the 1890s: ruled out position(s) 4,5
24. [bijection] decade:the 1970s: ruled out position(s) 5

---

<sub>seed `2026172662545` &middot; score 4.86 &middot; atoms 8 &middot; positives 1 &middot; solved by order</sub>
