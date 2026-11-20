# The Tuesday Pickleball Ladder

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `9e6dac0e321d`

## Introduction

The rec center runs a pickleball ladder on Tuesdays. Courts go by start time, and the sign-up sheet gets rewritten more than once.
Five players are involved. Determine each player's start time, paddle and gripe.
- **Player**: Ramesh, Buzz Kovacs, Yolanda, Dot Feeney and Arlene.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Paddle**: a bright orange paddle, a graphite paddle, a paddle with a taped grip, a hand-me-down paddle and a wooden loaner.
- **Gripe**: the sun, a wet court, a bad knee, the noisy court next door and a late night.
Every player has a different start time, paddle and gripe, so within each category every item is used exactly once.

## Clues

1. The player who blames a late night plays with a hand-me-down paddle.
2. Arlene does not play at 10am. The player who plays with a graphite paddle is later than 10am in start time order. Buzz Kovacs is later than 10am in start time order.
3. The player who blames a late night and noon are exactly one hour apart in start time order, in one direction or the other.
4. The player who plays with a hand-me-down paddle falls somewhere between the player who blames the noisy court next door and Arlene in start time order. Arlene does not play at 8am.
5. At least one of the following holds, and possibly more than one: (a) The player who blames the sun and the player who plays with a hand-me-down paddle are exactly one hour apart in start time order, in one direction or the other. (b) The player who plays with a wooden loaner is exactly one hour earlier than 11am, with no start time in between.
6. The player who plays with a bright orange paddle and Ramesh are exactly four hours apart in start time order.
7. The player who blames a bad knee falls somewhere between Buzz Kovacs and Yolanda in start time order.
8. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The player who blames the sun and Arlene are exactly one hour apart in start time order, in one direction or the other. (b) One of the player who plays with a hand-me-down paddle and Yolanda sits at an odd-numbered start time and the other at an even-numbered start time.

## Solving chart

*Start time vs Player*

| | Ramesh | Buzz Kovacs | Yolanda | Dot Feeney | Arlene |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Paddle*

| | a bright orange paddle | a graphite paddle | a paddle with a taped grip | a hand-me-down paddle | a wooden loaner |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Gripe*

| | the sun | a wet court | a bad knee | the noisy court next door | a late night |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Player vs Paddle*

| | a bright orange paddle | a graphite paddle | a paddle with a taped grip | a hand-me-down paddle | a wooden loaner |
|---|---|---|---|---|---|
| **Ramesh** | | | | | |
| **Buzz Kovacs** | | | | | |
| **Yolanda** | | | | | |
| **Dot Feeney** | | | | | |
| **Arlene** | | | | | |

*Player vs Gripe*

| | the sun | a wet court | a bad knee | the noisy court next door | a late night |
|---|---|---|---|---|---|
| **Ramesh** | | | | | |
| **Buzz Kovacs** | | | | | |
| **Yolanda** | | | | | |
| **Dot Feeney** | | | | | |
| **Arlene** | | | | | |

*Paddle vs Gripe*

| | the sun | a wet court | a bad knee | the noisy court next door | a late night |
|---|---|---|---|---|---|
| **a bright orange paddle** | | | | | |
| **a graphite paddle** | | | | | |
| **a paddle with a taped grip** | | | | | |
| **a hand-me-down paddle** | | | | | |
| **a wooden loaner** | | | | | |

## Solution

| Start time | Player | Paddle | Gripe |
|---|---|---|---|
| 8am | Yolanda | a bright orange paddle | a wet court |
| 9am | Arlene | a paddle with a taped grip | the sun |
| 10am | Dot Feeney | a wooden loaner | a bad knee |
| 11am | Buzz Kovacs | a hand-me-down paddle | a late night |
| noon | Ramesh | a graphite paddle | the noisy court next door |

## How it falls out

1. [direct] from clue 10 player:Arlene: ruled out position(s) 1
2. [direct] from clue 4 player:Arlene: ruled out position(s) 3
3. [order] from clue 11 gripe:a late night: ruled out position(s) 1,2,3,5
4. [order] from clue 7 player:Buzz Kovacs: ruled out position(s) 1,2,3
5. [order] from clue 6 paddle:a hand-me-down paddle: ruled out position(s) 1,5
6. [order] from clue 5 paddle:a graphite paddle: ruled out position(s) 1,2,3
7. [order] from clue 2 paddle:a bright orange paddle: ruled out position(s) 2,3,4
8. [order] from clue 2 player:Ramesh: ruled out position(s) 2,3,4
9. [order] from clue 1 gripe:a bad knee: ruled out position(s) 1,5
10. [order] from clue 1 player:Yolanda: ruled out position(s) 4,5
11. [direct] from clue 3 paddle:a hand-me-down paddle: ruled out position(s) 2,3
12. [order] from clue 6 gripe:the noisy court next door: ruled out position(s) 4
13. [order] from clue 6 player:Arlene: ruled out position(s) 4
14. [bijection] gripe:the sun: ruled out position(s) 4
15. [bijection] gripe:a wet court: ruled out position(s) 4
16. [bijection] gripe:a bad knee: ruled out position(s) 4
17. [bijection] paddle:a graphite paddle: ruled out position(s) 4
18. [bijection] paddle:a paddle with a taped grip: ruled out position(s) 4
19. [bijection] paddle:a wooden loaner: ruled out position(s) 4
20. [order] from clue 1 player:Yolanda: ruled out position(s) 3
21. [bijection] paddle:a bright orange paddle: ruled out position(s) 5
22. [bijection] paddle:a paddle with a taped grip: ruled out position(s) 5
23. [bijection] paddle:a wooden loaner: ruled out position(s) 5
24. [bijection] player:Dot Feeney: ruled out position(s) 1,2,4,5
25. [order] from clue 2 player:Ramesh: ruled out position(s) 1
26. [bijection] paddle:a paddle with a taped grip: ruled out position(s) 1
27. [bijection] paddle:a wooden loaner: ruled out position(s) 1
28. [bijection] player:Buzz Kovacs: ruled out position(s) 5
29. [bijection] player:Arlene: ruled out position(s) 5
30. [bijection] player:Yolanda: ruled out position(s) 2
31. [order] from clue 6 gripe:the noisy court next door: ruled out position(s) 1,2,3
32. [bijection] gripe:the sun: ruled out position(s) 5
33. [bijection] gripe:a wet court: ruled out position(s) 5
34. [disjunction] from clue 8 gripe:the sun: ruled out position(s) 1,3
35. [disjunction] from clue 9 paddle:a wooden loaner: ruled out position(s) 2
36. [bijection] gripe:a wet court: ruled out position(s) 2
37. [bijection] gripe:a bad knee: ruled out position(s) 2
38. [bijection] gripe:a wet court: ruled out position(s) 3
39. [bijection] paddle:a paddle with a taped grip: ruled out position(s) 3

---

<sub>seed `2026173128853` &middot; score 9.1022 &middot; atoms 11 &middot; positives 1 &middot; solved by disjunction</sub>
