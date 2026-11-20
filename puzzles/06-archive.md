# The Mislabelled Drawers

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `866511fa8a19`

## Introduction

The Vance Municipal Archive was reorganised in 1974 by somebody who has since left no forwarding address.
Four archivists are involved. Determine each archivist's shelf and condition.
- **Archivist**: Mr Pelletier, Ms Okafor, Mr Ravensworth and Ms Bhattacharya.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf and the fourth shelf.
- **Condition**: fire-scorched, over-repaired with tape, water-damaged and mouse-chewed.
Every archivist has a different shelf and condition, so within each category every item is used exactly once.

## Clues

1. Ms Bhattacharya does not describe theirs as mouse-chewed. Ms Bhattacharya files on the third shelf.
2. Mr Ravensworth describes theirs as over-repaired with tape.
3. Mr Pelletier is exactly one shelf lower than the second shelf, with no shelf in between.
4. The archivist who describes theirs as mouse-chewed is higher than the second shelf in shelf order.
5. Ms Okafor and the archivist who describes theirs as fire-scorched are exactly one shelf apart in shelf order, in one direction or the other.

## Solving chart

*Shelf vs Archivist*

| | Mr Pelletier | Ms Okafor | Mr Ravensworth | Ms Bhattacharya |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Condition*

| | fire-scorched | over-repaired with tape | water-damaged | mouse-chewed |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Archivist vs Condition*

| | fire-scorched | over-repaired with tape | water-damaged | mouse-chewed |
|---|---|---|---|---|
| **Mr Pelletier** | | | | |
| **Ms Okafor** | | | | |
| **Mr Ravensworth** | | | | |
| **Ms Bhattacharya** | | | | |

## Solution

| Shelf | Archivist | Condition |
|---|---|---|
| the bottom shelf | Mr Pelletier | water-damaged |
| the second shelf | Mr Ravensworth | over-repaired with tape |
| the third shelf | Ms Bhattacharya | fire-scorched |
| the fourth shelf | Ms Okafor | mouse-chewed |

## How it falls out

1. [direct] from clue 2 archivist:Ms Bhattacharya: ruled out position(s) 1,2,4
2. [direct] from clue 4 damage:mouse-chewed: ruled out position(s) 3
3. [bijection] archivist:Mr Pelletier: ruled out position(s) 3
4. [bijection] archivist:Ms Okafor: ruled out position(s) 3
5. [bijection] archivist:Mr Ravensworth: ruled out position(s) 3
6. [direct] from clue 3 damage:over-repaired with tape: ruled out position(s) 3
7. [order] from clue 6 damage:mouse-chewed: ruled out position(s) 1,2
8. [order] from clue 5 archivist:Mr Pelletier: ruled out position(s) 2,4
9. [order] from clue 1 damage:fire-scorched: ruled out position(s) 4
10. [bijection] archivist:Ms Okafor: ruled out position(s) 1
11. [bijection] archivist:Mr Ravensworth: ruled out position(s) 1
12. [bijection] damage:over-repaired with tape: ruled out position(s) 4
13. [bijection] damage:water-damaged: ruled out position(s) 4
14. [direct] from clue 3 archivist:Mr Ravensworth: ruled out position(s) 4
15. [direct] from clue 3 damage:over-repaired with tape: ruled out position(s) 1
16. [order] from clue 1 damage:fire-scorched: ruled out position(s) 2
17. [bijection] archivist:Ms Okafor: ruled out position(s) 2
18. [bijection] damage:water-damaged: ruled out position(s) 2
19. [order] from clue 1 damage:fire-scorched: ruled out position(s) 1
20. [bijection] damage:water-damaged: ruled out position(s) 3

---

<sub>seed `2026172822956` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
