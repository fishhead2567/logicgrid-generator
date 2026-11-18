# The Blind Tasting at Pemberton's

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `3e67e3a21be0`

## Introduction

Pemberton's holds a blind tasting each spring. The tasters are blind to the tea; the tea is not blind to them.
Five tasters are involved. Determine each taster's start time, tea and note.
- **Taster**: Bertrand, Yolanda, Rolf, Marguerite and Chidi.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Tea**: a Nilgiri frost, a roasted oolong, a smoked Lapsang, a silver needle white and a first-flush Darjeeling.
- **Tasting note**: stewed apricot; iron filings; wet slate; bruised peach; and hay and honey.
Every taster has a different start time, tea and note, so within each category every item is used exactly once.

## Clues

1. The taster who reports bruised peach samples a roasted oolong. The taster who samples a roasted oolong tastes at 8am.
2. The taster who reports stewed apricot falls somewhere between Marguerite and 9am in start time order. Rolf falls somewhere between 11am and 9am in start time order.
3. Bertrand and 10am are exactly one hour apart in start time order, in one direction or the other.
4. The taster who samples a smoked Lapsang is exactly one hour earlier than 10am, with no start time in between.
5. The taster who samples a Nilgiri frost is exactly one hour earlier than the taster who reports wet slate, with no start time in between.
6. Rolf and the taster who samples a silver needle white are exactly one hour apart in start time order, in one direction or the other.
7. Chidi is exactly one hour earlier than the taster who reports stewed apricot, with no start time in between.
8. The taster who reports hay and honey is earlier than the taster who samples a silver needle white in start time order.

## Solving chart

*Start time vs Taster*

| | Bertrand | Yolanda | Rolf | Marguerite | Chidi |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Tea*

| | a Nilgiri frost | a roasted oolong | a smoked Lapsang | a silver needle white | a first-flush Darjeeling |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Tasting note*

| | stewed apricot | iron filings | wet slate | bruised peach | hay and honey |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Taster vs Tea*

| | a Nilgiri frost | a roasted oolong | a smoked Lapsang | a silver needle white | a first-flush Darjeeling |
|---|---|---|---|---|---|
| **Bertrand** | | | | | |
| **Yolanda** | | | | | |
| **Rolf** | | | | | |
| **Marguerite** | | | | | |
| **Chidi** | | | | | |

*Taster vs Tasting note*

| | stewed apricot | iron filings | wet slate | bruised peach | hay and honey |
|---|---|---|---|---|---|
| **Bertrand** | | | | | |
| **Yolanda** | | | | | |
| **Rolf** | | | | | |
| **Marguerite** | | | | | |
| **Chidi** | | | | | |

*Tea vs Tasting note*

| | stewed apricot | iron filings | wet slate | bruised peach | hay and honey |
|---|---|---|---|---|---|
| **a Nilgiri frost** | | | | | |
| **a roasted oolong** | | | | | |
| **a smoked Lapsang** | | | | | |
| **a silver needle white** | | | | | |
| **a first-flush Darjeeling** | | | | | |

## Solution

| Start time | Taster | Tea | Tasting note |
|---|---|---|---|
| 8am | Yolanda | a roasted oolong | bruised peach |
| 9am | Chidi | a smoked Lapsang | hay and honey |
| 10am | Rolf | a Nilgiri frost | stewed apricot |
| 11am | Bertrand | a silver needle white | wet slate |
| noon | Marguerite | a first-flush Darjeeling | iron filings |

## How it falls out

1. [direct] from clue 2 tea:a roasted oolong: ruled out position(s) 2,3,4,5
2. [direct] from clue 5 note:bruised peach: ruled out position(s) 2,3,4,5
3. [bijection] note:stewed apricot: ruled out position(s) 1
4. [bijection] note:iron filings: ruled out position(s) 1
5. [bijection] note:wet slate: ruled out position(s) 1
6. [bijection] note:hay and honey: ruled out position(s) 1
7. [bijection] tea:a Nilgiri frost: ruled out position(s) 1
8. [bijection] tea:a smoked Lapsang: ruled out position(s) 1
9. [bijection] tea:a silver needle white: ruled out position(s) 1
10. [bijection] tea:a first-flush Darjeeling: ruled out position(s) 1
11. [order] from clue 10 tea:a Nilgiri frost: ruled out position(s) 5
12. [order] from clue 10 note:wet slate: ruled out position(s) 2
13. [order] from clue 9 taster:Bertrand: ruled out position(s) 1,3,5
14. [order] from clue 8 tea:a smoked Lapsang: ruled out position(s) 3,4,5
15. [order] from clue 7 note:stewed apricot: ruled out position(s) 2,5
16. [order] from clue 7 taster:Marguerite: ruled out position(s) 1,2,3
17. [order] from clue 6 note:hay and honey: ruled out position(s) 5
18. [order] from clue 6 tea:a silver needle white: ruled out position(s) 2
19. [order] from clue 4 taster:Rolf: ruled out position(s) 1,2,4,5
20. [order] from clue 3 tea:a silver needle white: ruled out position(s) 3,5
21. [order] from clue 6 note:hay and honey: ruled out position(s) 4
22. [order] from clue 1 taster:Chidi: ruled out position(s) 1,4,5
23. [bijection] taster:Yolanda: ruled out position(s) 3
24. [bijection] taster:Chidi: ruled out position(s) 3
25. [bijection] taster:Yolanda: ruled out position(s) 2,4,5
26. [bijection] tea:a Nilgiri frost: ruled out position(s) 2,4
27. [bijection] tea:a first-flush Darjeeling: ruled out position(s) 2,4
28. [bijection] tea:a first-flush Darjeeling: ruled out position(s) 3
29. [order] from clue 10 note:wet slate: ruled out position(s) 3,5
30. [order] from clue 1 note:stewed apricot: ruled out position(s) 4
31. [bijection] note:iron filings: ruled out position(s) 3,4
32. [bijection] note:hay and honey: ruled out position(s) 3
33. [bijection] note:iron filings: ruled out position(s) 2
34. [bijection] taster:Bertrand: ruled out position(s) 2
35. [bijection] taster:Marguerite: ruled out position(s) 4

---

<sub>seed `2026172686302` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
