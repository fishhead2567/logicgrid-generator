# Andy's Swiftest Birds

*Andy races pigeons, and each bird is bred for a different combination of stubbornness and speed.*

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `254e654098e6`

## Introduction

There are 5 races. Each has exactly one distance and one item from every other category below, and within each category every item belongs to a different race.
- **Distance** (listed in order): 200 miles, 300 miles, 400 miles, 500 miles and 600 miles.
- **Pigeon**: Hieronymus, Alabaster, Nutmeg, Dot and Grimsby.
- **Breed**: a Van Loon, a Busschaert, a Janssen, a Vandenabeele and a Sion.
- **Loft**: the stable loft, the orchard loft, the canal loft, the gable loft and the chapel loft.
The hundred mileses above are listed in order, from 200 miles to 600 miles.

## Clues

1. 200 miles goes with the orchard loft.
2. A Sion, 600 miles and the stable loft are three different races. The gable loft falls somewhere between a Busschaert and a Sion in distance order. Grimsby, a Sion and 600 miles are three different races.
3. A Busschaert falls somewhere between Nutmeg and 300 miles in distance order.
4. Grimsby and 400 miles are next to each other in distance order, in one order or the other.
5. Hieronymus falls somewhere between a Janssen and 200 miles in distance order.
6. 200 miles is immediately shorter than the canal loft's distance, with no distance in between.
7. A Van Loon and 300 miles are next to each other in distance order, in one order or the other.
8. Alabaster's distance is shorter than a Janssen's distance.
9. Grimsby's distance is shorter than a Vandenabeele's distance.

## Solving chart

*Distance vs Pigeon*

| | Hieronymus | Alabaster | Nutmeg | Dot | Grimsby |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Breed*

| | a Van Loon | a Busschaert | a Janssen | a Vandenabeele | a Sion |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Loft*

| | the stable loft | the orchard loft | the canal loft | the gable loft | the chapel loft |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Pigeon vs Breed*

| | a Van Loon | a Busschaert | a Janssen | a Vandenabeele | a Sion |
|---|---|---|---|---|---|
| **Hieronymus** | | | | | |
| **Alabaster** | | | | | |
| **Nutmeg** | | | | | |
| **Dot** | | | | | |
| **Grimsby** | | | | | |

*Pigeon vs Loft*

| | the stable loft | the orchard loft | the canal loft | the gable loft | the chapel loft |
|---|---|---|---|---|---|
| **Hieronymus** | | | | | |
| **Alabaster** | | | | | |
| **Nutmeg** | | | | | |
| **Dot** | | | | | |
| **Grimsby** | | | | | |

*Breed vs Loft*

| | the stable loft | the orchard loft | the canal loft | the gable loft | the chapel loft |
|---|---|---|---|---|---|
| **a Van Loon** | | | | | |
| **a Busschaert** | | | | | |
| **a Janssen** | | | | | |
| **a Vandenabeele** | | | | | |
| **a Sion** | | | | | |

## Solution

| Distance | Pigeon | Breed | Loft |
|---|---|---|---|
| 200 miles | Alabaster | a Van Loon | the orchard loft |
| 300 miles | Hieronymus | a Sion | the canal loft |
| 400 miles | Dot | a Janssen | the gable loft |
| 500 miles | Grimsby | a Busschaert | the stable loft |
| 600 miles | Nutmeg | a Vandenabeele | the chapel loft |

## How it falls out

1. [direct] from clue 9 loft:the orchard loft: ruled out position(s) 2,3,4,5
2. [bijection] from clue 11 breed:a Sion: ruled out position(s) 5
3. [bijection] from clue 11 loft:the stable loft: ruled out position(s) 5
4. [bijection] from clue 5 bird:Grimsby: ruled out position(s) 5
5. [bijection] loft:the stable loft: ruled out position(s) 1
6. [bijection] loft:the canal loft: ruled out position(s) 1
7. [bijection] loft:the gable loft: ruled out position(s) 1
8. [bijection] loft:the chapel loft: ruled out position(s) 1
9. [order] from clue 10 breed:a Vandenabeele: ruled out position(s) 1
10. [order] from clue 8 breed:a Van Loon: ruled out position(s) 2,4,5
11. [order] from clue 7 bird:Grimsby: ruled out position(s) 1,3
12. [order] from clue 10 breed:a Vandenabeele: ruled out position(s) 2
13. [order] from clue 6 loft:the gable loft: ruled out position(s) 5
14. [order] from clue 4 bird:Alabaster: ruled out position(s) 5
15. [order] from clue 4 breed:a Janssen: ruled out position(s) 1
16. [order] from clue 3 loft:the canal loft: ruled out position(s) 3,4,5
17. [order] from clue 2 breed:a Busschaert: ruled out position(s) 1,2,5
18. [order] from clue 2 bird:Nutmeg: ruled out position(s) 1,2,3
19. [order] from clue 6 loft:the gable loft: ruled out position(s) 4
20. [order] from clue 6 breed:a Sion: ruled out position(s) 3,4
21. [order] from clue 1 bird:Hieronymus: ruled out position(s) 1,5
22. [order] from clue 1 breed:a Janssen: ruled out position(s) 2
23. [bijection] breed:a Sion: ruled out position(s) 1
24. [bijection] loft:the stable loft: ruled out position(s) 2
25. [bijection] loft:the gable loft: ruled out position(s) 2
26. [bijection] loft:the chapel loft: ruled out position(s) 2
27. [bijection] loft:the chapel loft: ruled out position(s) 3,4
28. [order] from clue 6 breed:a Busschaert: ruled out position(s) 3
29. [order] from clue 2 bird:Nutmeg: ruled out position(s) 4
30. [bijection] from clue 5 bird:Grimsby: ruled out position(s) 2
31. [order] from clue 10 breed:a Vandenabeele: ruled out position(s) 3,4
32. [bijection] bird:Hieronymus: ruled out position(s) 4
33. [bijection] bird:Alabaster: ruled out position(s) 4
34. [bijection] bird:Dot: ruled out position(s) 4,5
35. [bijection] breed:a Janssen: ruled out position(s) 4,5
36. [bijection] breed:a Van Loon: ruled out position(s) 3
37. [bijection] loft:the stable loft: ruled out position(s) 3
38. [order] from clue 4 bird:Alabaster: ruled out position(s) 3
39. [order] from clue 1 bird:Hieronymus: ruled out position(s) 3
40. [bijection] bird:Alabaster: ruled out position(s) 2
_... and 2 further steps._

---

<sub>seed `2026172757573` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
