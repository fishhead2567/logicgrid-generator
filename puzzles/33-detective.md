# The Case of the Missing Trowel

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `17f4b197963e`

## Introduction

The Marchmont Mutual Improvement Society has taken on the case of the missing trowel with a seriousness it has never shown a book.
Five investigators are involved. Determine each investigator's start time, theory and alibi.
- **Investigator**: Leopold, Ngozi, Ariadne, Hortensia and Immaculata.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Theory**: the postman, nothing happened at all, a clerical error, an inside job and a magpie.
- **Alibi**: watching the snooker, a long bath, the dentist, no alibi whatsoever and a locked greenhouse.
Every investigator has a different start time, theory and alibi, so within each category every item is used exactly once.

## Clues

1. The following two do NOT both hold; either one alone may hold, and so may neither: (a) Hortensia and noon are exactly one hour apart in start time order, in one direction or the other. (b) Ngozi does not report at 10am.
2. At least one of the following holds, and possibly more than one: (a) The investigator who favours nothing happened at all reports at 9am. (b) The investigator who claims a locked greenhouse does not favour a magpie.
3. The investigator who favours an inside job falls somewhere between Ngozi and noon in start time order.
4. The investigator who favours an inside job does not report at 11am.
5. Ariadne and 10am are exactly two hours apart in start time order.
6. The investigator who favours a magpie is later than 9am in start time order.
7. One of the investigator who claims a long bath and Hortensia sits at an odd-numbered start time and the other at an even-numbered start time.
8. The investigator who favours a clerical error is exactly one hour earlier than Leopold, with no start time in between.
9. The investigator who favours a magpie is earlier than the investigator who claims watching the snooker in start time order.
10. The investigator who favours a magpie is earlier than the investigator who claims no alibi whatsoever in start time order.
11. The investigator who claims no alibi whatsoever falls somewhere between Ngozi and the investigator who favours nothing happened at all in start time order.

## Solving chart

*Start time vs Investigator*

| | Leopold | Ngozi | Ariadne | Hortensia | Immaculata |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Theory*

| | the postman | nothing happened at all | a clerical error | an inside job | a magpie |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Alibi*

| | watching the snooker | a long bath | the dentist | no alibi whatsoever | a locked greenhouse |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Investigator vs Theory*

| | the postman | nothing happened at all | a clerical error | an inside job | a magpie |
|---|---|---|---|---|---|
| **Leopold** | | | | | |
| **Ngozi** | | | | | |
| **Ariadne** | | | | | |
| **Hortensia** | | | | | |
| **Immaculata** | | | | | |

*Investigator vs Alibi*

| | watching the snooker | a long bath | the dentist | no alibi whatsoever | a locked greenhouse |
|---|---|---|---|---|---|
| **Leopold** | | | | | |
| **Ngozi** | | | | | |
| **Ariadne** | | | | | |
| **Hortensia** | | | | | |
| **Immaculata** | | | | | |

*Theory vs Alibi*

| | watching the snooker | a long bath | the dentist | no alibi whatsoever | a locked greenhouse |
|---|---|---|---|---|---|
| **the postman** | | | | | |
| **nothing happened at all** | | | | | |
| **a clerical error** | | | | | |
| **an inside job** | | | | | |
| **a magpie** | | | | | |

## Solution

| Start time | Investigator | Theory | Alibi |
|---|---|---|---|
| 8am | Ngozi | a clerical error | a locked greenhouse |
| 9am | Leopold | an inside job | a long bath |
| 10am | Hortensia | a magpie | the dentist |
| 11am | Immaculata | the postman | no alibi whatsoever |
| noon | Ariadne | nothing happened at all | watching the snooker |

## How it falls out

1. [direct] from clue 5 theory:an inside job: ruled out position(s) 4
2. [order] from clue 11 theory:an inside job: ruled out position(s) 1,5
3. [order] from clue 11 sleuth:Ngozi: ruled out position(s) 3,4,5
4. [order] from clue 9 theory:a clerical error: ruled out position(s) 5
5. [order] from clue 9 sleuth:Leopold: ruled out position(s) 1
6. [order] from clue 8 alibi:no alibi whatsoever: ruled out position(s) 1,5
7. [order] from clue 8 theory:nothing happened at all: ruled out position(s) 1,2
8. [order] from clue 4 theory:a magpie: ruled out position(s) 4,5
9. [order] from clue 3 theory:a magpie: ruled out position(s) 1,2
10. [order] from clue 4 alibi:no alibi whatsoever: ruled out position(s) 2,3
11. [order] from clue 8 theory:nothing happened at all: ruled out position(s) 3,4
12. [order] from clue 2 alibi:watching the snooker: ruled out position(s) 1,2,3
13. [order] from clue 1 sleuth:Ariadne: ruled out position(s) 2,3,4
14. [bijection] alibi:watching the snooker: ruled out position(s) 4
15. [bijection] alibi:a long bath: ruled out position(s) 4
16. [bijection] alibi:the dentist: ruled out position(s) 4
17. [bijection] alibi:a locked greenhouse: ruled out position(s) 4
18. [bijection] theory:the postman: ruled out position(s) 3,5
19. [bijection] theory:a clerical error: ruled out position(s) 3
20. [bijection] theory:an inside job: ruled out position(s) 3
21. [order] from clue 11 sleuth:Ngozi: ruled out position(s) 2
22. [order] from clue 9 sleuth:Leopold: ruled out position(s) 4
23. [bijection] alibi:a long bath: ruled out position(s) 5
24. [bijection] alibi:the dentist: ruled out position(s) 5
25. [bijection] alibi:a locked greenhouse: ruled out position(s) 5
26. [bijection] sleuth:Ariadne: ruled out position(s) 1
27. [bijection] sleuth:Hortensia: ruled out position(s) 1
28. [bijection] sleuth:Immaculata: ruled out position(s) 1
29. [bijection] theory:the postman: ruled out position(s) 2
30. [bijection] theory:a clerical error: ruled out position(s) 2
31. [order] from clue 9 sleuth:Leopold: ruled out position(s) 3
32. [bijection] sleuth:Leopold: ruled out position(s) 5
33. [bijection] sleuth:Hortensia: ruled out position(s) 5
34. [bijection] sleuth:Immaculata: ruled out position(s) 5
35. [order] from clue 9 theory:a clerical error: ruled out position(s) 4
36. [bijection] sleuth:Hortensia: ruled out position(s) 2
37. [bijection] sleuth:Immaculata: ruled out position(s) 2
38. [bijection] theory:the postman: ruled out position(s) 1
39. [disjunction] from clue 10 alibi:a locked greenhouse: ruled out position(s) 3
40. [disjunction] from clue 7 sleuth:Hortensia: ruled out position(s) 4
_... and 5 further steps._

---

<sub>seed `2026172836763` &middot; score 9.2622 &middot; atoms 11 &middot; positives 0 &middot; solved by disjunction</sub>
