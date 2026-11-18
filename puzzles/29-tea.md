# The Blind Tasting at Pemberton's

*Pemberton's holds a blind tasting each spring. The tasters are blind to the tea; the tea is not blind to them.*

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `b9d36185280e`

## Introduction

There are 5 tastings. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different tasting.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m., 11 a.m. and noon.
- **Tea**: a roasted oolong, a Keemun, a first-flush Darjeeling, a smoked Lapsang and a pressed pu-erh.
- **Tasting note**: pine smoke, iron filings, hay and honey, bruised peach and stewed apricot.
- **Cup**: a bone china cup, a pewter beaker, an enamel mug, a lacquered bowl and a glass tumbler.
The hours above are listed in order, from 8 a.m. to noon.

## Clues

1. Bruised peach goes with 9 a.m..
2. A smoked Lapsang's start time is immediately earlier than 10 a.m., with no start time in between.
3. A glass tumbler and 8 a.m. are exactly two hours apart in start time order. A glass tumbler does not go with a Keemun.
4. A pressed pu-erh and 9 a.m. both sit at odd-numbered hours or both at even-numbered hours.
5. One of a lacquered bowl and hay and honey sits at an odd-numbered start time and the other at an even-numbered start time. A lacquered bowl does not go with a pressed pu-erh.
6. Iron filings' start time is earlier than a first-flush Darjeeling's start time.
7. A bone china cup and a pressed pu-erh are next to each other in start time order, in one order or the other.
8. A pewter beaker falls somewhere between pine smoke and a pressed pu-erh in start time order.

## Solving chart

*Start time vs Tea*

| | a roasted oolong | a Keemun | a first-flush Darjeeling | a smoked Lapsang | a pressed pu-erh |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Tasting note*

| | pine smoke | iron filings | hay and honey | bruised peach | stewed apricot |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Cup*

| | a bone china cup | a pewter beaker | an enamel mug | a lacquered bowl | a glass tumbler |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Tea vs Tasting note*

| | pine smoke | iron filings | hay and honey | bruised peach | stewed apricot |
|---|---|---|---|---|---|
| **a roasted oolong** | | | | | |
| **a Keemun** | | | | | |
| **a first-flush Darjeeling** | | | | | |
| **a smoked Lapsang** | | | | | |
| **a pressed pu-erh** | | | | | |

*Tea vs Cup*

| | a bone china cup | a pewter beaker | an enamel mug | a lacquered bowl | a glass tumbler |
|---|---|---|---|---|---|
| **a roasted oolong** | | | | | |
| **a Keemun** | | | | | |
| **a first-flush Darjeeling** | | | | | |
| **a smoked Lapsang** | | | | | |
| **a pressed pu-erh** | | | | | |

*Tasting note vs Cup*

| | a bone china cup | a pewter beaker | an enamel mug | a lacquered bowl | a glass tumbler |
|---|---|---|---|---|---|
| **pine smoke** | | | | | |
| **iron filings** | | | | | |
| **hay and honey** | | | | | |
| **bruised peach** | | | | | |
| **stewed apricot** | | | | | |

## Solution

| Start time | Tea | Tasting note | Cup |
|---|---|---|---|
| 8 a.m. | a Keemun | pine smoke | a lacquered bowl |
| 9 a.m. | a smoked Lapsang | bruised peach | a pewter beaker |
| 10 a.m. | a roasted oolong | iron filings | a glass tumbler |
| 11 a.m. | a pressed pu-erh | hay and honey | an enamel mug |
| noon | a first-flush Darjeeling | stewed apricot | a bone china cup |

## How it falls out

1. [direct] from clue 3 note:bruised peach: ruled out position(s) 1,3,4,5
2. [bijection] note:pine smoke: ruled out position(s) 2
3. [bijection] note:iron filings: ruled out position(s) 2
4. [bijection] note:hay and honey: ruled out position(s) 2
5. [bijection] note:stewed apricot: ruled out position(s) 2
6. [order] from clue 10 cup:a pewter beaker: ruled out position(s) 1,5
7. [order] from clue 8 note:iron filings: ruled out position(s) 5
8. [order] from clue 8 tea:a first-flush Darjeeling: ruled out position(s) 1
9. [order] from clue 5 tea:a smoked Lapsang: ruled out position(s) 1,3,4,5
10. [order] from clue 4 cup:a glass tumbler: ruled out position(s) 1,2,4,5
11. [order] from clue 1 tea:a pressed pu-erh: ruled out position(s) 1,3,5
12. [order] from clue 10 note:pine smoke: ruled out position(s) 3
13. [order] from clue 9 cup:a bone china cup: ruled out position(s) 2,4
14. [direct] from clue 2 tea:a Keemun: ruled out position(s) 3
15. [bijection] cup:a bone china cup: ruled out position(s) 3
16. [bijection] cup:a pewter beaker: ruled out position(s) 3
17. [bijection] cup:an enamel mug: ruled out position(s) 3
18. [bijection] cup:a lacquered bowl: ruled out position(s) 3
19. [bijection] tea:a roasted oolong: ruled out position(s) 2
20. [bijection] tea:a Keemun: ruled out position(s) 2
21. [bijection] tea:a first-flush Darjeeling: ruled out position(s) 2
22. [bijection] tea:a pressed pu-erh: ruled out position(s) 2
23. [direct] from clue 6 cup:a lacquered bowl: ruled out position(s) 4
24. [order] from clue 10 cup:a pewter beaker: ruled out position(s) 4
25. [order] from clue 10 note:pine smoke: ruled out position(s) 4,5
26. [order] from clue 9 cup:a bone china cup: ruled out position(s) 1
27. [bijection] cup:an enamel mug: ruled out position(s) 2,5
28. [bijection] cup:a lacquered bowl: ruled out position(s) 2,5
29. [bijection] cup:an enamel mug: ruled out position(s) 1
30. [bijection] note:iron filings: ruled out position(s) 1
31. [bijection] note:hay and honey: ruled out position(s) 1
32. [bijection] note:stewed apricot: ruled out position(s) 1
33. [bijection] tea:a roasted oolong: ruled out position(s) 4
34. [bijection] tea:a Keemun: ruled out position(s) 4
35. [bijection] tea:a first-flush Darjeeling: ruled out position(s) 4
36. [order] from clue 8 tea:a first-flush Darjeeling: ruled out position(s) 3
37. [order] from clue 7 note:hay and honey: ruled out position(s) 3,5
38. [bijection] note:iron filings: ruled out position(s) 4
39. [bijection] note:stewed apricot: ruled out position(s) 4
40. [bijection] note:stewed apricot: ruled out position(s) 3
_... and 3 further steps._

---

<sub>seed `2026172805087` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
