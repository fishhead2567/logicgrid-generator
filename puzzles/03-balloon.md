# The Thistledown Balloon Ascent

*The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.*

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `9dd7edb34f24`

## Introduction

There are 5 balloons. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different balloon.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m., 11 a.m. and noon.
- **Envelope**: the moss-green envelope, the striped envelope, the patchwork envelope, the kingfisher envelope and the silver envelope.
- **Ballast**: lead shot, pea gravel, dried beans, sandbags and rock salt.
The hours above are listed in order, from 8 a.m. to noon.

## Clues

1. Dried beans' start time is immediately earlier than 11 a.m., with no start time in between. The moss-green envelope goes with 11 a.m..
2. The kingfisher envelope goes with 10 a.m..
3. Lead shot's start time is immediately earlier than the silver envelope's start time, with no start time in between. Pea gravel goes with the silver envelope.
4. Sandbags goes with the patchwork envelope.
5. The silver envelope's start time is earlier than sandbags' start time.

## Solving chart

*Start time vs Envelope*

| | the moss-green envelope | the striped envelope | the patchwork envelope | the kingfisher envelope | the silver envelope |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Start time vs Ballast*

| | lead shot | pea gravel | dried beans | sandbags | rock salt |
|---|---|---|---|---|---|
| **8 a.m.** | | | | | |
| **9 a.m.** | | | | | |
| **10 a.m.** | | | | | |
| **11 a.m.** | | | | | |
| **noon** | | | | | |

*Envelope vs Ballast*

| | lead shot | pea gravel | dried beans | sandbags | rock salt |
|---|---|---|---|---|---|
| **the moss-green envelope** | | | | | |
| **the striped envelope** | | | | | |
| **the patchwork envelope** | | | | | |
| **the kingfisher envelope** | | | | | |
| **the silver envelope** | | | | | |

## Solution

| Start time | Envelope | Ballast |
|---|---|---|
| 8 a.m. | the striped envelope | lead shot |
| 9 a.m. | the silver envelope | pea gravel |
| 10 a.m. | the kingfisher envelope | dried beans |
| 11 a.m. | the moss-green envelope | rock salt |
| noon | the patchwork envelope | sandbags |

## How it falls out

1. [direct] from clue 7 envelope:the kingfisher envelope: ruled out position(s) 1,2,4,5
2. [direct] from clue 1 envelope:the moss-green envelope: ruled out position(s) 1,2,3,5
3. [bijection] envelope:the striped envelope: ruled out position(s) 3,4
4. [bijection] envelope:the patchwork envelope: ruled out position(s) 3,4
5. [bijection] envelope:the silver envelope: ruled out position(s) 3,4
6. [direct] from clue 3 ballast:pea gravel: ruled out position(s) 3,4
7. [direct] from clue 6 ballast:sandbags: ruled out position(s) 3,4
8. [order] from clue 5 ballast:lead shot: ruled out position(s) 2,3,5
9. [order] from clue 5 envelope:the silver envelope: ruled out position(s) 1
10. [order] from clue 4 envelope:the silver envelope: ruled out position(s) 5
11. [order] from clue 4 ballast:sandbags: ruled out position(s) 1,2
12. [order] from clue 5 ballast:lead shot: ruled out position(s) 4
13. [order] from clue 2 ballast:dried beans: ruled out position(s) 1,2,4,5
14. [direct] from clue 6 envelope:the patchwork envelope: ruled out position(s) 1,2
15. [direct] from clue 3 ballast:pea gravel: ruled out position(s) 1,5
16. [bijection] ballast:rock salt: ruled out position(s) 1,2,3,5
17. [bijection] envelope:the striped envelope: ruled out position(s) 2,5

---

<sub>seed `2026172599193` &middot; score 4.14 &middot; atoms 7 &middot; positives 4 &middot; solved by order</sub>
