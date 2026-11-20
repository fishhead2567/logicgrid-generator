# The Crossings to Inverlaig

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `5c695503658f`

## Introduction

The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.
Five skippers are involved. Determine each skipper's start time and cargo.
- **Skipper**: Fearghas, Eilidh, Ruaridh, Calla and Murdo.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Notable cargo**: a refrigerated van, a brass band, a consignment of bees, a church organ and a wedding party.
Every skipper has a different start time and cargo, so within each category every item is used exactly once.

## Clues

1. Calla sails at noon.
2. Fearghas carries a wedding party.
3. Ruaridh carries a refrigerated van.
4. 8am is exactly one hour earlier than the skipper who carries a consignment of bees, with no start time in between.
5. Murdo is earlier than 9am in start time order.
6. Fearghas is exactly one hour earlier than the skipper who carries a brass band, with no start time in between.

## Solving chart

*Start time vs Skipper*

| | Fearghas | Eilidh | Ruaridh | Calla | Murdo |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Notable cargo*

| | a refrigerated van | a brass band | a consignment of bees | a church organ | a wedding party |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Skipper vs Notable cargo*

| | a refrigerated van | a brass band | a consignment of bees | a church organ | a wedding party |
|---|---|---|---|---|---|
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |
| **Ruaridh** | | | | | |
| **Calla** | | | | | |
| **Murdo** | | | | | |

## Solution

| Start time | Skipper | Notable cargo |
|---|---|---|
| 8am | Murdo | a church organ |
| 9am | Eilidh | a consignment of bees |
| 10am | Ruaridh | a refrigerated van |
| 11am | Fearghas | a wedding party |
| noon | Calla | a brass band |

## How it falls out

1. [direct] from clue 2 skipper:Calla: ruled out position(s) 1,2,3,4
2. [bijection] skipper:Fearghas: ruled out position(s) 5
3. [bijection] skipper:Eilidh: ruled out position(s) 5
4. [bijection] skipper:Ruaridh: ruled out position(s) 5
5. [bijection] skipper:Murdo: ruled out position(s) 5
6. [direct] from clue 1 cargo:a refrigerated van: ruled out position(s) 5
7. [direct] from clue 6 cargo:a wedding party: ruled out position(s) 5
8. [order] from clue 5 cargo:a consignment of bees: ruled out position(s) 1,3,4,5
9. [order] from clue 4 cargo:a brass band: ruled out position(s) 1
10. [order] from clue 3 skipper:Murdo: ruled out position(s) 2,3,4
11. [bijection] cargo:a refrigerated van: ruled out position(s) 2
12. [bijection] cargo:a brass band: ruled out position(s) 2
13. [bijection] cargo:a church organ: ruled out position(s) 2
14. [bijection] cargo:a wedding party: ruled out position(s) 2
15. [bijection] skipper:Fearghas: ruled out position(s) 1
16. [bijection] skipper:Eilidh: ruled out position(s) 1
17. [bijection] skipper:Ruaridh: ruled out position(s) 1
18. [direct] from clue 6 cargo:a wedding party: ruled out position(s) 1
19. [direct] from clue 6 skipper:Fearghas: ruled out position(s) 2
20. [order] from clue 4 cargo:a brass band: ruled out position(s) 3
21. [direct] from clue 1 cargo:a refrigerated van: ruled out position(s) 1
22. [direct] from clue 1 skipper:Ruaridh: ruled out position(s) 2
23. [bijection] cargo:a church organ: ruled out position(s) 3,4,5
24. [bijection] skipper:Eilidh: ruled out position(s) 3,4
25. [bijection] cargo:a brass band: ruled out position(s) 4
26. [order] from clue 4 skipper:Fearghas: ruled out position(s) 3
27. [direct] from clue 6 cargo:a wedding party: ruled out position(s) 3
28. [bijection] cargo:a refrigerated van: ruled out position(s) 4
29. [bijection] skipper:Ruaridh: ruled out position(s) 4

---

<sub>seed `2026172938797` &middot; score 4.38 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
