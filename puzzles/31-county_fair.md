# The Hollow Creek Pie Judging

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 12 &nbsp;&nbsp; **id** `839c46297d44`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Five bakers are involved. Determine each baker's placing, filling, county and crust.
- **Baker**: Odette, Bramwell, Marigold, Winnie and Thaddeus.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Filling**: pecan, green tomato, rhubarb, mincemeat and sour cherry.
- **Home county**: Quarry Hill, Little Pell, Fenwick, Dunmore and Hobbs Bend.
- **Crust**: a cut-out star top, a fork-crimped edge, a fluted rim, a crumb topping and a lattice top.
Every baker has a different placing, filling, county and crust, so within each category every item is used exactly once.

## Clues

1. The baker who uses a fork-crimped edge is worse than third in placing order.
2. Odette and the baker who bakes pecan are exactly four places apart in placing order.
3. The baker who uses a cut-out star top does not bake green tomato. Thaddeus is exactly one place better than the baker who uses a cut-out star top, with no placing in between.
4. The baker who comes from Fenwick is exactly one place better than the baker who bakes sour cherry, with no placing in between.
5. The baker who comes from Quarry Hill falls somewhere between Winnie and the baker who uses a lattice top in placing order.
6. Bramwell and the baker who uses a crumb topping are exactly three places apart in placing order.
7. Winnie and the baker who bakes rhubarb are exactly one place apart in placing order, in one direction or the other.
8. Thaddeus is better than the baker who uses a lattice top in placing order.
9. At least one of the following holds, and possibly more than one: (a) Marigold comes from Quarry Hill. (b) The baker who comes from Hobbs Bend and the baker who bakes sour cherry both sit at odd-numbered places or both at even-numbered places.
10. The baker who bakes sour cherry is exactly one place better than the baker who comes from Dunmore, with no placing in between.
11. Thaddeus and the baker who bakes mincemeat are exactly four places apart in placing order.
12. Bramwell is exactly one place better than the baker who comes from Dunmore, with no placing in between.

## Solving chart

*Placing vs Baker*

| | Odette | Bramwell | Marigold | Winnie | Thaddeus |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Filling*

| | pecan | green tomato | rhubarb | mincemeat | sour cherry |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Home county*

| | Quarry Hill | Little Pell | Fenwick | Dunmore | Hobbs Bend |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Crust*

| | a cut-out star top | a fork-crimped edge | a fluted rim | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Baker vs Filling*

| | pecan | green tomato | rhubarb | mincemeat | sour cherry |
|---|---|---|---|---|---|
| **Odette** | | | | | |
| **Bramwell** | | | | | |
| **Marigold** | | | | | |
| **Winnie** | | | | | |
| **Thaddeus** | | | | | |

*Baker vs Home county*

| | Quarry Hill | Little Pell | Fenwick | Dunmore | Hobbs Bend |
|---|---|---|---|---|---|
| **Odette** | | | | | |
| **Bramwell** | | | | | |
| **Marigold** | | | | | |
| **Winnie** | | | | | |
| **Thaddeus** | | | | | |

*Baker vs Crust*

| | a cut-out star top | a fork-crimped edge | a fluted rim | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **Odette** | | | | | |
| **Bramwell** | | | | | |
| **Marigold** | | | | | |
| **Winnie** | | | | | |
| **Thaddeus** | | | | | |

*Filling vs Home county*

| | Quarry Hill | Little Pell | Fenwick | Dunmore | Hobbs Bend |
|---|---|---|---|---|---|
| **pecan** | | | | | |
| **green tomato** | | | | | |
| **rhubarb** | | | | | |
| **mincemeat** | | | | | |
| **sour cherry** | | | | | |

*Filling vs Crust*

| | a cut-out star top | a fork-crimped edge | a fluted rim | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **pecan** | | | | | |
| **green tomato** | | | | | |
| **rhubarb** | | | | | |
| **mincemeat** | | | | | |
| **sour cherry** | | | | | |

*Home county vs Crust*

