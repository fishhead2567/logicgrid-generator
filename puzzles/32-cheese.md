# The Cheesemongers' Standoff

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `81dbc64fc4c9`

## Introduction

A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.
Five cheeses are involved. Determine each cheese's price, maker and rind.
- **Cheese**: Bellringer, Old Thrashing, Saltpans, Oakmoss and Fenland Blue.
- **Price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Maker**: Olubunmi, Perdita, Sigrid, Lachlan and Ambrose.
- **Rind**: a natural rind, a cider-washed rind, a cloth-bound rind, an ash-coated rind and a nettle-wrapped rind.
Every cheese has a different price, maker and rind, so within each category every item is used exactly once.

## Clues

1. Oakmoss and the cheese that was made by Perdita are exactly one price step apart in price order, in one direction or the other. Oakmoss falls somewhere between $3 and $9 in price order.
2. The cheese that has a natural rind falls somewhere between $3 and $7 in price order.
3. At least one of the following holds, and possibly more than one: (a) $5 is exactly one price step cheaper than Bellringer, with no price in between. (b) Fenland Blue has an ash-coated rind.
4. The cheese that has an ash-coated rind is cheaper than $7 in price order.
5. $5 is exactly one price step cheaper than the cheese that was made by Ambrose, with no price in between.
6. Old Thrashing and the cheese that has a cloth-bound rind are exactly one price step apart in price order, in one direction or the other.
7. The cheese that was made by Olubunmi is cheaper than the cheese that has a cider-washed rind in price order.
8. At least one of the following holds, and possibly more than one: (a) Saltpans and the cheese that was made by Ambrose are exactly one price step apart in price order, in one direction or the other. (b) Saltpans is exactly one price step cheaper than the cheese that was made by Sigrid, with no price in between.
9. The cheese that has an ash-coated rind is cheaper than Fenland Blue in price order. Fenland Blue is cheaper than the cheese that was made by Lachlan in price order.

## Solving chart

*Price vs Cheese*

| | Bellringer | Old Thrashing | Saltpans | Oakmoss | Fenland Blue |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Maker*

| | Olubunmi | Perdita | Sigrid | Lachlan | Ambrose |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Rind*

| | a natural rind | a cider-washed rind | a cloth-bound rind | an ash-coated rind | a nettle-wrapped rind |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Cheese vs Maker*

| | Olubunmi | Perdita | Sigrid | Lachlan | Ambrose |
|---|---|---|---|---|---|
| **Bellringer** | | | | | |
| **Old Thrashing** | | | | | |
| **Saltpans** | | | | | |
| **Oakmoss** | | | | | |
| **Fenland Blue** | | | | | |

*Cheese vs Rind*

| | a natural rind | a cider-washed rind | a cloth-bound rind | an ash-coated rind | a nettle-wrapped rind |
|---|---|---|---|---|---|
| **Bellringer** | | | | | |
| **Old Thrashing** | | | | | |
| **Saltpans** | | | | | |
| **Oakmoss** | | | | | |
| **Fenland Blue** | | | | | |

*Maker vs Rind*

| | a natural rind | a cider-washed rind | a cloth-bound rind | an ash-coated rind | a nettle-wrapped rind |
|---|---|---|---|---|---|
| **Olubunmi** | | | | | |
| **Perdita** | | | | | |
| **Sigrid** | | | | | |
| **Lachlan** | | | | | |
| **Ambrose** | | | | | |

## Solution

| Price | Cheese | Maker | Rind |
|---|---|---|---|
| $3 | Saltpans | Perdita | an ash-coated rind |
| $5 | Oakmoss | Sigrid | a natural rind |
| $7 | Bellringer | Ambrose | a nettle-wrapped rind |
| $9 | Fenland Blue | Olubunmi | a cloth-bound rind |
| $11 | Old Thrashing | Lachlan | a cider-washed rind |

## How it falls out

1. [order] from clue 10 maker:Ambrose: ruled out position(s) 1,2,4,5
2. [order] from clue 8 rind:an ash-coated rind: ruled out position(s) 5
3. [order] from clue 8 cheese:Fenland Blue: ruled out position(s) 1
4. [order] from clue 7 rind:a natural rind: ruled out position(s) 1,3,4,5
5. [order] from clue 6 cheese:Oakmoss: ruled out position(s) 1,4,5
6. [order] from clue 11 maker:Perdita: ruled out position(s) 5
7. [order] from clue 3 maker:Olubunmi: ruled out position(s) 5
8. [order] from clue 3 rind:a cider-washed rind: ruled out position(s) 1
9. [order] from clue 2 rind:an ash-coated rind: ruled out position(s) 3,4
10. [order] from clue 1 cheese:Fenland Blue: ruled out position(s) 5
11. [order] from clue 1 maker:Lachlan: ruled out position(s) 1,2
12. [bijection] maker:Olubunmi: ruled out position(s) 3
13. [bijection] maker:Perdita: ruled out position(s) 3
14. [bijection] maker:Sigrid: ruled out position(s) 3
15. [bijection] maker:Lachlan: ruled out position(s) 3
16. [bijection] rind:a cider-washed rind: ruled out position(s) 2
17. [bijection] rind:a cloth-bound rind: ruled out position(s) 2
18. [bijection] rind:an ash-coated rind: ruled out position(s) 2
19. [bijection] rind:a nettle-wrapped rind: ruled out position(s) 2
20. [order] from clue 5 cheese:Old Thrashing: ruled out position(s) 1
21. [bijection] rind:a cloth-bound rind: ruled out position(s) 1
22. [bijection] rind:a nettle-wrapped rind: ruled out position(s) 1
23. [disjunction] from clue 9 cheese:Saltpans: ruled out position(s) 5
24. [disjunction] from clue 4 cheese:Bellringer: ruled out position(s) 1,2,4,5
25. [disjunction] from clue 4 cheese:Fenland Blue: ruled out position(s) 3
26. [bijection] cheese:Old Thrashing: ruled out position(s) 3
27. [bijection] cheese:Saltpans: ruled out position(s) 3
28. [bijection] cheese:Oakmoss: ruled out position(s) 3
29. [bijection] cheese:Saltpans: ruled out position(s) 2,4
30. [bijection] cheese:Old Thrashing: ruled out position(s) 2,4
31. [order] from clue 11 maker:Perdita: ruled out position(s) 2,4
32. [disjunction] from clue 9 maker:Sigrid: ruled out position(s) 1,4,5
33. [order] from clue 5 rind:a cloth-bound rind: ruled out position(s) 3,5
34. [bijection] cheese:Fenland Blue: ruled out position(s) 2
35. [bijection] maker:Olubunmi: ruled out position(s) 1,2
36. [bijection] maker:Lachlan: ruled out position(s) 4
37. [bijection] rind:a cider-washed rind: ruled out position(s) 4
38. [bijection] rind:a nettle-wrapped rind: ruled out position(s) 4
39. [order] from clue 3 rind:a cider-washed rind: ruled out position(s) 3
40. [bijection] rind:a nettle-wrapped rind: ruled out position(s) 5

---

<sub>seed `2026172928847` &middot; score 9.7475 &middot; atoms 11 &middot; positives 0 &middot; solved by disjunction</sub>
