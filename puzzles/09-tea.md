# The Blind Tasting at Pemberton's

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `4b4eac547a7e`

## Introduction

Pemberton's holds a blind tasting each spring. The tasters are blind to the tea; the tea is not blind to them.
Four tasters are involved. Determine each taster's start time, tea and note.
- **Taster**: Ignatia, Yolanda, Marguerite and Rolf.
- **Start time** (listed from earlier to later): 8am, 9am, 10am and 11am.
- **Tea**: a pressed pu-erh, a Nilgiri frost, a roasted oolong and a Keemun.
- **Tasting note**: stewed apricot; hay and honey; wet slate; and bruised peach.
Every taster has a different start time, tea and note, so within each category every item is used exactly once.

## Clues

1. Ignatia and 10am are exactly one hour apart in start time order, in one direction or the other. Ignatia samples a roasted oolong.
2. The taster who reports wet slate samples a Keemun. Yolanda reports wet slate.
3. The taster who reports hay and honey is earlier than 10am in start time order. Marguerite and 10am are exactly one hour apart in start time order, in one direction or the other.
4. The taster who reports wet slate does not taste at 8am.
5. 9am falls somewhere between the taster who samples a Keemun and the taster who samples a pressed pu-erh in start time order.
6. The taster who reports stewed apricot and the taster who samples a Nilgiri frost are exactly one hour apart in start time order, in one direction or the other.

## Solving chart

*Start time vs Taster*

| | Ignatia | Yolanda | Marguerite | Rolf |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Tea*

| | a pressed pu-erh | a Nilgiri frost | a roasted oolong | a Keemun |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Tasting note*

| | stewed apricot | hay and honey | wet slate | bruised peach |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Taster vs Tea*

| | a pressed pu-erh | a Nilgiri frost | a roasted oolong | a Keemun |
|---|---|---|---|---|
| **Ignatia** | | | | |
| **Yolanda** | | | | |
| **Marguerite** | | | | |
| **Rolf** | | | | |

*Taster vs Tasting note*

| | stewed apricot | hay and honey | wet slate | bruised peach |
|---|---|---|---|---|
| **Ignatia** | | | | |
| **Yolanda** | | | | |
| **Marguerite** | | | | |
| **Rolf** | | | | |

*Tea vs Tasting note*

| | stewed apricot | hay and honey | wet slate | bruised peach |
|---|---|---|---|---|
| **a pressed pu-erh** | | | | |
| **a Nilgiri frost** | | | | |
| **a roasted oolong** | | | | |
| **a Keemun** | | | | |

## Solution

| Start time | Taster | Tea | Tasting note |
|---|---|---|---|
| 8am | Rolf | a pressed pu-erh | stewed apricot |
| 9am | Marguerite | a Nilgiri frost | hay and honey |
| 10am | Yolanda | a Keemun | wet slate |
| 11am | Ignatia | a roasted oolong | bruised peach |

## How it falls out

1. [direct] from clue 5 note:wet slate: ruled out position(s) 1
2. [direct] from clue 9 taster:Yolanda: ruled out position(s) 1
3. [direct] from clue 1 tea:a Keemun: ruled out position(s) 1
4. [order] from clue 7 taster:Marguerite: ruled out position(s) 1,3
5. [order] from clue 4 note:hay and honey: ruled out position(s) 3,4
6. [order] from clue 3 tea:a Keemun: ruled out position(s) 2
7. [order] from clue 3 tea:a pressed pu-erh: ruled out position(s) 2,3,4
8. [order] from clue 2 taster:Ignatia: ruled out position(s) 1,3
9. [direct] from clue 8 tea:a roasted oolong: ruled out position(s) 1,3
10. [direct] from clue 1 note:wet slate: ruled out position(s) 2
11. [direct] from clue 9 taster:Yolanda: ruled out position(s) 2
12. [bijection] taster:Rolf: ruled out position(s) 2,3,4
13. [bijection] tea:a Nilgiri frost: ruled out position(s) 1
14. [bijection] taster:Yolanda: ruled out position(s) 4
15. [direct] from clue 9 note:wet slate: ruled out position(s) 4
16. [direct] from clue 1 tea:a Keemun: ruled out position(s) 4
17. [bijection] note:stewed apricot: ruled out position(s) 3
18. [bijection] note:bruised peach: ruled out position(s) 3
19. [bijection] tea:a Nilgiri frost: ruled out position(s) 3
20. [order] from clue 6 note:stewed apricot: ruled out position(s) 2,4
21. [order] from clue 6 tea:a Nilgiri frost: ruled out position(s) 4
22. [bijection] note:hay and honey: ruled out position(s) 1
23. [bijection] note:bruised peach: ruled out position(s) 1
24. [bijection] note:bruised peach: ruled out position(s) 2
25. [bijection] tea:a roasted oolong: ruled out position(s) 2
26. [direct] from clue 8 taster:Ignatia: ruled out position(s) 2
27. [bijection] taster:Marguerite: ruled out position(s) 4

---

<sub>seed `2026172846713` &middot; score 4.73 &middot; atoms 9 &middot; positives 3 &middot; solved by order</sub>
