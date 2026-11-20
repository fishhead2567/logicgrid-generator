# The Build Server Contest

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 14 &nbsp;&nbsp; **id** `deefc147c273`

## Introduction

A creative-mode server, one weekend, and a block limit everybody swore they would stay under.
Five builders are involved. Determine each builder's score, build, biome and material.
- **Builder**: Oscar Pell, Thandiwe, Milo, Rafferty and Keiko.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Build**: a clock tower, a desert bazaar, a floating island, a mountain railway and a treetop village.
- **Biome**: a snowy tundra, a swamp, a cherry grove, a jungle and a mushroom field.
- **Material**: dark oak, copper, packed ice, sea lantern and quartz.
Every builder has a different score, build, biome and material, so within each category every item is used exactly once.

## Clues

1. The builder who builds in a swamp falls somewhere between Keiko and Thandiwe in score order. Thandiwe builds a desert bazaar. Keiko does not build it from dark oak.
2. The builder who builds it from sea lantern falls somewhere between 61 points and 73 points in score order. The builder who builds it from copper is higher than 61 points in score order.
3. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The builder who builds in a cherry grove and 70 points are exactly one score step apart in score order, in one direction or the other. (b) Keiko does not score 64 points.
4. The builder who builds in a swamp does not score 70 points. Oscar Pell and 70 points are exactly one score step apart in score order, in one direction or the other.
5. The builder who builds in a mushroom field is lower than 73 points in score order.
6. The builder who builds a mountain railway does not score 70 points.
7. At least one of the following holds, and possibly more than one: (a) Thandiwe is higher than 70 points in score order. (b) Keiko scores 70 points.
8. The builder who builds in a mushroom field and the builder who builds it from quartz are exactly one score step apart in score order, in one direction or the other.
9. The builder who builds a clock tower and the builder who builds it from dark oak are exactly one score step apart in score order, in one direction or the other.
10. The builder who builds in a jungle and the builder who builds a mountain railway are exactly one score step apart in score order, in one direction or the other.
11. The builder who builds in a snowy tundra falls somewhere between Milo and Thandiwe in score order.
12. The builder who builds a clock tower and Rafferty are exactly one score step apart in score order, in one direction or the other.
13. At least one of the following holds, and possibly more than one: (a) Rafferty does not build a floating island. (b) Milo does not build it from quartz.
14. The builder who builds in a swamp and the builder who builds it from packed ice are exactly one score step apart in score order, in one direction or the other.

## Solving chart

*Score vs Builder*

| | Oscar Pell | Thandiwe | Milo | Rafferty | Keiko |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Build*

| | a clock tower | a desert bazaar | a floating island | a mountain railway | a treetop village |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Biome*

| | a snowy tundra | a swamp | a cherry grove | a jungle | a mushroom field |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Material*

| | dark oak | copper | packed ice | sea lantern | quartz |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Builder vs Build*

| | a clock tower | a desert bazaar | a floating island | a mountain railway | a treetop village |
|---|---|---|---|---|---|
| **Oscar Pell** | | | | | |
| **Thandiwe** | | | | | |
| **Milo** | | | | | |
| **Rafferty** | | | | | |
| **Keiko** | | | | | |

*Builder vs Biome*

| | a snowy tundra | a swamp | a cherry grove | a jungle | a mushroom field |
|---|---|---|---|---|---|
| **Oscar Pell** | | | | | |
| **Thandiwe** | | | | | |
| **Milo** | | | | | |
| **Rafferty** | | | | | |
| **Keiko** | | | | | |

*Builder vs Material*

| | dark oak | copper | packed ice | sea lantern | quartz |
|---|---|---|---|---|---|
| **Oscar Pell** | | | | | |
| **Thandiwe** | | | | | |
| **Milo** | | | | | |
| **Rafferty** | | | | | |
| **Keiko** | | | | | |

*Build vs Biome*

| | a snowy tundra | a swamp | a cherry grove | a jungle | a mushroom field |
|---|---|---|---|---|---|
| **a clock tower** | | | | | |
| **a desert bazaar** | | | | | |
| **a floating island** | | | | | |
| **a mountain railway** | | | | | |
| **a treetop village** | | | | | |

*Build vs Material*

