# The Mislabelled Drawers

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `64fd78628fcd`

## Introduction

The Vance Municipal Archive was reorganised in 1974 by somebody who has since left no forwarding address.
Five archivists are involved. Determine each archivist's shelf, decade and condition.
- **Archivist**: Dr Mwangi, Ms Castellano, Dr Lindqvist, Mr Ravensworth and Ms Okafor.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Decade**: the 1890s, the 1970s, the 1910s, the 1950s and the 1830s.
- **Condition**: immaculate, water-damaged, fire-scorched, over-repaired with tape and foxed.
Every archivist has a different shelf, decade and condition, so within each category every item is used exactly once.

## Clues

1. Ms Castellano and the bottom shelf are exactly four shelves apart in shelf order. The archivist who covers the 1890s does not file on the bottom shelf.
2. The archivist who describes theirs as water-damaged and the bottom shelf are exactly one shelf apart in shelf order, in one direction or the other.
3. The archivist who describes theirs as foxed falls somewhere between Dr Lindqvist and Dr Mwangi in shelf order.
4. The archivist who covers the 1970s is exactly one shelf lower than the archivist who describes theirs as fire-scorched, with no shelf in between.
5. Dr Lindqvist is exactly one shelf lower than the archivist who describes theirs as over-repaired with tape, with no shelf in between.
6. Dr Lindqvist is exactly one shelf lower than the archivist who covers the 1910s, with no shelf in between.
7. Ms Okafor and the archivist who covers the 1970s are exactly one shelf apart in shelf order, in one direction or the other.
8. The archivist who describes theirs as water-damaged is lower than the archivist who covers the 1830s in shelf order.

## Solving chart

*Shelf vs Archivist*

| | Dr Mwangi | Ms Castellano | Dr Lindqvist | Mr Ravensworth | Ms Okafor |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Decade*

| | the 1890s | the 1970s | the 1910s | the 1950s | the 1830s |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Condition*

| | immaculate | water-damaged | fire-scorched | over-repaired with tape | foxed |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Archivist vs Decade*

| | the 1890s | the 1970s | the 1910s | the 1950s | the 1830s |
|---|---|---|---|---|---|
| **Dr Mwangi** | | | | | |
| **Ms Castellano** | | | | | |
| **Dr Lindqvist** | | | | | |
| **Mr Ravensworth** | | | | | |
| **Ms Okafor** | | | | | |

*Archivist vs Condition*

| | immaculate | water-damaged | fire-scorched | over-repaired with tape | foxed |
|---|---|---|---|---|---|
| **Dr Mwangi** | | | | | |
| **Ms Castellano** | | | | | |
| **Dr Lindqvist** | | | | | |
| **Mr Ravensworth** | | | | | |
| **Ms Okafor** | | | | | |

*Decade vs Condition*

| | immaculate | water-damaged | fire-scorched | over-repaired with tape | foxed |
|---|---|---|---|---|---|
| **the 1890s** | | | | | |
| **the 1970s** | | | | | |
| **the 1910s** | | | | | |
| **the 1950s** | | | | | |
| **the 1830s** | | | | | |

## Solution

| Shelf | Archivist | Decade | Condition |
|---|---|---|---|
| the bottom shelf | Dr Mwangi | the 1950s | immaculate |
| the second shelf | Ms Okafor | the 1890s | water-damaged |
| the third shelf | Mr Ravensworth | the 1970s | foxed |
| the fourth shelf | Dr Lindqvist | the 1830s | fire-scorched |
| the fifth shelf | Ms Castellano | the 1910s | over-repaired with tape |

## How it falls out

1. [direct] from clue 7 decade:the 1890s: ruled out position(s) 1
2. [order] from clue 8 archivist:Ms Castellano: ruled out position(s) 1,2,3,4
3. [order] from clue 6 damage:foxed: ruled out position(s) 1,5
4. [order] from clue 5 damage:water-damaged: ruled out position(s) 1,3,4,5
5. [order] from clue 4 decade:the 1970s: ruled out position(s) 5
6. [order] from clue 4 damage:fire-scorched: ruled out position(s) 1
7. [order] from clue 3 archivist:Dr Lindqvist: ruled out position(s) 5
8. [order] from clue 3 decade:the 1910s: ruled out position(s) 1
9. [order] from clue 2 damage:over-repaired with tape: ruled out position(s) 1
10. [order] from clue 1 decade:the 1830s: ruled out position(s) 1,2
11. [bijection] archivist:Dr Mwangi: ruled out position(s) 5
12. [bijection] archivist:Mr Ravensworth: ruled out position(s) 5
13. [bijection] archivist:Ms Okafor: ruled out position(s) 5
14. [bijection] damage:immaculate: ruled out position(s) 2
15. [bijection] damage:fire-scorched: ruled out position(s) 2
16. [bijection] damage:over-repaired with tape: ruled out position(s) 2
17. [bijection] damage:foxed: ruled out position(s) 2
18. [bijection] damage:immaculate: ruled out position(s) 3,4,5
19. [order] from clue 2 archivist:Dr Lindqvist: ruled out position(s) 1
20. [order] from clue 3 decade:the 1910s: ruled out position(s) 2
21. [order] from clue 4 decade:the 1970s: ruled out position(s) 1
22. [order] from clue 6 damage:foxed: ruled out position(s) 4
23. [order] from clue 6 archivist:Dr Lindqvist: ruled out position(s) 3
24. [order] from clue 6 archivist:Dr Mwangi: ruled out position(s) 3
25. [order] from clue 3 decade:the 1910s: ruled out position(s) 4
26. [order] from clue 2 damage:over-repaired with tape: ruled out position(s) 4
27. [bijection] damage:fire-scorched: ruled out position(s) 3
28. [bijection] damage:over-repaired with tape: ruled out position(s) 3
29. [bijection] damage:fire-scorched: ruled out position(s) 5
30. [bijection] decade:the 1950s: ruled out position(s) 2,3,4,5
31. [order] from clue 2 archivist:Dr Lindqvist: ruled out position(s) 2
32. [order] from clue 6 archivist:Dr Mwangi: ruled out position(s) 4
33. [order] from clue 3 decade:the 1910s: ruled out position(s) 3
34. [order] from clue 4 decade:the 1970s: ruled out position(s) 2,4
35. [order] from clue 9 archivist:Ms Okafor: ruled out position(s) 1,3
36. [bijection] archivist:Mr Ravensworth: ruled out position(s) 4
37. [bijection] archivist:Ms Okafor: ruled out position(s) 4
38. [bijection] archivist:Mr Ravensworth: ruled out position(s) 1,2
39. [bijection] decade:the 1890s: ruled out position(s) 3,5
40. [bijection] decade:the 1830s: ruled out position(s) 3,5
_... and 2 further steps._

---

<sub>seed `2026172830626` &middot; score 5.675 &middot; atoms 9 &middot; positives 0 &middot; solved by order</sub>
