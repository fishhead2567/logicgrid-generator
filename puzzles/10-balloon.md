# The Thistledown Balloon Ascent

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `b44a026ec09b`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Four pilots are involved. Determine each pilot's start time, landing site and ballast.
- **Pilot**: Anneliese, Montague, Rosalind and Delphine.
- **Start time** (listed from earlier to later): 8am, 9am, 10am and 11am.
- **Landed at**: a reservoir bank, a golf course bunker, a railway siding and a caravan park.
- **Ballast**: dried beans, sandbags, iron filings and lead shot.
Every pilot has a different start time, landing site and ballast, so within each category every item is used exactly once.

## Clues

1. The pilot who carries dried beans is earlier than the pilot who comes down in a golf course bunker in start time order. The pilot who comes down in a golf course bunker launches at 10am.
2. Montague carries sandbags.
3. The pilot who comes down in a reservoir bank is later than 9am in start time order. The pilot who comes down in a caravan park does not launch at 9am.
4. Delphine does not carry iron filings. Delphine is later than 10am in start time order.
5. Anneliese does not come down in a caravan park.
6. Anneliese does not come down in a golf course bunker.
7. The pilot who carries dried beans does not come down in a railway siding.

## Solving chart

*Start time vs Pilot*

| | Anneliese | Montague | Rosalind | Delphine |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Landed at*

| | a reservoir bank | a golf course bunker | a railway siding | a caravan park |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Ballast*

| | dried beans | sandbags | iron filings | lead shot |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Pilot vs Landed at*

| | a reservoir bank | a golf course bunker | a railway siding | a caravan park |
|---|---|---|---|---|
| **Anneliese** | | | | |
| **Montague** | | | | |
| **Rosalind** | | | | |
| **Delphine** | | | | |

*Pilot vs Ballast*

| | dried beans | sandbags | iron filings | lead shot |
|---|---|---|---|---|
| **Anneliese** | | | | |
| **Montague** | | | | |
| **Rosalind** | | | | |
| **Delphine** | | | | |

*Landed at vs Ballast*

| | dried beans | sandbags | iron filings | lead shot |
|---|---|---|---|---|
| **a reservoir bank** | | | | |
| **a golf course bunker** | | | | |
| **a railway siding** | | | | |
| **a caravan park** | | | | |

## Solution

| Start time | Pilot | Landed at | Ballast |
|---|---|---|---|
| 8am | Rosalind | a caravan park | dried beans |
| 9am | Anneliese | a railway siding | iron filings |
| 10am | Montague | a golf course bunker | sandbags |
| 11am | Delphine | a reservoir bank | lead shot |

## How it falls out

1. [direct] from clue 2 landing:a caravan park: ruled out position(s) 2
2. [direct] from clue 1 landing:a golf course bunker: ruled out position(s) 1,2,4
3. [direct] from clue 4 pilot:Anneliese: ruled out position(s) 3
4. [bijection] landing:a reservoir bank: ruled out position(s) 3
5. [bijection] landing:a railway siding: ruled out position(s) 3
6. [bijection] landing:a caravan park: ruled out position(s) 3
7. [order] from clue 10 ballast:dried beans: ruled out position(s) 3,4
8. [order] from clue 9 pilot:Delphine: ruled out position(s) 1,2,3
9. [order] from clue 3 landing:a reservoir bank: ruled out position(s) 1,2
10. [direct] from clue 6 ballast:iron filings: ruled out position(s) 4
11. [bijection] landing:a railway siding: ruled out position(s) 4
12. [bijection] landing:a caravan park: ruled out position(s) 4
13. [bijection] landing:a railway siding: ruled out position(s) 1
14. [bijection] pilot:Anneliese: ruled out position(s) 4
15. [bijection] pilot:Montague: ruled out position(s) 4
16. [bijection] pilot:Rosalind: ruled out position(s) 4
17. [direct] from clue 7 ballast:sandbags: ruled out position(s) 4
18. [direct] from clue 5 pilot:Anneliese: ruled out position(s) 1
19. [direct] from clue 8 ballast:dried beans: ruled out position(s) 2
20. [bijection] ballast:sandbags: ruled out position(s) 1
21. [bijection] ballast:iron filings: ruled out position(s) 1
22. [bijection] ballast:lead shot: ruled out position(s) 1
23. [bijection] ballast:lead shot: ruled out position(s) 2,3
24. [bijection] pilot:Montague: ruled out position(s) 2
25. [bijection] pilot:Rosalind: ruled out position(s) 2
26. [direct] from clue 7 ballast:sandbags: ruled out position(s) 2
27. [direct] from clue 7 pilot:Montague: ruled out position(s) 1
28. [bijection] ballast:iron filings: ruled out position(s) 3
29. [bijection] pilot:Rosalind: ruled out position(s) 3

---

<sub>seed `2026172654626` &middot; score 4.93 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
