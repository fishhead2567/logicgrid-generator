# The Hollow Creek Pie Judging

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `fdac0fe2797e`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Five bakers are involved. Determine each baker's placing, filling and crust.
- **Baker**: Odette, Bramwell, Thaddeus, Caspian and Marigold.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Filling**: blackberry, green tomato, mincemeat, pecan and rhubarb.
- **Crust**: a braided edge, a double crust, a fork-crimped edge, a crumb topping and a lattice top.
Every baker has a different placing, filling and crust, so within each category every item is used exactly once.

## Clues

1. Second is exactly one place better than Bramwell, with no placing in between. Bramwell uses a braided edge.
2. Caspian places first.
3. The baker who uses a double crust falls somewhere between fifth and first in placing order.
4. The baker who uses a crumb topping is worse than third in placing order. The baker who bakes rhubarb and third are exactly one place apart in placing order, in one direction or the other.
5. Marigold is better than third in placing order.
6. The baker who uses a fork-crimped edge is better than the baker who bakes mincemeat in placing order. Odette and the baker who bakes mincemeat are exactly two places apart in placing order.
7. Caspian and the baker who bakes blackberry are exactly two places apart in placing order.
8. The baker who uses a crumb topping falls somewhere between the baker who bakes blackberry and the baker who bakes pecan in placing order.

## Solving chart

*Placing vs Baker*

| | Odette | Bramwell | Thaddeus | Caspian | Marigold |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Filling*

| | blackberry | green tomato | mincemeat | pecan | rhubarb |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Crust*

| | a braided edge | a double crust | a fork-crimped edge | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Baker vs Filling*

| | blackberry | green tomato | mincemeat | pecan | rhubarb |
|---|---|---|---|---|---|
| **Odette** | | | | | |
| **Bramwell** | | | | | |
| **Thaddeus** | | | | | |
| **Caspian** | | | | | |
| **Marigold** | | | | | |

*Baker vs Crust*

| | a braided edge | a double crust | a fork-crimped edge | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **Odette** | | | | | |
| **Bramwell** | | | | | |
| **Thaddeus** | | | | | |
| **Caspian** | | | | | |
| **Marigold** | | | | | |

*Filling vs Crust*

| | a braided edge | a double crust | a fork-crimped edge | a crumb topping | a lattice top |
|---|---|---|---|---|---|
| **blackberry** | | | | | |
| **green tomato** | | | | | |
| **mincemeat** | | | | | |
| **pecan** | | | | | |
| **rhubarb** | | | | | |

## Solution

| Placing | Baker | Filling | Crust |
|---|---|---|---|
| first | Caspian | green tomato | a fork-crimped edge |
| second | Marigold | mincemeat | a double crust |
| third | Bramwell | blackberry | a braided edge |
| fourth | Odette | rhubarb | a crumb topping |
| fifth | Thaddeus | pecan | a lattice top |

## How it falls out

1. [direct] from clue 3 baker:Caspian: ruled out position(s) 2,3,4,5
2. [bijection] baker:Odette: ruled out position(s) 1
3. [bijection] baker:Bramwell: ruled out position(s) 1
4. [bijection] baker:Thaddeus: ruled out position(s) 1
5. [bijection] baker:Marigold: ruled out position(s) 1
6. [direct] from clue 4 crust:a braided edge: ruled out position(s) 1
7. [order] from clue 11 filling:rhubarb: ruled out position(s) 1,3,5
8. [order] from clue 10 crust:a fork-crimped edge: ruled out position(s) 5
9. [order] from clue 10 filling:mincemeat: ruled out position(s) 1
10. [order] from clue 9 baker:Bramwell: ruled out position(s) 2,4,5
11. [order] from clue 8 crust:a crumb topping: ruled out position(s) 1,5
12. [order] from clue 7 filling:blackberry: ruled out position(s) 1,2,4,5
13. [order] from clue 8 crust:a crumb topping: ruled out position(s) 3
14. [order] from clue 8 filling:pecan: ruled out position(s) 2,3,4
15. [order] from clue 6 baker:Marigold: ruled out position(s) 3,4,5
16. [order] from clue 5 crust:a double crust: ruled out position(s) 1,5
17. [order] from clue 1 crust:a crumb topping: ruled out position(s) 2
18. [order] from clue 8 filling:pecan: ruled out position(s) 1
19. [direct] from clue 4 crust:a braided edge: ruled out position(s) 2,4,5
20. [bijection] baker:Odette: ruled out position(s) 2,3
21. [bijection] baker:Thaddeus: ruled out position(s) 2,3
22. [bijection] crust:a double crust: ruled out position(s) 3,4
23. [bijection] crust:a fork-crimped edge: ruled out position(s) 3,4
24. [bijection] crust:a lattice top: ruled out position(s) 3,4
25. [bijection] crust:a lattice top: ruled out position(s) 1,2
26. [bijection] filling:green tomato: ruled out position(s) 3,5
27. [bijection] filling:mincemeat: ruled out position(s) 3,5
28. [bijection] filling:green tomato: ruled out position(s) 2,4
29. [order] from clue 2 baker:Odette: ruled out position(s) 5
30. [order] from clue 2 filling:mincemeat: ruled out position(s) 4
31. [order] from clue 10 crust:a fork-crimped edge: ruled out position(s) 2
32. [bijection] baker:Thaddeus: ruled out position(s) 4
33. [bijection] filling:rhubarb: ruled out position(s) 2

---

<sub>seed `2026172905090` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
