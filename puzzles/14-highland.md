# The Heavies at Kinloch Rannoch

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `63256e76ce23`

## Introduction

The heavy events, measured to the foot, in a field where the wind counts for more than anybody admits.
Five throwers are involved. Determine each thrower's best throw and tartan.
- **Thrower**: Fiona Strachan, Duncan Rait, Angus Dunbar, Isla Kinnear and Lachlan Cree.
- **Best throw** (listed from shorter to longer): 28 feet, 32 feet, 36 feet, 40 feet and 44 feet.
- **Tartan**: Mackenzie weathered, Buchanan, Cameron of Erracht, Fraser hunting and Lamont ancient.
Every thrower has a different best throw and tartan, so within each category every item is used exactly once.

## Clues

1. Isla Kinnear throws 28 feet.
2. Isla Kinnear wears Lamont ancient.
3. The thrower who wears Mackenzie weathered is longer than 32 feet in best throw order.
4. Fiona Strachan does not throw 36 feet. The thrower who wears Fraser hunting and Fiona Strachan are exactly one throw step apart in best throw order, in one direction or the other.
5. 32 feet is exactly one throw step shorter than the thrower who wears Cameron of Erracht, with no best throw in between.
6. The thrower who wears Mackenzie weathered is exactly one throw step shorter than Duncan Rait, with no best throw in between.
7. The thrower who wears Lamont ancient and Angus Dunbar are exactly one throw step apart in best throw order, in one direction or the other.

## Solving chart

*Best throw vs Thrower*

| | Fiona Strachan | Duncan Rait | Angus Dunbar | Isla Kinnear | Lachlan Cree |
|---|---|---|---|---|---|
| **28 feet** | | | | | |
| **32 feet** | | | | | |
| **36 feet** | | | | | |
| **40 feet** | | | | | |
| **44 feet** | | | | | |

*Best throw vs Tartan*

| | Mackenzie weathered | Buchanan | Cameron of Erracht | Fraser hunting | Lamont ancient |
|---|---|---|---|---|---|
| **28 feet** | | | | | |
| **32 feet** | | | | | |
| **36 feet** | | | | | |
| **40 feet** | | | | | |
| **44 feet** | | | | | |

*Thrower vs Tartan*

| | Mackenzie weathered | Buchanan | Cameron of Erracht | Fraser hunting | Lamont ancient |
|---|---|---|---|---|---|
| **Fiona Strachan** | | | | | |
| **Duncan Rait** | | | | | |
| **Angus Dunbar** | | | | | |
| **Isla Kinnear** | | | | | |
| **Lachlan Cree** | | | | | |

## Solution

| Best throw | Thrower | Tartan |
|---|---|---|
| 28 feet | Isla Kinnear | Lamont ancient |
| 32 feet | Angus Dunbar | Buchanan |
| 36 feet | Lachlan Cree | Cameron of Erracht |
| 40 feet | Fiona Strachan | Mackenzie weathered |
| 44 feet | Duncan Rait | Fraser hunting |

## How it falls out

1. [direct] from clue 6 thrower:Fiona Strachan: ruled out position(s) 3
2. [direct] from clue 2 thrower:Isla Kinnear: ruled out position(s) 2,3,4,5
3. [direct] from clue 8 tartan:Lamont ancient: ruled out position(s) 2,3,4,5
4. [bijection] tartan:Mackenzie weathered: ruled out position(s) 1
5. [bijection] tartan:Buchanan: ruled out position(s) 1
6. [bijection] tartan:Cameron of Erracht: ruled out position(s) 1
7. [bijection] tartan:Fraser hunting: ruled out position(s) 1
8. [bijection] thrower:Fiona Strachan: ruled out position(s) 1
9. [bijection] thrower:Duncan Rait: ruled out position(s) 1
10. [bijection] thrower:Angus Dunbar: ruled out position(s) 1
11. [bijection] thrower:Lachlan Cree: ruled out position(s) 1
12. [order] from clue 7 tartan:Mackenzie weathered: ruled out position(s) 2
13. [order] from clue 5 thrower:Angus Dunbar: ruled out position(s) 3,4,5
14. [order] from clue 4 tartan:Mackenzie weathered: ruled out position(s) 5
15. [order] from clue 4 thrower:Duncan Rait: ruled out position(s) 2,3
16. [order] from clue 3 tartan:Cameron of Erracht: ruled out position(s) 2,4,5
17. [order] from clue 1 tartan:Fraser hunting: ruled out position(s) 2
18. [bijection] tartan:Mackenzie weathered: ruled out position(s) 3
19. [bijection] tartan:Buchanan: ruled out position(s) 3
20. [bijection] tartan:Fraser hunting: ruled out position(s) 3
21. [bijection] tartan:Buchanan: ruled out position(s) 4,5
22. [bijection] thrower:Fiona Strachan: ruled out position(s) 2
23. [bijection] thrower:Lachlan Cree: ruled out position(s) 2
24. [bijection] thrower:Lachlan Cree: ruled out position(s) 4,5
25. [order] from clue 4 thrower:Duncan Rait: ruled out position(s) 4
26. [bijection] tartan:Fraser hunting: ruled out position(s) 4
27. [bijection] thrower:Fiona Strachan: ruled out position(s) 5

---

<sub>seed `2026172886308` &middot; score 4.62 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
