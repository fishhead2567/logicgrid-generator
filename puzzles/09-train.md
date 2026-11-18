# The Loft Layout Dispute

*The members of the model railway society share one loft layout and a deep well of resentment.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `13751cae6c00`

## Introduction

There are 5 members. Each has exactly one shelf and one item from every other category below, and within each category every item belongs to a different member.
- **Shelf** (listed in order): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Modeller**: Abiodun, Hendrik, Esperanza, Gilbert and Rosamond.
- **Rolling stock**: a brass pannier tank, a gleaming Pacific, a rake of milk tankers, a battered autocoach and a scratch-built crane wagon.
- **Grievance**: somebody else's couplings, the choice of era, the wiring, the lighting and the timetable.
The shelves above are listed in order, from the bottom shelf to the fifth shelf.

## Clues

1. The choice of era goes with Gilbert. Gilbert falls somewhere between the fifth shelf and a scratch-built crane wagon in shelf order.
2. The lighting goes with Abiodun. Abiodun and a battered autocoach are next to each other in shelf order, in one order or the other.
3. The timetable, Esperanza and the third shelf are three different members. Esperanza and the bottom shelf are next to each other in shelf order, in one order or the other.
4. The second shelf falls somewhere between Rosamond and a rake of milk tankers in shelf order.
5. The fourth shelf is lower than a gleaming Pacific's shelf. The wiring does not go with a gleaming Pacific.
6. The third shelf is lower than Rosamond's shelf.
7. A brass pannier tank's shelf is lower than the wiring's shelf.

## Solving chart

*Shelf vs Modeller*

| | Abiodun | Hendrik | Esperanza | Gilbert | Rosamond |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Rolling stock*

| | a brass pannier tank | a gleaming Pacific | a rake of milk tankers | a battered autocoach | a scratch-built crane wagon |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Grievance*

| | somebody else's couplings | the choice of era | the wiring | the lighting | the timetable |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Modeller vs Rolling stock*

| | a brass pannier tank | a gleaming Pacific | a rake of milk tankers | a battered autocoach | a scratch-built crane wagon |
|---|---|---|---|---|---|
| **Abiodun** | | | | | |
| **Hendrik** | | | | | |
| **Esperanza** | | | | | |
| **Gilbert** | | | | | |
| **Rosamond** | | | | | |

*Modeller vs Grievance*

| | somebody else's couplings | the choice of era | the wiring | the lighting | the timetable |
|---|---|---|---|---|---|
| **Abiodun** | | | | | |
| **Hendrik** | | | | | |
| **Esperanza** | | | | | |
| **Gilbert** | | | | | |
| **Rosamond** | | | | | |

*Rolling stock vs Grievance*

| | somebody else's couplings | the choice of era | the wiring | the lighting | the timetable |
|---|---|---|---|---|---|
| **a brass pannier tank** | | | | | |
| **a gleaming Pacific** | | | | | |
| **a rake of milk tankers** | | | | | |
| **a battered autocoach** | | | | | |
| **a scratch-built crane wagon** | | | | | |

## Solution

| Shelf | Modeller | Rolling stock | Grievance |
|---|---|---|---|
| the bottom shelf | Hendrik | a rake of milk tankers | the timetable |
| the second shelf | Esperanza | a scratch-built crane wagon | somebody else's couplings |
| the third shelf | Gilbert | a brass pannier tank | the choice of era |
| the fourth shelf | Rosamond | a battered autocoach | the wiring |
| the fifth shelf | Abiodun | a gleaming Pacific | the lighting |

## How it falls out

1. [bijection] from clue 10 grievance:the timetable: ruled out position(s) 3
2. [bijection] from clue 10 modeller:Esperanza: ruled out position(s) 3
3. [order] from clue 8 modeller:Esperanza: ruled out position(s) 1,4,5
4. [order] from clue 7 stock:a brass pannier tank: ruled out position(s) 5
5. [order] from clue 7 grievance:the wiring: ruled out position(s) 1
6. [order] from clue 6 modeller:Rosamond: ruled out position(s) 2
7. [order] from clue 6 stock:a rake of milk tankers: ruled out position(s) 2
8. [order] from clue 5 modeller:Rosamond: ruled out position(s) 1,3
9. [order] from clue 6 stock:a rake of milk tankers: ruled out position(s) 3,4,5
10. [order] from clue 4 modeller:Gilbert: ruled out position(s) 1,5
11. [order] from clue 4 stock:a scratch-built crane wagon: ruled out position(s) 4,5
12. [order] from clue 1 stock:a gleaming Pacific: ruled out position(s) 1,2,3,4
13. [bijection] from clue 10 grievance:the timetable: ruled out position(s) 2
14. [direct] from clue 11 grievance:the wiring: ruled out position(s) 5
15. [order] from clue 7 stock:a brass pannier tank: ruled out position(s) 4
16. [direct] from clue 3 grievance:the choice of era: ruled out position(s) 1,5
17. [bijection] modeller:Abiodun: ruled out position(s) 2
18. [bijection] modeller:Hendrik: ruled out position(s) 2
19. [bijection] modeller:Gilbert: ruled out position(s) 2
20. [bijection] stock:a brass pannier tank: ruled out position(s) 1
21. [bijection] stock:a battered autocoach: ruled out position(s) 1,5
22. [bijection] stock:a scratch-built crane wagon: ruled out position(s) 1
23. [bijection] stock:a battered autocoach: ruled out position(s) 2,3
24. [order] from clue 7 grievance:the wiring: ruled out position(s) 2
25. [direct] from clue 3 grievance:the choice of era: ruled out position(s) 2
26. [order] from clue 9 modeller:Abiodun: ruled out position(s) 1,4
27. [direct] from clue 2 grievance:the lighting: ruled out position(s) 1,2,4
28. [bijection] grievance:somebody else's couplings: ruled out position(s) 1,3,4,5
29. [bijection] modeller:Hendrik: ruled out position(s) 3,4,5
30. [bijection] grievance:the timetable: ruled out position(s) 4,5
31. [bijection] grievance:the lighting: ruled out position(s) 3
32. [direct] from clue 2 modeller:Abiodun: ruled out position(s) 3
33. [bijection] modeller:Rosamond: ruled out position(s) 5
34. [bijection] modeller:Gilbert: ruled out position(s) 4
35. [order] from clue 4 stock:a scratch-built crane wagon: ruled out position(s) 3
36. [direct] from clue 3 grievance:the choice of era: ruled out position(s) 4
37. [bijection] grievance:the wiring: ruled out position(s) 3
38. [bijection] stock:a brass pannier tank: ruled out position(s) 2

---

<sub>seed `2026172646707` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
