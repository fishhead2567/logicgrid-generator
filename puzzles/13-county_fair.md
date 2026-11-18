# The Hollow Creek Pie Judging

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `dc4abc9a5a35`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Four bakers are involved. Determine each baker's placing, filling and county.
- **Baker**: Bramwell, Odette, Thaddeus and Winnie.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Filling**: green tomato, rhubarb, buttermilk and sour cherry.
- **Home county**: Fenwick, Sweetwater, Quarry Hill and Hobbs Bend.
Every baker has a different placing, filling and county, so within each category every item is used exactly once.

## Clues

1. Bramwell falls somewhere between first and third in placing order. The baker who bakes rhubarb places first.
2. The baker who comes from Sweetwater is exactly one place better than fourth, with no placing in between. Winnie falls somewhere between first and fourth in placing order.
3. The baker who comes from Hobbs Bend and second are exactly one place apart in placing order, in one direction or the other.
4. The baker who bakes green tomato and third are exactly one place apart in placing order, in one direction or the other.
5. The baker who comes from Quarry Hill falls somewhere between Odette and Thaddeus in placing order.
6. Thaddeus is better than the baker who comes from Quarry Hill in placing order.
7. The baker who bakes sour cherry is exactly one place better than the baker who comes from Sweetwater, with no placing in between.

## Solving chart

*Placing vs Baker*

| | Bramwell | Odette | Thaddeus | Winnie |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Filling*

| | green tomato | rhubarb | buttermilk | sour cherry |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Home county*

| | Fenwick | Sweetwater | Quarry Hill | Hobbs Bend |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Baker vs Filling*

| | green tomato | rhubarb | buttermilk | sour cherry |
|---|---|---|---|---|
| **Bramwell** | | | | |
| **Odette** | | | | |
| **Thaddeus** | | | | |
| **Winnie** | | | | |

*Baker vs Home county*

| | Fenwick | Sweetwater | Quarry Hill | Hobbs Bend |
|---|---|---|---|---|
| **Bramwell** | | | | |
| **Odette** | | | | |
| **Thaddeus** | | | | |
| **Winnie** | | | | |

*Filling vs Home county*

| | Fenwick | Sweetwater | Quarry Hill | Hobbs Bend |
|---|---|---|---|---|
| **green tomato** | | | | |
| **rhubarb** | | | | |
| **buttermilk** | | | | |
| **sour cherry** | | | | |

## Solution

| Placing | Baker | Filling | Home county |
|---|---|---|---|
| first | Thaddeus | rhubarb | Hobbs Bend |
| second | Bramwell | sour cherry | Quarry Hill |
| third | Winnie | buttermilk | Sweetwater |
| fourth | Odette | green tomato | Fenwick |

## How it falls out

1. [direct] from clue 4 filling:rhubarb: ruled out position(s) 2,3,4
2. [bijection] filling:green tomato: ruled out position(s) 1
3. [bijection] filling:buttermilk: ruled out position(s) 1
4. [bijection] filling:sour cherry: ruled out position(s) 1
5. [order] from clue 9 baker:Thaddeus: ruled out position(s) 4
6. [order] from clue 9 county:Quarry Hill: ruled out position(s) 1
7. [order] from clue 8 filling:sour cherry: ruled out position(s) 4
8. [order] from clue 8 county:Sweetwater: ruled out position(s) 1,2
9. [order] from clue 7 county:Hobbs Bend: ruled out position(s) 2,4
10. [order] from clue 6 filling:green tomato: ruled out position(s) 3
11. [order] from clue 5 county:Sweetwater: ruled out position(s) 4
12. [order] from clue 8 filling:sour cherry: ruled out position(s) 3
13. [order] from clue 3 baker:Winnie: ruled out position(s) 1,4
14. [order] from clue 2 county:Quarry Hill: ruled out position(s) 4
15. [order] from clue 2 baker:Odette: ruled out position(s) 2
16. [order] from clue 9 baker:Thaddeus: ruled out position(s) 3
17. [order] from clue 2 baker:Odette: ruled out position(s) 1
18. [order] from clue 1 baker:Bramwell: ruled out position(s) 1,3,4
19. [bijection] baker:Thaddeus: ruled out position(s) 2
20. [bijection] baker:Winnie: ruled out position(s) 2
21. [bijection] baker:Odette: ruled out position(s) 3
22. [bijection] county:Fenwick: ruled out position(s) 3
23. [bijection] county:Quarry Hill: ruled out position(s) 3
24. [bijection] county:Hobbs Bend: ruled out position(s) 3
25. [bijection] county:Fenwick: ruled out position(s) 1,2
26. [bijection] filling:green tomato: ruled out position(s) 2
27. [bijection] filling:buttermilk: ruled out position(s) 2
28. [bijection] filling:buttermilk: ruled out position(s) 4

---

<sub>seed `2026172678383` &middot; score 5.13 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
