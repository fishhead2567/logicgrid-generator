# Plot Wars on the Ashcombe Allotments

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `c37adfb45fd5`

## Introduction

The Ashcombe allotment committee has been locked in a slow war over compost, shade and the correct way to stake a bean.
Four plot-holders are involved. Determine each plot-holder's placing and crop.
- **Plot-holder**: Senga, Alphonse, Ewan and Rosamund.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Prize crop**: a row of leeks, a cauliflower, a pumpkin and a bed of beetroot.
Every plot-holder has a different placing and crop, so within each category every item is used exactly once.

## Clues

1. The plot-holder who grows a cauliflower places second.
2. Rosamund grows a row of leeks.
3. Senga grows a cauliflower.
4. Ewan and fourth are exactly one place apart in placing order, in one direction or the other.
5. The plot-holder who grows a bed of beetroot and Alphonse are exactly one place apart in placing order, in one direction or the other.

## Solving chart

*Placing vs Plot-holder*

| | Senga | Alphonse | Ewan | Rosamund |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Prize crop*

| | a row of leeks | a cauliflower | a pumpkin | a bed of beetroot |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Plot-holder vs Prize crop*

| | a row of leeks | a cauliflower | a pumpkin | a bed of beetroot |
|---|---|---|---|---|
| **Senga** | | | | |
| **Alphonse** | | | | |
| **Ewan** | | | | |
| **Rosamund** | | | | |

## Solution

| Placing | Plot-holder | Prize crop |
|---|---|---|
| first | Rosamund | a row of leeks |
| second | Senga | a cauliflower |
| third | Ewan | a bed of beetroot |
| fourth | Alphonse | a pumpkin |

## How it falls out

1. [direct] from clue 4 crop:a cauliflower: ruled out position(s) 1,3,4
2. [direct] from clue 5 holder:Senga: ruled out position(s) 1,3,4
3. [bijection] crop:a row of leeks: ruled out position(s) 2
4. [bijection] crop:a pumpkin: ruled out position(s) 2
5. [bijection] crop:a bed of beetroot: ruled out position(s) 2
6. [bijection] holder:Alphonse: ruled out position(s) 2
7. [bijection] holder:Ewan: ruled out position(s) 2
8. [bijection] holder:Rosamund: ruled out position(s) 2
9. [order] from clue 2 crop:a bed of beetroot: ruled out position(s) 1
10. [order] from clue 2 holder:Alphonse: ruled out position(s) 1
11. [order] from clue 1 holder:Ewan: ruled out position(s) 1,4
12. [bijection] holder:Alphonse: ruled out position(s) 3
13. [bijection] holder:Rosamund: ruled out position(s) 3
14. [bijection] holder:Rosamund: ruled out position(s) 4
15. [direct] from clue 3 crop:a row of leeks: ruled out position(s) 3,4
16. [order] from clue 2 crop:a bed of beetroot: ruled out position(s) 4
17. [bijection] crop:a pumpkin: ruled out position(s) 1,3

---

<sub>seed `2026172630869` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
