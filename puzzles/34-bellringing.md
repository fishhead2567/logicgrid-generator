# The Quarter-Peal at St Botolph's

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `da3fb11dd65d`

## Introduction

The Tuesday practice, and a tower captain keeping a ledger of everyone's mistakes.
Five ringers are involved. Determine each ringer's round, bell and slip.
- **Ringer**: Fenwick, Lavinia, Dorcas, Ambrose and Prudence.
- **Round** (listed from earlier to later): round one, round two, round three, round four and round five.
- **Bell**: the fifth, the fourth, the tenor, the sharp second and the third.
- **Slip**: a fired shot, a missed dodge, a dropped rope, nothing at all and a clipped backstroke.
Every ringer has a different round, bell and slip, so within each category every item is used exactly once.

## Clues

1. Round two is exactly one round earlier than Dorcas, with no round in between. The ringer who takes the tenor is later than round two in round order.
2. The ringer who is blamed for a missed dodge and round two are exactly one round apart in round order, in one direction or the other.
3. The ringer who is blamed for nothing at all and round four are exactly one round apart in round order, in one direction or the other.
4. Ambrose does not ring in round one. The ringer who takes the tenor falls somewhere between Ambrose and Fenwick in round order.
5. At least one of the following holds, and possibly more than one: (a) The ringer who takes the tenor is later than round four in round order. (b) The ringer who takes the fifth and Fenwick both sit at odd-numbered rounds or both at even-numbered rounds.
6. The ringer who takes the fourth and the ringer who is blamed for a clipped backstroke are exactly one round apart in round order, in one direction or the other.
7. Lavinia falls somewhere between the ringer who is blamed for a clipped backstroke and the ringer who is blamed for a dropped rope in round order.
8. The ringer who takes the tenor and the ringer who is blamed for a dropped rope are exactly three rounds apart in round order.
9. The ringer who is blamed for a clipped backstroke is exactly one round earlier than the ringer who takes the third, with no round in between.

## Solving chart

*Round vs Ringer*

| | Fenwick | Lavinia | Dorcas | Ambrose | Prudence |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Round vs Bell*

| | the fifth | the fourth | the tenor | the sharp second | the third |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Round vs Slip*

| | a fired shot | a missed dodge | a dropped rope | nothing at all | a clipped backstroke |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Ringer vs Bell*

| | the fifth | the fourth | the tenor | the sharp second | the third |
|---|---|---|---|---|---|
| **Fenwick** | | | | | |
| **Lavinia** | | | | | |
| **Dorcas** | | | | | |
| **Ambrose** | | | | | |
| **Prudence** | | | | | |

*Ringer vs Slip*

| | a fired shot | a missed dodge | a dropped rope | nothing at all | a clipped backstroke |
|---|---|---|---|---|---|
| **Fenwick** | | | | | |
| **Lavinia** | | | | | |
| **Dorcas** | | | | | |
| **Ambrose** | | | | | |
| **Prudence** | | | | | |

*Bell vs Slip*

| | a fired shot | a missed dodge | a dropped rope | nothing at all | a clipped backstroke |
|---|---|---|---|---|---|
| **the fifth** | | | | | |
| **the fourth** | | | | | |
| **the tenor** | | | | | |
| **the sharp second** | | | | | |
| **the third** | | | | | |

## Solution

| Round | Ringer | Bell | Slip |
|---|---|---|---|
| round one | Fenwick | the fifth | a dropped rope |
| round two | Lavinia | the sharp second | a fired shot |
| round three | Dorcas | the fourth | a missed dodge |
| round four | Prudence | the tenor | a clipped backstroke |
| round five | Ambrose | the third | nothing at all |

## How it falls out

1. [direct] from clue 7 ringer:Ambrose: ruled out position(s) 1
2. [order] from clue 11 ringer:Dorcas: ruled out position(s) 1,2,4,5
3. [order] from clue 10 ringer:Lavinia: ruled out position(s) 1,5
4. [order] from clue 6 bell:the tenor: ruled out position(s) 1,5
5. [order] from clue 5 bell:the tenor: ruled out position(s) 3
6. [order] from clue 5 slip:a dropped rope: ruled out position(s) 2,3,4
7. [order] from clue 6 ringer:Fenwick: ruled out position(s) 4
8. [order] from clue 4 slip:nothing at all: ruled out position(s) 1,2,4
9. [order] from clue 3 slip:a clipped backstroke: ruled out position(s) 5
10. [order] from clue 3 bell:the third: ruled out position(s) 1
11. [order] from clue 2 slip:a missed dodge: ruled out position(s) 2,4,5
12. [order] from clue 1 bell:the tenor: ruled out position(s) 2
13. [order] from clue 6 ringer:Ambrose: ruled out position(s) 4
14. [order] from clue 5 slip:a dropped rope: ruled out position(s) 5
15. [order] from clue 10 ringer:Lavinia: ruled out position(s) 4
16. [order] from clue 10 slip:a clipped backstroke: ruled out position(s) 1,2
17. [order] from clue 8 bell:the fourth: ruled out position(s) 1
18. [order] from clue 3 bell:the third: ruled out position(s) 2,3
19. [bijection] bell:the fifth: ruled out position(s) 4
20. [bijection] bell:the fourth: ruled out position(s) 4
21. [bijection] bell:the sharp second: ruled out position(s) 4
22. [bijection] bell:the third: ruled out position(s) 4
23. [bijection] ringer:Fenwick: ruled out position(s) 3
24. [bijection] ringer:Lavinia: ruled out position(s) 3
25. [bijection] ringer:Ambrose: ruled out position(s) 3
26. [bijection] ringer:Prudence: ruled out position(s) 3
27. [bijection] ringer:Prudence: ruled out position(s) 1,2,5
28. [bijection] slip:a fired shot: ruled out position(s) 1
29. [bijection] slip:a missed dodge: ruled out position(s) 1
30. [bijection] slip:a fired shot: ruled out position(s) 3,4,5
31. [order] from clue 3 slip:a clipped backstroke: ruled out position(s) 3
32. [order] from clue 8 bell:the fourth: ruled out position(s) 2
33. [bijection] bell:the fifth: ruled out position(s) 5
34. [bijection] bell:the fourth: ruled out position(s) 5
35. [bijection] bell:the sharp second: ruled out position(s) 5
36. [bijection] ringer:Fenwick: ruled out position(s) 2
37. [bijection] ringer:Ambrose: ruled out position(s) 2
38. [bijection] ringer:Fenwick: ruled out position(s) 5
39. [bijection] slip:nothing at all: ruled out position(s) 3
40. [bijection] bell:the fifth: ruled out position(s) 3
_... and 3 further steps._

---

<sub>seed `2026173044688` &middot; score 8.7392 &middot; atoms 11 &middot; positives 0 &middot; solved by disjunction</sub>
