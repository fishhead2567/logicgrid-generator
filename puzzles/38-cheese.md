# The Cheesemongers' Standoff

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `d3851309d716`

## Introduction

A case of opinionated cheeses, their equally opinionated makers, and one display that has begun to smell like a political scandal.
Five cheeses are involved. Determine each cheese's price, maker and ageing.
- **Cheese**: Fenland Blue, Saltpans, Old Thrashing, Bellringer and Oakmoss.
- **Price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Maker**: Olubunmi, Lachlan, Perdita, Sigrid and Teodoro.
- **Aged for**: fourteen months, nine months, thirty months, three weeks and five months.
Every cheese has a different price, maker and ageing, so within each category every item is used exactly once.

## Clues

1. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The cheese that was aged for thirty months is dearer than $7 in price order. (b) Saltpans is dearer than $9 in price order.
2. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The cheese that was aged for fourteen months and $5 are exactly one price step apart in price order, in one direction or the other. (b) Oakmoss is dearer than $9 in price order.
3. The cheese that was aged for thirty months is dearer than $7 in price order. Bellringer is cheaper than $7 in price order.
4. The cheese that was made by Teodoro and $3 are exactly one price step apart in price order, in one direction or the other.
5. The cheese that was aged for five months was not made by Sigrid. The cheese that was aged for five months is exactly one price step cheaper than $11, with no price in between.
6. At least one of the following holds, and possibly more than one: (a) Old Thrashing and $7 are exactly one price step apart in price order, in one direction or the other. (b) The cheese that was aged for nine months is exactly one price step cheaper than the cheese that was made by Teodoro, with no price in between.
7. The cheese that was made by Lachlan is exactly one price step cheaper than Saltpans, with no price in between.
8. The cheese that was made by Lachlan falls somewhere between the cheese that was aged for thirty months and the cheese that was aged for three weeks in price order.
9. Fenland Blue falls somewhere between the cheese that was aged for nine months and the cheese that was made by Sigrid in price order.
10. Bellringer and the cheese that was made by Perdita are exactly one price step apart in price order, in one direction or the other.

## Solving chart

*Price vs Cheese*

| | Fenland Blue | Saltpans | Old Thrashing | Bellringer | Oakmoss |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Maker*

| | Olubunmi | Lachlan | Perdita | Sigrid | Teodoro |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Aged for*

| | fourteen months | nine months | thirty months | three weeks | five months |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Cheese vs Maker*

| | Olubunmi | Lachlan | Perdita | Sigrid | Teodoro |
|---|---|---|---|---|---|
| **Fenland Blue** | | | | | |
| **Saltpans** | | | | | |
| **Old Thrashing** | | | | | |
| **Bellringer** | | | | | |
| **Oakmoss** | | | | | |

*Cheese vs Aged for*

| | fourteen months | nine months | thirty months | three weeks | five months |
|---|---|---|---|---|---|
| **Fenland Blue** | | | | | |
| **Saltpans** | | | | | |
| **Old Thrashing** | | | | | |
| **Bellringer** | | | | | |
| **Oakmoss** | | | | | |

*Maker vs Aged for*

| | fourteen months | nine months | thirty months | three weeks | five months |
|---|---|---|---|---|---|
| **Olubunmi** | | | | | |
| **Lachlan** | | | | | |
| **Perdita** | | | | | |
| **Sigrid** | | | | | |
| **Teodoro** | | | | | |

## Solution

| Price | Cheese | Maker | Aged for |
|---|---|---|---|
| $3 | Oakmoss | Perdita | nine months |
| $5 | Bellringer | Teodoro | three weeks |
| $7 | Fenland Blue | Lachlan | fourteen months |
| $9 | Saltpans | Olubunmi | five months |
| $11 | Old Thrashing | Sigrid | thirty months |

## How it falls out

1. [order] from clue 12 age:five months: ruled out position(s) 1,2,3,5
2. [order] from clue 11 maker:Lachlan: ruled out position(s) 5
3. [order] from clue 11 cheese:Saltpans: ruled out position(s) 1
4. [order] from clue 8 age:thirty months: ruled out position(s) 1,2,3
5. [order] from clue 7 maker:Lachlan: ruled out position(s) 1
6. [order] from clue 7 age:three weeks: ruled out position(s) 4,5
7. [order] from clue 11 cheese:Saltpans: ruled out position(s) 2
8. [order] from clue 6 cheese:Bellringer: ruled out position(s) 3,4,5
9. [order] from clue 5 maker:Perdita: ruled out position(s) 4,5
10. [order] from clue 3 maker:Teodoro: ruled out position(s) 1,3,4,5
11. [order] from clue 1 cheese:Fenland Blue: ruled out position(s) 1,5
12. [direct] from clue 2 maker:Sigrid: ruled out position(s) 4
13. [bijection] age:fourteen months: ruled out position(s) 4
14. [bijection] age:nine months: ruled out position(s) 4
15. [bijection] age:thirty months: ruled out position(s) 4
16. [bijection] maker:Olubunmi: ruled out position(s) 2
17. [bijection] maker:Lachlan: ruled out position(s) 2
18. [bijection] maker:Perdita: ruled out position(s) 2
19. [bijection] maker:Sigrid: ruled out position(s) 2
20. [order] from clue 5 cheese:Bellringer: ruled out position(s) 1
21. [order] from clue 11 cheese:Saltpans: ruled out position(s) 3
22. [bijection] age:fourteen months: ruled out position(s) 5
23. [bijection] age:nine months: ruled out position(s) 5
24. [bijection] cheese:Fenland Blue: ruled out position(s) 2
25. [bijection] cheese:Old Thrashing: ruled out position(s) 2
26. [bijection] cheese:Oakmoss: ruled out position(s) 2
27. [order] from clue 1 maker:Sigrid: ruled out position(s) 1,3
28. [bijection] maker:Olubunmi: ruled out position(s) 5
29. [disjunction] from clue 10 cheese:Saltpans: ruled out position(s) 5
30. [order] from clue 11 maker:Lachlan: ruled out position(s) 4
31. [order] from clue 7 age:three weeks: ruled out position(s) 3
32. [bijection] cheese:Fenland Blue: ruled out position(s) 4
33. [bijection] cheese:Old Thrashing: ruled out position(s) 4
34. [bijection] cheese:Oakmoss: ruled out position(s) 4
35. [bijection] maker:Olubunmi: ruled out position(s) 3
36. [bijection] maker:Perdita: ruled out position(s) 3
37. [bijection] maker:Olubunmi: ruled out position(s) 1
38. [disjunction] from clue 9 age:nine months: ruled out position(s) 2,3
39. [bijection] age:fourteen months: ruled out position(s) 1
40. [bijection] age:three weeks: ruled out position(s) 1
_... and 5 further steps._

---

<sub>seed `2026172876358` &middot; score 9.6333 &middot; atoms 12 &middot; positives 0 &middot; solved by disjunction</sub>
