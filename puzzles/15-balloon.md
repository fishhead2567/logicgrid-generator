# The Thistledown Balloon Ascent

*The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 4 &nbsp;&nbsp; **id** `09f6ecfb0659`

## Introduction

There are 4 balloons. Each has exactly one start time and one item from every other category below, and within each category every item belongs to a different balloon.
- **Start time** (listed in order): 8 a.m., 9 a.m., 10 a.m. and 11 a.m..
- **Pilot**: Grover, Delphine, Rosalind and Horatio.
- **Envelope**: the saffron envelope, the striped envelope, the kingfisher envelope and the silver envelope.
- **Ballast**: dried beans, pea gravel, lead shot and rock salt.
The hours above are listed in order, from 8 a.m. to 11 a.m..

## Clues

1. Lead shot goes with 11 a.m.. Rosalind and 11 a.m. are next to each other in start time order, in one order or the other.
2. The saffron envelope does not go with 9 a.m, but rock salt goes with 9 a.m.
3. The striped envelope's start time is earlier than Horatio's start time. Delphine falls somewhere between dried beans and the striped envelope in start time order.
4. The kingfisher envelope's start time is immediately earlier than Delphine's start time, with no start time in between.

## Solving chart

*Start time vs Pilot*

| | Grover | Delphine | Rosalind | Horatio |
|---|---|---|---|---|
| **8 a.m.** | | | | |
| **9 a.m.** | | | | |
| **10 a.m.** | | | | |
| **11 a.m.** | | | | |

*Start time vs Envelope*

| | the saffron envelope | the striped envelope | the kingfisher envelope | the silver envelope |
|---|---|---|---|---|
| **8 a.m.** | | | | |
| **9 a.m.** | | | | |
| **10 a.m.** | | | | |
| **11 a.m.** | | | | |

*Start time vs Ballast*

| | dried beans | pea gravel | lead shot | rock salt |
|---|---|---|---|---|
| **8 a.m.** | | | | |
| **9 a.m.** | | | | |
| **10 a.m.** | | | | |
| **11 a.m.** | | | | |

*Pilot vs Envelope*

| | the saffron envelope | the striped envelope | the kingfisher envelope | the silver envelope |
|---|---|---|---|---|
| **Grover** | | | | |
| **Delphine** | | | | |
| **Rosalind** | | | | |
| **Horatio** | | | | |

*Pilot vs Ballast*

| | dried beans | pea gravel | lead shot | rock salt |
|---|---|---|---|---|
| **Grover** | | | | |
| **Delphine** | | | | |
| **Rosalind** | | | | |
| **Horatio** | | | | |

*Envelope vs Ballast*

| | dried beans | pea gravel | lead shot | rock salt |
|---|---|---|---|---|
| **the saffron envelope** | | | | |
| **the striped envelope** | | | | |
| **the kingfisher envelope** | | | | |
| **the silver envelope** | | | | |

## Solution

| Start time | Pilot | Envelope | Ballast |
|---|---|---|---|
| 8 a.m. | Grover | the kingfisher envelope | dried beans |
| 9 a.m. | Delphine | the silver envelope | rock salt |
| 10 a.m. | Rosalind | the striped envelope | pea gravel |
| 11 a.m. | Horatio | the saffron envelope | lead shot |

## How it falls out

1. [direct] from clue 7 ballast:lead shot: ruled out position(s) 1,2,3
2. [direct] from clue 6 envelope:the saffron envelope: ruled out position(s) 2
3. [direct] from clue 4 ballast:rock salt: ruled out position(s) 1,3,4
4. [bijection] ballast:dried beans: ruled out position(s) 2,4
5. [bijection] ballast:pea gravel: ruled out position(s) 2,4
6. [order] from clue 5 envelope:the kingfisher envelope: ruled out position(s) 4
7. [order] from clue 5 pilot:Delphine: ruled out position(s) 1
8. [order] from clue 3 envelope:the striped envelope: ruled out position(s) 4
9. [order] from clue 3 pilot:Horatio: ruled out position(s) 1
10. [order] from clue 2 pilot:Rosalind: ruled out position(s) 1,2,4
11. [order] from clue 1 pilot:Delphine: ruled out position(s) 3,4
12. [order] from clue 1 envelope:the striped envelope: ruled out position(s) 2
13. [order] from clue 5 envelope:the kingfisher envelope: ruled out position(s) 2,3
14. [bijection] envelope:the saffron envelope: ruled out position(s) 1
15. [bijection] envelope:the striped envelope: ruled out position(s) 1
16. [bijection] envelope:the silver envelope: ruled out position(s) 1
17. [bijection] envelope:the silver envelope: ruled out position(s) 3,4
18. [bijection] pilot:Grover: ruled out position(s) 2,3
19. [bijection] pilot:Horatio: ruled out position(s) 2,3
20. [bijection] pilot:Grover: ruled out position(s) 4
21. [order] from clue 1 ballast:dried beans: ruled out position(s) 3
22. [bijection] ballast:pea gravel: ruled out position(s) 1
23. [bijection] envelope:the saffron envelope: ruled out position(s) 3

---

<sub>seed `2026172694221` &middot; score 4.93 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
