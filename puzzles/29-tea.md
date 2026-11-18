# The Blind Tasting at Pemberton's

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `5a255b2d0dd9`

## Introduction

Pemberton's holds a blind tasting each spring. The tasters are blind to the tea; the tea is not blind to them.
Five tasters are involved. Determine each taster's start time, note and cup.
- **Taster**: Yolanda, Marguerite, Chidi, Rolf and Soren.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Tasting note**: wet slate; stewed apricot; pine smoke; hay and honey; and bruised peach.
- **Cup**: a glass tumbler, a bone china cup, a pewter beaker, an enamel mug and a stoneware cup.
Every taster has a different start time, note and cup, so within each category every item is used exactly once.

## Clues

1. Soren reports pine smoke. 9am falls somewhere between the taster who reports pine smoke and the taster who reports wet slate in start time order. Yolanda does not report wet slate.
2. Chidi does not taste at 8am.
3. The taster who drinks from a pewter beaker is exactly one hour earlier than noon, with no start time in between.
4. The taster who reports pine smoke and 10am are exactly one hour apart in start time order, in one direction or the other.
5. Rolf is earlier than the taster who drinks from a glass tumbler in start time order.
6. The taster who drinks from a stoneware cup and Soren are exactly one hour apart in start time order, in one direction or the other.
7. The taster who drinks from a stoneware cup and Rolf are exactly one hour apart in start time order, in one direction or the other.
8. Yolanda is earlier than the taster who reports bruised peach in start time order.
9. The taster who drinks from a bone china cup falls somewhere between the taster who reports stewed apricot and the taster who reports wet slate in start time order.

## Solving chart

*Start time vs Taster*

| | Yolanda | Marguerite | Chidi | Rolf | Soren |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Tasting note*

| | wet slate | stewed apricot | pine smoke | hay and honey | bruised peach |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Cup*

| | a glass tumbler | a bone china cup | a pewter beaker | an enamel mug | a stoneware cup |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Taster vs Tasting note*

| | wet slate | stewed apricot | pine smoke | hay and honey | bruised peach |
|---|---|---|---|---|---|
| **Yolanda** | | | | | |
| **Marguerite** | | | | | |
| **Chidi** | | | | | |
| **Rolf** | | | | | |
| **Soren** | | | | | |

*Taster vs Cup*

| | a glass tumbler | a bone china cup | a pewter beaker | an enamel mug | a stoneware cup |
|---|---|---|---|---|---|
| **Yolanda** | | | | | |
| **Marguerite** | | | | | |
| **Chidi** | | | | | |
| **Rolf** | | | | | |
| **Soren** | | | | | |

*Tasting note vs Cup*

| | a glass tumbler | a bone china cup | a pewter beaker | an enamel mug | a stoneware cup |
|---|---|---|---|---|---|
| **wet slate** | | | | | |
| **stewed apricot** | | | | | |
| **pine smoke** | | | | | |
| **hay and honey** | | | | | |
| **bruised peach** | | | | | |

## Solution

| Start time | Taster | Tasting note | Cup |
|---|---|---|---|
| 8am | Marguerite | wet slate | an enamel mug |
| 9am | Rolf | hay and honey | a bone china cup |
| 10am | Yolanda | stewed apricot | a stoneware cup |
| 11am | Soren | pine smoke | a pewter beaker |
| noon | Chidi | bruised peach | a glass tumbler |

## How it falls out

1. [direct] from clue 5 taster:Chidi: ruled out position(s) 1
2. [order] from clue 10 cup:a pewter beaker: ruled out position(s) 1,2,3,5
3. [order] from clue 9 taster:Yolanda: ruled out position(s) 5
4. [order] from clue 9 note:bruised peach: ruled out position(s) 1
5. [order] from clue 8 note:pine smoke: ruled out position(s) 1,3,5
6. [order] from clue 6 taster:Rolf: ruled out position(s) 5
7. [order] from clue 6 cup:a glass tumbler: ruled out position(s) 1
8. [order] from clue 3 note:pine smoke: ruled out position(s) 2
9. [order] from clue 3 note:wet slate: ruled out position(s) 2,3,4,5
10. [order] from clue 1 cup:a bone china cup: ruled out position(s) 1,5
11. [order] from clue 1 note:stewed apricot: ruled out position(s) 1,2
12. [direct] from clue 7 taster:Yolanda: ruled out position(s) 1
13. [order] from clue 9 note:bruised peach: ruled out position(s) 2
14. [direct] from clue 2 taster:Soren: ruled out position(s) 1,2,3,5
15. [order] from clue 11 cup:a stoneware cup: ruled out position(s) 1,2,4
16. [order] from clue 4 taster:Rolf: ruled out position(s) 1,3
17. [order] from clue 6 cup:a glass tumbler: ruled out position(s) 2
18. [bijection] cup:a glass tumbler: ruled out position(s) 4
19. [bijection] cup:a bone china cup: ruled out position(s) 4
20. [bijection] cup:an enamel mug: ruled out position(s) 4
21. [bijection] cup:an enamel mug: ruled out position(s) 2,3,5
22. [bijection] note:stewed apricot: ruled out position(s) 4
23. [bijection] note:hay and honey: ruled out position(s) 1,4
24. [bijection] note:bruised peach: ruled out position(s) 4
25. [bijection] note:hay and honey: ruled out position(s) 3,5
26. [bijection] taster:Yolanda: ruled out position(s) 4
27. [bijection] taster:Marguerite: ruled out position(s) 4
28. [bijection] taster:Chidi: ruled out position(s) 4
29. [bijection] taster:Rolf: ruled out position(s) 4
30. [bijection] taster:Marguerite: ruled out position(s) 2,3,5
31. [order] from clue 4 cup:a stoneware cup: ruled out position(s) 5
32. [bijection] cup:a glass tumbler: ruled out position(s) 3
33. [bijection] cup:a bone china cup: ruled out position(s) 3
34. [bijection] taster:Yolanda: ruled out position(s) 2
35. [bijection] taster:Chidi: ruled out position(s) 2
36. [bijection] taster:Chidi: ruled out position(s) 3
37. [order] from clue 9 note:bruised peach: ruled out position(s) 3
38. [bijection] note:stewed apricot: ruled out position(s) 5

---

<sub>seed `2026172805087` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
