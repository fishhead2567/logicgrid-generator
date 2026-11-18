# The Thistledown Balloon Ascent

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `806399ad4383`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Five pilots are involved. Determine each pilot's start time, envelope and ballast.
- **Pilot**: Isolde, Montague, Grover, Anneliese and Delphine.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Envelope**: the patchwork envelope, the saffron envelope, the silver envelope, the oxblood envelope and the kingfisher envelope.
- **Ballast**: lead shot, bottled water, iron filings, pea gravel and sandbags.
Every pilot has a different start time, envelope and ballast, so within each category every item is used exactly once.

## Clues

1. Montague flies the silver envelope.
2. Anneliese falls somewhere between the pilot who carries pea gravel and 8am in start time order.
3. Anneliese does not launch at 9am.
4. The pilot who flies the saffron envelope falls somewhere between the pilot who carries bottled water and 10am in start time order.
5. The pilot who carries pea gravel and Delphine are exactly four hours apart in start time order.
6. The pilot who carries iron filings falls somewhere between the pilot who flies the saffron envelope and Grover in start time order.
7. The pilot who carries sandbags does not fly the oxblood envelope. The pilot who flies the silver envelope is earlier than the pilot who carries sandbags in start time order.
8. The pilot who flies the kingfisher envelope and Anneliese are exactly one hour apart in start time order, in one direction or the other.

## Solving chart

*Start time vs Pilot*

| | Isolde | Montague | Grover | Anneliese | Delphine |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Envelope*

| | the patchwork envelope | the saffron envelope | the silver envelope | the oxblood envelope | the kingfisher envelope |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Ballast*

| | lead shot | bottled water | iron filings | pea gravel | sandbags |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Pilot vs Envelope*

| | the patchwork envelope | the saffron envelope | the silver envelope | the oxblood envelope | the kingfisher envelope |
|---|---|---|---|---|---|
| **Isolde** | | | | | |
| **Montague** | | | | | |
| **Grover** | | | | | |
| **Anneliese** | | | | | |
| **Delphine** | | | | | |

*Pilot vs Ballast*

| | lead shot | bottled water | iron filings | pea gravel | sandbags |
|---|---|---|---|---|---|
| **Isolde** | | | | | |
| **Montague** | | | | | |
| **Grover** | | | | | |
| **Anneliese** | | | | | |
| **Delphine** | | | | | |

*Envelope vs Ballast*

| | lead shot | bottled water | iron filings | pea gravel | sandbags |
|---|---|---|---|---|---|
| **the patchwork envelope** | | | | | |
| **the saffron envelope** | | | | | |
| **the silver envelope** | | | | | |
| **the oxblood envelope** | | | | | |
| **the kingfisher envelope** | | | | | |

## Solution

| Start time | Pilot | Envelope | Ballast |
|---|---|---|---|
| 8am | Delphine | the oxblood envelope | bottled water |
| 9am | Isolde | the saffron envelope | lead shot |
| 10am | Montague | the silver envelope | iron filings |
| 11am | Anneliese | the patchwork envelope | sandbags |
| noon | Grover | the kingfisher envelope | pea gravel |

## How it falls out

1. [direct] from clue 3 pilot:Anneliese: ruled out position(s) 2
2. [order] from clue 9 envelope:the silver envelope: ruled out position(s) 5
3. [order] from clue 9 ballast:sandbags: ruled out position(s) 1
4. [order] from clue 8 ballast:iron filings: ruled out position(s) 1,5
5. [order] from clue 6 ballast:pea gravel: ruled out position(s) 2,3,4
6. [order] from clue 6 pilot:Delphine: ruled out position(s) 2,3,4
7. [order] from clue 5 pilot:Anneliese: ruled out position(s) 1,5
8. [order] from clue 5 ballast:pea gravel: ruled out position(s) 1
9. [order] from clue 6 pilot:Delphine: ruled out position(s) 5
10. [order] from clue 2 envelope:the kingfisher envelope: ruled out position(s) 1
11. [order] from clue 1 envelope:the saffron envelope: ruled out position(s) 1,3,5
12. [order] from clue 1 ballast:bottled water: ruled out position(s) 2,3,4
13. [order] from clue 8 pilot:Grover: ruled out position(s) 3
14. [direct] from clue 4 pilot:Montague: ruled out position(s) 5
15. [bijection] ballast:lead shot: ruled out position(s) 5
16. [bijection] ballast:bottled water: ruled out position(s) 5
17. [bijection] ballast:sandbags: ruled out position(s) 5
18. [bijection] pilot:Isolde: ruled out position(s) 1
19. [bijection] pilot:Montague: ruled out position(s) 1
20. [bijection] pilot:Grover: ruled out position(s) 1
21. [order] from clue 8 ballast:iron filings: ruled out position(s) 2
22. [direct] from clue 4 envelope:the silver envelope: ruled out position(s) 1
23. [order] from clue 9 envelope:the silver envelope: ruled out position(s) 4
24. [order] from clue 9 ballast:sandbags: ruled out position(s) 2
25. [direct] from clue 4 pilot:Montague: ruled out position(s) 4
26. [order] from clue 1 envelope:the saffron envelope: ruled out position(s) 4
27. [order] from clue 8 pilot:Grover: ruled out position(s) 2
28. [bijection] ballast:lead shot: ruled out position(s) 1
29. [bijection] ballast:lead shot: ruled out position(s) 3,4
30. [bijection] envelope:the patchwork envelope: ruled out position(s) 2
31. [bijection] envelope:the silver envelope: ruled out position(s) 2
32. [bijection] envelope:the oxblood envelope: ruled out position(s) 2
33. [bijection] envelope:the kingfisher envelope: ruled out position(s) 2
34. [order] from clue 9 ballast:sandbags: ruled out position(s) 3
35. [direct] from clue 7 envelope:the oxblood envelope: ruled out position(s) 4
36. [direct] from clue 4 pilot:Montague: ruled out position(s) 2
37. [bijection] ballast:iron filings: ruled out position(s) 4
38. [bijection] envelope:the patchwork envelope: ruled out position(s) 3
39. [bijection] envelope:the oxblood envelope: ruled out position(s) 3
40. [bijection] envelope:the kingfisher envelope: ruled out position(s) 3
_... and 8 further steps._

---

<sub>seed `2026172781330` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
