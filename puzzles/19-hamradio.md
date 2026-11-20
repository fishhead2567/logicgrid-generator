# Field Day on Barrow Hill

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `679d8f5c378b`

## Introduction

A club field day spread over a week, one operator a night, and a generator that has its own opinions.
Five operators are involved. Determine each operator's night, band and mode.
- **Operator**: Nkem, Bartholomew, Yusuf, Rosalind and Clementine.
- **Night** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Band**: 10 metres, 15 metres, 40 metres, 20 metres and 160 metres.
- **Mode**: CW, slow-scan television, AM, RTTY and SSB.
Every operator has a different night, band and mode, so within each category every item is used exactly once.

## Clues

1. Clementine falls somewhere between Friday and Monday in night order.
2. The operator who works 15 metres does not operate CW. The operator who works 15 metres and Thursday are exactly three days apart in night order.
3. The operator who operates AM and Monday are exactly one day apart in night order, in one direction or the other.
4. The operator who operates RTTY is exactly one day earlier than Friday, with no night in between.
5. Clementine does not operate RTTY.
6. The operator who works 15 metres and Yusuf are exactly two days apart in night order.
7. The operator who operates slow-scan television is exactly one day earlier than the operator who works 10 metres, with no night in between.
8. Bartholomew is exactly one day earlier than the operator who works 40 metres, with no night in between.
9. The operator who operates slow-scan television and Nkem are exactly one day apart in night order, in one direction or the other.
10. The operator who works 20 metres does not operate slow-scan television.

## Solving chart

*Night vs Operator*

| | Nkem | Bartholomew | Yusuf | Rosalind | Clementine |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Night vs Band*

| | 10 metres | 15 metres | 40 metres | 20 metres | 160 metres |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Night vs Mode*

| | CW | slow-scan television | AM | RTTY | SSB |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Operator vs Band*

| | 10 metres | 15 metres | 40 metres | 20 metres | 160 metres |
|---|---|---|---|---|---|
| **Nkem** | | | | | |
| **Bartholomew** | | | | | |
| **Yusuf** | | | | | |
| **Rosalind** | | | | | |
| **Clementine** | | | | | |

*Operator vs Mode*

| | CW | slow-scan television | AM | RTTY | SSB |
|---|---|---|---|---|---|
| **Nkem** | | | | | |
| **Bartholomew** | | | | | |
| **Yusuf** | | | | | |
| **Rosalind** | | | | | |
| **Clementine** | | | | | |

*Band vs Mode*

| | CW | slow-scan television | AM | RTTY | SSB |
|---|---|---|---|---|---|
| **10 metres** | | | | | |
| **15 metres** | | | | | |
| **40 metres** | | | | | |
| **20 metres** | | | | | |
| **160 metres** | | | | | |

## Solution

| Night | Operator | Band | Mode |
|---|---|---|---|
| Monday | Bartholomew | 15 metres | SSB |
| Tuesday | Clementine | 40 metres | AM |
| Wednesday | Yusuf | 160 metres | slow-scan television |
| Thursday | Nkem | 10 metres | RTTY |
| Friday | Rosalind | 20 metres | CW |

## How it falls out

1. [order] from clue 11 band:15 metres: ruled out position(s) 2,3,4,5
2. [order] from clue 10 mode:slow-scan television: ruled out position(s) 5
3. [order] from clue 10 band:10 metres: ruled out position(s) 1
4. [order] from clue 9 mode:AM: ruled out position(s) 1,3,4,5
5. [order] from clue 8 operator:Clementine: ruled out position(s) 1,5
6. [order] from clue 7 operator:Bartholomew: ruled out position(s) 5
7. [order] from clue 7 band:40 metres: ruled out position(s) 1
8. [order] from clue 4 operator:Yusuf: ruled out position(s) 1,2,4,5
9. [order] from clue 3 mode:RTTY: ruled out position(s) 1,2,3,5
10. [direct] from clue 5 operator:Clementine: ruled out position(s) 4
11. [direct] from clue 1 mode:CW: ruled out position(s) 1
12. [bijection] band:20 metres: ruled out position(s) 1
13. [bijection] band:160 metres: ruled out position(s) 1
14. [bijection] mode:CW: ruled out position(s) 2,4
15. [bijection] mode:slow-scan television: ruled out position(s) 2,4
16. [bijection] mode:SSB: ruled out position(s) 2,4
17. [bijection] operator:Nkem: ruled out position(s) 3
18. [bijection] operator:Bartholomew: ruled out position(s) 3
19. [bijection] operator:Rosalind: ruled out position(s) 3
20. [bijection] operator:Clementine: ruled out position(s) 3
21. [order] from clue 7 band:40 metres: ruled out position(s) 4
22. [order] from clue 10 band:10 metres: ruled out position(s) 3,5
23. [order] from clue 2 operator:Nkem: ruled out position(s) 1,5
24. [bijection] operator:Nkem: ruled out position(s) 2
25. [bijection] operator:Bartholomew: ruled out position(s) 2
26. [bijection] operator:Rosalind: ruled out position(s) 2
27. [bijection] operator:Rosalind: ruled out position(s) 1,4
28. [order] from clue 7 band:40 metres: ruled out position(s) 3
29. [order] from clue 2 mode:slow-scan television: ruled out position(s) 1
30. [order] from clue 10 band:10 metres: ruled out position(s) 2
31. [direct] from clue 6 band:20 metres: ruled out position(s) 3
32. [bijection] band:20 metres: ruled out position(s) 4
33. [bijection] band:160 metres: ruled out position(s) 4
34. [bijection] band:160 metres: ruled out position(s) 2,5
35. [bijection] mode:CW: ruled out position(s) 3
36. [bijection] mode:SSB: ruled out position(s) 3
37. [bijection] mode:SSB: ruled out position(s) 5
38. [bijection] operator:Bartholomew: ruled out position(s) 4
39. [order] from clue 7 band:40 metres: ruled out position(s) 5
40. [bijection] band:20 metres: ruled out position(s) 2

---

<sub>seed `2026172925903` &middot; score 5.675 &middot; atoms 11 &middot; positives 0 &middot; solved by order</sub>
