# The Cheesemongers' Standoff

*A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.*

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `ad5c617866a4`

## Introduction

There are 5 wheels. Each has exactly one price and one item from every other category below, and within each category every item belongs to a different wheel.
- **Price** (listed in order): $3, $5, $7, $9 and $11.
- **Cheese**: Old Thrashing, Winter Tarn, Oakmoss, Glebe Farmhouse and Saltpans.
- **Maker**: Sigrid, Teodoro, Hepzibah, Lachlan and Perdita.
- **Rind**: an ash-coated rind, a natural rind, a nettle-wrapped rind, a cider-washed rind and a cloth-bound rind.
- **Aged for**: five months, two years, nine months, two months and thirty months.
The price steps above are listed in order, from $3 to $11.

## Clues

1. $9 is immediately cheaper than Hepzibah's price, with no price in between. Five months, $9 and a cloth-bound rind are three different wheels.
2. At least one of the following holds, and possibly more than one: (a) Five months and $7 are next to each other in price order, in one order or the other. (b) An ash-coated rind's price is immediately cheaper than Old Thrashing's price, with no price in between.
3. Teodoro falls somewhere between $5 and a nettle-wrapped rind in price order. Teodoro's price is cheaper than a natural rind's price. Five months falls somewhere between a cloth-bound rind and a nettle-wrapped rind in price order.
4. Thirty months falls somewhere between Sigrid and $11 in price order.
5. Oakmoss' price is cheaper than two years' price.
6. Nine months' price is immediately cheaper than an ash-coated rind's price, with no price in between.
7. Lachlan does not go with a cloth-bound rind.
8. Nine months does not go with Oakmoss.
9. A cider-washed rind's price is immediately cheaper than Saltpans' price, with no price in between. Nine months' price is cheaper than Saltpans' price. A natural rind falls somewhere between nine months and Glebe Farmhouse in price order.
10. At least one of the following holds, and possibly more than one: (a) An ash-coated rind's price is immediately cheaper than Perdita's price, with no price in between. (b) Thirty months goes with a nettle-wrapped rind.

## Solving chart

*Price vs Cheese*

| | Old Thrashing | Winter Tarn | Oakmoss | Glebe Farmhouse | Saltpans |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Maker*

| | Sigrid | Teodoro | Hepzibah | Lachlan | Perdita |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Rind*

| | an ash-coated rind | a natural rind | a nettle-wrapped rind | a cider-washed rind | a cloth-bound rind |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Aged for*

| | five months | two years | nine months | two months | thirty months |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Cheese vs Maker*

| | Sigrid | Teodoro | Hepzibah | Lachlan | Perdita |
|---|---|---|---|---|---|
| **Old Thrashing** | | | | | |
| **Winter Tarn** | | | | | |
| **Oakmoss** | | | | | |
| **Glebe Farmhouse** | | | | | |
| **Saltpans** | | | | | |

*Cheese vs Rind*

| | an ash-coated rind | a natural rind | a nettle-wrapped rind | a cider-washed rind | a cloth-bound rind |
|---|---|---|---|---|---|
| **Old Thrashing** | | | | | |
| **Winter Tarn** | | | | | |
| **Oakmoss** | | | | | |
| **Glebe Farmhouse** | | | | | |
| **Saltpans** | | | | | |

*Cheese vs Aged for*

| | five months | two years | nine months | two months | thirty months |
|---|---|---|---|---|---|
| **Old Thrashing** | | | | | |
| **Winter Tarn** | | | | | |
| **Oakmoss** | | | | | |
| **Glebe Farmhouse** | | | | | |
| **Saltpans** | | | | | |

*Maker vs Rind*

| | an ash-coated rind | a natural rind | a nettle-wrapped rind | a cider-washed rind | a cloth-bound rind |
|---|---|---|---|---|---|
| **Sigrid** | | | | | |
| **Teodoro** | | | | | |
| **Hepzibah** | | | | | |
| **Lachlan** | | | | | |
| **Perdita** | | | | | |

*Maker vs Aged for*

| | five months | two years | nine months | two months | thirty months |
|---|---|---|---|---|---|
| **Sigrid** | | | | | |
| **Teodoro** | | | | | |
| **Hepzibah** | | | | | |
| **Lachlan** | | | | | |
| **Perdita** | | | | | |

