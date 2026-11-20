# The Thistledown Balloon Ascent

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `1326e86f0870`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Five pilots are involved. Determine each pilot's start time, landing site and ballast.
- **Pilot**: Isolde, Anneliese, Rosalind, Grover and Horatio.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Landed at**: a cricket pitch, a cabbage field, a golf course bunker, a reservoir bank and a caravan park.
- **Ballast**: pea gravel, dried beans, lead shot, iron filings and sandbags.
Every pilot has a different start time, landing site and ballast, so within each category every item is used exactly once.

## Clues

1. Rosalind comes down in a golf course bunker. The pilot who comes down in a caravan park falls somewhere between Grover and Rosalind in start time order.
2. The pilot who carries iron filings is earlier than noon in start time order.
3. Isolde does not launch at 9am.
4. The pilot who carries dried beans and noon are exactly one hour apart in start time order, in one direction or the other.
5. The pilot who comes down in a cabbage field is later than 10am in start time order.
6. The pilot who carries pea gravel does not come down in a reservoir bank.
7. The pilot who carries iron filings and Horatio are exactly two hours apart in start time order. Grover is earlier than the pilot who carries iron filings in start time order.
8. The pilot who carries lead shot and Horatio are exactly one hour apart in start time order, in one direction or the other.
9. The pilot who carries sandbags falls somewhere between the pilot who comes down in a caravan park and the pilot who comes down in a golf course bunker in start time order.

## Solving chart

*Start time vs Pilot*

| | Isolde | Anneliese | Rosalind | Grover | Horatio |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Landed at*

| | a cricket pitch | a cabbage field | a golf course bunker | a reservoir bank | a caravan park |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Ballast*

| | pea gravel | dried beans | lead shot | iron filings | sandbags |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Pilot vs Landed at*

| | a cricket pitch | a cabbage field | a golf course bunker | a reservoir bank | a caravan park |
|---|---|---|---|---|---|
| **Isolde** | | | | | |
| **Anneliese** | | | | | |
| **Rosalind** | | | | | |
| **Grover** | | | | | |
| **Horatio** | | | | | |

*Pilot vs Ballast*

| | pea gravel | dried beans | lead shot | iron filings | sandbags |
|---|---|---|---|---|---|
| **Isolde** | | | | | |
| **Anneliese** | | | | | |
| **Rosalind** | | | | | |
| **Grover** | | | | | |
| **Horatio** | | | | | |

*Landed at vs Ballast*

| | pea gravel | dried beans | lead shot | iron filings | sandbags |
|---|---|---|---|---|---|
| **a cricket pitch** | | | | | |
| **a cabbage field** | | | | | |
| **a golf course bunker** | | | | | |
| **a reservoir bank** | | | | | |
| **a caravan park** | | | | | |

## Solution

| Start time | Pilot | Landed at | Ballast |
|---|---|---|---|
| 8am | Grover | a cricket pitch | pea gravel |
| 9am | Anneliese | a caravan park | iron filings |
| 10am | Isolde | a reservoir bank | sandbags |
| 11am | Horatio | a cabbage field | dried beans |
| noon | Rosalind | a golf course bunker | lead shot |

## How it falls out

1. [direct] from clue 3 pilot:Isolde: ruled out position(s) 2
2. [order] from clue 11 ballast:dried beans: ruled out position(s) 1,2,3,5
3. [order] from clue 10 ballast:sandbags: ruled out position(s) 1,5
4. [order] from clue 8 pilot:Grover: ruled out position(s) 5
5. [order] from clue 8 ballast:iron filings: ruled out position(s) 1
6. [order] from clue 5 ballast:iron filings: ruled out position(s) 5
7. [order] from clue 9 pilot:Horatio: ruled out position(s) 3
8. [order] from clue 8 pilot:Grover: ruled out position(s) 4
9. [order] from clue 4 landing:a caravan park: ruled out position(s) 1,5
10. [order] from clue 4 pilot:Rosalind: ruled out position(s) 2
11. [order] from clue 10 landing:a golf course bunker: ruled out position(s) 3
12. [order] from clue 1 landing:a cabbage field: ruled out position(s) 1,2,3
13. [direct] from clue 7 landing:a golf course bunker: ruled out position(s) 2
14. [direct] from clue 7 pilot:Rosalind: ruled out position(s) 3
15. [bijection] ballast:pea gravel: ruled out position(s) 4
16. [bijection] ballast:lead shot: ruled out position(s) 4
17. [bijection] ballast:iron filings: ruled out position(s) 4
18. [bijection] ballast:sandbags: ruled out position(s) 4
19. [order] from clue 9 pilot:Horatio: ruled out position(s) 2
20. [order] from clue 8 pilot:Grover: ruled out position(s) 3
21. [order] from clue 4 pilot:Rosalind: ruled out position(s) 1
22. [direct] from clue 7 landing:a golf course bunker: ruled out position(s) 1
23. [order] from clue 10 ballast:sandbags: ruled out position(s) 2
24. [order] from clue 10 landing:a caravan park: ruled out position(s) 3,4
25. [order] from clue 4 pilot:Grover: ruled out position(s) 2
26. [order] from clue 2 ballast:lead shot: ruled out position(s) 1
27. [order] from clue 2 pilot:Horatio: ruled out position(s) 5
28. [bijection] ballast:pea gravel: ruled out position(s) 3
29. [bijection] ballast:lead shot: ruled out position(s) 3
30. [bijection] ballast:iron filings: ruled out position(s) 3
31. [bijection] ballast:pea gravel: ruled out position(s) 2,5
32. [bijection] landing:a cricket pitch: ruled out position(s) 2
33. [bijection] landing:a reservoir bank: ruled out position(s) 2
34. [bijection] pilot:Isolde: ruled out position(s) 1
35. [bijection] pilot:Anneliese: ruled out position(s) 1
36. [bijection] pilot:Horatio: ruled out position(s) 1
37. [bijection] pilot:Anneliese: ruled out position(s) 3,4,5
38. [order] from clue 2 ballast:lead shot: ruled out position(s) 2
39. [direct] from clue 6 landing:a reservoir bank: ruled out position(s) 1
40. [bijection] landing:a cricket pitch: ruled out position(s) 3,4,5
_... and 7 further steps._

---

<sub>seed `2026172965498` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
