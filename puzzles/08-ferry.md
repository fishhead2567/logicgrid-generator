# The Crossings to Inverlaig

*The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.*

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `ed9fb1307098`

## Introduction

There are 5 crossings. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different crossing.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m., 11 a.m. and noon.
- **Skipper**: Senga, Eilidh, Calla, Tormod and Fearghas.
- **Notable cargo**: a consignment of bees, a church organ, a film crew and no permits, a refrigerated van and a wedding party.
The hours above are listed in order, from 8 a.m. to noon.

## Clues

1. Eilidh's start time is earlier than 11 a.m.. A refrigerated van goes with 11 a.m..
2. Calla's start time is earlier than a film crew and no permits' start time. Calla goes with 10 a.m..
3. A wedding party goes with Tormod.
4. A refrigerated van goes with Senga.
5. A church organ's start time is earlier than Tormod's start time.

## Solving chart

*Start time vs Skipper*

| | Senga | Eilidh | Calla | Tormod | Fearghas |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Notable cargo*

| | a consignment of bees | a church organ | a film crew and no permits | a refrigerated van | a wedding party |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Skipper vs Notable cargo*

| | a consignment of bees | a church organ | a film crew and no permits | a refrigerated van | a wedding party |
|---|---|---|---|---|---|
| **Senga** | | | | | |
| **Eilidh** | | | | | |
| **Calla** | | | | | |
| **Tormod** | | | | | |
| **Fearghas** | | | | | |

## Solution

| Start time | Skipper | Notable cargo |
|---|---|---|
| 8 a.m. | Eilidh | a church organ |
| 9 a.m. | Tormod | a wedding party |
| 10 a.m. | Calla | a consignment of bees |
| 11 a.m. | Senga | a refrigerated van |
| noon | Fearghas | a film crew and no permits |

## How it falls out

1. [direct] from clue 5 skipper:Calla: ruled out position(s) 1,2,4,5
2. [direct] from clue 2 cargo:a refrigerated van: ruled out position(s) 1,2,3,5
3. [direct] from clue 7 skipper:Senga: ruled out position(s) 1,2,3,5
4. [bijection] cargo:a consignment of bees: ruled out position(s) 4
5. [bijection] cargo:a church organ: ruled out position(s) 4
6. [bijection] cargo:a film crew and no permits: ruled out position(s) 4
7. [bijection] cargo:a wedding party: ruled out position(s) 4
8. [bijection] skipper:Eilidh: ruled out position(s) 3,4
9. [bijection] skipper:Tormod: ruled out position(s) 3,4
10. [bijection] skipper:Fearghas: ruled out position(s) 3,4
11. [direct] from clue 4 cargo:a wedding party: ruled out position(s) 3
12. [order] from clue 6 skipper:Eilidh: ruled out position(s) 5
13. [order] from clue 3 cargo:a film crew and no permits: ruled out position(s) 1,2,3
14. [order] from clue 1 cargo:a church organ: ruled out position(s) 5
15. [order] from clue 1 skipper:Tormod: ruled out position(s) 1
16. [direct] from clue 4 cargo:a wedding party: ruled out position(s) 1
17. [bijection] cargo:a consignment of bees: ruled out position(s) 5
18. [bijection] cargo:a wedding party: ruled out position(s) 5
19. [direct] from clue 4 skipper:Tormod: ruled out position(s) 5
20. [order] from clue 1 cargo:a church organ: ruled out position(s) 2,3
21. [bijection] cargo:a consignment of bees: ruled out position(s) 1,2
22. [bijection] skipper:Eilidh: ruled out position(s) 2
23. [bijection] skipper:Fearghas: ruled out position(s) 2
24. [bijection] skipper:Fearghas: ruled out position(s) 1

---

<sub>seed `2026172638788` &middot; score 4.14 &middot; atoms 7 &middot; positives 4 &middot; solved by order</sub>
