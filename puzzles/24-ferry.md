# The Crossings to Inverlaig

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `e45cb743da43`

## Introduction

The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.
Five skippers are involved. Determine each skipper's start time, cargo, vessel and reason.
- **Skipper**: Ruaridh, Senga, Tormod, Fearghas and Eilidh.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Notable cargo**: a wedding party; a brass band; nineteen sheep; a film crew and no permits; and a church organ.
- **Vessel**: the Steadfast, the Siller Grey, the Three Brothers, the Kelpie and the Ailsa Belle.
- **Delay blamed on**: fog, paperwork, the tide, a slipway repair and a missing deckhand.
Every skipper has a different start time, cargo, vessel and reason, so within each category every item is used exactly once.

## Clues

1. The skipper who commands the Ailsa Belle sails at 8am. The skipper who blames a slipway repair and 8am are exactly four hours apart in start time order.
2. The skipper who carries a church organ commands the Three Brothers.
3. Senga does not sail at noon.
4. The skipper who commands the Steadfast is exactly one hour earlier than the skipper who carries a brass band, with no start time in between.
5. The skipper who carries a wedding party is exactly one hour earlier than Tormod, with no start time in between.
6. The skipper who carries a brass band and the skipper who blames the tide are exactly four hours apart in start time order.
7. Eilidh is exactly one hour earlier than the skipper who blames a missing deckhand, with no start time in between.
8. The skipper who carries nineteen sheep and the skipper who blames the tide are exactly three hours apart in start time order.
9. The skipper who blames fog is exactly one hour earlier than the skipper who carries a church organ, with no start time in between.
10. Senga does not blame a missing deckhand. The skipper who commands the Kelpie falls somewhere between the skipper who blames a missing deckhand and Ruaridh in start time order.

## Solving chart

*Start time vs Skipper*

| | Ruaridh | Senga | Tormod | Fearghas | Eilidh |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Notable cargo*

| | a wedding party | a brass band | nineteen sheep | a film crew and no permits | a church organ |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Vessel*

| | the Steadfast | the Siller Grey | the Three Brothers | the Kelpie | the Ailsa Belle |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Delay blamed on*

| | fog | paperwork | the tide | a slipway repair | a missing deckhand |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Skipper vs Notable cargo*

| | a wedding party | a brass band | nineteen sheep | a film crew and no permits | a church organ |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Senga** | | | | | |
| **Tormod** | | | | | |
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |

*Skipper vs Vessel*

| | the Steadfast | the Siller Grey | the Three Brothers | the Kelpie | the Ailsa Belle |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Senga** | | | | | |
| **Tormod** | | | | | |
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |

*Skipper vs Delay blamed on*

| | fog | paperwork | the tide | a slipway repair | a missing deckhand |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Senga** | | | | | |
| **Tormod** | | | | | |
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |

*Notable cargo vs Vessel*

| | the Steadfast | the Siller Grey | the Three Brothers | the Kelpie | the Ailsa Belle |
|---|---|---|---|---|---|
| **a wedding party** | | | | | |
| **a brass band** | | | | | |
| **nineteen sheep** | | | | | |
| **a film crew and no permits** | | | | | |
| **a church organ** | | | | | |

*Notable cargo vs Delay blamed on*

| | fog | paperwork | the tide | a slipway repair | a missing deckhand |
|---|---|---|---|---|---|
| **a wedding party** | | | | | |
| **a brass band** | | | | | |
| **nineteen sheep** | | | | | |
| **a film crew and no permits** | | | | | |
| **a church organ** | | | | | |

*Vessel vs Delay blamed on*

| | fog | paperwork | the tide | a slipway repair | a missing deckhand |
|---|---|---|---|---|---|
| **the Steadfast** | | | | | |
| **the Siller Grey** | | | | | |
| **the Three Brothers** | | | | | |
| **the Kelpie** | | | | | |
| **the Ailsa Belle** | | | | | |

