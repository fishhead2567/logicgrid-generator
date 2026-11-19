# The Great American Road Trip

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `117e699ee6a0`

## Introduction

Everybody set out the same weekend, each for a different national park, each certain theirs is the better drive.
Five drivers are involved. Determine each driver's distance, park and ride.
- **Driver**: Anneke, Hector Salas, Roy Tubbs, Simone and Wendell.
- **Distance** (listed from shorter to longer): 200 miles, 300 miles, 400 miles, 500 miles and 600 miles.
- **Park**: Olympic, the Badlands, Yellowstone, Acadia and the Great Smoky Mountains.
- **Ride**: a minivan with a roof box, a hatchback packed to the roof, a station wagon, an old convertible and a rented camper.
Every driver has a different distance, park and ride, so within each category every item is used exactly once.

## Clues

1. The driver who heads for the Great Smoky Mountains covers 600 miles. Wendell is exactly one hundred miles shorter than 600 miles, with no distance in between.
2. Simone drives a hatchback packed to the roof.
3. The driver who drives a minivan with a roof box falls somewhere between 300 miles and 600 miles in distance order.
4. 400 miles falls somewhere between Anneke and Hector Salas in distance order. Hector Salas and 200 miles are exactly one hundred miles apart in distance order, in one direction or the other.
5. The driver who drives an old convertible is shorter than 400 miles in distance order.
6. 200 miles is exactly one hundred miles shorter than the driver who heads for Yellowstone, with no distance in between.
7. The driver who heads for Acadia is shorter than Hector Salas in distance order.
8. Roy Tubbs does not head for the Badlands.
9. The driver who drives a rented camper is exactly one hundred miles shorter than the driver who heads for the Great Smoky Mountains, with no distance in between.

## Solving chart

*Distance vs Driver*

| | Anneke | Hector Salas | Roy Tubbs | Simone | Wendell |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Park*

| | Olympic | the Badlands | Yellowstone | Acadia | the Great Smoky Mountains |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Ride*

| | a minivan with a roof box | a hatchback packed to the roof | a station wagon | an old convertible | a rented camper |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Driver vs Park*

| | Olympic | the Badlands | Yellowstone | Acadia | the Great Smoky Mountains |
|---|---|---|---|---|---|
| **Anneke** | | | | | |
| **Hector Salas** | | | | | |
| **Roy Tubbs** | | | | | |
| **Simone** | | | | | |
| **Wendell** | | | | | |

*Driver vs Ride*

| | a minivan with a roof box | a hatchback packed to the roof | a station wagon | an old convertible | a rented camper |
|---|---|---|---|---|---|
| **Anneke** | | | | | |
| **Hector Salas** | | | | | |
| **Roy Tubbs** | | | | | |
| **Simone** | | | | | |
| **Wendell** | | | | | |

*Park vs Ride*

| | a minivan with a roof box | a hatchback packed to the roof | a station wagon | an old convertible | a rented camper |
|---|---|---|---|---|---|
| **Olympic** | | | | | |
| **the Badlands** | | | | | |
| **Yellowstone** | | | | | |
| **Acadia** | | | | | |
| **the Great Smoky Mountains** | | | | | |

## Solution

| Distance | Driver | Park | Ride |
|---|---|---|---|
| 200 miles | Simone | Acadia | a hatchback packed to the roof |
| 300 miles | Hector Salas | Yellowstone | an old convertible |
| 400 miles | Roy Tubbs | Olympic | a minivan with a roof box |
| 500 miles | Wendell | the Badlands | a rented camper |
| 600 miles | Anneke | the Great Smoky Mountains | a station wagon |

## How it falls out

1. [direct] from clue 2 park:the Great Smoky Mountains: ruled out position(s) 1,2,3,4
2. [bijection] park:Olympic: ruled out position(s) 5
3. [bijection] park:the Badlands: ruled out position(s) 5
4. [bijection] park:Yellowstone: ruled out position(s) 5
5. [bijection] park:Acadia: ruled out position(s) 5
6. [order] from clue 11 park:Yellowstone: ruled out position(s) 1,3,4
7. [order] from clue 10 ride:a minivan with a roof box: ruled out position(s) 1,2,5
8. [order] from clue 7 driver:Anneke: ruled out position(s) 3
9. [order] from clue 7 driver:Hector Salas: ruled out position(s) 3
10. [order] from clue 6 driver:Wendell: ruled out position(s) 1,2,3,5
11. [order] from clue 5 ride:an old convertible: ruled out position(s) 3,4,5
12. [order] from clue 4 ride:a rented camper: ruled out position(s) 1,2,3,5
13. [order] from clue 3 driver:Hector Salas: ruled out position(s) 1
14. [order] from clue 1 driver:Hector Salas: ruled out position(s) 4,5
15. [order] from clue 7 driver:Anneke: ruled out position(s) 1,2
16. [order] from clue 3 park:Acadia: ruled out position(s) 2,3,4
17. [bijection] driver:Anneke: ruled out position(s) 4
18. [bijection] driver:Roy Tubbs: ruled out position(s) 2,4
19. [bijection] driver:Simone: ruled out position(s) 2,4
20. [bijection] park:Olympic: ruled out position(s) 1,2
21. [bijection] park:the Badlands: ruled out position(s) 1,2
22. [bijection] ride:a minivan with a roof box: ruled out position(s) 4
23. [bijection] ride:a hatchback packed to the roof: ruled out position(s) 4
24. [bijection] ride:a station wagon: ruled out position(s) 4
25. [direct] from clue 8 ride:a hatchback packed to the roof: ruled out position(s) 2
26. [bijection] driver:Roy Tubbs: ruled out position(s) 5
27. [bijection] driver:Simone: ruled out position(s) 5
28. [bijection] ride:a hatchback packed to the roof: ruled out position(s) 3
29. [bijection] ride:a station wagon: ruled out position(s) 3
30. [direct] from clue 8 driver:Simone: ruled out position(s) 3
31. [direct] from clue 8 ride:a hatchback packed to the roof: ruled out position(s) 5
32. [bijection] driver:Roy Tubbs: ruled out position(s) 1
33. [bijection] ride:a station wagon: ruled out position(s) 1
34. [bijection] ride:an old convertible: ruled out position(s) 1
35. [bijection] ride:a station wagon: ruled out position(s) 2
36. [direct] from clue 9 park:the Badlands: ruled out position(s) 3
37. [bijection] park:Olympic: ruled out position(s) 4

---

<sub>seed `2026172770467` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
