# The Case of the Missing Trowel

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `75291c4e810a`

## Introduction

The Marchmont Mutual Improvement Society has taken on the case of the missing trowel with a seriousness it has never shown a book.
Five investigators are involved. Determine each investigator's start time, clue and alibi.
- **Investigator**: Ariadne, Fergus, Leopold, Ngozi and Immaculata.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Clue produced**: a dropped glove, a smell of creosote, an anonymous note, a tyre mark and a bootprint.
- **Alibi**: the dentist, a locked greenhouse, a long bath, choir practice and a bus replacement service.
Every investigator has a different start time, clue and alibi, so within each category every item is used exactly once.

## Clues

1. Leopold reports at 10am.
2. The investigator who produces a smell of creosote and Ngozi are exactly two hours apart in start time order. Ngozi claims the dentist.
3. Immaculata and 9am are exactly three hours apart in start time order. The investigator who produces a dropped glove and 9am are exactly two hours apart in start time order.
4. The investigator who claims choir practice and 8am are exactly three hours apart in start time order.
5. One of the investigator who produces a tyre mark and 9am sits at an odd-numbered start time and the other at an even-numbered start time.
6. The investigator who produces a tyre mark does not report at 8am.
7. The investigator who claims a locked greenhouse does not produce an anonymous note.
8. The investigator who claims the dentist is exactly one hour earlier than Fergus, with no start time in between.
9. The investigator who produces a smell of creosote falls somewhere between the investigator who claims a bus replacement service and the investigator who claims the dentist in start time order.
10. The investigator who claims the dentist does not produce an anonymous note.

## Solving chart

*Start time vs Investigator*

| | Ariadne | Fergus | Leopold | Ngozi | Immaculata |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Clue produced*

| | a dropped glove | a smell of creosote | an anonymous note | a tyre mark | a bootprint |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Alibi*

| | the dentist | a locked greenhouse | a long bath | choir practice | a bus replacement service |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Investigator vs Clue produced*

| | a dropped glove | a smell of creosote | an anonymous note | a tyre mark | a bootprint |
|---|---|---|---|---|---|
| **Ariadne** | | | | | |
| **Fergus** | | | | | |
| **Leopold** | | | | | |
| **Ngozi** | | | | | |
| **Immaculata** | | | | | |

*Investigator vs Alibi*

| | the dentist | a locked greenhouse | a long bath | choir practice | a bus replacement service |
|---|---|---|---|---|---|
| **Ariadne** | | | | | |
| **Fergus** | | | | | |
| **Leopold** | | | | | |
| **Ngozi** | | | | | |
| **Immaculata** | | | | | |

*Clue produced vs Alibi*

| | the dentist | a locked greenhouse | a long bath | choir practice | a bus replacement service |
|---|---|---|---|---|---|
| **a dropped glove** | | | | | |
| **a smell of creosote** | | | | | |
| **an anonymous note** | | | | | |
| **a tyre mark** | | | | | |
| **a bootprint** | | | | | |

## Solution

| Start time | Investigator | Clue produced | Alibi |
|---|---|---|---|
| 8am | Ngozi | a bootprint | the dentist |
| 9am | Fergus | an anonymous note | a long bath |
| 10am | Leopold | a smell of creosote | a locked greenhouse |
| 11am | Ariadne | a dropped glove | choir practice |
| noon | Immaculata | a tyre mark | a bus replacement service |

## How it falls out

1. [direct] from clue 5 clue:a tyre mark: ruled out position(s) 1
2. [direct] from clue 2 sleuth:Leopold: ruled out position(s) 1,2,4,5
3. [bijection] sleuth:Ariadne: ruled out position(s) 3
4. [bijection] sleuth:Fergus: ruled out position(s) 3
5. [bijection] sleuth:Ngozi: ruled out position(s) 3
6. [bijection] sleuth:Immaculata: ruled out position(s) 3
7. [direct] from clue 3 alibi:the dentist: ruled out position(s) 3
8. [order] from clue 11 clue:a dropped glove: ruled out position(s) 1,2,3,5
9. [order] from clue 10 clue:a smell of creosote: ruled out position(s) 1,5
10. [order] from clue 9 alibi:choir practice: ruled out position(s) 1,2,3,5
11. [order] from clue 7 sleuth:Immaculata: ruled out position(s) 1,2,4
12. [order] from clue 6 alibi:the dentist: ruled out position(s) 2,5
13. [order] from clue 6 sleuth:Fergus: ruled out position(s) 1,4
14. [order] from clue 1 clue:a tyre mark: ruled out position(s) 2,4
15. [direct] from clue 3 sleuth:Ngozi: ruled out position(s) 2,5
16. [order] from clue 10 clue:a smell of creosote: ruled out position(s) 4
17. [bijection] alibi:the dentist: ruled out position(s) 4
18. [bijection] alibi:a locked greenhouse: ruled out position(s) 4
19. [bijection] alibi:a long bath: ruled out position(s) 4
20. [bijection] alibi:a bus replacement service: ruled out position(s) 4
21. [bijection] clue:an anonymous note: ruled out position(s) 4
22. [bijection] clue:a bootprint: ruled out position(s) 4
23. [bijection] sleuth:Ariadne: ruled out position(s) 5
24. [bijection] sleuth:Fergus: ruled out position(s) 5
25. [direct] from clue 12 clue:an anonymous note: ruled out position(s) 1
26. [order] from clue 4 alibi:a bus replacement service: ruled out position(s) 1,2
27. [direct] from clue 3 sleuth:Ngozi: ruled out position(s) 4
28. [order] from clue 10 clue:a smell of creosote: ruled out position(s) 2
29. [order] from clue 4 alibi:a bus replacement service: ruled out position(s) 3
30. [bijection] alibi:a locked greenhouse: ruled out position(s) 1,5
31. [bijection] alibi:a long bath: ruled out position(s) 1,5
32. [bijection] clue:an anonymous note: ruled out position(s) 3
33. [bijection] clue:a tyre mark: ruled out position(s) 3
34. [bijection] clue:a bootprint: ruled out position(s) 3
35. [bijection] clue:a bootprint: ruled out position(s) 2,5
36. [bijection] sleuth:Ariadne: ruled out position(s) 1,2
37. [bijection] clue:an anonymous note: ruled out position(s) 5
38. [direct] from clue 8 alibi:a locked greenhouse: ruled out position(s) 2
39. [bijection] alibi:a long bath: ruled out position(s) 3

---

<sub>seed `2026173013012` &middot; score 5.355 &middot; atoms 12 &middot; positives 2 &middot; solved by order</sub>