## Solution

| Start time | Skipper | Notable cargo | Vessel | Delay blamed on |
|---|---|---|---|---|
| 8am | Ruaridh | a film crew and no permits | the Ailsa Belle | the tide |
| 9am | Eilidh | a wedding party | the Kelpie | fog |
| 10am | Tormod | a church organ | the Three Brothers | a missing deckhand |
| 11am | Senga | nineteen sheep | the Steadfast | paperwork |
| noon | Fearghas | a brass band | the Siller Grey | a slipway repair |

## How it falls out

1. [direct] from clue 8 vessel:the Ailsa Belle: ruled out position(s) 2,3,4,5
2. [direct] from clue 7 skipper:Senga: ruled out position(s) 5
3. [bijection] vessel:the Steadfast: ruled out position(s) 1
4. [bijection] vessel:the Siller Grey: ruled out position(s) 1
5. [bijection] vessel:the Three Brothers: ruled out position(s) 1
6. [bijection] vessel:the Kelpie: ruled out position(s) 1
7. [direct] from clue 6 cargo:a church organ: ruled out position(s) 1
8. [order] from clue 12 vessel:the Steadfast: ruled out position(s) 5
9. [order] from clue 12 cargo:a brass band: ruled out position(s) 1,2
10. [order] from clue 10 cargo:a brass band: ruled out position(s) 3,4
11. [order] from clue 10 delay:the tide: ruled out position(s) 2,3,4,5
12. [order] from clue 12 vessel:the Steadfast: ruled out position(s) 2,3
13. [order] from clue 9 vessel:the Kelpie: ruled out position(s) 5
14. [order] from clue 5 delay:fog: ruled out position(s) 5
15. [order] from clue 4 delay:a slipway repair: ruled out position(s) 1,2,3,4
16. [order] from clue 3 skipper:Eilidh: ruled out position(s) 5
17. [order] from clue 3 delay:a missing deckhand: ruled out position(s) 1
18. [order] from clue 2 cargo:a wedding party: ruled out position(s) 5
19. [order] from clue 2 skipper:Tormod: ruled out position(s) 1
20. [order] from clue 1 cargo:nineteen sheep: ruled out position(s) 1,2,3,5
21. [bijection] cargo:a wedding party: ruled out position(s) 4
22. [bijection] cargo:a film crew and no permits: ruled out position(s) 4,5
23. [bijection] cargo:a church organ: ruled out position(s) 4,5
24. [bijection] delay:fog: ruled out position(s) 1
25. [bijection] delay:paperwork: ruled out position(s) 1,5
26. [bijection] delay:a missing deckhand: ruled out position(s) 5
27. [bijection] vessel:the Siller Grey: ruled out position(s) 4
28. [bijection] vessel:the Three Brothers: ruled out position(s) 4
29. [bijection] vessel:the Kelpie: ruled out position(s) 4
30. [order] from clue 9 skipper:Ruaridh: ruled out position(s) 3
31. [order] from clue 3 skipper:Eilidh: ruled out position(s) 4
32. [direct] from clue 6 vessel:the Three Brothers: ruled out position(s) 5
33. [order] from clue 5 delay:fog: ruled out position(s) 3,4
34. [order] from clue 5 cargo:a church organ: ruled out position(s) 2
35. [direct] from clue 6 vessel:the Three Brothers: ruled out position(s) 2
36. [order] from clue 2 skipper:Tormod: ruled out position(s) 5
37. [bijection] cargo:a wedding party: ruled out position(s) 3
38. [bijection] cargo:a film crew and no permits: ruled out position(s) 3
39. [bijection] delay:paperwork: ruled out position(s) 2
40. [bijection] delay:a missing deckhand: ruled out position(s) 2
_... and 16 further steps._

---

<sub>seed `2026172765492` &middot; score 6.01 &middot; atoms 12 &middot; positives 2 &middot; solved by order</sub>
