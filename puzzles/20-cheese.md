# The Cheesemongers' Standoff

*A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.*

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `456fd47e5f63`

## Introduction

There are 5 wheels. Each has exactly one price and one item from every other category below, and within each category every item belongs to a different wheel.
- **Price** (listed in order): $3, $5, $7, $9 and $11.
- **Cheese**: Old Thrashing, Saltpans, Bellringer, Fenland Blue and Glebe Farmhouse.
- **Maker**: Hepzibah, Lachlan, Teodoro, Ambrose and Sigrid.
- **Aged for**: two years, five months, nine months, fourteen months and three weeks.
The price steps above are listed in order, from $3 to $11.

## Clues

1. Five months goes with $3.
2. Two years, Lachlan and $9 are three different wheels. Two years, Glebe Farmhouse and $11 are three different wheels. Sigrid's price is immediately cheaper than Glebe Farmhouse's price, with no price in between.
3. $9 is cheaper than Fenland Blue's price.
4. Teodoro falls somewhere between five months and Old Thrashing in price order.
5. Bellringer falls somewhere between fourteen months and two years in price order.
6. Old Thrashing falls somewhere between three weeks and Teodoro in price order.
7. Bellringer and Ambrose are next to each other in price order, in one order or the other.

## Solving chart

*Price vs Cheese*

| | Old Thrashing | Saltpans | Bellringer | Fenland Blue | Glebe Farmhouse |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Maker*

| | Hepzibah | Lachlan | Teodoro | Ambrose | Sigrid |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Aged for*

| | two years | five months | nine months | fourteen months | three weeks |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Cheese vs Maker*

| | Hepzibah | Lachlan | Teodoro | Ambrose | Sigrid |
|---|---|---|---|---|---|
| **Old Thrashing** | | | | | |
| **Saltpans** | | | | | |
| **Bellringer** | | | | | |
| **Fenland Blue** | | | | | |
| **Glebe Farmhouse** | | | | | |

*Cheese vs Aged for*

| | two years | five months | nine months | fourteen months | three weeks |
|---|---|---|---|---|---|
| **Old Thrashing** | | | | | |
| **Saltpans** | | | | | |
| **Bellringer** | | | | | |
| **Fenland Blue** | | | | | |
| **Glebe Farmhouse** | | | | | |

*Maker vs Aged for*

| | two years | five months | nine months | fourteen months | three weeks |
|---|---|---|---|---|---|
| **Hepzibah** | | | | | |
| **Lachlan** | | | | | |
| **Teodoro** | | | | | |
| **Ambrose** | | | | | |
| **Sigrid** | | | | | |

## Solution

| Price | Cheese | Maker | Aged for |
|---|---|---|---|
| $3 | Saltpans | Sigrid | five months |
| $5 | Glebe Farmhouse | Teodoro | nine months |
| $7 | Old Thrashing | Ambrose | two years |
| $9 | Bellringer | Hepzibah | three weeks |
| $11 | Fenland Blue | Lachlan | fourteen months |

## How it falls out

1. [direct] from clue 8 age:five months: ruled out position(s) 2,3,4,5
2. [bijection] from clue 5 age:two years: ruled out position(s) 4
3. [bijection] from clue 5 maker:Lachlan: ruled out position(s) 4
4. [bijection] from clue 3 age:two years: ruled out position(s) 5
5. [bijection] from clue 3 cheese:Glebe Farmhouse: ruled out position(s) 5
6. [bijection] age:two years: ruled out position(s) 1
7. [bijection] age:nine months: ruled out position(s) 1
8. [bijection] age:fourteen months: ruled out position(s) 1
9. [bijection] age:three weeks: ruled out position(s) 1
10. [order] from clue 7 cheese:Fenland Blue: ruled out position(s) 1,2,3,4
11. [order] from clue 6 cheese:Old Thrashing: ruled out position(s) 1,5
12. [order] from clue 4 cheese:Bellringer: ruled out position(s) 1,2,5
13. [order] from clue 4 age:fourteen months: ruled out position(s) 2,3
14. [order] from clue 9 maker:Ambrose: ruled out position(s) 1
15. [order] from clue 2 maker:Teodoro: ruled out position(s) 1,4,5
16. [order] from clue 2 cheese:Old Thrashing: ruled out position(s) 2
17. [order] from clue 6 age:three weeks: ruled out position(s) 2,3
18. [order] from clue 1 maker:Sigrid: ruled out position(s) 4,5
19. [order] from clue 1 cheese:Glebe Farmhouse: ruled out position(s) 1
20. [bijection] cheese:Saltpans: ruled out position(s) 5
21. [bijection] cheese:Saltpans: ruled out position(s) 2,3,4
22. [bijection] cheese:Glebe Farmhouse: ruled out position(s) 3,4
23. [bijection] from clue 3 age:two years: ruled out position(s) 2
24. [bijection] from clue 5 maker:Lachlan: ruled out position(s) 3
25. [order] from clue 4 cheese:Bellringer: ruled out position(s) 3
26. [order] from clue 4 age:fourteen months: ruled out position(s) 4
27. [order] from clue 9 maker:Ambrose: ruled out position(s) 2,4
28. [order] from clue 1 maker:Sigrid: ruled out position(s) 2,3
29. [bijection] age:nine months: ruled out position(s) 3,5
30. [bijection] age:three weeks: ruled out position(s) 5
31. [bijection] age:nine months: ruled out position(s) 4
32. [bijection] cheese:Old Thrashing: ruled out position(s) 4
33. [bijection] maker:Hepzibah: ruled out position(s) 1
34. [bijection] maker:Lachlan: ruled out position(s) 1
35. [bijection] maker:Hepzibah: ruled out position(s) 2,3,5
36. [order] from clue 2 maker:Teodoro: ruled out position(s) 3
37. [bijection] maker:Lachlan: ruled out position(s) 2
38. [bijection] maker:Ambrose: ruled out position(s) 5

---

<sub>seed `2026172733816` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
