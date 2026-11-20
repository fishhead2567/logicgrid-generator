# The Mislabelled Drawers

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `8cdc3efb624d`

## Introduction

The Vance Municipal Archive was reorganised in 1974 by somebody who has since left no forwarding address.
Four archivists are involved. Determine each archivist's shelf and decade.
- **Archivist**: Dr Mwangi, Mr Pelletier, Ms Castellano and Mr Ravensworth.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf and the fourth shelf.
- **Decade**: the 1890s, the 1950s, the 1830s and the 1910s.
Every archivist has a different shelf and decade, so within each category every item is used exactly once.

## Clues

1. The archivist who covers the 1950s files on the third shelf.
2. Mr Pelletier files on the second shelf.
3. Ms Castellano is exactly one shelf lower than the fourth shelf, with no shelf in between.
4. The archivist who covers the 1890s and the second shelf are exactly one shelf apart in shelf order, in one direction or the other.
5. Mr Ravensworth and the archivist who covers the 1950s are exactly one shelf apart in shelf order, in one direction or the other.
6. Mr Pelletier is lower than the archivist who covers the 1830s in shelf order.

## Solving chart

*Shelf vs Archivist*

| | Dr Mwangi | Mr Pelletier | Ms Castellano | Mr Ravensworth |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Decade*

| | the 1890s | the 1950s | the 1830s | the 1910s |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Archivist vs Decade*

| | the 1890s | the 1950s | the 1830s | the 1910s |
|---|---|---|---|---|
| **Dr Mwangi** | | | | |
| **Mr Pelletier** | | | | |
| **Ms Castellano** | | | | |
| **Mr Ravensworth** | | | | |

## Solution

| Shelf | Archivist | Decade |
|---|---|---|
| the bottom shelf | Dr Mwangi | the 1890s |
| the second shelf | Mr Pelletier | the 1910s |
| the third shelf | Ms Castellano | the 1950s |
| the fourth shelf | Mr Ravensworth | the 1830s |

## How it falls out

1. [direct] from clue 5 decade:the 1950s: ruled out position(s) 1,2,4
2. [direct] from clue 3 archivist:Mr Pelletier: ruled out position(s) 1,3,4
3. [bijection] archivist:Dr Mwangi: ruled out position(s) 2
4. [bijection] archivist:Ms Castellano: ruled out position(s) 2
5. [bijection] archivist:Mr Ravensworth: ruled out position(s) 2
6. [bijection] decade:the 1890s: ruled out position(s) 3
7. [bijection] decade:the 1830s: ruled out position(s) 3
8. [bijection] decade:the 1910s: ruled out position(s) 3
9. [order] from clue 6 decade:the 1830s: ruled out position(s) 1,2
10. [order] from clue 4 archivist:Mr Ravensworth: ruled out position(s) 1,3
11. [order] from clue 2 archivist:Ms Castellano: ruled out position(s) 1,4
12. [order] from clue 1 decade:the 1890s: ruled out position(s) 2,4
13. [bijection] archivist:Dr Mwangi: ruled out position(s) 3,4
14. [bijection] decade:the 1910s: ruled out position(s) 1,4

---

<sub>seed `2026172883364` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
