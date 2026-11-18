# The Hollow Creek Pie Judging

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `7592df768a12`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Four bakers are involved. Determine each baker's placing, county and crust.
- **Baker**: Winnie, Odette, Loretta and Caspian.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Home county**: Hobbs Bend, Fenwick, Quarry Hill and Ardmore.
- **Crust**: a fork-crimped edge, a fluted rim, a crumb topping and a double crust.
Every baker has a different placing, county and crust, so within each category every item is used exactly once.

## Clues

1. The baker who uses a fluted rim places third.
2. First is exactly one place better than the baker who comes from Hobbs Bend, with no placing in between.
3. The baker who uses a crumb topping and second are exactly one place apart in placing order, in one direction or the other.
4. Loretta is better than the baker who comes from Fenwick in placing order.
5. Winnie is exactly one place better than the baker who comes from Quarry Hill, with no placing in between.
6. The baker who uses a fork-crimped edge is exactly one place better than Odette, with no placing in between.

## Solving chart

*Placing vs Baker*

| | Winnie | Odette | Loretta | Caspian |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Home county*

| | Hobbs Bend | Fenwick | Quarry Hill | Ardmore |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Crust*

| | a fork-crimped edge | a fluted rim | a crumb topping | a double crust |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Baker vs Home county*

| | Hobbs Bend | Fenwick | Quarry Hill | Ardmore |
|---|---|---|---|---|
| **Winnie** | | | | |
| **Odette** | | | | |
| **Loretta** | | | | |
| **Caspian** | | | | |

*Baker vs Crust*

| | a fork-crimped edge | a fluted rim | a crumb topping | a double crust |
|---|---|---|---|---|
| **Winnie** | | | | |
| **Odette** | | | | |
| **Loretta** | | | | |
| **Caspian** | | | | |

*Home county vs Crust*

| | a fork-crimped edge | a fluted rim | a crumb topping | a double crust |
|---|---|---|---|---|
| **Hobbs Bend** | | | | |
| **Fenwick** | | | | |
| **Quarry Hill** | | | | |
| **Ardmore** | | | | |

## Solution

| Placing | Baker | Home county | Crust |
|---|---|---|---|
| first | Loretta | Ardmore | a crumb topping |
| second | Winnie | Hobbs Bend | a fork-crimped edge |
| third | Odette | Quarry Hill | a fluted rim |
| fourth | Caspian | Fenwick | a double crust |

## How it falls out

1. [direct] from clue 5 crust:a fluted rim: ruled out position(s) 1,2,4
2. [bijection] crust:a fork-crimped edge: ruled out position(s) 3
3. [bijection] crust:a crumb topping: ruled out position(s) 3
4. [bijection] crust:a double crust: ruled out position(s) 3
5. [order] from clue 6 crust:a fork-crimped edge: ruled out position(s) 4
6. [order] from clue 6 baker:Odette: ruled out position(s) 1,4
7. [order] from clue 4 baker:Winnie: ruled out position(s) 4
8. [order] from clue 4 county:Quarry Hill: ruled out position(s) 1
9. [order] from clue 3 crust:a crumb topping: ruled out position(s) 2,4
10. [order] from clue 2 baker:Loretta: ruled out position(s) 4
11. [order] from clue 2 county:Fenwick: ruled out position(s) 1
12. [order] from clue 1 county:Hobbs Bend: ruled out position(s) 1,3,4
13. [bijection] baker:Caspian: ruled out position(s) 1,2,3
14. [bijection] county:Fenwick: ruled out position(s) 2
15. [bijection] county:Quarry Hill: ruled out position(s) 2
16. [bijection] county:Ardmore: ruled out position(s) 2
17. [bijection] county:Ardmore: ruled out position(s) 3,4
18. [bijection] crust:a fork-crimped edge: ruled out position(s) 1
19. [bijection] crust:a double crust: ruled out position(s) 1
20. [bijection] crust:a double crust: ruled out position(s) 2
21. [order] from clue 6 baker:Odette: ruled out position(s) 2
22. [order] from clue 4 baker:Winnie: ruled out position(s) 1
23. [bijection] baker:Winnie: ruled out position(s) 3
24. [bijection] baker:Loretta: ruled out position(s) 3
25. [bijection] baker:Loretta: ruled out position(s) 2
26. [order] from clue 4 county:Quarry Hill: ruled out position(s) 4
27. [bijection] county:Fenwick: ruled out position(s) 3

---

<sub>seed `2026172710059` &middot; score 5.13 &middot; atoms 6 &middot; positives 1 &middot; solved by order</sub>
