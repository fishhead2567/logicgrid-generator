# The Mesa Verde Balloon Ascent

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `052ccc576fca`

## Introduction

The Mesa Verde Ascent is less a race than a slow argument conducted at two thousand feet.
Five pilots are involved. Determine each pilot's start time, envelope and landing site.
- **Pilot**: Annika, Grover, Rosa, Rafael and Delia.
- **Start time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Envelope**: the oxblood envelope, the saffron envelope, the striped envelope, the silver envelope and the kingfisher envelope.
- **Landed at**: a cabbage field, an RV park, a rail siding, a flooded quarry and a little-league outfield.
Every pilot has a different start time, envelope and landing site, so within each category every item is used exactly once.

## Clues

1. The pilot who flies the silver envelope and noon are exactly one hour apart in start time order, in one direction or the other.
2. The pilot who comes down in a flooded quarry and noon are exactly two hours apart in start time order.
3. Annika and 10am are exactly one hour apart in start time order, in one direction or the other.
4. The pilot who flies the striped envelope and noon are exactly two hours apart in start time order.
5. Delia is exactly one hour earlier than the pilot who comes down in a flooded quarry, with no start time in between.
6. At least one of the following holds, and possibly more than one: (a) The pilot who comes down in a cabbage field and Delia are exactly two hours apart in start time order. (b) Grover flies the saffron envelope.
7. The pilot who flies the saffron envelope and Rafael are exactly one hour apart in start time order, in one direction or the other.
8. The pilot who flies the striped envelope is earlier than the pilot who comes down in a rail siding in start time order.
9. Rosa is earlier than the pilot who flies the kingfisher envelope in start time order.
10. At least one of the following holds, and possibly more than one: (a) Grover comes down in a cabbage field. (b) Rafael comes down in a flooded quarry.
11. The pilot who comes down in an RV park and Grover are exactly three hours apart in start time order.

## Solving chart

*Start time vs Pilot*

| | Annika | Grover | Rosa | Rafael | Delia |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Envelope*

| | the oxblood envelope | the saffron envelope | the striped envelope | the silver envelope | the kingfisher envelope |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Start time vs Landed at*

| | a cabbage field | an RV park | a rail siding | a flooded quarry | a little-league outfield |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Pilot vs Envelope*

| | the oxblood envelope | the saffron envelope | the striped envelope | the silver envelope | the kingfisher envelope |
|---|---|---|---|---|---|
| **Annika** | | | | | |
| **Grover** | | | | | |
| **Rosa** | | | | | |
| **Rafael** | | | | | |
| **Delia** | | | | | |

*Pilot vs Landed at*

| | a cabbage field | an RV park | a rail siding | a flooded quarry | a little-league outfield |
|---|---|---|---|---|---|
| **Annika** | | | | | |
| **Grover** | | | | | |
| **Rosa** | | | | | |
| **Rafael** | | | | | |
| **Delia** | | | | | |

*Envelope vs Landed at*

| | a cabbage field | an RV park | a rail siding | a flooded quarry | a little-league outfield |
|---|---|---|---|---|---|
| **the oxblood envelope** | | | | | |
| **the saffron envelope** | | | | | |
| **the striped envelope** | | | | | |
| **the silver envelope** | | | | | |
| **the kingfisher envelope** | | | | | |

## Solution

| Start time | Pilot | Envelope | Landed at |
|---|---|---|---|
| 8am | Rosa | the oxblood envelope | a little-league outfield |
| 9am | Delia | the saffron envelope | an RV park |
| 10am | Rafael | the striped envelope | a flooded quarry |
| 11am | Annika | the silver envelope | a cabbage field |
| noon | Grover | the kingfisher envelope | a rail siding |

## How it falls out

1. [order] from clue 11 envelope:the striped envelope: ruled out position(s) 5
2. [order] from clue 11 landing:a rail siding: ruled out position(s) 1
3. [order] from clue 9 envelope:the striped envelope: ruled out position(s) 1,2,4
4. [order] from clue 11 landing:a rail siding: ruled out position(s) 2,3
5. [order] from clue 8 landing:a flooded quarry: ruled out position(s) 1,2,4,5
6. [order] from clue 7 pilot:Delia: ruled out position(s) 1,3,4,5
7. [order] from clue 5 landing:an RV park: ruled out position(s) 3
8. [order] from clue 5 pilot:Grover: ruled out position(s) 3
9. [order] from clue 3 envelope:the silver envelope: ruled out position(s) 1,2,3,5
10. [order] from clue 2 pilot:Annika: ruled out position(s) 1,3,5
11. [order] from clue 1 pilot:Rosa: ruled out position(s) 5
12. [order] from clue 1 envelope:the kingfisher envelope: ruled out position(s) 1
13. [bijection] envelope:the oxblood envelope: ruled out position(s) 3,4
14. [bijection] envelope:the saffron envelope: ruled out position(s) 3,4
15. [bijection] envelope:the kingfisher envelope: ruled out position(s) 3,4
16. [bijection] landing:a cabbage field: ruled out position(s) 3
17. [bijection] landing:a little-league outfield: ruled out position(s) 3
18. [bijection] pilot:Annika: ruled out position(s) 2
19. [bijection] pilot:Grover: ruled out position(s) 2
20. [bijection] pilot:Rosa: ruled out position(s) 2
21. [bijection] pilot:Rafael: ruled out position(s) 2
22. [order] from clue 5 landing:an RV park: ruled out position(s) 5
23. [order] from clue 4 envelope:the saffron envelope: ruled out position(s) 1
24. [order] from clue 4 pilot:Rafael: ruled out position(s) 5
25. [bijection] envelope:the oxblood envelope: ruled out position(s) 2,5
26. [bijection] pilot:Grover: ruled out position(s) 4
27. [bijection] pilot:Rosa: ruled out position(s) 4
28. [bijection] pilot:Rafael: ruled out position(s) 4
29. [bijection] pilot:Grover: ruled out position(s) 1
30. [order] from clue 4 envelope:the saffron envelope: ruled out position(s) 5
31. [order] from clue 5 landing:an RV park: ruled out position(s) 1,4
32. [bijection] envelope:the kingfisher envelope: ruled out position(s) 2
33. [bijection] landing:a cabbage field: ruled out position(s) 2
34. [bijection] landing:a little-league outfield: ruled out position(s) 2
35. [disjunction] from clue 10 landing:a cabbage field: ruled out position(s) 1,5
36. [disjunction] from clue 6 pilot:Rafael: ruled out position(s) 1
37. [bijection] landing:a rail siding: ruled out position(s) 4
38. [bijection] landing:a little-league outfield: ruled out position(s) 4
39. [bijection] landing:a little-league outfield: ruled out position(s) 5
40. [bijection] pilot:Rosa: ruled out position(s) 3

---

<sub>seed `2026173200124` &middot; score 9.2622 &middot; atoms 11 &middot; positives 0 &middot; solved by disjunction</sub>
