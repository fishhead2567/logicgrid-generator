# The Thistledown Balloon Ascent

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `806399ad4383`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Five pilots are involved. Determine each pilot's start time, envelope and ballast.
- **Pilot**: Isolde, Montague, Grover, Anneliese and Delphine.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Envelope**: the patchwork envelope, the saffron envelope, the silver envelope, the oxblood envelope and the kingfisher envelope.
- **Ballast**: lead shot, bottled water, iron filings, pea gravel and sandbags.
Every pilot has a different start time, envelope and ballast, so within each category every item is used exactly once.

## Clues

1. Isolde launches at 9am.
2. The pilot who carries sandbags launches at 11am.
3. 11am falls somewhere between Grover and Isolde in start time order.
4. 11am falls somewhere between the pilot who carries lead shot and the pilot who flies the kingfisher envelope in start time order.
5. The pilot who carries pea gravel and Anneliese are exactly one hour apart in start time order, in one direction or the other.
6. The pilot who carries lead shot does not fly the oxblood envelope.
7. The pilot who carries bottled water and the pilot who flies the patchwork envelope are exactly three hours apart in start time order.
8. Montague is exactly one hour earlier than the pilot who carries sandbags, with no start time in between.
9. The pilot who carries lead shot is exactly one hour earlier than the pilot who flies the silver envelope, with no start time in between.
10. The pilot who carries iron filings falls somewhere between the pilot who flies the patchwork envelope and Isolde in start time order.

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

1. [direct] from clue 8 pilot:Isolde: ruled out position(s) 1,3,4,5
2. [direct] from clue 6 ballast:sandbags: ruled out position(s) 1,2,3,5
3. [bijection] ballast:lead shot: ruled out position(s) 4
4. [bijection] ballast:bottled water: ruled out position(s) 4
5. [bijection] ballast:iron filings: ruled out position(s) 4
6. [bijection] ballast:pea gravel: ruled out position(s) 4
7. [bijection] pilot:Montague: ruled out position(s) 2
8. [bijection] pilot:Grover: ruled out position(s) 2
9. [bijection] pilot:Anneliese: ruled out position(s) 2
10. [bijection] pilot:Delphine: ruled out position(s) 2
11. [order] from clue 10 ballast:bottled water: ruled out position(s) 3
12. [order] from clue 10 envelope:the patchwork envelope: ruled out position(s) 1,3
13. [order] from clue 9 envelope:the kingfisher envelope: ruled out position(s) 4
14. [order] from clue 7 ballast:iron filings: ruled out position(s) 1,2,5
15. [order] from clue 7 envelope:the patchwork envelope: ruled out position(s) 2
16. [order] from clue 10 ballast:bottled water: ruled out position(s) 5
17. [order] from clue 5 ballast:pea gravel: ruled out position(s) 1
18. [order] from clue 5 pilot:Anneliese: ruled out position(s) 5
19. [order] from clue 4 ballast:lead shot: ruled out position(s) 5
20. [order] from clue 4 envelope:the silver envelope: ruled out position(s) 1,5
21. [order] from clue 9 envelope:the kingfisher envelope: ruled out position(s) 1,2,3
22. [order] from clue 3 pilot:Grover: ruled out position(s) 1,3,4
23. [order] from clue 2 pilot:Montague: ruled out position(s) 1,4,5
24. [bijection] ballast:lead shot: ruled out position(s) 3
25. [bijection] ballast:pea gravel: ruled out position(s) 3
26. [bijection] ballast:pea gravel: ruled out position(s) 2
27. [bijection] envelope:the patchwork envelope: ruled out position(s) 5
28. [bijection] envelope:the saffron envelope: ruled out position(s) 5
29. [bijection] envelope:the oxblood envelope: ruled out position(s) 5
30. [bijection] pilot:Anneliese: ruled out position(s) 3
31. [bijection] pilot:Delphine: ruled out position(s) 3,5
32. [order] from clue 10 ballast:bottled water: ruled out position(s) 2
33. [order] from clue 5 pilot:Anneliese: ruled out position(s) 1
34. [order] from clue 4 envelope:the silver envelope: ruled out position(s) 4
35. [bijection] ballast:lead shot: ruled out position(s) 1
36. [bijection] envelope:the saffron envelope: ruled out position(s) 4
37. [bijection] envelope:the oxblood envelope: ruled out position(s) 4
38. [bijection] pilot:Delphine: ruled out position(s) 4
39. [order] from clue 4 envelope:the silver envelope: ruled out position(s) 2
40. [direct] from clue 1 envelope:the oxblood envelope: ruled out position(s) 2
_... and 3 further steps._

---

<sub>seed `2026172781330` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