| | a cut-out star top | a fork-crimped edge | a fluted rim | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **Quarry Hill** | | | | | |
| **Little Pell** | | | | | |
| **Fenwick** | | | | | |
| **Dunmore** | | | | | |
| **Hobbs Bend** | | | | | |

## Solution

| Placing | Baker | Filling | Home county | Crust |
|---|---|---|---|---|
| first | Thaddeus | pecan | Little Pell | a crumb topping |
| second | Marigold | rhubarb | Hobbs Bend | a cut-out star top |
| third | Winnie | green tomato | Fenwick | a fluted rim |
| fourth | Bramwell | sour cherry | Quarry Hill | a fork-crimped edge |
| fifth | Odette | mincemeat | Dunmore | a lattice top |

## How it falls out

1. [order] from clue 13 baker:Odette: ruled out position(s) 2,3,4
2. [order] from clue 13 filling:pecan: ruled out position(s) 2,3,4
3. [order] from clue 11 baker:Thaddeus: ruled out position(s) 5
4. [order] from clue 11 crust:a cut-out star top: ruled out position(s) 1
5. [order] from clue 9 filling:sour cherry: ruled out position(s) 5
6. [order] from clue 9 county:Dunmore: ruled out position(s) 1
7. [order] from clue 8 baker:Thaddeus: ruled out position(s) 2,3,4
8. [order] from clue 8 filling:mincemeat: ruled out position(s) 1,2,3,4
9. [order] from clue 11 crust:a cut-out star top: ruled out position(s) 3,4,5
10. [order] from clue 7 county:Fenwick: ruled out position(s) 4,5
11. [order] from clue 7 filling:sour cherry: ruled out position(s) 1
12. [order] from clue 9 county:Dunmore: ruled out position(s) 2
13. [order] from clue 6 baker:Bramwell: ruled out position(s) 3
14. [order] from clue 6 crust:a crumb topping: ruled out position(s) 3
15. [order] from clue 5 baker:Bramwell: ruled out position(s) 1,5
16. [order] from clue 5 county:Dunmore: ruled out position(s) 4
17. [order] from clue 9 filling:sour cherry: ruled out position(s) 3
18. [order] from clue 7 county:Fenwick: ruled out position(s) 2
19. [order] from clue 6 crust:a crumb topping: ruled out position(s) 2,4
20. [order] from clue 4 crust:a fork-crimped edge: ruled out position(s) 1,2,3
21. [order] from clue 2 crust:a lattice top: ruled out position(s) 1
22. [order] from clue 1 county:Quarry Hill: ruled out position(s) 1,5
23. [direct] from clue 3 filling:green tomato: ruled out position(s) 2
24. [bijection] baker:Odette: ruled out position(s) 1
25. [bijection] baker:Marigold: ruled out position(s) 1
26. [bijection] baker:Winnie: ruled out position(s) 1
27. [bijection] crust:a fluted rim: ruled out position(s) 2
28. [bijection] crust:a lattice top: ruled out position(s) 2
29. [bijection] filling:pecan: ruled out position(s) 5
30. [bijection] filling:green tomato: ruled out position(s) 5
31. [bijection] filling:rhubarb: ruled out position(s) 5
32. [order] from clue 1 county:Quarry Hill: ruled out position(s) 2
33. [order] from clue 1 baker:Winnie: ruled out position(s) 4
34. [bijection] baker:Marigold: ruled out position(s) 5
35. [bijection] baker:Winnie: ruled out position(s) 5
36. [bijection] filling:green tomato: ruled out position(s) 1
37. [bijection] filling:rhubarb: ruled out position(s) 1
38. [order] from clue 1 crust:a lattice top: ruled out position(s) 3
39. [bijection] crust:a fluted rim: ruled out position(s) 1,4,5
40. [bijection] crust:a crumb topping: ruled out position(s) 5
_... and 19 further steps._

---

<sub>seed `2026173135112` &middot; score 9.3142 &middot; atoms 13 &middot; positives 0 &middot; solved by disjunction</sub>
