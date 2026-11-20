# The Walling Match at Gunnerside

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `f5dfd113b889`

## Introduction

A measured length of fallen wall each, and a whole morning in which to rebuild it to the satisfaction of a judge who will push on every cope.
Five wallers are involved. Determine each waller's finishing time, stone and feature.
- **Waller**: Ossian Baird, Hilda Crowther, Mab Teasdale, Ewart Beck and Clem Hartley.
- **Finishing time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Stone**: green slate, red sandstone, Welsh rubble, Cotswold oolite and Dales limestone.
- **Feature built**: a water smoot, a stile, a set of throughstones, a cripple hole and a lunky hole.
Every waller has a different finishing time, stone and feature, so within each category every item is used exactly once.

## Clues

1. The waller who builds in a set of throughstones finishes at 11am.
2. Ossian Baird is exactly one hour earlier than 11am, with no finishing time in between.
3. 9am is exactly one hour earlier than the waller who works in Dales limestone, with no finishing time in between.
4. At least one of the following holds, and possibly more than one: (a) The waller who builds in a stile and the waller who works in Cotswold oolite are exactly one hour apart in finishing time order, in one direction or the other. (b) The waller who builds in a stile and the waller who works in green slate are exactly one hour apart in finishing time order, in one direction or the other.
5. The waller who builds in a stile and Clem Hartley are exactly one hour apart in finishing time order, in one direction or the other.
6. Ewart Beck falls somewhere between the waller who builds in a stile and the waller who builds in a water smoot in finishing time order.
7. Clem Hartley is exactly one hour earlier than the waller who works in Welsh rubble, with no finishing time in between.
8. At least one of the following holds, and possibly more than one: (a) The waller who works in red sandstone is earlier than Mab Teasdale in finishing time order. (b) Ossian Baird works in Welsh rubble.
9. Clem Hartley is earlier than the waller who builds in a set of throughstones in finishing time order.
10. The waller who builds in a cripple hole does not work in Cotswold oolite. Ossian Baird does not build in a cripple hole.

## Solving chart

*Finishing time vs Waller*

| | Ossian Baird | Hilda Crowther | Mab Teasdale | Ewart Beck | Clem Hartley |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Finishing time vs Stone*

| | green slate | red sandstone | Welsh rubble | Cotswold oolite | Dales limestone |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Finishing time vs Feature built*

| | a water smoot | a stile | a set of throughstones | a cripple hole | a lunky hole |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Waller vs Stone*

| | green slate | red sandstone | Welsh rubble | Cotswold oolite | Dales limestone |
|---|---|---|---|---|---|
| **Ossian Baird** | | | | | |
| **Hilda Crowther** | | | | | |
| **Mab Teasdale** | | | | | |
| **Ewart Beck** | | | | | |
| **Clem Hartley** | | | | | |

*Waller vs Feature built*

| | a water smoot | a stile | a set of throughstones | a cripple hole | a lunky hole |
|---|---|---|---|---|---|
| **Ossian Baird** | | | | | |
| **Hilda Crowther** | | | | | |
| **Mab Teasdale** | | | | | |
| **Ewart Beck** | | | | | |
| **Clem Hartley** | | | | | |

*Stone vs Feature built*

| | a water smoot | a stile | a set of throughstones | a cripple hole | a lunky hole |
|---|---|---|---|---|---|
| **green slate** | | | | | |
| **red sandstone** | | | | | |
| **Welsh rubble** | | | | | |
| **Cotswold oolite** | | | | | |
| **Dales limestone** | | | | | |

## Solution

| Finishing time | Waller | Stone | Feature built |
|---|---|---|---|
| 8am | Clem Hartley | green slate | a cripple hole |
| 9am | Hilda Crowther | Welsh rubble | a stile |
| 10am | Ossian Baird | Dales limestone | a lunky hole |
| 11am | Ewart Beck | red sandstone | a set of throughstones |
| noon | Mab Teasdale | Cotswold oolite | a water smoot |

## How it falls out

1. [direct] from clue 10 feature:a set of throughstones: ruled out position(s) 1,2,3,5
2. [bijection] feature:a water smoot: ruled out position(s) 4
3. [bijection] feature:a stile: ruled out position(s) 4
4. [bijection] feature:a cripple hole: ruled out position(s) 4
5. [bijection] feature:a lunky hole: ruled out position(s) 4
6. [order] from clue 11 waller:Ewart Beck: ruled out position(s) 1,5
7. [order] from clue 9 stone:Dales limestone: ruled out position(s) 1,2,4,5
8. [order] from clue 8 waller:Clem Hartley: ruled out position(s) 5
9. [order] from clue 8 stone:Welsh rubble: ruled out position(s) 1
10. [order] from clue 4 waller:Ossian Baird: ruled out position(s) 1,2,4,5
11. [order] from clue 1 waller:Clem Hartley: ruled out position(s) 4
12. [order] from clue 8 stone:Welsh rubble: ruled out position(s) 5
13. [order] from clue 6 feature:a stile: ruled out position(s) 5
14. [order] from clue 11 feature:a water smoot: ruled out position(s) 2
15. [direct] from clue 7 feature:a cripple hole: ruled out position(s) 3
16. [bijection] stone:green slate: ruled out position(s) 3
17. [bijection] stone:red sandstone: ruled out position(s) 3
18. [bijection] stone:Welsh rubble: ruled out position(s) 3
19. [bijection] stone:Cotswold oolite: ruled out position(s) 3
20. [bijection] waller:Hilda Crowther: ruled out position(s) 3
21. [bijection] waller:Mab Teasdale: ruled out position(s) 3
22. [bijection] waller:Ewart Beck: ruled out position(s) 3
23. [bijection] waller:Clem Hartley: ruled out position(s) 3
24. [order] from clue 8 waller:Clem Hartley: ruled out position(s) 2
25. [order] from clue 8 stone:Welsh rubble: ruled out position(s) 4
26. [order] from clue 6 feature:a stile: ruled out position(s) 1,3
27. [order] from clue 11 waller:Ewart Beck: ruled out position(s) 2
28. [order] from clue 11 feature:a water smoot: ruled out position(s) 1,3
29. [bijection] feature:a cripple hole: ruled out position(s) 2,5
30. [bijection] feature:a lunky hole: ruled out position(s) 2,5
31. [bijection] feature:a lunky hole: ruled out position(s) 1
32. [bijection] stone:green slate: ruled out position(s) 2
33. [bijection] stone:red sandstone: ruled out position(s) 2
34. [bijection] stone:Cotswold oolite: ruled out position(s) 2
35. [bijection] waller:Hilda Crowther: ruled out position(s) 1,4
36. [bijection] waller:Mab Teasdale: ruled out position(s) 1,4
37. [direct] from clue 3 stone:Cotswold oolite: ruled out position(s) 1
38. [disjunction] from clue 5 stone:green slate: ruled out position(s) 4,5
39. [disjunction] from clue 2 stone:red sandstone: ruled out position(s) 5
40. [bijection] stone:red sandstone: ruled out position(s) 1
_... and 3 further steps._

---

<sub>seed `2026173152610` &middot; score 9.3755 &middot; atoms 11 &middot; positives 1 &middot; solved by disjunction</sub>
