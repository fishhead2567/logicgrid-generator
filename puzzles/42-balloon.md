# The Thistledown Balloon Ascent

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `c61dbfe2a5c6`

## Introduction

The Thistledown Ascent is less a race than a slow argument conducted at two thousand feet.
Five pilots are involved. Determine each pilot's start time, envelope and ballast.
- **Pilot**: Grover, Rosalind, Anneliese, Montague and Delphine.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Envelope**: the oxblood envelope, the silver envelope, the striped envelope, the moss-green envelope and the patchwork envelope.
- **Ballast**: pea gravel, dried beans, rock salt, bottled water and lead shot.
Every pilot has a different start time, envelope and ballast, so within each category every item is used exactly once.

## Clues

1. The pilot who flies the patchwork envelope launches at 10am.
2. The pilot who carries bottled water falls somewhere between Anneliese and noon in start time order. The pilot who carries pea gravel is earlier than noon in start time order.
3. At least one of the following holds, and possibly more than one: (a) The pilot who flies the oxblood envelope launches at 8am. (b) The pilot who carries pea gravel does not launch at 8am.
4. Anneliese falls somewhere between the pilot who carries bottled water and 8am in start time order.
5. Grover falls somewhere between the pilot who carries lead shot and noon in start time order.
6. The pilot who flies the moss-green envelope is later than 10am in start time order.
7. The pilot who flies the silver envelope and noon are exactly one hour apart in start time order, in one direction or the other.
8. The pilot who flies the striped envelope and 9am are exactly one hour apart in start time order, in one direction or the other.
9. The pilot who carries lead shot and Delphine are exactly one hour apart in start time order, in one direction or the other.
10. Montague is earlier than the pilot who flies the moss-green envelope in start time order.
11. The pilot who carries dried beans and the pilot who flies the striped envelope are exactly one hour apart in start time order, in one direction or the other.

## Solving chart

*Start time vs Pilot*

| | Grover | Rosalind | Anneliese | Montague | Delphine |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Envelope*

| | the oxblood envelope | the silver envelope | the striped envelope | the moss-green envelope | the patchwork envelope |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Ballast*

| | pea gravel | dried beans | rock salt | bottled water | lead shot |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Pilot vs Envelope*

| | the oxblood envelope | the silver envelope | the striped envelope | the moss-green envelope | the patchwork envelope |
|---|---|---|---|---|---|
| **Grover** | | | | | |
| **Rosalind** | | | | | |
| **Anneliese** | | | | | |
| **Montague** | | | | | |
| **Delphine** | | | | | |

*Pilot vs Ballast*

| | pea gravel | dried beans | rock salt | bottled water | lead shot |
|---|---|---|---|---|---|
| **Grover** | | | | | |
| **Rosalind** | | | | | |
| **Anneliese** | | | | | |
| **Montague** | | | | | |
| **Delphine** | | | | | |

*Envelope vs Ballast*

| | pea gravel | dried beans | rock salt | bottled water | lead shot |
|---|---|---|---|---|---|
| **the oxblood envelope** | | | | | |
| **the silver envelope** | | | | | |
| **the striped envelope** | | | | | |
| **the moss-green envelope** | | | | | |
| **the patchwork envelope** | | | | | |

## Solution

| Start time | Pilot | Envelope | Ballast |
|---|---|---|---|
| 8am | Montague | the striped envelope | lead shot |
| 9am | Delphine | the oxblood envelope | dried beans |
| 10am | Anneliese | the patchwork envelope | pea gravel |
| 11am | Grover | the silver envelope | bottled water |
| noon | Rosalind | the moss-green envelope | rock salt |

## How it falls out

1. [direct] from clue 4 envelope:the patchwork envelope: ruled out position(s) 1,2,4,5
2. [bijection] envelope:the oxblood envelope: ruled out position(s) 3
3. [bijection] envelope:the silver envelope: ruled out position(s) 3
4. [bijection] envelope:the striped envelope: ruled out position(s) 3
5. [bijection] envelope:the moss-green envelope: ruled out position(s) 3
6. [order] from clue 10 pilot:Anneliese: ruled out position(s) 1,5
7. [order] from clue 10 ballast:bottled water: ruled out position(s) 1,2
8. [order] from clue 9 envelope:the striped envelope: ruled out position(s) 2,4,5
9. [order] from clue 8 pilot:Montague: ruled out position(s) 5
10. [order] from clue 8 envelope:the moss-green envelope: ruled out position(s) 1
11. [order] from clue 7 envelope:the silver envelope: ruled out position(s) 1,2,5
12. [order] from clue 6 ballast:bottled water: ruled out position(s) 5
13. [order] from clue 6 pilot:Anneliese: ruled out position(s) 4
14. [order] from clue 5 pilot:Grover: ruled out position(s) 1,5
15. [order] from clue 5 ballast:lead shot: ruled out position(s) 4,5
16. [order] from clue 12 pilot:Delphine: ruled out position(s) 5
17. [order] from clue 3 ballast:pea gravel: ruled out position(s) 5
18. [order] from clue 2 ballast:dried beans: ruled out position(s) 1,3,4,5
19. [order] from clue 1 envelope:the moss-green envelope: ruled out position(s) 2
20. [bijection] ballast:pea gravel: ruled out position(s) 2
21. [bijection] ballast:rock salt: ruled out position(s) 2
22. [bijection] ballast:lead shot: ruled out position(s) 2
23. [bijection] ballast:rock salt: ruled out position(s) 1,3,4
24. [bijection] envelope:the oxblood envelope: ruled out position(s) 1,4
25. [bijection] envelope:the moss-green envelope: ruled out position(s) 4
26. [bijection] envelope:the oxblood envelope: ruled out position(s) 5
27. [bijection] pilot:Rosalind: ruled out position(s) 1,2,3,4
28. [order] from clue 12 pilot:Delphine: ruled out position(s) 1,3
29. [bijection] pilot:Montague: ruled out position(s) 2,3,4
30. [disjunction] from clue 11 ballast:pea gravel: ruled out position(s) 1
31. [bijection] ballast:lead shot: ruled out position(s) 3
32. [order] from clue 12 pilot:Delphine: ruled out position(s) 4
33. [bijection] pilot:Grover: ruled out position(s) 2
34. [bijection] pilot:Anneliese: ruled out position(s) 2
35. [bijection] pilot:Grover: ruled out position(s) 3
36. [order] from clue 10 ballast:bottled water: ruled out position(s) 3
37. [bijection] ballast:pea gravel: ruled out position(s) 4

---

<sub>seed `2026172908034` &middot; score 8.5792 &middot; atoms 12 &middot; positives 1 &middot; solved by disjunction</sub>
