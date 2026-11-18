# Andy's Swiftest Birds

*Andy races pigeons, and each bird is bred for a different combination of stubbornness and speed.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `52c15f5a6abe`

## Introduction

There are 4 races. Each has exactly one distance and one item from every other category below, and within each category every item belongs to a different race.
- **Distance** (listed in order): 200 miles, 300 miles, 400 miles and 500 miles.
- **Pigeon**: Cadwallader, Dot, Pip and Alabaster.
- **Plumage**: slate blue, mealy red, dun and grizzle.
- **Loft**: the chapel loft, the canal loft, the orchard loft and the stable loft.
The hundred mileses above are listed in order, from 200 miles to 500 miles.

## Clues

1. 300 miles goes with the orchard loft.
2. The chapel loft's distance is immediately shorter than Pip's distance, with no distance in between. The chapel loft goes with mealy red.
3. 400 miles falls somewhere between Cadwallader and Dot in distance order.
4. Dun falls somewhere between Cadwallader and Pip in distance order.
5. The stable loft falls somewhere between mealy red and slate blue in distance order.

## Solving chart

*Distance vs Pigeon*

| | Cadwallader | Dot | Pip | Alabaster |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Plumage*

| | slate blue | mealy red | dun | grizzle |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Loft*

| | the chapel loft | the canal loft | the orchard loft | the stable loft |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Pigeon vs Plumage*

| | slate blue | mealy red | dun | grizzle |
|---|---|---|---|---|
| **Cadwallader** | | | | |
| **Dot** | | | | |
| **Pip** | | | | |
| **Alabaster** | | | | |

*Pigeon vs Loft*

| | the chapel loft | the canal loft | the orchard loft | the stable loft |
|---|---|---|---|---|
| **Cadwallader** | | | | |
| **Dot** | | | | |
| **Pip** | | | | |
| **Alabaster** | | | | |

*Plumage vs Loft*

| | the chapel loft | the canal loft | the orchard loft | the stable loft |
|---|---|---|---|---|
| **slate blue** | | | | |
| **mealy red** | | | | |
| **dun** | | | | |
| **grizzle** | | | | |

## Solution

| Distance | Pigeon | Plumage | Loft |
|---|---|---|---|
| 200 miles | Dot | mealy red | the chapel loft |
| 300 miles | Pip | grizzle | the orchard loft |
| 400 miles | Alabaster | dun | the stable loft |
| 500 miles | Cadwallader | slate blue | the canal loft |

## How it falls out

1. [direct] from clue 1 loft:the orchard loft: ruled out position(s) 1,3,4
2. [bijection] loft:the chapel loft: ruled out position(s) 2
3. [bijection] loft:the canal loft: ruled out position(s) 2
4. [bijection] loft:the stable loft: ruled out position(s) 2
5. [direct] from clue 4 plumage:mealy red: ruled out position(s) 2
6. [order] from clue 6 bird:Cadwallader: ruled out position(s) 3
7. [order] from clue 6 bird:Dot: ruled out position(s) 3
8. [order] from clue 5 loft:the chapel loft: ruled out position(s) 4
9. [order] from clue 5 bird:Pip: ruled out position(s) 1,3
10. [order] from clue 3 plumage:dun: ruled out position(s) 1,4
11. [order] from clue 2 loft:the stable loft: ruled out position(s) 1,4
12. [order] from clue 2 plumage:mealy red: ruled out position(s) 3
13. [order] from clue 2 plumage:slate blue: ruled out position(s) 3
14. [direct] from clue 4 loft:the chapel loft: ruled out position(s) 3
15. [direct] from clue 4 plumage:mealy red: ruled out position(s) 4
16. [order] from clue 2 plumage:slate blue: ruled out position(s) 1,2
17. [order] from clue 5 bird:Pip: ruled out position(s) 4
18. [order] from clue 3 plumage:dun: ruled out position(s) 2
19. [order] from clue 3 bird:Cadwallader: ruled out position(s) 1,2
20. [order] from clue 6 bird:Dot: ruled out position(s) 4
21. [bijection] bird:Dot: ruled out position(s) 2
22. [bijection] bird:Alabaster: ruled out position(s) 2,4
23. [bijection] bird:Alabaster: ruled out position(s) 1
24. [bijection] loft:the canal loft: ruled out position(s) 1,3
25. [bijection] plumage:grizzle: ruled out position(s) 1,3,4

---

<sub>seed `2026172662545` &middot; score 4.93 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
