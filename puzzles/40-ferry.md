# The Crossings to Inverlaig

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `d5e7c2e47f6f`

## Introduction

The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.
Five skippers are involved. Determine each skipper's start time, cargo and vessel.
- **Skipper**: Ruaridh, Murdo, Senga, Tormod and Fearghas.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Notable cargo**: a consignment of bees; a church organ; a brass band; a film crew and no permits; and a refrigerated van.
- **Vessel**: the Tern, the Broch Maid, the Siller Grey, the Three Brothers and the Kelpie.
Every skipper has a different start time, cargo and vessel, so within each category every item is used exactly once.

## Clues

1. The skipper who carries a film crew and no permits commands the Tern.
2. 9am is exactly one hour earlier than Fearghas, with no start time in between.
3. Tormod is exactly one hour earlier than 9am, with no start time in between.
4. The skipper who carries a brass band falls somewhere between 11am and the skipper who commands the Broch Maid in start time order.
5. At least one of the following holds, and possibly more than one: (a) Ruaridh is earlier than noon in start time order. (b) The skipper who carries a church organ commands the Kelpie.
6. 9am is exactly one hour earlier than the skipper who carries a church organ, with no start time in between.
7. The skipper who carries a brass band and Senga both sit at odd-numbered hours or both at even-numbered hours.
8. At least one of the following holds, and possibly more than one: (a) Fearghas and the skipper who commands the Broch Maid are exactly one hour apart in start time order, in one direction or the other. (b) The skipper who carries a church organ and the skipper who commands the Three Brothers both sit at odd-numbered hours or both at even-numbered hours.
9. The skipper who commands the Three Brothers is earlier than Senga in start time order. The skipper who carries a refrigerated van is earlier than Senga in start time order.
10. The skipper who carries a church organ is exactly one hour earlier than the skipper who commands the Siller Grey, with no start time in between.

## Solving chart

*Start time vs Skipper*

| | Ruaridh | Murdo | Senga | Tormod | Fearghas |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Notable cargo*

| | a consignment of bees | a church organ | a brass band | a film crew and no permits | a refrigerated van |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Vessel*

| | the Tern | the Broch Maid | the Siller Grey | the Three Brothers | the Kelpie |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Skipper vs Notable cargo*

| | a consignment of bees | a church organ | a brass band | a film crew and no permits | a refrigerated van |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Murdo** | | | | | |
| **Senga** | | | | | |
| **Tormod** | | | | | |
| **Fearghas** | | | | | |

*Skipper vs Vessel*

| | the Tern | the Broch Maid | the Siller Grey | the Three Brothers | the Kelpie |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Murdo** | | | | | |
| **Senga** | | | | | |
| **Tormod** | | | | | |
| **Fearghas** | | | | | |

*Notable cargo vs Vessel*

| | the Tern | the Broch Maid | the Siller Grey | the Three Brothers | the Kelpie |
|---|---|---|---|---|---|
| **a consignment of bees** | | | | | |
| **a church organ** | | | | | |
| **a brass band** | | | | | |
| **a film crew and no permits** | | | | | |
| **a refrigerated van** | | | | | |

## Solution

| Start time | Skipper | Notable cargo | Vessel |
|---|---|---|---|
| 8am | Tormod | a refrigerated van | the Broch Maid |
| 9am | Ruaridh | a brass band | the Kelpie |
| 10am | Fearghas | a church organ | the Three Brothers |
| 11am | Senga | a consignment of bees | the Siller Grey |
| noon | Murdo | a film crew and no permits | the Tern |

## How it falls out

1. [order] from clue 10 skipper:Fearghas: ruled out position(s) 1,2,4,5
2. [order] from clue 9 cargo:a refrigerated van: ruled out position(s) 5
3. [order] from clue 9 skipper:Senga: ruled out position(s) 1
4. [order] from clue 7 cargo:a church organ: ruled out position(s) 1,2,4,5
5. [order] from clue 6 skipper:Tormod: ruled out position(s) 2,3,4,5
6. [order] from clue 5 vessel:the Siller Grey: ruled out position(s) 1,2,3,5
7. [order] from clue 3 cargo:a brass band: ruled out position(s) 1,4,5
8. [order] from clue 3 vessel:the Broch Maid: ruled out position(s) 3,4,5
9. [order] from clue 1 vessel:the Three Brothers: ruled out position(s) 5
10. [bijection] cargo:a consignment of bees: ruled out position(s) 3
11. [bijection] cargo:a brass band: ruled out position(s) 3
12. [bijection] cargo:a film crew and no permits: ruled out position(s) 3
13. [bijection] cargo:a refrigerated van: ruled out position(s) 3
14. [bijection] skipper:Ruaridh: ruled out position(s) 1,3
15. [bijection] skipper:Murdo: ruled out position(s) 1,3
16. [bijection] skipper:Senga: ruled out position(s) 3
17. [bijection] vessel:the Tern: ruled out position(s) 4
18. [bijection] vessel:the Three Brothers: ruled out position(s) 4
19. [bijection] vessel:the Kelpie: ruled out position(s) 4
20. [direct] from clue 2 cargo:a film crew and no permits: ruled out position(s) 4
21. [direct] from clue 2 vessel:the Tern: ruled out position(s) 3
22. [order] from clue 11 skipper:Senga: ruled out position(s) 5
23. [order] from clue 9 cargo:a refrigerated van: ruled out position(s) 4
24. [order] from clue 3 vessel:the Broch Maid: ruled out position(s) 2
25. [bijection] cargo:a consignment of bees: ruled out position(s) 2
26. [bijection] cargo:a film crew and no permits: ruled out position(s) 2
27. [bijection] cargo:a refrigerated van: ruled out position(s) 2
28. [bijection] cargo:a consignment of bees: ruled out position(s) 1,5
29. [bijection] vessel:the Tern: ruled out position(s) 1
30. [bijection] vessel:the Three Brothers: ruled out position(s) 1
31. [bijection] vessel:the Kelpie: ruled out position(s) 1
32. [order] from clue 1 skipper:Senga: ruled out position(s) 2
33. [direct] from clue 2 cargo:a film crew and no permits: ruled out position(s) 1
34. [direct] from clue 2 vessel:the Tern: ruled out position(s) 2
35. [bijection] skipper:Ruaridh: ruled out position(s) 4
36. [bijection] skipper:Murdo: ruled out position(s) 4
37. [bijection] vessel:the Kelpie: ruled out position(s) 5
38. [disjunction] from clue 8 vessel:the Three Brothers: ruled out position(s) 2
39. [bijection] vessel:the Kelpie: ruled out position(s) 3
40. [disjunction] from clue 4 skipper:Ruaridh: ruled out position(s) 5
_... and 1 further steps._

---

<sub>seed `2026172996925` &middot; score 9.1022 &middot; atoms 11 &middot; positives 1 &middot; solved by disjunction</sub>
