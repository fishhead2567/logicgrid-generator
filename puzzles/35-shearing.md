# The Blades Final at Waihopai

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `7ae49d9ac489`

## Introduction

Down the board, judged on the floor as much as on the clock, and the wool classer is taking notes.
Five shearers are involved. Determine each shearer's placing, handpiece and penalty.
- **Shearer**: Wiremu, Manaia, Shona Garrick, Tipene and Deirdre Pollok.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Handpiece**: a narrow comb, a cover comb, a wide comb, an old Sunbeam and a spare set of blades.
- **Penalty**: a missed belly, a skin nick, a slow pen, a dropped sheep and a faultless board.
Every shearer has a different placing, handpiece and penalty, so within each category every item is used exactly once.

## Clues

1. Wiremu is docked for a slow pen. Wiremu is exactly one place better than the shearer who uses a cover comb, with no placing in between.
2. At least one of the following holds, and possibly more than one: (a) The shearer who uses a spare set of blades and third are exactly one place apart in placing order, in one direction or the other. (b) One of first and Deirdre Pollok sits at an odd-numbered placing and the other at an even-numbered placing.
3. At least one of the following holds, and possibly more than one: (a) The shearer who is docked for a skin nick is worse than second in placing order. (b) The shearer who is docked for a slow pen places fourth.
4. The shearer who is docked for a missed belly does not place first.
5. The shearer who is docked for a missed belly and second are exactly one place apart in placing order, in one direction or the other.
6. Fourth is exactly one place better than Manaia, with no placing in between.
7. At least one of the following holds, and possibly more than one: (a) Manaia is better than the shearer who uses a wide comb in placing order. (b) The shearer who uses a narrow comb and second are exactly two places apart in placing order.
8. The shearer who uses an old Sunbeam and fifth are exactly three places apart in placing order.
9. The shearer who uses a wide comb and the shearer who is docked for a faultless board are exactly three places apart in placing order.
10. The shearer who is docked for a slow pen is better than Tipene in placing order.

## Solving chart

*Placing vs Shearer*

| | Wiremu | Manaia | Shona Garrick | Tipene | Deirdre Pollok |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Handpiece*

| | a narrow comb | a cover comb | a wide comb | an old Sunbeam | a spare set of blades |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Penalty*

| | a missed belly | a skin nick | a slow pen | a dropped sheep | a faultless board |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Shearer vs Handpiece*

| | a narrow comb | a cover comb | a wide comb | an old Sunbeam | a spare set of blades |
|---|---|---|---|---|---|
| **Wiremu** | | | | | |
| **Manaia** | | | | | |
| **Shona Garrick** | | | | | |
| **Tipene** | | | | | |
| **Deirdre Pollok** | | | | | |

*Shearer vs Penalty*

| | a missed belly | a skin nick | a slow pen | a dropped sheep | a faultless board |
|---|---|---|---|---|---|
| **Wiremu** | | | | | |
| **Manaia** | | | | | |
| **Shona Garrick** | | | | | |
| **Tipene** | | | | | |
| **Deirdre Pollok** | | | | | |

*Handpiece vs Penalty*

| | a missed belly | a skin nick | a slow pen | a dropped sheep | a faultless board |
|---|---|---|---|---|---|
| **a narrow comb** | | | | | |
| **a cover comb** | | | | | |
| **a wide comb** | | | | | |
| **an old Sunbeam** | | | | | |
| **a spare set of blades** | | | | | |

## Solution

| Placing | Shearer | Handpiece | Penalty |
|---|---|---|---|
| first | Shona Garrick | a wide comb | a dropped sheep |
| second | Wiremu | an old Sunbeam | a slow pen |
| third | Tipene | a cover comb | a missed belly |
| fourth | Deirdre Pollok | a narrow comb | a faultless board |
| fifth | Manaia | a spare set of blades | a skin nick |

## How it falls out

1. [direct] from clue 2 penalty:a missed belly: ruled out position(s) 1
2. [order] from clue 11 penalty:a slow pen: ruled out position(s) 5
3. [order] from clue 11 shearer:Tipene: ruled out position(s) 1
4. [order] from clue 10 handpiece:an old Sunbeam: ruled out position(s) 1,3,4,5
5. [order] from clue 7 shearer:Wiremu: ruled out position(s) 5
6. [order] from clue 7 handpiece:a cover comb: ruled out position(s) 1
7. [order] from clue 6 penalty:a missed belly: ruled out position(s) 2,4,5
8. [order] from clue 5 shearer:Manaia: ruled out position(s) 1,2,3,4
9. [order] from clue 4 handpiece:a wide comb: ruled out position(s) 3
10. [order] from clue 4 penalty:a faultless board: ruled out position(s) 3
11. [bijection] handpiece:a narrow comb: ruled out position(s) 2
12. [bijection] handpiece:a cover comb: ruled out position(s) 2
13. [bijection] handpiece:a wide comb: ruled out position(s) 2
14. [bijection] handpiece:a spare set of blades: ruled out position(s) 2
15. [bijection] penalty:a skin nick: ruled out position(s) 3
16. [bijection] penalty:a slow pen: ruled out position(s) 3
17. [bijection] penalty:a dropped sheep: ruled out position(s) 3
18. [bijection] shearer:Shona Garrick: ruled out position(s) 5
19. [bijection] shearer:Tipene: ruled out position(s) 5
20. [bijection] shearer:Deirdre Pollok: ruled out position(s) 5
21. [order] from clue 11 penalty:a slow pen: ruled out position(s) 4
22. [direct] from clue 1 shearer:Wiremu: ruled out position(s) 3,4
23. [order] from clue 4 penalty:a faultless board: ruled out position(s) 5
24. [order] from clue 7 shearer:Wiremu: ruled out position(s) 1
25. [order] from clue 7 handpiece:a cover comb: ruled out position(s) 4,5
26. [direct] from clue 1 penalty:a slow pen: ruled out position(s) 1
27. [order] from clue 11 shearer:Tipene: ruled out position(s) 2
28. [bijection] handpiece:a narrow comb: ruled out position(s) 3
29. [bijection] handpiece:a spare set of blades: ruled out position(s) 3
30. [bijection] penalty:a skin nick: ruled out position(s) 2
31. [bijection] penalty:a dropped sheep: ruled out position(s) 2
32. [bijection] penalty:a faultless board: ruled out position(s) 2
33. [bijection] shearer:Shona Garrick: ruled out position(s) 2
34. [bijection] shearer:Deirdre Pollok: ruled out position(s) 2
35. [order] from clue 4 handpiece:a wide comb: ruled out position(s) 5
36. [disjunction] from clue 9 penalty:a skin nick: ruled out position(s) 1
37. [disjunction] from clue 8 handpiece:a wide comb: ruled out position(s) 4
38. [disjunction] from clue 8 handpiece:a narrow comb: ruled out position(s) 1,5
39. [order] from clue 4 penalty:a faultless board: ruled out position(s) 1
40. [bijection] handpiece:a spare set of blades: ruled out position(s) 1,4
_... and 7 further steps._

---

<sub>seed `2026173052607` &middot; score 9.6853 &middot; atoms 11 &middot; positives 1 &middot; solved by disjunction</sub>
