# The Blades Final at Waihopai

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `8832c12fd7e5`

## Introduction

Six shearers down the board, judged on the floor as much as on the clock, and the wool classer is taking notes.
Five shearers are involved. Determine each shearer's placing, handpiece and penalty.
- **Shearer**: Rangi, Manaia, Deirdre Pollok, Tipene and Bevan Toft.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Handpiece**: a spare set of blades, a wide comb, a borrowed handpiece, Lister blades and an old Sunbeam.
- **Penalty**: a missed belly, tufts on the britch, a slow pen, a skin nick and a faultless board.
Every shearer has a different placing, handpiece and penalty, so within each category every item is used exactly once.

## Clues

1. Tipene places third.
2. Third is exactly one place better than the shearer who uses an old Sunbeam, with no placing in between.
3. The shearer who is docked for a faultless board and fourth are exactly one place apart in placing order, in one direction or the other.
4. The shearer who uses Lister blades and Manaia both sit at odd-numbered places or both at even-numbered places. Manaia is better than fourth in placing order.
5. The shearer who uses a borrowed handpiece is better than fifth in placing order.
6. The shearer who is docked for a skin nick falls somewhere between the shearer who uses a wide comb and Deirdre Pollok in placing order.
7. The shearer who uses Lister blades and Deirdre Pollok are exactly two places apart in placing order.
8. Tipene is exactly one place better than the shearer who is docked for a skin nick, with no placing in between.
9. The shearer who is docked for tufts on the britch and Bevan Toft are exactly three places apart in placing order.
10. The shearer who uses a wide comb and the shearer who is docked for a missed belly are exactly two places apart in placing order.

## Solving chart

*Placing vs Shearer*

| | Rangi | Manaia | Deirdre Pollok | Tipene | Bevan Toft |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Handpiece*

| | a spare set of blades | a wide comb | a borrowed handpiece | Lister blades | an old Sunbeam |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Penalty*

| | a missed belly | tufts on the britch | a slow pen | a skin nick | a faultless board |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Shearer vs Handpiece*

| | a spare set of blades | a wide comb | a borrowed handpiece | Lister blades | an old Sunbeam |
|---|---|---|---|---|---|
| **Rangi** | | | | | |
| **Manaia** | | | | | |
| **Deirdre Pollok** | | | | | |
| **Tipene** | | | | | |
| **Bevan Toft** | | | | | |

*Shearer vs Penalty*

| | a missed belly | tufts on the britch | a slow pen | a skin nick | a faultless board |
|---|---|---|---|---|---|
| **Rangi** | | | | | |
| **Manaia** | | | | | |
| **Deirdre Pollok** | | | | | |
| **Tipene** | | | | | |
| **Bevan Toft** | | | | | |

*Handpiece vs Penalty*

| | a missed belly | tufts on the britch | a slow pen | a skin nick | a faultless board |
|---|---|---|---|---|---|
| **a spare set of blades** | | | | | |
| **a wide comb** | | | | | |
| **a borrowed handpiece** | | | | | |
| **Lister blades** | | | | | |
| **an old Sunbeam** | | | | | |

## Solution

| Placing | Shearer | Handpiece | Penalty |
|---|---|---|---|
| first | Manaia | a wide comb | tufts on the britch |
| second | Rangi | a borrowed handpiece | a slow pen |
| third | Tipene | Lister blades | a missed belly |
| fourth | Bevan Toft | an old Sunbeam | a skin nick |
| fifth | Deirdre Pollok | a spare set of blades | a faultless board |

## How it falls out

1. [direct] from clue 10 shearer:Tipene: ruled out position(s) 1,2,4,5
2. [bijection] shearer:Rangi: ruled out position(s) 3
3. [bijection] shearer:Manaia: ruled out position(s) 3
4. [bijection] shearer:Deirdre Pollok: ruled out position(s) 3
5. [bijection] shearer:Bevan Toft: ruled out position(s) 3
6. [order] from clue 11 penalty:a skin nick: ruled out position(s) 1,5
7. [order] from clue 8 penalty:a skin nick: ruled out position(s) 2,3
8. [order] from clue 11 handpiece:a wide comb: ruled out position(s) 4
9. [order] from clue 11 shearer:Deirdre Pollok: ruled out position(s) 4
10. [order] from clue 9 penalty:a missed belly: ruled out position(s) 2
11. [order] from clue 7 penalty:a faultless board: ruled out position(s) 1,2,4
12. [order] from clue 6 shearer:Manaia: ruled out position(s) 4,5
13. [order] from clue 5 handpiece:an old Sunbeam: ruled out position(s) 1,2,3,5
14. [order] from clue 4 handpiece:Lister blades: ruled out position(s) 1,2,5
15. [order] from clue 3 penalty:tufts on the britch: ruled out position(s) 3
16. [order] from clue 1 handpiece:a borrowed handpiece: ruled out position(s) 5
17. [bijection] handpiece:a spare set of blades: ruled out position(s) 4
18. [bijection] handpiece:a borrowed handpiece: ruled out position(s) 4
19. [bijection] handpiece:Lister blades: ruled out position(s) 4
20. [bijection] penalty:a missed belly: ruled out position(s) 4
21. [bijection] penalty:tufts on the britch: ruled out position(s) 4
22. [bijection] penalty:a slow pen: ruled out position(s) 4
23. [order] from clue 3 shearer:Bevan Toft: ruled out position(s) 1
24. [order] from clue 9 handpiece:a wide comb: ruled out position(s) 2
25. [order] from clue 4 shearer:Deirdre Pollok: ruled out position(s) 2
26. [order] from clue 2 shearer:Manaia: ruled out position(s) 2
27. [bijection] handpiece:a spare set of blades: ruled out position(s) 3
28. [bijection] handpiece:a wide comb: ruled out position(s) 3
29. [bijection] handpiece:a borrowed handpiece: ruled out position(s) 3
30. [bijection] shearer:Rangi: ruled out position(s) 1
31. [bijection] shearer:Deirdre Pollok: ruled out position(s) 1
32. [order] from clue 11 handpiece:a wide comb: ruled out position(s) 5
33. [order] from clue 9 penalty:a missed belly: ruled out position(s) 1,5
34. [bijection] handpiece:a spare set of blades: ruled out position(s) 1
35. [bijection] handpiece:a borrowed handpiece: ruled out position(s) 1
36. [bijection] handpiece:a spare set of blades: ruled out position(s) 2
37. [bijection] penalty:a slow pen: ruled out position(s) 3
38. [bijection] penalty:a faultless board: ruled out position(s) 3
39. [bijection] shearer:Rangi: ruled out position(s) 5
40. [bijection] shearer:Bevan Toft: ruled out position(s) 5
_... and 6 further steps._

---

<sub>seed `2026172857576` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
