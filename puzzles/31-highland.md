# The Heavies at Kinloch Rannoch

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `4e68c71b9042`

## Introduction

The heavy events, measured to the foot, in a field where the wind counts for more than anybody admits.
Five throwers are involved. Determine each thrower's best throw, event and grumble.
- **Thrower**: Duncan Rait, Lachlan Cree, Angus Dunbar, Morag Inglis and Isla Kinnear.
- **Best throw** (listed from shorter to longer): 28 feet, 32 feet, 36 feet, 40 feet and 44 feet.
- **Event**: the open stone, the Scottish hammer, the Braemar stone, the caber toss and the sheaf toss.
- **Grumble**: no excuse whatsoever, a turned ankle, a slipped grip, a soft run-up and a crosswind.
Every thrower has a different best throw, event and grumble, so within each category every item is used exactly once.

## Clues

1. The thrower who competes in the sheaf toss throws 40 feet.
2. The thrower who complains of a slipped grip falls somewhere between 28 feet and Angus Dunbar in best throw order.
3. The thrower who complains of a crosswind and 28 feet are exactly one throw step apart in best throw order, in one direction or the other.
4. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The thrower who competes in the Scottish hammer complains of a soft run-up. (b) The thrower who competes in the Braemar stone does not throw 28 feet.
5. The thrower who competes in the Braemar stone and 28 feet are exactly one throw step apart in best throw order, in one direction or the other.
6. At least one of the following holds, and possibly more than one: (a) Angus Dunbar does not complain of a soft run-up. (b) Lachlan Cree does not complain of no excuse whatsoever.
7. At least one of the following holds, and possibly more than one: (a) The thrower who complains of a turned ankle and Morag Inglis are exactly one throw step apart in best throw order, in one direction or the other. (b) Lachlan Cree is shorter than the thrower who complains of no excuse whatsoever in best throw order.
8. The thrower who complains of a turned ankle and Isla Kinnear are exactly one throw step apart in best throw order, in one direction or the other.
9. The thrower who complains of a slipped grip is shorter than the thrower who competes in the open stone in best throw order.
10. Morag Inglis is exactly one throw step shorter than the thrower who competes in the caber toss, with no best throw in between.

## Solving chart

*Best throw vs Thrower*

| | Duncan Rait | Lachlan Cree | Angus Dunbar | Morag Inglis | Isla Kinnear |
|---|---|---|---|---|---|
| **28 feet** | | | | | |
| **32 feet** | | | | | |
| **36 feet** | | | | | |
| **40 feet** | | | | | |
| **44 feet** | | | | | |

*Best throw vs Event*

| | the open stone | the Scottish hammer | the Braemar stone | the caber toss | the sheaf toss |
|---|---|---|---|---|---|
| **28 feet** | | | | | |
| **32 feet** | | | | | |
| **36 feet** | | | | | |
| **40 feet** | | | | | |
| **44 feet** | | | | | |

*Best throw vs Grumble*

| | no excuse whatsoever | a turned ankle | a slipped grip | a soft run-up | a crosswind |
|---|---|---|---|---|---|
| **28 feet** | | | | | |
| **32 feet** | | | | | |
| **36 feet** | | | | | |
| **40 feet** | | | | | |
| **44 feet** | | | | | |

*Thrower vs Event*

| | the open stone | the Scottish hammer | the Braemar stone | the caber toss | the sheaf toss |
|---|---|---|---|---|---|
| **Duncan Rait** | | | | | |
| **Lachlan Cree** | | | | | |
| **Angus Dunbar** | | | | | |
| **Morag Inglis** | | | | | |
| **Isla Kinnear** | | | | | |

*Thrower vs Grumble*

| | no excuse whatsoever | a turned ankle | a slipped grip | a soft run-up | a crosswind |
|---|---|---|---|---|---|
| **Duncan Rait** | | | | | |
| **Lachlan Cree** | | | | | |
| **Angus Dunbar** | | | | | |
| **Morag Inglis** | | | | | |
| **Isla Kinnear** | | | | | |

*Event vs Grumble*

