# Plot Wars on the Ashcombe Allotments

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `2f5ecd966970`

## Introduction

The Ashcombe allotment committee has been locked in a slow war over compost, shade and the correct way to stake a bean.
Five plot-holders are involved. Determine each plot-holder's placing and crop.
- **Plot-holder**: Obadiah, Senga, Kasimir, Philippa and Ewan.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Prize crop**: a rhubarb crown, a runner bean, a bed of beetroot, a row of leeks and a pumpkin.
Every plot-holder has a different placing and crop, so within each category every item is used exactly once.

## Clues

1. Kasimir places first. Ewan and first are exactly one place apart in placing order, in one direction or the other.
2. Kasimir grows a pumpkin.
3. The plot-holder who grows a runner bean does not place second. The plot-holder who grows a bed of beetroot does not place second.
4. The plot-holder who grows a rhubarb crown is better than fifth in placing order. Senga is better than the plot-holder who grows a rhubarb crown in placing order.
5. The plot-holder who grows a runner bean is better than fourth in placing order.
6. The plot-holder who grows a rhubarb crown and Philippa are exactly one place apart in placing order, in one direction or the other.

## Solving chart

*Placing vs Plot-holder*

| | Obadiah | Senga | Kasimir | Philippa | Ewan |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Prize crop*

| | a rhubarb crown | a runner bean | a bed of beetroot | a row of leeks | a pumpkin |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Plot-holder vs Prize crop*

| | a rhubarb crown | a runner bean | a bed of beetroot | a row of leeks | a pumpkin |
|---|---|---|---|---|---|
| **Obadiah** | | | | | |
| **Senga** | | | | | |
| **Kasimir** | | | | | |
| **Philippa** | | | | | |
| **Ewan** | | | | | |

## Solution

| Placing | Plot-holder | Prize crop |
|---|---|---|
| first | Kasimir | a pumpkin |
| second | Ewan | a row of leeks |
| third | Senga | a runner bean |
| fourth | Obadiah | a rhubarb crown |
| fifth | Philippa | a bed of beetroot |

## How it falls out

1. [direct] from clue 9 crop:a bed of beetroot: ruled out position(s) 2
2. [direct] from clue 6 crop:a runner bean: ruled out position(s) 2
3. [direct] from clue 3 holder:Kasimir: ruled out position(s) 2,3,4,5
4. [direct] from clue 2 crop:a pumpkin: ruled out position(s) 2,3,4,5
5. [bijection] crop:a rhubarb crown: ruled out position(s) 1
6. [bijection] crop:a runner bean: ruled out position(s) 1
7. [bijection] crop:a bed of beetroot: ruled out position(s) 1
8. [bijection] crop:a row of leeks: ruled out position(s) 1
9. [bijection] holder:Obadiah: ruled out position(s) 1
10. [bijection] holder:Senga: ruled out position(s) 1
11. [bijection] holder:Philippa: ruled out position(s) 1
12. [bijection] holder:Ewan: ruled out position(s) 1
13. [order] from clue 8 holder:Senga: ruled out position(s) 5
14. [order] from clue 8 crop:a rhubarb crown: ruled out position(s) 2
15. [order] from clue 7 crop:a runner bean: ruled out position(s) 4,5
16. [order] from clue 4 crop:a rhubarb crown: ruled out position(s) 5
17. [order] from clue 8 holder:Senga: ruled out position(s) 4
18. [order] from clue 1 holder:Ewan: ruled out position(s) 3,4,5
19. [bijection] crop:a rhubarb crown: ruled out position(s) 3
20. [bijection] crop:a bed of beetroot: ruled out position(s) 3
21. [bijection] crop:a row of leeks: ruled out position(s) 3
22. [bijection] crop:a row of leeks: ruled out position(s) 4,5
23. [bijection] holder:Obadiah: ruled out position(s) 2
24. [bijection] holder:Senga: ruled out position(s) 2
25. [bijection] holder:Philippa: ruled out position(s) 2
26. [order] from clue 5 holder:Philippa: ruled out position(s) 4
27. [bijection] crop:a bed of beetroot: ruled out position(s) 4
28. [bijection] holder:Obadiah: ruled out position(s) 3
29. [bijection] holder:Philippa: ruled out position(s) 3
30. [bijection] holder:Obadiah: ruled out position(s) 5

---

<sub>seed `2026172786305` &middot; score 4.62 &middot; atoms 9 &middot; positives 2 &middot; solved by order</sub>
