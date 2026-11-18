# The Crossings to Inverlaig

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `822daab59fc7`

## Introduction

The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.
Five skippers are involved. Determine each skipper's start time, vessel and reason.
- **Skipper**: Ruaridh, Murdo, Fearghas, Eilidh and Senga.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Vessel**: the Steadfast, the Kelpie, the Ailsa Belle, the Broch Maid and the Tern.
- **Delay blamed on**: paperwork, a missing deckhand, a passenger's dog, the tide and fog.
Every skipper has a different start time, vessel and reason, so within each category every item is used exactly once.

## Clues

1. Ruaridh is exactly one hour earlier than 11am, with no start time in between.
2. The skipper who commands the Tern and 9am are exactly one hour apart in start time order, in one direction or the other.
3. 11am falls somewhere between the skipper who blames the tide and the skipper who commands the Tern in start time order.
4. Murdo and 8am are exactly four hours apart in start time order.
5. At least one of the following holds, and possibly more than one: (a) Murdo is earlier than the skipper who commands the Broch Maid in start time order. (b) Fearghas sails at 9am.
6. Senga and the skipper who commands the Tern both sit at odd-numbered hours or both at even-numbered hours.
7. The skipper who blames paperwork and the skipper who commands the Steadfast are exactly four hours apart in start time order.
8. Ruaridh is earlier than the skipper who commands the Broch Maid in start time order.
9. The skipper who blames fog is exactly one hour earlier than the skipper who commands the Steadfast, with no start time in between.
10. The skipper who commands the Kelpie falls somewhere between the skipper who blames a passenger's dog and the skipper who blames fog in start time order.

## Solving chart

*Start time vs Skipper*

| | Ruaridh | Murdo | Fearghas | Eilidh | Senga |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Vessel*

| | the Steadfast | the Kelpie | the Ailsa Belle | the Broch Maid | the Tern |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Delay blamed on*

| | paperwork | a missing deckhand | a passenger's dog | the tide | fog |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Skipper vs Vessel*

| | the Steadfast | the Kelpie | the Ailsa Belle | the Broch Maid | the Tern |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Murdo** | | | | | |
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |
| **Senga** | | | | | |

*Skipper vs Delay blamed on*

| | paperwork | a missing deckhand | a passenger's dog | the tide | fog |
|---|---|---|---|---|---|
| **Ruaridh** | | | | | |
| **Murdo** | | | | | |
| **Fearghas** | | | | | |
| **Eilidh** | | | | | |
| **Senga** | | | | | |

*Vessel vs Delay blamed on*

| | paperwork | a missing deckhand | a passenger's dog | the tide | fog |
|---|---|---|---|---|---|
| **the Steadfast** | | | | | |
| **the Kelpie** | | | | | |
| **the Ailsa Belle** | | | | | |
| **the Broch Maid** | | | | | |
| **the Tern** | | | | | |

## Solution

| Start time | Skipper | Vessel | Delay blamed on |
|---|---|---|---|
| 8am | Senga | the Tern | paperwork |
| 9am | Fearghas | the Ailsa Belle | a passenger's dog |
| 10am | Ruaridh | the Kelpie | a missing deckhand |
| 11am | Eilidh | the Broch Maid | fog |
| noon | Murdo | the Steadfast | the tide |

## How it falls out

1. [order] from clue 9 vessel:the Tern: ruled out position(s) 2,4,5
2. [order] from clue 8 vessel:the Kelpie: ruled out position(s) 1,5
3. [order] from clue 7 skipper:Ruaridh: ruled out position(s) 5
4. [order] from clue 7 vessel:the Broch Maid: ruled out position(s) 1
5. [order] from clue 6 delay:fog: ruled out position(s) 5
6. [order] from clue 6 vessel:the Steadfast: ruled out position(s) 1
7. [order] from clue 5 skipper:Senga: ruled out position(s) 2,4
8. [order] from clue 4 delay:the tide: ruled out position(s) 1,2,3,4
9. [order] from clue 3 skipper:Murdo: ruled out position(s) 1,2,3,4
10. [order] from clue 2 skipper:Ruaridh: ruled out position(s) 1,2,4
11. [order] from clue 7 vessel:the Broch Maid: ruled out position(s) 2,3
12. [order] from clue 1 delay:paperwork: ruled out position(s) 2,3,4,5
13. [order] from clue 1 vessel:the Steadfast: ruled out position(s) 2,3,4
14. [order] from clue 6 delay:fog: ruled out position(s) 1,2,3
15. [order] from clue 8 vessel:the Kelpie: ruled out position(s) 4
16. [order] from clue 8 delay:a passenger's dog: ruled out position(s) 3,4,5
17. [bijection] delay:a missing deckhand: ruled out position(s) 1,4,5
18. [bijection] delay:a passenger's dog: ruled out position(s) 1
19. [bijection] delay:a missing deckhand: ruled out position(s) 2
20. [bijection] skipper:Fearghas: ruled out position(s) 3,5
21. [bijection] skipper:Eilidh: ruled out position(s) 3,5
22. [bijection] skipper:Senga: ruled out position(s) 3,5
23. [bijection] vessel:the Ailsa Belle: ruled out position(s) 5
24. [bijection] vessel:the Broch Maid: ruled out position(s) 5
25. [order] from clue 8 vessel:the Kelpie: ruled out position(s) 2
26. [bijection] skipper:Fearghas: ruled out position(s) 1
27. [bijection] skipper:Eilidh: ruled out position(s) 1
28. [bijection] vessel:the Ailsa Belle: ruled out position(s) 3,4
29. [bijection] vessel:the Tern: ruled out position(s) 3
30. [bijection] vessel:the Ailsa Belle: ruled out position(s) 1
31. [disjunction] from clue 10 skipper:Fearghas: ruled out position(s) 4
32. [bijection] skipper:Eilidh: ruled out position(s) 2

---

<sub>seed `2026172941492` &middot; score 8.7392 &middot; atoms 10 &middot; positives 0 &middot; solved by disjunction</sub>
