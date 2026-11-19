# The Thistledown Balloon Ascent

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `c911d3778874`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Five pilots are involved. Determine each pilot's start time, landing site and ballast.
- **Pilot**: Grover, Delphine, Horatio, Anneliese and Montague.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Landed at**: a cabbage field, a flooded quarry, a golf course bunker, a caravan park and a cricket pitch.
- **Ballast**: iron filings, bottled water, dried beans, rock salt and lead shot.
Every pilot has a different start time, landing site and ballast, so within each category every item is used exactly once.

## Clues

1. The pilot who comes down in a golf course bunker launches at 9am.
2. The pilot who comes down in a caravan park is earlier than 10am in start time order.
3. The pilot who carries rock salt and 11am are exactly one hour apart in start time order, in one direction or the other.
4. Montague does not launch at 8am.
5. The pilot who carries iron filings does not launch at noon.
6. Delphine falls somewhere between the pilot who carries bottled water and the pilot who carries rock salt in start time order.
7. The pilot who comes down in a flooded quarry is exactly one hour earlier than Horatio, with no start time in between.
8. The pilot who carries lead shot and the pilot who comes down in a flooded quarry are exactly two hours apart in start time order.
9. The pilot who carries rock salt is exactly one hour earlier than Grover, with no start time in between.
10. The pilot who comes down in a cabbage field falls somewhere between the pilot who carries iron filings and the pilot who carries lead shot in start time order.

## Solving chart

*Start time vs Pilot*

| | Grover | Delphine | Horatio | Anneliese | Montague |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Landed at*

| | a cabbage field | a flooded quarry | a golf course bunker | a caravan park | a cricket pitch |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Ballast*

| | iron filings | bottled water | dried beans | rock salt | lead shot |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Pilot vs Landed at*

| | a cabbage field | a flooded quarry | a golf course bunker | a caravan park | a cricket pitch |
|---|---|---|---|---|---|
| **Grover** | | | | | |
| **Delphine** | | | | | |
| **Horatio** | | | | | |
| **Anneliese** | | | | | |
| **Montague** | | | | | |

*Pilot vs Ballast*

| | iron filings | bottled water | dried beans | rock salt | lead shot |
|---|---|---|---|---|---|
| **Grover** | | | | | |
| **Delphine** | | | | | |
| **Horatio** | | | | | |
| **Anneliese** | | | | | |
| **Montague** | | | | | |

*Landed at vs Ballast*

| | iron filings | bottled water | dried beans | rock salt | lead shot |
|---|---|---|---|---|---|
| **a cabbage field** | | | | | |
| **a flooded quarry** | | | | | |
| **a golf course bunker** | | | | | |
| **a caravan park** | | | | | |
| **a cricket pitch** | | | | | |

## Solution

| Start time | Pilot | Landed at | Ballast |
|---|---|---|---|
| 8am | Anneliese | a caravan park | bottled water |
| 9am | Delphine | a golf course bunker | lead shot |
| 10am | Montague | a cabbage field | rock salt |
| 11am | Grover | a flooded quarry | iron filings |
| noon | Horatio | a cricket pitch | dried beans |

## How it falls out

1. [direct] from clue 10 landing:a golf course bunker: ruled out position(s) 1,3,4,5
2. [direct] from clue 9 ballast:iron filings: ruled out position(s) 5
3. [direct] from clue 6 pilot:Montague: ruled out position(s) 1
4. [bijection] landing:a cabbage field: ruled out position(s) 2
5. [bijection] landing:a flooded quarry: ruled out position(s) 2
6. [bijection] landing:a caravan park: ruled out position(s) 2
7. [bijection] landing:a cricket pitch: ruled out position(s) 2
8. [order] from clue 8 ballast:lead shot: ruled out position(s) 4
9. [order] from clue 7 landing:a cabbage field: ruled out position(s) 1,5
10. [order] from clue 7 ballast:lead shot: ruled out position(s) 3
11. [order] from clue 8 landing:a flooded quarry: ruled out position(s) 1,5
12. [order] from clue 5 pilot:Delphine: ruled out position(s) 1,5
13. [order] from clue 4 pilot:Horatio: ruled out position(s) 1,2,3
14. [order] from clue 3 ballast:rock salt: ruled out position(s) 1,2,4
15. [order] from clue 5 ballast:bottled water: ruled out position(s) 4
16. [order] from clue 2 ballast:rock salt: ruled out position(s) 5
17. [order] from clue 2 pilot:Grover: ruled out position(s) 1,2,3,5
18. [order] from clue 5 pilot:Delphine: ruled out position(s) 3
19. [order] from clue 5 ballast:bottled water: ruled out position(s) 2,3
20. [order] from clue 1 landing:a caravan park: ruled out position(s) 3,4,5
21. [bijection] ballast:iron filings: ruled out position(s) 3
22. [bijection] ballast:dried beans: ruled out position(s) 3
23. [bijection] landing:a cricket pitch: ruled out position(s) 1
24. [bijection] landing:a cricket pitch: ruled out position(s) 3,4
25. [bijection] pilot:Delphine: ruled out position(s) 4
26. [bijection] pilot:Horatio: ruled out position(s) 4
27. [bijection] pilot:Anneliese: ruled out position(s) 4
28. [bijection] pilot:Montague: ruled out position(s) 4
29. [bijection] pilot:Anneliese: ruled out position(s) 2,3,5
30. [order] from clue 4 landing:a flooded quarry: ruled out position(s) 3
31. [order] from clue 8 ballast:lead shot: ruled out position(s) 1,5
32. [order] from clue 5 ballast:bottled water: ruled out position(s) 5
33. [order] from clue 7 landing:a cabbage field: ruled out position(s) 4
34. [order] from clue 7 ballast:iron filings: ruled out position(s) 1,2
35. [bijection] ballast:dried beans: ruled out position(s) 1,2,4
36. [bijection] pilot:Montague: ruled out position(s) 2,5

---

<sub>seed `2026172897171` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
