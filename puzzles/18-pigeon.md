# Andy's Swiftest Birds

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `ae610c336401`

## Introduction

Andy races pigeons, and each bird is bred for a different combination of stubbornness and speed.
Five pigeons are involved. Determine each pigeon's distance, breed and loft.
- **Pigeon**: Hieronymus, Grimsby, Dot, Cadwallader and Alabaster.
- **Distance** (listed from shorter to longer): 200 miles, 300 miles, 400 miles, 500 miles and 600 miles.
- **Breed**: a Delbar, a Sion, a Busschaert, a Vandenabeele and a Stichelbaut.
- **Loft**: the canal loft, the stable loft, the chapel loft, the orchard loft and the gable loft.
Every pigeon has a different distance, breed and loft, so within each category every item is used exactly once.

## Clues

1. The pigeon that descends from a Delbar flies 200 miles.
2. Hieronymus flies 500 miles.
3. Cadwallader is kept in the gable loft.
4. The pigeon that is kept in the canal loft is exactly one hundred miles shorter than 600 miles, with no distance in between.
5. The pigeon that descends from a Sion is exactly one hundred miles shorter than 600 miles, with no distance in between.
6. 300 miles falls somewhere between Alabaster and Grimsby in distance order.
7. The pigeon that descends from a Stichelbaut and 300 miles are exactly one hundred miles apart in distance order, in one direction or the other.
8. The pigeon that is kept in the canal loft is exactly one hundred miles shorter than the pigeon that descends from a Vandenabeele, with no distance in between.
9. The pigeon that is kept in the orchard loft is exactly one hundred miles shorter than Alabaster, with no distance in between.
10. Grimsby is shorter than the pigeon that is kept in the stable loft in distance order.

## Solving chart

*Distance vs Pigeon*

| | Hieronymus | Grimsby | Dot | Cadwallader | Alabaster |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Breed*

| | a Delbar | a Sion | a Busschaert | a Vandenabeele | a Stichelbaut |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Loft*

| | the canal loft | the stable loft | the chapel loft | the orchard loft | the gable loft |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Pigeon vs Breed*

| | a Delbar | a Sion | a Busschaert | a Vandenabeele | a Stichelbaut |
|---|---|---|---|---|---|
| **Hieronymus** | | | | | |
| **Grimsby** | | | | | |
| **Dot** | | | | | |
| **Cadwallader** | | | | | |
| **Alabaster** | | | | | |

*Pigeon vs Loft*

| | the canal loft | the stable loft | the chapel loft | the orchard loft | the gable loft |
|---|---|---|---|---|---|
| **Hieronymus** | | | | | |
| **Grimsby** | | | | | |
| **Dot** | | | | | |
| **Cadwallader** | | | | | |
| **Alabaster** | | | | | |

*Breed vs Loft*

| | the canal loft | the stable loft | the chapel loft | the orchard loft | the gable loft |
|---|---|---|---|---|---|
| **a Delbar** | | | | | |
| **a Sion** | | | | | |
| **a Busschaert** | | | | | |
| **a Vandenabeele** | | | | | |
| **a Stichelbaut** | | | | | |

## Solution

| Distance | Pigeon | Breed | Loft |
|---|---|---|---|
| 200 miles | Grimsby | a Delbar | the chapel loft |
| 300 miles | Dot | a Busschaert | the orchard loft |
| 400 miles | Alabaster | a Stichelbaut | the stable loft |
| 500 miles | Hieronymus | a Sion | the canal loft |
| 600 miles | Cadwallader | a Vandenabeele | the gable loft |

## How it falls out

1. [direct] from clue 4 breed:a Delbar: ruled out position(s) 2,3,4,5
2. [direct] from clue 3 bird:Hieronymus: ruled out position(s) 1,2,3,5
3. [bijection] bird:Grimsby: ruled out position(s) 4
4. [bijection] bird:Dot: ruled out position(s) 4
5. [bijection] bird:Cadwallader: ruled out position(s) 4
6. [bijection] bird:Alabaster: ruled out position(s) 4
7. [bijection] breed:a Sion: ruled out position(s) 1
8. [bijection] breed:a Busschaert: ruled out position(s) 1
9. [bijection] breed:a Vandenabeele: ruled out position(s) 1
10. [bijection] breed:a Stichelbaut: ruled out position(s) 1
11. [direct] from clue 2 loft:the gable loft: ruled out position(s) 4
12. [order] from clue 10 loft:the canal loft: ruled out position(s) 5
13. [order] from clue 9 loft:the orchard loft: ruled out position(s) 3,5
14. [order] from clue 9 bird:Alabaster: ruled out position(s) 1
15. [order] from clue 8 breed:a Sion: ruled out position(s) 2,3,5
16. [order] from clue 7 breed:a Stichelbaut: ruled out position(s) 2,4,5
17. [order] from clue 6 bird:Alabaster: ruled out position(s) 2
18. [order] from clue 6 bird:Grimsby: ruled out position(s) 2,3,5
19. [order] from clue 9 loft:the orchard loft: ruled out position(s) 1
20. [order] from clue 5 loft:the canal loft: ruled out position(s) 1,2,3
21. [order] from clue 10 breed:a Vandenabeele: ruled out position(s) 2,3,4
22. [order] from clue 1 loft:the stable loft: ruled out position(s) 1
23. [bijection] bird:Dot: ruled out position(s) 1
24. [bijection] bird:Cadwallader: ruled out position(s) 1
25. [bijection] breed:a Busschaert: ruled out position(s) 3,4,5
26. [bijection] loft:the stable loft: ruled out position(s) 4
27. [bijection] loft:the chapel loft: ruled out position(s) 4
28. [bijection] loft:the orchard loft: ruled out position(s) 4
29. [order] from clue 9 bird:Alabaster: ruled out position(s) 5
30. [direct] from clue 2 loft:the gable loft: ruled out position(s) 1
31. [bijection] bird:Dot: ruled out position(s) 3
32. [bijection] bird:Cadwallader: ruled out position(s) 3
33. [bijection] loft:the stable loft: ruled out position(s) 2
34. [bijection] loft:the chapel loft: ruled out position(s) 2
35. [bijection] loft:the gable loft: ruled out position(s) 2
36. [bijection] loft:the chapel loft: ruled out position(s) 3,5
37. [direct] from clue 2 bird:Cadwallader: ruled out position(s) 2
38. [direct] from clue 2 loft:the gable loft: ruled out position(s) 3
39. [bijection] bird:Dot: ruled out position(s) 5
40. [bijection] loft:the stable loft: ruled out position(s) 5

---

<sub>seed `2026172717978` &middot; score 5.195 &middot; atoms 10 &middot; positives 3 &middot; solved by order</sub>
