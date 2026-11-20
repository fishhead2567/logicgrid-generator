# The Hollow Creek Pie Judging

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `a08194eea68e`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Five bakers are involved. Determine each baker's placing, county and crust.
- **Baker**: Bramwell, Thaddeus, Odette, Winnie and Marigold.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Home county**: Little Pell, Ardmore, Fenwick, Quarry Hill and Sweetwater.
- **Crust**: a double crust, a crumb topping, a fluted rim, a cut-out star top and a braided edge.
Every baker has a different placing, county and crust, so within each category every item is used exactly once.

## Clues

1. The baker who uses a crumb topping places third.
2. Odette and second are exactly one place apart in placing order, in one direction or the other. Thaddeus and second are exactly one place apart in placing order, in one direction or the other.
3. The baker who comes from Fenwick and second are exactly one place apart in placing order, in one direction or the other.
4. The baker who comes from Sweetwater and fourth are exactly one place apart in placing order, in one direction or the other. Thaddeus does not come from Sweetwater.
5. The baker who comes from Quarry Hill is worse than fourth in placing order.
6. Bramwell and the baker who uses a cut-out star top are exactly one place apart in placing order, in one direction or the other.
7. The baker who comes from Little Pell is exactly one place better than the baker who uses a cut-out star top, with no placing in between.
8. The baker who uses a double crust is better than Winnie in placing order.
9. Thaddeus and the baker who uses a double crust are exactly one place apart in placing order, in one direction or the other.
10. The baker who comes from Fenwick does not use a fluted rim.

## Solving chart

*Placing vs Baker*

| | Bramwell | Thaddeus | Odette | Winnie | Marigold |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Home county*

| | Little Pell | Ardmore | Fenwick | Quarry Hill | Sweetwater |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Crust*

| | a double crust | a crumb topping | a fluted rim | a cut-out star top | a braided edge |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Baker vs Home county*

| | Little Pell | Ardmore | Fenwick | Quarry Hill | Sweetwater |
|---|---|---|---|---|---|
| **Bramwell** | | | | | |
| **Thaddeus** | | | | | |
| **Odette** | | | | | |
| **Winnie** | | | | | |
| **Marigold** | | | | | |

*Baker vs Crust*

| | a double crust | a crumb topping | a fluted rim | a cut-out star top | a braided edge |
|---|---|---|---|---|---|
| **Bramwell** | | | | | |
| **Thaddeus** | | | | | |
| **Odette** | | | | | |
| **Winnie** | | | | | |
| **Marigold** | | | | | |

*Home county vs Crust*

| | a double crust | a crumb topping | a fluted rim | a cut-out star top | a braided edge |
|---|---|---|---|---|---|
| **Little Pell** | | | | | |
| **Ardmore** | | | | | |
| **Fenwick** | | | | | |
| **Quarry Hill** | | | | | |
| **Sweetwater** | | | | | |

## Solution

| Placing | Baker | Home county | Crust |
|---|---|---|---|
| first | Thaddeus | Fenwick | a braided edge |
| second | Marigold | Ardmore | a double crust |
| third | Odette | Sweetwater | a crumb topping |
| fourth | Bramwell | Little Pell | a fluted rim |
| fifth | Winnie | Quarry Hill | a cut-out star top |

## How it falls out

1. [direct] from clue 1 crust:a crumb topping: ruled out position(s) 1,2,4,5
2. [bijection] crust:a double crust: ruled out position(s) 3
3. [bijection] crust:a fluted rim: ruled out position(s) 3
4. [bijection] crust:a cut-out star top: ruled out position(s) 3
5. [bijection] crust:a braided edge: ruled out position(s) 3
6. [order] from clue 10 baker:Odette: ruled out position(s) 2,4,5
7. [order] from clue 9 county:Quarry Hill: ruled out position(s) 1,2,3,4
8. [order] from clue 6 baker:Thaddeus: ruled out position(s) 2,4,5
9. [order] from clue 11 crust:a double crust: ruled out position(s) 1,5
10. [order] from clue 5 baker:Winnie: ruled out position(s) 1,2
11. [order] from clue 4 county:Little Pell: ruled out position(s) 2,5
12. [order] from clue 4 crust:a cut-out star top: ruled out position(s) 1
13. [order] from clue 8 baker:Bramwell: ruled out position(s) 2
14. [order] from clue 3 county:Fenwick: ruled out position(s) 2,4,5
15. [order] from clue 2 county:Sweetwater: ruled out position(s) 1,2,4
16. [bijection] baker:Marigold: ruled out position(s) 1,3,4,5
17. [bijection] county:Ardmore: ruled out position(s) 5
18. [bijection] county:Sweetwater: ruled out position(s) 5
19. [bijection] county:Ardmore: ruled out position(s) 1,3,4
20. [direct] from clue 12 baker:Thaddeus: ruled out position(s) 3
21. [order] from clue 11 crust:a double crust: ruled out position(s) 4
22. [bijection] baker:Bramwell: ruled out position(s) 1
23. [bijection] baker:Odette: ruled out position(s) 1
24. [bijection] county:Little Pell: ruled out position(s) 3
25. [bijection] county:Fenwick: ruled out position(s) 3
26. [bijection] county:Little Pell: ruled out position(s) 1
27. [bijection] crust:a fluted rim: ruled out position(s) 2
28. [bijection] crust:a cut-out star top: ruled out position(s) 2
29. [bijection] crust:a braided edge: ruled out position(s) 2
30. [direct] from clue 7 crust:a fluted rim: ruled out position(s) 1
31. [order] from clue 4 crust:a cut-out star top: ruled out position(s) 4
32. [order] from clue 8 baker:Bramwell: ruled out position(s) 3,5
33. [bijection] baker:Winnie: ruled out position(s) 3,4
34. [bijection] crust:a fluted rim: ruled out position(s) 5
35. [bijection] crust:a braided edge: ruled out position(s) 5
36. [bijection] crust:a braided edge: ruled out position(s) 4

---

<sub>seed `2026173025906` &middot; score 5.515 &middot; atoms 12 &middot; positives 1 &middot; solved by order</sub>
