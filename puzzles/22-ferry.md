# The Crossings to Inverlaig

*The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.*

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `20af1e5095ce`

## Introduction

There are 5 crossings. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different crossing.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m., 11 a.m. and noon.
- **Skipper**: Fearghas, Eilidh, Murdo, Calla and Senga.
- **Notable cargo**: a film crew and no permits, a refrigerated van, nineteen sheep, a consignment of bees and a church organ.
- **Delay blamed on**: a fouled propeller, a passenger's dog, a slipway repair, fog and a missing deckhand.
The hours above are listed in order, from 8 a.m. to noon.

## Clues

1. Calla falls somewhere between a consignment of bees and 9 a.m. in start time order. A consignment of bees goes with a slipway repair. A film crew and no permits goes with 9 a.m..
2. Murdo falls somewhere between nineteen sheep and noon in start time order.
3. Eilidh falls somewhere between a church organ and 10 a.m. in start time order.
4. A missing deckhand's start time is earlier than 10 a.m.. A missing deckhand does not go with Senga.
5. A fouled propeller does not go with 10 a.m..
6. A passenger's dog and 8 a.m. are exactly four hours apart in start time order.
7. A church organ does not go with Fearghas.
8. Senga's start time is earlier than a consignment of bees' start time.

## Solving chart

*Start time vs Skipper*

| | Fearghas | Eilidh | Murdo | Calla | Senga |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Notable cargo*

| | a film crew and no permits | a refrigerated van | nineteen sheep | a consignment of bees | a church organ |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Delay blamed on*

| | a fouled propeller | a passenger's dog | a slipway repair | fog | a missing deckhand |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Skipper vs Notable cargo*

| | a film crew and no permits | a refrigerated van | nineteen sheep | a consignment of bees | a church organ |
|---|---|---|---|---|---|
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |
| **Murdo** | | | | | |
| **Calla** | | | | | |
| **Senga** | | | | | |

*Skipper vs Delay blamed on*

| | a fouled propeller | a passenger's dog | a slipway repair | fog | a missing deckhand |
|---|---|---|---|---|---|
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |
| **Murdo** | | | | | |
| **Calla** | | | | | |
| **Senga** | | | | | |

*Notable cargo vs Delay blamed on*

| | a fouled propeller | a passenger's dog | a slipway repair | fog | a missing deckhand |
|---|---|---|---|---|---|
| **a film crew and no permits** | | | | | |
| **a refrigerated van** | | | | | |
| **nineteen sheep** | | | | | |
| **a consignment of bees** | | | | | |
| **a church organ** | | | | | |

## Solution

| Start time | Skipper | Notable cargo | Delay blamed on |
|---|---|---|---|
| 8 a.m. | Senga | a church organ | a fouled propeller |
| 9 a.m. | Eilidh | a film crew and no permits | a missing deckhand |
| 10 a.m. | Calla | nineteen sheep | fog |
| 11 a.m. | Murdo | a consignment of bees | a slipway repair |
| noon | Fearghas | a refrigerated van | a passenger's dog |

## How it falls out

1. [direct] from clue 8 cargo:a film crew and no permits: ruled out position(s) 1,3,4,5
2. [direct] from clue 2 delay:a fouled propeller: ruled out position(s) 3
3. [bijection] cargo:a refrigerated van: ruled out position(s) 2
4. [bijection] cargo:nineteen sheep: ruled out position(s) 2
5. [bijection] cargo:a consignment of bees: ruled out position(s) 2
6. [bijection] cargo:a church organ: ruled out position(s) 2
7. [direct] from clue 10 delay:a slipway repair: ruled out position(s) 2
8. [order] from clue 11 skipper:Calla: ruled out position(s) 1,2,5
9. [order] from clue 11 cargo:a consignment of bees: ruled out position(s) 1,3
10. [order] from clue 9 skipper:Eilidh: ruled out position(s) 1,3,5
11. [order] from clue 9 cargo:a church organ: ruled out position(s) 3,4
12. [order] from clue 6 skipper:Murdo: ruled out position(s) 1,5
13. [order] from clue 6 cargo:nineteen sheep: ruled out position(s) 4,5
14. [order] from clue 5 delay:a missing deckhand: ruled out position(s) 3,4,5
15. [order] from clue 4 delay:a passenger's dog: ruled out position(s) 1,2,3,4
16. [order] from clue 3 skipper:Senga: ruled out position(s) 5
17. [direct] from clue 10 delay:a slipway repair: ruled out position(s) 1,3
18. [bijection] delay:a fouled propeller: ruled out position(s) 5
19. [bijection] delay:a slipway repair: ruled out position(s) 5
20. [bijection] delay:fog: ruled out position(s) 5
21. [bijection] delay:fog: ruled out position(s) 1,2,4
22. [bijection] skipper:Fearghas: ruled out position(s) 1,2,3,4
23. [direct] from clue 7 cargo:a church organ: ruled out position(s) 5
24. [order] from clue 9 skipper:Eilidh: ruled out position(s) 4
25. [direct] from clue 10 cargo:a consignment of bees: ruled out position(s) 5
26. [order] from clue 11 skipper:Calla: ruled out position(s) 4
27. [order] from clue 3 skipper:Senga: ruled out position(s) 4
28. [bijection] cargo:a refrigerated van: ruled out position(s) 1,4
29. [bijection] cargo:nineteen sheep: ruled out position(s) 1
30. [bijection] cargo:a refrigerated van: ruled out position(s) 3
31. [bijection] delay:a fouled propeller: ruled out position(s) 4
32. [bijection] skipper:Murdo: ruled out position(s) 2,3
33. [bijection] skipper:Senga: ruled out position(s) 2,3
34. [direct] from clue 1 delay:a missing deckhand: ruled out position(s) 1
35. [bijection] delay:a fouled propeller: ruled out position(s) 2

---

<sub>seed `2026172749654` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
