# The Crossings to Inverlaig

*The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `4f8f847e661d`

## Introduction

There are 5 crossings. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different crossing.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m., 11 a.m. and noon.
- **Skipper**: Ruaridh, Senga, Calla, Fearghas and Murdo.
- **Vessel**: the Siller Grey, the Steadfast, the Three Brothers, the Tern and the Broch Maid.
The hours above are listed in order, from 8 a.m. to noon.

## Clues

1. Calla goes with 11 a.m..
2. 10 a.m. goes with the Three Brothers.
3. The Siller Grey's start time is earlier than 9 a.m..
4. 10 a.m. is immediately earlier than the Tern's start time, with no start time in between.
5. 11 a.m. is earlier than Murdo's start time.
6. Fearghas and the Tern are next to each other in start time order, in one order or the other.
7. Senga and the Broch Maid are next to each other in start time order, in one order or the other.

## Solving chart

*Start time vs Skipper*

| | Ruaridh | Senga | Calla | Fearghas | Murdo |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Vessel*

| | the Siller Grey | the Steadfast | the Three Brothers | the Tern | the Broch Maid |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Skipper vs Vessel*

| | the Siller Grey | the Steadfast | the Three Brothers | the Tern | the Broch Maid |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Senga** | | | | | |
| **Calla** | | | | | |
| **Fearghas** | | | | | |
| **Murdo** | | | | | |

## Solution

| Start time | Skipper | Vessel |
|---|---|---|
| 8 a.m. | Senga | the Siller Grey |
| 9 a.m. | Ruaridh | the Broch Maid |
| 10 a.m. | Fearghas | the Three Brothers |
| 11 a.m. | Calla | the Tern |
| noon | Murdo | the Steadfast |

## How it falls out

1. [direct] from clue 7 skipper:Calla: ruled out position(s) 1,2,3,5
2. [direct] from clue 5 vessel:the Three Brothers: ruled out position(s) 1,2,4,5
3. [bijection] skipper:Ruaridh: ruled out position(s) 4
4. [bijection] skipper:Senga: ruled out position(s) 4
5. [bijection] skipper:Fearghas: ruled out position(s) 4
6. [bijection] skipper:Murdo: ruled out position(s) 4
7. [bijection] vessel:the Siller Grey: ruled out position(s) 3
8. [bijection] vessel:the Steadfast: ruled out position(s) 3
9. [bijection] vessel:the Tern: ruled out position(s) 3
10. [bijection] vessel:the Broch Maid: ruled out position(s) 3
11. [order] from clue 6 skipper:Murdo: ruled out position(s) 1,2,3
12. [order] from clue 4 vessel:the Tern: ruled out position(s) 5
13. [order] from clue 3 vessel:the Tern: ruled out position(s) 1,2
14. [order] from clue 4 skipper:Fearghas: ruled out position(s) 1,2
15. [order] from clue 2 vessel:the Siller Grey: ruled out position(s) 2,4,5
16. [order] from clue 1 vessel:the Broch Maid: ruled out position(s) 5
17. [bijection] skipper:Ruaridh: ruled out position(s) 5
18. [bijection] skipper:Senga: ruled out position(s) 5
19. [bijection] skipper:Fearghas: ruled out position(s) 5
20. [bijection] vessel:the Steadfast: ruled out position(s) 1,4
21. [bijection] vessel:the Broch Maid: ruled out position(s) 1,4
22. [bijection] vessel:the Steadfast: ruled out position(s) 2
23. [order] from clue 1 skipper:Senga: ruled out position(s) 2
24. [bijection] skipper:Ruaridh: ruled out position(s) 3
25. [bijection] skipper:Senga: ruled out position(s) 3
26. [bijection] skipper:Ruaridh: ruled out position(s) 1

---

<sub>seed `2026172783112` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
