# The Thistledown Balloon Ascent

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `499d363d1146`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Four pilots are involved. Determine each pilot's start time, envelope and landing site.
- **Pilot**: Horatio, Isolde, Grover and Delphine.
- **Start time** (listed from earlier to later): 8am, 9am, 10am and 11am.
- **Envelope**: the saffron envelope, the moss-green envelope, the striped envelope and the kingfisher envelope.
- **Landed at**: a cricket pitch, a flooded quarry, a caravan park and a railway siding.
Every pilot has a different start time, envelope and landing site, so within each category every item is used exactly once.

## Clues

1. The pilot who comes down in a railway siding launches at 9am.
2. The pilot who flies the kingfisher envelope comes down in a railway siding.
3. The pilot who comes down in a flooded quarry falls somewhere between Horatio and 11am in start time order. 9am falls somewhere between Delphine and Horatio in start time order.
4. The pilot who comes down in a cricket pitch is exactly one hour earlier than 9am, with no start time in between.
5. 10am falls somewhere between Delphine and Isolde in start time order.
6. The pilot who flies the striped envelope does not come down in a flooded quarry.
7. The pilot who flies the saffron envelope and Grover are exactly one hour apart in start time order, in one direction or the other.

## Solving chart

*Start time vs Pilot*

| | Horatio | Isolde | Grover | Delphine |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Envelope*

| | the saffron envelope | the moss-green envelope | the striped envelope | the kingfisher envelope |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Start time vs Landed at*

| | a cricket pitch | a flooded quarry | a caravan park | a railway siding |
|---|---|---|---|---|
| **8am** | | | | |
| **9am** | | | | |
| **10am** | | | | |
| **11am** | | | | |

*Pilot vs Envelope*

| | the saffron envelope | the moss-green envelope | the striped envelope | the kingfisher envelope |
|---|---|---|---|---|
| **Horatio** | | | | |
| **Isolde** | | | | |
| **Grover** | | | | |
| **Delphine** | | | | |

*Pilot vs Landed at*

| | a cricket pitch | a flooded quarry | a caravan park | a railway siding |
|---|---|---|---|---|
| **Horatio** | | | | |
| **Isolde** | | | | |
| **Grover** | | | | |
| **Delphine** | | | | |

*Envelope vs Landed at*

| | a cricket pitch | a flooded quarry | a caravan park | a railway siding |
|---|---|---|---|---|
| **the saffron envelope** | | | | |
| **the moss-green envelope** | | | | |
| **the striped envelope** | | | | |
| **the kingfisher envelope** | | | | |

## Solution

| Start time | Pilot | Envelope | Landed at |
|---|---|---|---|
| 8am | Horatio | the striped envelope | a cricket pitch |
| 9am | Isolde | the kingfisher envelope | a railway siding |
| 10am | Grover | the moss-green envelope | a flooded quarry |
| 11am | Delphine | the saffron envelope | a caravan park |

## How it falls out

1. [direct] from clue 3 landing:a railway siding: ruled out position(s) 1,3,4
2. [direct] from clue 4 envelope:the kingfisher envelope: ruled out position(s) 1,3,4
3. [bijection] envelope:the saffron envelope: ruled out position(s) 2
4. [bijection] envelope:the moss-green envelope: ruled out position(s) 2
5. [bijection] envelope:the striped envelope: ruled out position(s) 2
6. [bijection] landing:a cricket pitch: ruled out position(s) 2
7. [bijection] landing:a flooded quarry: ruled out position(s) 2
8. [bijection] landing:a caravan park: ruled out position(s) 2
9. [order] from clue 8 pilot:Grover: ruled out position(s) 1
10. [order] from clue 7 pilot:Delphine: ruled out position(s) 3
11. [order] from clue 7 pilot:Isolde: ruled out position(s) 3
12. [order] from clue 5 pilot:Delphine: ruled out position(s) 2
13. [order] from clue 5 pilot:Horatio: ruled out position(s) 2
14. [order] from clue 2 landing:a cricket pitch: ruled out position(s) 3,4
15. [order] from clue 1 landing:a flooded quarry: ruled out position(s) 1,4
16. [order] from clue 1 pilot:Horatio: ruled out position(s) 3,4
17. [order] from clue 5 pilot:Delphine: ruled out position(s) 1
18. [order] from clue 7 pilot:Isolde: ruled out position(s) 4
19. [direct] from clue 6 envelope:the striped envelope: ruled out position(s) 3
20. [bijection] landing:a caravan park: ruled out position(s) 1,3
21. [bijection] pilot:Isolde: ruled out position(s) 1
22. [bijection] pilot:Grover: ruled out position(s) 4
23. [bijection] pilot:Grover: ruled out position(s) 2
24. [order] from clue 8 envelope:the saffron envelope: ruled out position(s) 1,3
25. [bijection] envelope:the moss-green envelope: ruled out position(s) 4
26. [bijection] envelope:the striped envelope: ruled out position(s) 4
27. [bijection] envelope:the moss-green envelope: ruled out position(s) 1

---

<sub>seed `2026172694221` &middot; score 4.93 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
