# The Crossings to Inverlaig

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `19304b56f314`

## Introduction

The Inverlaig ferry runs a full day of crossings in theory, and a variable number in practice.
Five skippers are involved. Determine each skipper's start time and reason.
- **Skipper**: Eilidh, Fearghas, Ruaridh, Calla and Murdo.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Delay blamed on**: the tide, a passenger's dog, fog, paperwork and a slipway repair.
Every skipper has a different start time and reason, so within each category every item is used exactly once.

## Clues

1. Fearghas is earlier than 11am in start time order. The skipper who blames paperwork sails at 11am.
2. Ruaridh is earlier than the skipper who blames fog in start time order. Ruaridh sails at 10am.
3. Calla blames a slipway repair.
4. Eilidh blames paperwork.
5. The skipper who blames a passenger's dog is earlier than Calla in start time order.

## Solving chart

*Start time vs Skipper*

| | Eilidh | Fearghas | Ruaridh | Calla | Murdo |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Delay blamed on*

| | the tide | a passenger's dog | fog | paperwork | a slipway repair |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Skipper vs Delay blamed on*

| | the tide | a passenger's dog | fog | paperwork | a slipway repair |
|---|---|---|---|---|---|
| **Eilidh** | | | | | |
| **Fearghas** | | | | | |
| **Ruaridh** | | | | | |
| **Calla** | | | | | |
| **Murdo** | | | | | |

## Solution

| Start time | Skipper | Delay blamed on |
|---|---|---|
| 8am | Fearghas | a passenger's dog |
| 9am | Calla | a slipway repair |
| 10am | Ruaridh | the tide |
| 11am | Eilidh | paperwork |
| noon | Murdo | fog |

## How it falls out

1. [direct] from clue 5 skipper:Ruaridh: ruled out position(s) 1,2,4,5
2. [direct] from clue 2 delay:paperwork: ruled out position(s) 1,2,3,5
3. [direct] from clue 7 skipper:Eilidh: ruled out position(s) 1,2,3,5
4. [bijection] delay:the tide: ruled out position(s) 4
5. [bijection] delay:a passenger's dog: ruled out position(s) 4
6. [bijection] delay:fog: ruled out position(s) 4
7. [bijection] delay:a slipway repair: ruled out position(s) 4
8. [bijection] skipper:Fearghas: ruled out position(s) 3,4
9. [bijection] skipper:Calla: ruled out position(s) 3,4
10. [bijection] skipper:Murdo: ruled out position(s) 3,4
11. [direct] from clue 4 delay:a slipway repair: ruled out position(s) 3
12. [order] from clue 6 skipper:Fearghas: ruled out position(s) 5
13. [order] from clue 3 delay:fog: ruled out position(s) 1,2,3
14. [order] from clue 1 delay:a passenger's dog: ruled out position(s) 5
15. [order] from clue 1 skipper:Calla: ruled out position(s) 1
16. [direct] from clue 4 delay:a slipway repair: ruled out position(s) 1
17. [bijection] delay:the tide: ruled out position(s) 5
18. [bijection] delay:a slipway repair: ruled out position(s) 5
19. [direct] from clue 4 skipper:Calla: ruled out position(s) 5
20. [order] from clue 1 delay:a passenger's dog: ruled out position(s) 2,3
21. [bijection] delay:the tide: ruled out position(s) 1,2
22. [bijection] skipper:Fearghas: ruled out position(s) 2
23. [bijection] skipper:Murdo: ruled out position(s) 2
24. [bijection] skipper:Murdo: ruled out position(s) 1

---

<sub>seed `2026172638788` &middot; score 4.14 &middot; atoms 7 &middot; positives 4 &middot; solved by order</sub>
