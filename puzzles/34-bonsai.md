# The Autumn Show at Kiyosumi

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `1085880a8d1d`

## Introduction

Six trees on six stands, judged on a hundred-point sheet, and the wiring marks are what everybody is looking for.
Five exhibitors are involved. Determine each exhibitor's judged score, style and species.
- **Exhibitor**: Hiroshi Mita, Emi Tsuchida, Jun Kawabe, Takumi Ishii and Noriko Hase.
- **Judged score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Style**: moyogi, chokkan, ikadabuki, bunjin and kengai.
- **Species**: a hinoki cypress, a zelkova, a winged elm, a Japanese black pine and a Chinese quince.
Every exhibitor has a different judged score, style and species, so within each category every item is used exactly once.

## Clues

1. 64 points is exactly one score step lower than the exhibitor who has grown a zelkova, with no judged score in between. The exhibitor who shows ikadabuki is not awarded 64 points.
2. The exhibitor who shows kengai is higher than 67 points in judged score order.
3. At least one of the following holds, and possibly more than one: (a) The exhibitor who shows moyogi and 73 points are exactly one score step apart in judged score order, in one direction or the other. (b) Emi Tsuchida is lower than the exhibitor who shows bunjin in judged score order.
4. 67 points falls somewhere between the exhibitor who has grown a hinoki cypress and the exhibitor who shows ikadabuki in judged score order.
5. Jun Kawabe and 61 points are exactly one score step apart in judged score order, in one direction or the other.
6. Hiroshi Mita is lower than the exhibitor who shows chokkan in judged score order.
7. The exhibitor who shows bunjin is lower than Emi Tsuchida in judged score order.
8. The exhibitor who has grown a Chinese quince falls somewhere between Hiroshi Mita and Takumi Ishii in judged score order.
9. The exhibitor who has grown a hinoki cypress and the exhibitor who shows chokkan are exactly one score step apart in judged score order, in one direction or the other.
10. Emi Tsuchida and the exhibitor who has grown a zelkova are exactly one score step apart in judged score order, in one direction or the other.
11. Noriko Hase is lower than the exhibitor who has grown a Japanese black pine in judged score order.

## Solving chart

*Judged score vs Exhibitor*

| | Hiroshi Mita | Emi Tsuchida | Jun Kawabe | Takumi Ishii | Noriko Hase |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Judged score vs Style*

| | moyogi | chokkan | ikadabuki | bunjin | kengai |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Judged score vs Species*

| | a hinoki cypress | a zelkova | a winged elm | a Japanese black pine | a Chinese quince |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Exhibitor vs Style*

| | moyogi | chokkan | ikadabuki | bunjin | kengai |
|---|---|---|---|---|---|
| **Hiroshi Mita** | | | | | |
| **Emi Tsuchida** | | | | | |
| **Jun Kawabe** | | | | | |
| **Takumi Ishii** | | | | | |
| **Noriko Hase** | | | | | |

*Exhibitor vs Species*

| | a hinoki cypress | a zelkova | a winged elm | a Japanese black pine | a Chinese quince |
|---|---|---|---|---|---|
| **Hiroshi Mita** | | | | | |
| **Emi Tsuchida** | | | | | |
| **Jun Kawabe** | | | | | |
| **Takumi Ishii** | | | | | |
| **Noriko Hase** | | | | | |

*Style vs Species*

| | a hinoki cypress | a zelkova | a winged elm | a Japanese black pine | a Chinese quince |
|---|---|---|---|---|---|
| **moyogi** | | | | | |
| **chokkan** | | | | | |
| **ikadabuki** | | | | | |
| **bunjin** | | | | | |
| **kengai** | | | | | |

## Solution

| Judged score | Exhibitor | Style | Species |
|---|---|---|---|
| 61 points | Hiroshi Mita | ikadabuki | a winged elm |
| 64 points | Jun Kawabe | bunjin | a Chinese quince |
| 67 points | Noriko Hase | chokkan | a zelkova |
| 70 points | Emi Tsuchida | moyogi | a hinoki cypress |
| 73 points | Takumi Ishii | kengai | a Japanese black pine |

## How it falls out

1. [direct] from clue 12 style:ikadabuki: ruled out position(s) 2
2. [order] from clue 11 species:a zelkova: ruled out position(s) 1,2,4,5
3. [order] from clue 9 style:kengai: ruled out position(s) 1,2,3
4. [order] from clue 8 exhibitor:Emi Tsuchida: ruled out position(s) 1,3,5
5. [order] from clue 6 style:bunjin: ruled out position(s) 4,5
6. [order] from clue 5 exhibitor:Noriko Hase: ruled out position(s) 5
7. [order] from clue 5 species:a Japanese black pine: ruled out position(s) 1
8. [order] from clue 4 species:a Chinese quince: ruled out position(s) 1,5
9. [order] from clue 3 species:a hinoki cypress: ruled out position(s) 3
10. [order] from clue 3 style:ikadabuki: ruled out position(s) 3
11. [order] from clue 2 exhibitor:Jun Kawabe: ruled out position(s) 1,3,4,5
12. [order] from clue 1 exhibitor:Hiroshi Mita: ruled out position(s) 5
13. [order] from clue 1 style:chokkan: ruled out position(s) 1
14. [bijection] exhibitor:Hiroshi Mita: ruled out position(s) 2
15. [bijection] exhibitor:Emi Tsuchida: ruled out position(s) 2
16. [bijection] exhibitor:Takumi Ishii: ruled out position(s) 2
17. [bijection] exhibitor:Noriko Hase: ruled out position(s) 2
18. [bijection] exhibitor:Takumi Ishii: ruled out position(s) 1,3,4
19. [bijection] species:a winged elm: ruled out position(s) 3
20. [bijection] species:a Japanese black pine: ruled out position(s) 3
21. [bijection] species:a Chinese quince: ruled out position(s) 3
22. [order] from clue 4 exhibitor:Hiroshi Mita: ruled out position(s) 4
23. [bijection] exhibitor:Noriko Hase: ruled out position(s) 4
24. [disjunction] from clue 7 style:moyogi: ruled out position(s) 1,2,3,5
25. [bijection] style:chokkan: ruled out position(s) 4
26. [bijection] style:ikadabuki: ruled out position(s) 4
27. [bijection] style:kengai: ruled out position(s) 4
28. [order] from clue 10 species:a hinoki cypress: ruled out position(s) 5
29. [bijection] style:chokkan: ruled out position(s) 5
30. [bijection] style:ikadabuki: ruled out position(s) 5
31. [order] from clue 3 species:a hinoki cypress: ruled out position(s) 1,2
32. [order] from clue 10 style:chokkan: ruled out position(s) 2
33. [order] from clue 1 exhibitor:Hiroshi Mita: ruled out position(s) 3
34. [bijection] exhibitor:Noriko Hase: ruled out position(s) 1
35. [bijection] species:a winged elm: ruled out position(s) 4
36. [bijection] species:a Japanese black pine: ruled out position(s) 4
37. [bijection] species:a Chinese quince: ruled out position(s) 4
38. [bijection] species:a winged elm: ruled out position(s) 2,5
39. [bijection] style:bunjin: ruled out position(s) 1,3
40. [order] from clue 5 species:a Japanese black pine: ruled out position(s) 2

---

<sub>seed `2026172944685` &middot; score 8.7392 &middot; atoms 12 &middot; positives 0 &middot; solved by disjunction</sub>
