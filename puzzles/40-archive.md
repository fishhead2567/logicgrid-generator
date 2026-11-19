# The Mislabelled Drawers

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `c10d27909278`

## Introduction

The Vance Municipal Archive was reorganised in 1974 by somebody who has since left no forwarding address.
Five archivists are involved. Determine each archivist's shelf, holding and condition.
- **Archivist**: Ms Castellano, Mr Ravensworth, Ms Okafor, Mr Pelletier and Dr Mwangi.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Holding**: the harbour dredging reports, a folder of libel writs, a box of unopened wills, the lost property register and a set of tram timetables.
- **Condition**: mouse-chewed, over-repaired with tape, fire-scorched, foxed and water-damaged.
Every archivist has a different shelf, holding and condition, so within each category every item is used exactly once.

## Clues

1. At least one of the following holds, and possibly more than one: (a) The archivist who describes theirs as foxed files on the second shelf. (b) One of the archivist who describes theirs as mouse-chewed and the third shelf sits at an odd-numbered shelf and the other at an even-numbered shelf.
2. At least one of the following holds, and possibly more than one: (a) Mr Ravensworth is exactly one shelf lower than the second shelf, with no shelf in between. (b) Dr Mwangi files on the fifth shelf.
3. The archivist who catalogues a box of unopened wills is lower than Mr Pelletier in shelf order. The archivist who catalogues a box of unopened wills does not file on the bottom shelf.
4. The archivist who catalogues the lost property register and the second shelf are exactly two shelves apart in shelf order.
5. Dr Mwangi is lower than the archivist who describes theirs as water-damaged in shelf order.
6. The archivist who describes theirs as fire-scorched falls somewhere between the archivist who catalogues a box of unopened wills and the archivist who catalogues a set of tram timetables in shelf order.
7. Ms Okafor and the archivist who catalogues a box of unopened wills are exactly one shelf apart in shelf order, in one direction or the other.
8. The archivist who describes theirs as over-repaired with tape is lower than the archivist who catalogues a folder of libel writs in shelf order.
9. Mr Pelletier and the archivist who catalogues the harbour dredging reports are exactly one shelf apart in shelf order, in one direction or the other.

## Solving chart

*Shelf vs Archivist*

| | Ms Castellano | Mr Ravensworth | Ms Okafor | Mr Pelletier | Dr Mwangi |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Holding*

| | the harbour dredging reports | a folder of libel writs | a box of unopened wills | the lost property register | a set of tram timetables |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Condition*

| | mouse-chewed | over-repaired with tape | fire-scorched | foxed | water-damaged |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Archivist vs Holding*

| | the harbour dredging reports | a folder of libel writs | a box of unopened wills | the lost property register | a set of tram timetables |
|---|---|---|---|---|---|
| **Ms Castellano** | | | | | |
| **Mr Ravensworth** | | | | | |
| **Ms Okafor** | | | | | |
| **Mr Pelletier** | | | | | |
| **Dr Mwangi** | | | | | |

*Archivist vs Condition*

| | mouse-chewed | over-repaired with tape | fire-scorched | foxed | water-damaged |
|---|---|---|---|---|---|
| **Ms Castellano** | | | | | |
| **Mr Ravensworth** | | | | | |
| **Ms Okafor** | | | | | |
| **Mr Pelletier** | | | | | |
| **Dr Mwangi** | | | | | |

*Holding vs Condition*

| | mouse-chewed | over-repaired with tape | fire-scorched | foxed | water-damaged |
|---|---|---|---|---|---|
| **the harbour dredging reports** | | | | | |
| **a folder of libel writs** | | | | | |
| **a box of unopened wills** | | | | | |
| **the lost property register** | | | | | |
| **a set of tram timetables** | | | | | |

## Solution

| Shelf | Archivist | Holding | Condition |
|---|---|---|---|
| the bottom shelf | Mr Ravensworth | a set of tram timetables | over-repaired with tape |
| the second shelf | Ms Okafor | a folder of libel writs | fire-scorched |
| the third shelf | Dr Mwangi | a box of unopened wills | foxed |
| the fourth shelf | Mr Pelletier | the lost property register | mouse-chewed |
| the fifth shelf | Ms Castellano | the harbour dredging reports | water-damaged |

## How it falls out

1. [direct] from clue 3 holding:a box of unopened wills: ruled out position(s) 1
2. [order] from clue 10 archivist:Dr Mwangi: ruled out position(s) 5
3. [order] from clue 10 damage:water-damaged: ruled out position(s) 1
4. [order] from clue 9 damage:over-repaired with tape: ruled out position(s) 5
5. [order] from clue 9 holding:a folder of libel writs: ruled out position(s) 1
6. [order] from clue 6 holding:the lost property register: ruled out position(s) 1,2,3,5
7. [order] from clue 5 holding:a box of unopened wills: ruled out position(s) 5
8. [order] from clue 5 archivist:Mr Pelletier: ruled out position(s) 1,2
9. [order] from clue 2 holding:the harbour dredging reports: ruled out position(s) 1
10. [order] from clue 1 damage:fire-scorched: ruled out position(s) 1,5
11. [order] from clue 1 holding:a set of tram timetables: ruled out position(s) 3
12. [bijection] holding:the harbour dredging reports: ruled out position(s) 4
13. [bijection] holding:a folder of libel writs: ruled out position(s) 4
14. [bijection] holding:a box of unopened wills: ruled out position(s) 4
15. [bijection] holding:a set of tram timetables: ruled out position(s) 4
16. [bijection] holding:a set of tram timetables: ruled out position(s) 2,5
17. [order] from clue 8 archivist:Ms Okafor: ruled out position(s) 5
18. [order] from clue 1 damage:fire-scorched: ruled out position(s) 3,4
19. [order] from clue 1 holding:a box of unopened wills: ruled out position(s) 2
20. [order] from clue 8 archivist:Ms Okafor: ruled out position(s) 1,3
21. [order] from clue 5 archivist:Mr Pelletier: ruled out position(s) 3
22. [order] from clue 2 archivist:Mr Pelletier: ruled out position(s) 5
23. [order] from clue 2 holding:the harbour dredging reports: ruled out position(s) 2
24. [bijection] archivist:Ms Castellano: ruled out position(s) 4
25. [bijection] archivist:Mr Ravensworth: ruled out position(s) 4
26. [bijection] archivist:Ms Okafor: ruled out position(s) 4
27. [bijection] archivist:Dr Mwangi: ruled out position(s) 4
28. [bijection] damage:mouse-chewed: ruled out position(s) 2
29. [bijection] damage:over-repaired with tape: ruled out position(s) 2
30. [bijection] damage:foxed: ruled out position(s) 2
31. [bijection] damage:water-damaged: ruled out position(s) 2
32. [bijection] holding:the harbour dredging reports: ruled out position(s) 3
33. [bijection] holding:a folder of libel writs: ruled out position(s) 3
34. [bijection] holding:a folder of libel writs: ruled out position(s) 5
35. [order] from clue 9 damage:over-repaired with tape: ruled out position(s) 3,4
36. [bijection] archivist:Ms Castellano: ruled out position(s) 2
37. [bijection] archivist:Mr Ravensworth: ruled out position(s) 2
38. [bijection] archivist:Dr Mwangi: ruled out position(s) 2
39. [bijection] damage:mouse-chewed: ruled out position(s) 1
40. [bijection] damage:foxed: ruled out position(s) 1
_... and 8 further steps._

---

<sub>seed `2026172992199` &middot; score 9.7475 &middot; atoms 10 &middot; positives 0 &middot; solved by disjunction</sub>
