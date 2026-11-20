# The Case of the Missing Trowel

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `28f365a69c47`

## Introduction

The Marchmont Mutual Improvement Society has taken on the case of the missing trowel with a seriousness it has never shown a book.
Four investigators are involved. Determine each investigator's start time, theory and alibi.
- **Investigator**: Fergus, Ariadne, Hortensia and Leopold.
- **Start time** (listed from earlier to later): 8am, 9am, 10am and 11am.
- **Theory**: a conspiracy of two, a magpie, an inside job and the postman.
- **Alibi**: no alibi whatsoever, the dentist, watching the snooker and a bus replacement service.
Every investigator has a different start time, theory and alibi, so within each category every item is used exactly once.

## Clues

1. Ariadne claims a bus replacement service.
2. 8am is exactly one hour earlier than Hortensia, with no start time in between. The investigator who claims watching the snooker falls somewhere between 11am and 8am in start time order.
3. The investigator who claims a bus replacement service and 9am are exactly one hour apart in start time order, in one direction or the other.
4. The investigator who favours the postman is earlier than 11am in start time order.
5. Fergus falls somewhere between the investigator who favours a magpie and the investigator who favours the postman in start time order.
6. The investigator who claims a bus replacement service and the investigator who favours an inside job are exactly one hour apart in start time order, in one direction or the other.
7. The investigator who claims the dentist is exactly one hour earlier than Fergus, with no start time in between.

## Solving chart

*Start time vs Investigator*

| | Fergus | Ariadne | Hortensia | Leopold |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Theory*

| | a conspiracy of two | a magpie | an inside job | the postman |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Alibi*

| | no alibi whatsoever | the dentist | watching the snooker | a bus replacement service |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Investigator vs Theory*

| | a conspiracy of two | a magpie | an inside job | the postman |
|---|---|---|---|---|
| **Fergus** | | | | |
| **Ariadne** | | | | |
| **Hortensia** | | | | |
| **Leopold** | | | | |

*Investigator vs Alibi*

| | no alibi whatsoever | the dentist | watching the snooker | a bus replacement service |
|---|---|---|---|---|
| **Fergus** | | | | |
| **Ariadne** | | | | |
| **Hortensia** | | | | |
| **Leopold** | | | | |

*Theory vs Alibi*

| | no alibi whatsoever | the dentist | watching the snooker | a bus replacement service |
|---|---|---|---|---|
| **a conspiracy of two** | | | | |
| **a magpie** | | | | |
| **an inside job** | | | | |
| **the postman** | | | | |

## Solution

| Start time | Investigator | Theory | Alibi |
|---|---|---|---|
| 8am | Ariadne | the postman | a bus replacement service |
| 9am | Hortensia | an inside job | the dentist |
| 10am | Fergus | a conspiracy of two | watching the snooker |
| 11am | Leopold | a magpie | no alibi whatsoever |

## How it falls out

1. [order] from clue 8 sleuth:Fergus: ruled out position(s) 1,4
2. [order] from clue 7 alibi:a bus replacement service: ruled out position(s) 2,4
3. [order] from clue 6 theory:the postman: ruled out position(s) 4
4. [order] from clue 8 theory:a magpie: ruled out position(s) 2
5. [order] from clue 5 alibi:the dentist: ruled out position(s) 3,4
6. [order] from clue 4 alibi:watching the snooker: ruled out position(s) 1,4
7. [order] from clue 3 theory:an inside job: ruled out position(s) 1,3
8. [order] from clue 2 sleuth:Hortensia: ruled out position(s) 1,3,4
9. [direct] from clue 1 sleuth:Ariadne: ruled out position(s) 2,4
10. [bijection] alibi:no alibi whatsoever: ruled out position(s) 1,2,3
11. [bijection] sleuth:Fergus: ruled out position(s) 2
12. [bijection] sleuth:Leopold: ruled out position(s) 2
13. [bijection] sleuth:Leopold: ruled out position(s) 1,3
14. [order] from clue 8 theory:a magpie: ruled out position(s) 1,3
15. [order] from clue 8 theory:the postman: ruled out position(s) 3
16. [order] from clue 5 alibi:the dentist: ruled out position(s) 1
17. [bijection] alibi:watching the snooker: ruled out position(s) 2
18. [bijection] alibi:a bus replacement service: ruled out position(s) 3
19. [bijection] sleuth:Ariadne: ruled out position(s) 3
20. [bijection] theory:a conspiracy of two: ruled out position(s) 4
21. [bijection] theory:an inside job: ruled out position(s) 4
22. [bijection] theory:a conspiracy of two: ruled out position(s) 1,2
23. [bijection] theory:the postman: ruled out position(s) 2

---

<sub>seed `2026172986311` &middot; score 5.13 &middot; atoms 8 &middot; positives 1 &middot; solved by order</sub>
