# Plot Wars on the Ashcombe Allotments

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `72f1fc6b9311`

## Introduction

The Ashcombe allotment committee has been locked in a slow war over compost, shade and the correct way to stake a bean.
Five plot-holders are involved. Determine each plot-holder's placing and crop.
- **Plot-holder**: Ewan, Senga, Philippa, Kasimir and Obadiah.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Prize crop**: a pumpkin, a row of leeks, a marrow, a runner bean and a bed of beetroot.
Every plot-holder has a different placing and crop, so within each category every item is used exactly once.

## Clues

1. The plot-holder who grows a marrow places fifth.
2. The plot-holder who grows a bed of beetroot places second.
3. Obadiah grows a row of leeks.
4. Senga is exactly one place better than fifth, with no placing in between.
5. The plot-holder who grows a pumpkin and fifth are exactly one place apart in placing order, in one direction or the other.
6. Philippa is better than the plot-holder who grows a runner bean in placing order.
7. The plot-holder who grows a bed of beetroot is exactly one place better than Kasimir, with no placing in between.

## Solving chart

*Placing vs Plot-holder*

| | Ewan | Senga | Philippa | Kasimir | Obadiah |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Prize crop*

| | a pumpkin | a row of leeks | a marrow | a runner bean | a bed of beetroot |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Plot-holder vs Prize crop*

| | a pumpkin | a row of leeks | a marrow | a runner bean | a bed of beetroot |
|---|---|---|---|---|---|
| **Ewan** | | | | | |
| **Senga** | | | | | |
| **Philippa** | | | | | |
| **Kasimir** | | | | | |
| **Obadiah** | | | | | |

## Solution

| Placing | Plot-holder | Prize crop |
|---|---|---|
| first | Obadiah | a row of leeks |
| second | Philippa | a bed of beetroot |
| third | Kasimir | a runner bean |
| fourth | Senga | a pumpkin |
| fifth | Ewan | a marrow |

## How it falls out

1. [direct] from clue 2 crop:a bed of beetroot: ruled out position(s) 1,3,4,5
2. [direct] from clue 1 crop:a marrow: ruled out position(s) 1,2,3,4
3. [bijection] crop:a pumpkin: ruled out position(s) 2,5
4. [bijection] crop:a row of leeks: ruled out position(s) 2,5
5. [bijection] crop:a runner bean: ruled out position(s) 2,5
6. [direct] from clue 3 holder:Obadiah: ruled out position(s) 2,5
7. [order] from clue 7 holder:Philippa: ruled out position(s) 4,5
8. [order] from clue 7 crop:a runner bean: ruled out position(s) 1
9. [order] from clue 6 holder:Senga: ruled out position(s) 1,2,3,5
10. [order] from clue 5 crop:a pumpkin: ruled out position(s) 1,3
11. [order] from clue 4 holder:Kasimir: ruled out position(s) 1,2,4,5
12. [bijection] crop:a row of leeks: ruled out position(s) 4
13. [bijection] crop:a runner bean: ruled out position(s) 4
14. [bijection] crop:a row of leeks: ruled out position(s) 3
15. [bijection] holder:Ewan: ruled out position(s) 3,4
16. [bijection] holder:Philippa: ruled out position(s) 3
17. [bijection] holder:Obadiah: ruled out position(s) 3,4
18. [bijection] holder:Ewan: ruled out position(s) 1,2
19. [bijection] holder:Philippa: ruled out position(s) 1

---

<sub>seed `2026172791280` &middot; score 4.38 &middot; atoms 7 &middot; positives 3 &middot; solved by order</sub>