*Rind vs Aged for*

| | five months | two years | nine months | two months | thirty months |
|---|---|---|---|---|---|
| **an ash-coated rind** | | | | | |
| **a natural rind** | | | | | |
| **a nettle-wrapped rind** | | | | | |
| **a cider-washed rind** | | | | | |
| **a cloth-bound rind** | | | | | |

## Solution

| Price | Cheese | Maker | Rind | Aged for |
|---|---|---|---|---|
| $3 | Oakmoss | Sigrid | a cloth-bound rind | two months |
| $5 | Winter Tarn | Lachlan | a cider-washed rind | nine months |
| $7 | Saltpans | Teodoro | an ash-coated rind | five months |
| $9 | Old Thrashing | Perdita | a natural rind | thirty months |
| $11 | Glebe Farmhouse | Hepzibah | a nettle-wrapped rind | two years |

## How it falls out

1. [bijection] from clue 2 age:five months: ruled out position(s) 4
2. [bijection] from clue 2 rind:a cloth-bound rind: ruled out position(s) 4
3. [order] from clue 15 maker:Teodoro: ruled out position(s) 1,2,5
4. [order] from clue 15 rind:a nettle-wrapped rind: ruled out position(s) 1,2,3
5. [order] from clue 14 rind:a natural rind: ruled out position(s) 1,2,3
6. [order] from clue 13 age:nine months: ruled out position(s) 5
7. [order] from clue 13 cheese:Saltpans: ruled out position(s) 1
8. [order] from clue 12 maker:Hepzibah: ruled out position(s) 1,2,3,4
9. [order] from clue 11 rind:a natural rind: ruled out position(s) 5
10. [order] from clue 11 age:nine months: ruled out position(s) 4
11. [order] from clue 11 cheese:Glebe Farmhouse: ruled out position(s) 1,2,3,4
12. [order] from clue 14 maker:Teodoro: ruled out position(s) 4
13. [order] from clue 8 age:thirty months: ruled out position(s) 1,5
14. [order] from clue 8 maker:Sigrid: ruled out position(s) 4,5
15. [order] from clue 7 cheese:Oakmoss: ruled out position(s) 5
16. [order] from clue 7 age:two years: ruled out position(s) 1
17. [order] from clue 5 rind:a cider-washed rind: ruled out position(s) 5
18. [order] from clue 3 age:five months: ruled out position(s) 1,5
19. [order] from clue 3 rind:a cloth-bound rind: ruled out position(s) 3,5
20. [order] from clue 1 rind:an ash-coated rind: ruled out position(s) 1,5
21. [bijection] cheese:Old Thrashing: ruled out position(s) 5
22. [bijection] cheese:Winter Tarn: ruled out position(s) 5
23. [bijection] cheese:Saltpans: ruled out position(s) 5
24. [bijection] maker:Sigrid: ruled out position(s) 3
25. [bijection] maker:Lachlan: ruled out position(s) 3,5
26. [bijection] maker:Perdita: ruled out position(s) 3,5
27. [bijection] rind:an ash-coated rind: ruled out position(s) 4
28. [bijection] rind:a nettle-wrapped rind: ruled out position(s) 4
29. [bijection] rind:a cider-washed rind: ruled out position(s) 4
30. [order] from clue 1 age:nine months: ruled out position(s) 3
31. [disjunction] from clue 10 rind:an ash-coated rind: ruled out position(s) 2
32. [disjunction] from clue 10 maker:Perdita: ruled out position(s) 1,2
33. [order] from clue 1 age:nine months: ruled out position(s) 1
34. [order] from clue 13 cheese:Saltpans: ruled out position(s) 2
35. [order] from clue 5 rind:a cider-washed rind: ruled out position(s) 1
36. [direct] from clue 9 cheese:Oakmoss: ruled out position(s) 2
37. [bijection] age:five months: ruled out position(s) 2
38. [bijection] age:two years: ruled out position(s) 2
39. [bijection] age:two months: ruled out position(s) 2
40. [bijection] age:thirty months: ruled out position(s) 2
_... and 14 further steps._

---

<sub>seed `2026172892196` &middot; score 10.1105 &middot; atoms 15 &middot; positives 0 &middot; solved by disjunction</sub>
