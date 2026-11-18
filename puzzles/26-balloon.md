# The Thistledown Balloon Ascent

*The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.*

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `5e39809fcbb6`

## Introduction

There are 5 balloons. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different balloon.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m., 11 a.m. and noon.
- **Pilot**: Rosalind, Grover, Anneliese, Montague and Horatio.
- **Envelope**: the saffron envelope, the moss-green envelope, the silver envelope, the patchwork envelope and the oxblood envelope.
- **Ballast**: bottled water, pea gravel, sandbags, dried beans and iron filings.
The hours above are listed in order, from 8 a.m. to noon.

## Clues

1. Bottled water goes with the patchwork envelope.
2. The saffron envelope's start time is earlier than 9 a.m.. Dried beans, Anneliese and 9 a.m. are three different balloons. The saffron envelope and Montague are next to each other in start time order, in one order or the other.
3. 10 a.m. is immediately earlier than pea gravel's start time, with no start time in between.
4. The moss-green envelope's start time is earlier than 11 a.m..
5. Anneliese and 9 a.m. are exactly three hours apart in start time order.
6. Sandbags, Horatio and 9 a.m. are three different balloons.
7. 8 a.m. is earlier than Rosalind's start time.
8. Rosalind's start time is immediately earlier than iron filings' start time, with no start time in between.
9. The silver envelope and Horatio are next to each other in start time order, in one order or the other.

## Solving chart

*Start time vs Pilot*

| | Rosalind | Grover | Anneliese | Montague | Horatio |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Envelope*

| | the saffron envelope | the moss-green envelope | the silver envelope | the patchwork envelope | the oxblood envelope |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Ballast*

| | bottled water | pea gravel | sandbags | dried beans | iron filings |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Pilot vs Envelope*

| | the saffron envelope | the moss-green envelope | the silver envelope | the patchwork envelope | the oxblood envelope |
|---|---|---|---|---|---|
| **Rosalind** | | | | | |
| **Grover** | | | | | |
| **Anneliese** | | | | | |
| **Montague** | | | | | |
| **Horatio** | | | | | |

*Pilot vs Ballast*

| | bottled water | pea gravel | sandbags | dried beans | iron filings |
|---|---|---|---|---|---|
| **Rosalind** | | | | | |
| **Grover** | | | | | |
| **Anneliese** | | | | | |
| **Montague** | | | | | |
| **Horatio** | | | | | |

*Envelope vs Ballast*

| | bottled water | pea gravel | sandbags | dried beans | iron filings |
|---|---|---|---|---|---|
| **the saffron envelope** | | | | | |
| **the moss-green envelope** | | | | | |
| **the silver envelope** | | | | | |
| **the patchwork envelope** | | | | | |
| **the oxblood envelope** | | | | | |

## Solution

| Start time | Pilot | Envelope | Ballast |
|---|---|---|---|
| 8 a.m. | Grover | the saffron envelope | sandbags |
| 9 a.m. | Montague | the patchwork envelope | bottled water |
| 10 a.m. | Horatio | the moss-green envelope | dried beans |
| 11 a.m. | Rosalind | the silver envelope | pea gravel |
| noon | Anneliese | the oxblood envelope | iron filings |

## How it falls out

1. [bijection] from clue 10 ballast:sandbags: ruled out position(s) 2
2. [bijection] from clue 10 pilot:Horatio: ruled out position(s) 2
3. [bijection] from clue 2 ballast:dried beans: ruled out position(s) 2
4. [bijection] from clue 2 pilot:Anneliese: ruled out position(s) 2
5. [order] from clue 11 envelope:the saffron envelope: ruled out position(s) 2,3,4,5
6. [order] from clue 9 ballast:pea gravel: ruled out position(s) 1,2,3,5
7. [order] from clue 8 envelope:the silver envelope: ruled out position(s) 1
8. [order] from clue 7 pilot:Montague: ruled out position(s) 1,3,4,5
9. [order] from clue 6 pilot:Rosalind: ruled out position(s) 5
10. [order] from clue 6 ballast:iron filings: ruled out position(s) 1
11. [order] from clue 4 envelope:the moss-green envelope: ruled out position(s) 4,5
12. [order] from clue 3 pilot:Anneliese: ruled out position(s) 1,3,4
13. [order] from clue 1 pilot:Rosalind: ruled out position(s) 1
14. [order] from clue 6 ballast:iron filings: ruled out position(s) 2
15. [bijection] from clue 2 ballast:dried beans: ruled out position(s) 5
16. [bijection] ballast:bottled water: ruled out position(s) 4
17. [bijection] ballast:sandbags: ruled out position(s) 4
18. [bijection] ballast:dried beans: ruled out position(s) 4
19. [bijection] ballast:iron filings: ruled out position(s) 4
20. [bijection] ballast:bottled water: ruled out position(s) 1,3,5
21. [bijection] envelope:the moss-green envelope: ruled out position(s) 1
22. [bijection] envelope:the patchwork envelope: ruled out position(s) 1
23. [bijection] envelope:the oxblood envelope: ruled out position(s) 1
24. [bijection] pilot:Rosalind: ruled out position(s) 2
25. [bijection] pilot:Grover: ruled out position(s) 2,5
26. [bijection] pilot:Horatio: ruled out position(s) 5
27. [order] from clue 6 pilot:Rosalind: ruled out position(s) 3
28. [order] from clue 6 ballast:iron filings: ruled out position(s) 3
29. [direct] from clue 5 envelope:the patchwork envelope: ruled out position(s) 3,4,5
30. [bijection] ballast:sandbags: ruled out position(s) 5
31. [bijection] envelope:the moss-green envelope: ruled out position(s) 2
32. [bijection] envelope:the silver envelope: ruled out position(s) 2
33. [bijection] envelope:the oxblood envelope: ruled out position(s) 2
34. [bijection] pilot:Grover: ruled out position(s) 4
35. [bijection] pilot:Horatio: ruled out position(s) 4
36. [order] from clue 8 envelope:the silver envelope: ruled out position(s) 3,5
37. [order] from clue 8 pilot:Horatio: ruled out position(s) 1
38. [bijection] from clue 10 ballast:sandbags: ruled out position(s) 3
39. [bijection] ballast:dried beans: ruled out position(s) 1
40. [bijection] envelope:the oxblood envelope: ruled out position(s) 3,4
_... and 1 further steps._

---

<sub>seed `2026172781330` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
