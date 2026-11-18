# Andy's Swiftest Birds

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `0b2dbd7e7112`

## Introduction

Andy races pigeons, and each bird is bred for a different combination of stubbornness and speed.
Four pigeons are involved. Determine each pigeon's distance, plumage and breed.
- **Pigeon**: Grimsby, Cadwallader, Nutmeg and Dot.
- **Distance** (listed from shorter to longer): 200 miles, 300 miles, 400 miles and 500 miles.
- **Plumage**: chequered black, bronze, slate blue and mealy red.
- **Breed**: a Delbar, a Van Loon, a Sion and a Janssen.
Every pigeon has a different distance, plumage and breed, so within each category every item is used exactly once.

## Clues

1. Grimsby is chequered black.
2. Dot does not fly 300 miles. The pigeon that descends from a Janssen is longer than 300 miles in distance order.
3. The pigeon that descends from a Sion falls somewhere between 500 miles and the pigeon that is mealy red in distance order.
4. The pigeon that descends from a Janssen and the pigeon that is slate blue are exactly one hundred miles apart in distance order, in one direction or the other.
5. The pigeon that descends from a Janssen falls somewhere between the pigeon that is bronze and the pigeon that is mealy red in distance order.
6. The pigeon that descends from a Delbar is shorter than Dot in distance order. Nutmeg does not descend from a Delbar.

## Solving chart

*Distance vs Pigeon*

| | Grimsby | Cadwallader | Nutmeg | Dot |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Plumage*

| | chequered black | bronze | slate blue | mealy red |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Breed*

| | a Delbar | a Van Loon | a Sion | a Janssen |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Pigeon vs Plumage*

| | chequered black | bronze | slate blue | mealy red |
|---|---|---|---|---|
| **Grimsby** | | | | |
| **Cadwallader** | | | | |
| **Nutmeg** | | | | |
| **Dot** | | | | |

*Pigeon vs Breed*

| | a Delbar | a Van Loon | a Sion | a Janssen |
|---|---|---|---|---|
| **Grimsby** | | | | |
| **Cadwallader** | | | | |
| **Nutmeg** | | | | |
| **Dot** | | | | |

*Plumage vs Breed*

| | a Delbar | a Van Loon | a Sion | a Janssen |
|---|---|---|---|---|
| **chequered black** | | | | |
| **bronze** | | | | |
| **slate blue** | | | | |
| **mealy red** | | | | |

## Solution

| Distance | Pigeon | Plumage | Breed |
|---|---|---|---|
| 200 miles | Cadwallader | mealy red | a Delbar |
| 300 miles | Nutmeg | slate blue | a Sion |
| 400 miles | Grimsby | chequered black | a Janssen |
| 500 miles | Dot | bronze | a Van Loon |

## How it falls out

1. [direct] from clue 5 bird:Dot: ruled out position(s) 2
2. [order] from clue 8 breed:a Janssen: ruled out position(s) 1,4
3. [order] from clue 4 breed:a Delbar: ruled out position(s) 4
4. [order] from clue 4 bird:Dot: ruled out position(s) 1
5. [order] from clue 3 breed:a Janssen: ruled out position(s) 2
6. [order] from clue 8 plumage:bronze: ruled out position(s) 3
7. [order] from clue 8 plumage:mealy red: ruled out position(s) 3
8. [order] from clue 7 plumage:slate blue: ruled out position(s) 1,3
9. [order] from clue 1 breed:a Sion: ruled out position(s) 1,4
10. [order] from clue 1 plumage:mealy red: ruled out position(s) 4
11. [order] from clue 8 plumage:bronze: ruled out position(s) 1,2
12. [bijection] breed:a Delbar: ruled out position(s) 3
13. [bijection] breed:a Van Loon: ruled out position(s) 3
14. [bijection] breed:a Sion: ruled out position(s) 3
15. [bijection] breed:a Van Loon: ruled out position(s) 1,2
16. [bijection] plumage:chequered black: ruled out position(s) 4
17. [bijection] plumage:slate blue: ruled out position(s) 4
18. [bijection] plumage:chequered black: ruled out position(s) 1,2
19. [direct] from clue 6 bird:Grimsby: ruled out position(s) 1,2,4
20. [order] from clue 1 plumage:mealy red: ruled out position(s) 2
21. [bijection] bird:Cadwallader: ruled out position(s) 3
22. [bijection] bird:Nutmeg: ruled out position(s) 3
23. [bijection] bird:Dot: ruled out position(s) 3
24. [bijection] breed:a Delbar: ruled out position(s) 2
25. [direct] from clue 2 bird:Nutmeg: ruled out position(s) 1
26. [bijection] bird:Cadwallader: ruled out position(s) 4
27. [bijection] bird:Nutmeg: ruled out position(s) 4
28. [bijection] bird:Cadwallader: ruled out position(s) 2

---

<sub>seed `2026172662545` &middot; score 5.13 &middot; atoms 8 &middot; positives 1 &middot; solved by order</sub>
