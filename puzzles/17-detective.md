# The Case of the Missing Trowel

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `c10f8d448e10`

## Introduction

The Marchmont Mutual Improvement Society has taken on the case of the missing trowel with a seriousness it has never shown a book.
Five investigators are involved. Determine each investigator's start time and theory.
- **Investigator**: Ariadne, Leopold, Fergus, Hortensia and Immaculata.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Theory**: a conspiracy of two, nothing happened at all, a magpie, an inside job and a clerical error.
Every investigator has a different start time and theory, so within each category every item is used exactly once.

## Clues

1. The investigator who favours a clerical error is exactly one hour earlier than 10am, with no start time in between.
2. The investigator who favours a conspiracy of two and 10am are exactly one hour apart in start time order, in one direction or the other.
3. Ariadne is later than 11am in start time order. The investigator who favours nothing happened at all falls somewhere between Ariadne and Immaculata in start time order.
4. The investigator who favours a magpie is exactly one hour earlier than Fergus, with no start time in between.
5. The investigator who favours nothing happened at all is exactly one hour earlier than Leopold, with no start time in between.

## Solving chart

*Start time vs Investigator*

| | Ariadne | Leopold | Fergus | Hortensia | Immaculata |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Theory*

| | a conspiracy of two | nothing happened at all | a magpie | an inside job | a clerical error |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Investigator vs Theory*

| | a conspiracy of two | nothing happened at all | a magpie | an inside job | a clerical error |
|---|---|---|---|---|---|
| **Ariadne** | | | | | |
| **Leopold** | | | | | |
| **Fergus** | | | | | |
| **Hortensia** | | | | | |
| **Immaculata** | | | | | |

## Solution

| Start time | Investigator | Theory |
|---|---|---|
| 8am | Immaculata | a magpie |
| 9am | Fergus | a clerical error |
| 10am | Hortensia | nothing happened at all |
| 11am | Leopold | a conspiracy of two |
| noon | Ariadne | an inside job |

## How it falls out

1. [order] from clue 6 sleuth:Ariadne: ruled out position(s) 1,2,3,4
2. [order] from clue 5 theory:nothing happened at all: ruled out position(s) 5
3. [order] from clue 5 sleuth:Leopold: ruled out position(s) 1
4. [order] from clue 4 theory:a conspiracy of two: ruled out position(s) 1,3,5
5. [order] from clue 3 theory:a magpie: ruled out position(s) 5
6. [order] from clue 3 sleuth:Fergus: ruled out position(s) 1
7. [order] from clue 2 theory:a clerical error: ruled out position(s) 1,3,4,5
8. [order] from clue 1 theory:nothing happened at all: ruled out position(s) 1
9. [order] from clue 1 sleuth:Immaculata: ruled out position(s) 4,5
10. [order] from clue 5 sleuth:Leopold: ruled out position(s) 2
11. [bijection] sleuth:Leopold: ruled out position(s) 5
12. [bijection] sleuth:Fergus: ruled out position(s) 5
13. [bijection] sleuth:Hortensia: ruled out position(s) 5
14. [bijection] theory:a conspiracy of two: ruled out position(s) 2
15. [bijection] theory:nothing happened at all: ruled out position(s) 2
16. [bijection] theory:a magpie: ruled out position(s) 2
17. [bijection] theory:an inside job: ruled out position(s) 2
18. [bijection] theory:an inside job: ruled out position(s) 1,3,4
19. [order] from clue 3 theory:a magpie: ruled out position(s) 4
20. [order] from clue 3 sleuth:Fergus: ruled out position(s) 3
21. [order] from clue 5 theory:nothing happened at all: ruled out position(s) 4
22. [order] from clue 5 sleuth:Leopold: ruled out position(s) 3
23. [order] from clue 1 sleuth:Immaculata: ruled out position(s) 3
24. [bijection] sleuth:Fergus: ruled out position(s) 4
25. [bijection] sleuth:Hortensia: ruled out position(s) 4
26. [bijection] sleuth:Hortensia: ruled out position(s) 1,2
27. [bijection] theory:a magpie: ruled out position(s) 3
28. [bijection] sleuth:Immaculata: ruled out position(s) 2

---

<sub>seed `2026172810062` &middot; score 5.1 &middot; atoms 6 &middot; positives 0 &middot; solved by order</sub>