| | dark oak | copper | packed ice | sea lantern | quartz |
|---|---|---|---|---|---|
| **a clock tower** | | | | | |
| **a desert bazaar** | | | | | |
| **a floating island** | | | | | |
| **a mountain railway** | | | | | |
| **a treetop village** | | | | | |

*Biome vs Material*

| | dark oak | copper | packed ice | sea lantern | quartz |
|---|---|---|---|---|---|
| **a snowy tundra** | | | | | |
| **a swamp** | | | | | |
| **a cherry grove** | | | | | |
| **a jungle** | | | | | |
| **a mushroom field** | | | | | |

## Solution

| Score | Builder | Build | Biome | Material |
|---|---|---|---|---|
| 61 points | Milo | a floating island | a jungle | quartz |
| 64 points | Keiko | a mountain railway | a mushroom field | packed ice |
| 67 points | Oscar Pell | a clock tower | a swamp | sea lantern |
| 70 points | Rafferty | a treetop village | a snowy tundra | dark oak |
| 73 points | Thandiwe | a desert bazaar | a cherry grove | copper |

## How it falls out

1. [direct] from clue 13 build:a mountain railway: ruled out position(s) 4
2. [direct] from clue 7 biome:a swamp: ruled out position(s) 4
3. [order] from clue 14 biome:a snowy tundra: ruled out position(s) 1,5
4. [order] from clue 11 material:copper: ruled out position(s) 1
5. [order] from clue 9 builder:Oscar Pell: ruled out position(s) 1,2,4
6. [order] from clue 8 biome:a mushroom field: ruled out position(s) 5
7. [order] from clue 4 material:sea lantern: ruled out position(s) 1,5
8. [order] from clue 3 material:packed ice: ruled out position(s) 5
9. [order] from clue 2 biome:a swamp: ruled out position(s) 1,5
10. [order] from clue 1 biome:a jungle: ruled out position(s) 5
11. [bijection] biome:a cherry grove: ruled out position(s) 1,2,3,4
12. [disjunction] from clue 18 builder:Keiko: ruled out position(s) 1,3,4,5
13. [disjunction] from clue 6 builder:Thandiwe: ruled out position(s) 1,2,3,4
14. [order] from clue 14 builder:Milo: ruled out position(s) 4,5
15. [order] from clue 2 biome:a swamp: ruled out position(s) 2
16. [order] from clue 3 material:packed ice: ruled out position(s) 1,3
17. [direct] from clue 16 build:a desert bazaar: ruled out position(s) 1,2,3,4
18. [direct] from clue 12 material:dark oak: ruled out position(s) 2
19. [order] from clue 10 build:a clock tower: ruled out position(s) 1
20. [bijection] biome:a snowy tundra: ruled out position(s) 3
21. [bijection] biome:a jungle: ruled out position(s) 3
22. [bijection] biome:a mushroom field: ruled out position(s) 3
23. [bijection] build:a clock tower: ruled out position(s) 5
24. [bijection] build:a floating island: ruled out position(s) 5
25. [bijection] build:a mountain railway: ruled out position(s) 5
26. [bijection] build:a treetop village: ruled out position(s) 5
27. [bijection] builder:Oscar Pell: ruled out position(s) 5
28. [bijection] builder:Milo: ruled out position(s) 2
29. [bijection] builder:Rafferty: ruled out position(s) 2,5
30. [bijection] builder:Rafferty: ruled out position(s) 1,3
31. [order] from clue 5 build:a clock tower: ruled out position(s) 2,4
32. [order] from clue 10 material:dark oak: ruled out position(s) 1,3,5
33. [order] from clue 15 material:quartz: ruled out position(s) 4
34. [bijection] build:a floating island: ruled out position(s) 3
35. [bijection] build:a mountain railway: ruled out position(s) 3
36. [bijection] build:a treetop village: ruled out position(s) 3
37. [bijection] builder:Milo: ruled out position(s) 3
38. [bijection] material:copper: ruled out position(s) 4
39. [bijection] material:packed ice: ruled out position(s) 4
40. [bijection] material:sea lantern: ruled out position(s) 4
_... and 12 further steps._

---

<sub>seed `2026173208043` &middot; score 10.0883 &middot; atoms 18 &middot; positives 1 &middot; solved by disjunction</sub>
