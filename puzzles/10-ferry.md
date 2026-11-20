# The Crossings to Inverlaig

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `585a94cbab89`

## Introduction

The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.
Five skippers are involved. Determine each skipper's start time, vessel and reason.
- **Skipper**: Calla, Eilidh, Tormod, Senga and Ruaridh.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Vessel**: the Ailsa Belle, the Tern, the Broch Maid, the Siller Grey and the Steadfast.
- **Delay blamed on**: fog, a missing deckhand, a fouled propeller, paperwork and a passenger's dog.
Every skipper has a different start time, vessel and reason, so within each category every item is used exactly once.

## Clues

1. The skipper who commands the Siller Grey sails at 10am.
2. The skipper who blames a passenger's dog falls somewhere between Eilidh and Ruaridh in start time order. Eilidh commands the Steadfast.
3. Eilidh blames a missing deckhand.
4. The skipper who blames a fouled propeller and 9am are exactly one hour apart in start time order, in one direction or the other.
5. The skipper who commands the Steadfast and 9am are exactly one hour apart in start time order, in one direction or the other.
6. 9am is exactly one hour earlier than Tormod, with no start time in between.
7. 10am falls somewhere between Eilidh and Senga in start time order.
8. The skipper who blames paperwork falls somewhere between the skipper who commands the Siller Grey and the skipper who commands the Steadfast in start time order.
9. Ruaridh and the skipper who commands the Broch Maid are exactly one hour apart in start time order, in one direction or the other.
10. The skipper who commands the Tern is earlier than the skipper who blames fog in start time order.

## Solving chart

*Start time vs Skipper*

| | Calla | Eilidh | Tormod | Senga | Ruaridh |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Vessel*

| | the Ailsa Belle | the Tern | the Broch Maid | the Siller Grey | the Steadfast |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Delay blamed on*

| | fog | a missing deckhand | a fouled propeller | paperwork | a passenger's dog |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Skipper vs Vessel*

| | the Ailsa Belle | the Tern | the Broch Maid | the Siller Grey | the Steadfast |
|---|---|---|---|---|---|
| **Calla** | | | | | |
| **Eilidh** | | | | | |
| **Tormod** | | | | | |
| **Senga** | | | | | |
| **Ruaridh** | | | | | |

*Skipper vs Delay blamed on*

| | fog | a missing deckhand | a fouled propeller | paperwork | a passenger's dog |
|---|---|---|---|---|---|
| **Calla** | | | | | |
| **Eilidh** | | | | | |
| **Tormod** | | | | | |
| **Senga** | | | | | |
| **Ruaridh** | | | | | |

*Vessel vs Delay blamed on*

| | fog | a missing deckhand | a fouled propeller | paperwork | a passenger's dog |
|---|---|---|---|---|---|
| **the Ailsa Belle** | | | | | |
| **the Tern** | | | | | |
| **the Broch Maid** | | | | | |
| **the Siller Grey** | | | | | |
| **the Steadfast** | | | | | |

## Solution

| Start time | Skipper | Vessel | Delay blamed on |
|---|---|---|---|
| 8am | Eilidh | the Steadfast | a missing deckhand |
| 9am | Calla | the Tern | paperwork |
| 10am | Tormod | the Siller Grey | a fouled propeller |
| 11am | Senga | the Broch Maid | a passenger's dog |
| noon | Ruaridh | the Ailsa Belle | fog |

## How it falls out

1. [direct] from clue 2 vessel:the Siller Grey: ruled out position(s) 1,2,4,5
2. [bijection] vessel:the Ailsa Belle: ruled out position(s) 3
3. [bijection] vessel:the Tern: ruled out position(s) 3
4. [bijection] vessel:the Broch Maid: ruled out position(s) 3
5. [bijection] vessel:the Steadfast: ruled out position(s) 3
6. [direct] from clue 6 skipper:Eilidh: ruled out position(s) 3
7. [direct] from clue 3 delay:a missing deckhand: ruled out position(s) 3
8. [order] from clue 11 delay:a passenger's dog: ruled out position(s) 1,5
9. [order] from clue 9 delay:paperwork: ruled out position(s) 1,3,5
10. [order] from clue 9 vessel:the Steadfast: ruled out position(s) 2,4
11. [order] from clue 8 skipper:Senga: ruled out position(s) 3
12. [order] from clue 7 vessel:the Steadfast: ruled out position(s) 5
13. [order] from clue 9 delay:paperwork: ruled out position(s) 4
14. [order] from clue 5 delay:a fouled propeller: ruled out position(s) 2,4,5
15. [order] from clue 4 skipper:Tormod: ruled out position(s) 1,2,4,5
16. [order] from clue 1 vessel:the Tern: ruled out position(s) 5
17. [order] from clue 1 delay:fog: ruled out position(s) 1
18. [direct] from clue 6 skipper:Eilidh: ruled out position(s) 2,4,5
19. [order] from clue 11 skipper:Ruaridh: ruled out position(s) 1,2
20. [order] from clue 10 vessel:the Broch Maid: ruled out position(s) 1
21. [order] from clue 8 skipper:Senga: ruled out position(s) 1,2
22. [direct] from clue 3 delay:a missing deckhand: ruled out position(s) 2,4,5
23. [bijection] delay:fog: ruled out position(s) 2
24. [bijection] delay:a fouled propeller: ruled out position(s) 1
25. [bijection] delay:a passenger's dog: ruled out position(s) 2
26. [bijection] delay:fog: ruled out position(s) 3,4
27. [bijection] skipper:Calla: ruled out position(s) 1,3
28. [bijection] skipper:Ruaridh: ruled out position(s) 3
29. [bijection] skipper:Calla: ruled out position(s) 4,5
30. [bijection] vessel:the Ailsa Belle: ruled out position(s) 1
31. [bijection] vessel:the Tern: ruled out position(s) 1
32. [order] from clue 10 vessel:the Broch Maid: ruled out position(s) 2
33. [bijection] delay:a passenger's dog: ruled out position(s) 3
34. [order] from clue 11 skipper:Ruaridh: ruled out position(s) 4
35. [order] from clue 10 vessel:the Broch Maid: ruled out position(s) 5
36. [bijection] skipper:Senga: ruled out position(s) 5
37. [bijection] vessel:the Ailsa Belle: ruled out position(s) 4
38. [bijection] vessel:the Tern: ruled out position(s) 4
39. [bijection] vessel:the Ailsa Belle: ruled out position(s) 2

---

<sub>seed `2026172854632` &middot; score 5.195 &middot; atoms 11 &middot; positives 3 &middot; solved by order</sub>
