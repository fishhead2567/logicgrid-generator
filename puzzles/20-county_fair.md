# The Hollow Creek Pie Judging

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `e5bb8c381851`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Five bakers are involved. Determine each baker's placing, filling and crust.
- **Baker**: Marigold, Bramwell, Winnie, Odette and Caspian.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Filling**: mincemeat, green tomato, sour cherry, pecan and blackberry.
- **Crust**: a crumb topping, a braided edge, a fluted rim, a fork-crimped edge and a cut-out star top.
Every baker has a different placing, filling and crust, so within each category every item is used exactly once.

## Clues

1. Odette places second.
2. The baker who bakes pecan places fifth.
3. Winnie and fourth are exactly one place apart in placing order, in one direction or the other. The baker who bakes sour cherry does not place fourth.
4. Marigold and the baker who uses a cut-out star top are exactly two places apart in placing order. Second is exactly one place better than Marigold, with no placing in between.
5. The baker who bakes green tomato is exactly one place better than third, with no placing in between.
6. Third falls somewhere between the baker who uses a fluted rim and the baker who bakes mincemeat in placing order.
7. Caspian does not place first.
8. The baker who bakes sour cherry is exactly one place better than the baker who uses a fork-crimped edge, with no placing in between.
9. The baker who uses a cut-out star top is better than the baker who bakes pecan in placing order.
10. The baker who bakes green tomato is exactly one place better than the baker who uses a crumb topping, with no placing in between.
11. Caspian does not bake blackberry.

## Solving chart

*Placing vs Baker*

| | Marigold | Bramwell | Winnie | Odette | Caspian |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Filling*

| | mincemeat | green tomato | sour cherry | pecan | blackberry |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Crust*

| | a crumb topping | a braided edge | a fluted rim | a fork-crimped edge | a cut-out star top |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Baker vs Filling*

| | mincemeat | green tomato | sour cherry | pecan | blackberry |
|---|---|---|---|---|---|
| **Marigold** | | | | | |
| **Bramwell** | | | | | |
| **Winnie** | | | | | |
| **Odette** | | | | | |
| **Caspian** | | | | | |

*Baker vs Crust*

| | a crumb topping | a braided edge | a fluted rim | a fork-crimped edge | a cut-out star top |
|---|---|---|---|---|---|
| **Marigold** | | | | | |
| **Bramwell** | | | | | |
| **Winnie** | | | | | |
| **Odette** | | | | | |
| **Caspian** | | | | | |

*Filling vs Crust*

| | a crumb topping | a braided edge | a fluted rim | a fork-crimped edge | a cut-out star top |
|---|---|---|---|---|---|
| **mincemeat** | | | | | |
| **green tomato** | | | | | |
| **sour cherry** | | | | | |
| **pecan** | | | | | |
| **blackberry** | | | | | |

## Solution

| Placing | Baker | Filling | Crust |
|---|---|---|---|
| first | Bramwell | blackberry | a cut-out star top |
| second | Odette | green tomato | a fluted rim |
| third | Marigold | sour cherry | a crumb topping |
| fourth | Caspian | mincemeat | a fork-crimped edge |
| fifth | Winnie | pecan | a braided edge |

## How it falls out

1. [direct] from clue 8 baker:Odette: ruled out position(s) 1,3,4,5
2. [direct] from clue 5 filling:sour cherry: ruled out position(s) 4
3. [direct] from clue 4 filling:pecan: ruled out position(s) 1,2,3,4
4. [direct] from clue 1 baker:Caspian: ruled out position(s) 1
5. [bijection] baker:Marigold: ruled out position(s) 2
6. [bijection] baker:Bramwell: ruled out position(s) 2
7. [bijection] baker:Winnie: ruled out position(s) 2
8. [bijection] baker:Caspian: ruled out position(s) 2
9. [bijection] filling:mincemeat: ruled out position(s) 5
10. [bijection] filling:green tomato: ruled out position(s) 5
11. [bijection] filling:sour cherry: ruled out position(s) 5
12. [bijection] filling:blackberry: ruled out position(s) 5
13. [order] from clue 13 crust:a fork-crimped edge: ruled out position(s) 1,5
14. [order] from clue 12 crust:a fluted rim: ruled out position(s) 3
15. [order] from clue 12 filling:mincemeat: ruled out position(s) 3
16. [order] from clue 11 crust:a cut-out star top: ruled out position(s) 4
17. [order] from clue 10 crust:a cut-out star top: ruled out position(s) 5
18. [order] from clue 9 baker:Winnie: ruled out position(s) 1,4
19. [order] from clue 7 crust:a crumb topping: ruled out position(s) 1
20. [order] from clue 3 filling:green tomato: ruled out position(s) 1,3,4
21. [order] from clue 7 crust:a crumb topping: ruled out position(s) 2,4,5
22. [order] from clue 2 baker:Marigold: ruled out position(s) 1,4,5
23. [order] from clue 11 crust:a cut-out star top: ruled out position(s) 2,3
24. [bijection] baker:Bramwell: ruled out position(s) 3
25. [bijection] baker:Winnie: ruled out position(s) 3
26. [bijection] baker:Caspian: ruled out position(s) 3
27. [bijection] baker:Bramwell: ruled out position(s) 4,5
28. [bijection] crust:a braided edge: ruled out position(s) 1,3
29. [bijection] crust:a fluted rim: ruled out position(s) 1
30. [bijection] crust:a fork-crimped edge: ruled out position(s) 3
31. [bijection] filling:mincemeat: ruled out position(s) 2
32. [bijection] filling:sour cherry: ruled out position(s) 2
33. [bijection] filling:blackberry: ruled out position(s) 2
34. [bijection] baker:Caspian: ruled out position(s) 5
35. [direct] from clue 6 filling:blackberry: ruled out position(s) 4
36. [bijection] filling:mincemeat: ruled out position(s) 1
37. [order] from clue 12 crust:a fluted rim: ruled out position(s) 4,5
38. [bijection] crust:a braided edge: ruled out position(s) 2
39. [bijection] crust:a fork-crimped edge: ruled out position(s) 2
40. [bijection] crust:a braided edge: ruled out position(s) 4
_... and 2 further steps._

---

<sub>seed `2026172733816` &middot; score 5.355 &middot; atoms 13 &middot; positives 2 &middot; solved by order</sub>