| | no excuse whatsoever | a turned ankle | a slipped grip | a soft run-up | a crosswind |
|---|---|---|---|---|---|
| **the open stone** | | | | | |
| **the Scottish hammer** | | | | | |
| **the Braemar stone** | | | | | |
| **the caber toss** | | | | | |
| **the sheaf toss** | | | | | |

## Solution

| Best throw | Thrower | Event | Grumble |
|---|---|---|---|
| 28 feet | Duncan Rait | the Scottish hammer | no excuse whatsoever |
| 32 feet | Morag Inglis | the Braemar stone | a crosswind |
| 36 feet | Lachlan Cree | the caber toss | a turned ankle |
| 40 feet | Isla Kinnear | the sheaf toss | a slipped grip |
| 44 feet | Angus Dunbar | the open stone | a soft run-up |

## How it falls out

1. [direct] from clue 3 event:the sheaf toss: ruled out position(s) 1,2,3,5
2. [bijection] event:the open stone: ruled out position(s) 4
3. [bijection] event:the Scottish hammer: ruled out position(s) 4
4. [bijection] event:the Braemar stone: ruled out position(s) 4
5. [bijection] event:the caber toss: ruled out position(s) 4
6. [order] from clue 8 thrower:Morag Inglis: ruled out position(s) 3,5
7. [order] from clue 8 event:the caber toss: ruled out position(s) 1
8. [order] from clue 7 grumble:a slipped grip: ruled out position(s) 1,5
9. [order] from clue 7 thrower:Angus Dunbar: ruled out position(s) 1,2
10. [order] from clue 5 grumble:a crosswind: ruled out position(s) 1,3,4,5
11. [order] from clue 2 event:the Braemar stone: ruled out position(s) 1,3,5
12. [order] from clue 1 event:the open stone: ruled out position(s) 1,2
13. [bijection] event:the Scottish hammer: ruled out position(s) 2
14. [bijection] event:the caber toss: ruled out position(s) 2
15. [bijection] event:the Scottish hammer: ruled out position(s) 3,5
16. [bijection] grumble:no excuse whatsoever: ruled out position(s) 2
17. [bijection] grumble:a turned ankle: ruled out position(s) 2
18. [bijection] grumble:a slipped grip: ruled out position(s) 2
19. [bijection] grumble:a soft run-up: ruled out position(s) 2
20. [order] from clue 7 thrower:Angus Dunbar: ruled out position(s) 3
21. [order] from clue 1 event:the open stone: ruled out position(s) 3
22. [order] from clue 4 thrower:Isla Kinnear: ruled out position(s) 1
23. [order] from clue 8 thrower:Morag Inglis: ruled out position(s) 1
24. [bijection] event:the caber toss: ruled out position(s) 5
25. [order] from clue 8 thrower:Morag Inglis: ruled out position(s) 4
26. [bijection] thrower:Duncan Rait: ruled out position(s) 2
27. [bijection] thrower:Lachlan Cree: ruled out position(s) 2
28. [bijection] thrower:Isla Kinnear: ruled out position(s) 2
29. [order] from clue 4 grumble:a turned ankle: ruled out position(s) 1
30. [disjunction] from clue 6 grumble:a soft run-up: ruled out position(s) 1
31. [bijection] grumble:no excuse whatsoever: ruled out position(s) 3,4,5
32. [disjunction] from clue 10 grumble:a turned ankle: ruled out position(s) 4,5
33. [order] from clue 4 thrower:Isla Kinnear: ruled out position(s) 3,5
34. [bijection] grumble:a slipped grip: ruled out position(s) 3
35. [bijection] grumble:a soft run-up: ruled out position(s) 3
36. [bijection] grumble:a soft run-up: ruled out position(s) 4
37. [bijection] thrower:Duncan Rait: ruled out position(s) 4
38. [bijection] thrower:Lachlan Cree: ruled out position(s) 4
39. [bijection] thrower:Angus Dunbar: ruled out position(s) 4
40. [disjunction] from clue 9 thrower:Lachlan Cree: ruled out position(s) 1,5
_... and 1 further steps._

---

<sub>seed `2026172920928` &middot; score 9.4733 &middot; atoms 10 &middot; positives 1 &middot; solved by disjunction</sub>
