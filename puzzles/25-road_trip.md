# The Great American Road Trip

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `69664b3d88cb`

## Introduction

Everybody set out the same weekend, each for a different national park, each certain theirs is the better drive.
Five drivers are involved. Determine each driver's distance, park and snag.
- **Driver**: Gil Ostrander, Hector Salas, Wendell, Roy Tubbs and Marguerite.
- **Distance** (listed from shorter to longer): 200 miles, 300 miles, 400 miles, 500 miles and 600 miles.
- **Park**: Olympic, the Badlands, Yellowstone, Zion and the Great Smoky Mountains.
- **Snag**: a wrong turn in Nebraska, a dead phone battery, a closed pass, a flat tire and a thunderstorm.
Every driver has a different distance, park and snag, so within each category every item is used exactly once.

## Clues

1. The driver who heads for Olympic is exactly one hundred miles shorter than 400 miles, with no distance in between. The driver who is delayed by a closed pass covers 400 miles.
2. Roy Tubbs falls somewhere between 300 miles and the driver who is delayed by a dead phone battery in distance order.
3. The driver who heads for Zion and 500 miles are exactly one hundred miles apart in distance order, in one direction or the other.
4. Wendell is exactly one hundred miles shorter than 600 miles, with no distance in between.
5. The driver who is delayed by a wrong turn in Nebraska falls somewhere between the driver who heads for Yellowstone and the driver who heads for Zion in distance order.
6. The driver who heads for the Badlands and the driver who is delayed by a flat tire are exactly one hundred miles apart in distance order, in one direction or the other.
7. Gil Ostrander is exactly one hundred miles shorter than the driver who heads for the Great Smoky Mountains, with no distance in between.
8. The driver who is delayed by a thunderstorm is shorter than Hector Salas in distance order.

## Solving chart

*Distance vs Driver*

| | Gil Ostrander | Hector Salas | Wendell | Roy Tubbs | Marguerite |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Park*

| | Olympic | the Badlands | Yellowstone | Zion | the Great Smoky Mountains |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Distance vs Snag*

| | a wrong turn in Nebraska | a dead phone battery | a closed pass | a flat tire | a thunderstorm |
|---|---|---|---|---|---|
| **200 miles** | | | | | |
| **300 miles** | | | | | |
| **400 miles** | | | | | |
| **500 miles** | | | | | |
| **600 miles** | | | | | |

*Driver vs Park*

| | Olympic | the Badlands | Yellowstone | Zion | the Great Smoky Mountains |
|---|---|---|---|---|---|
| **Gil Ostrander** | | | | | |
| **Hector Salas** | | | | | |
| **Wendell** | | | | | |
| **Roy Tubbs** | | | | | |
| **Marguerite** | | | | | |

*Driver vs Snag*

| | a wrong turn in Nebraska | a dead phone battery | a closed pass | a flat tire | a thunderstorm |
|---|---|---|---|---|---|
| **Gil Ostrander** | | | | | |
| **Hector Salas** | | | | | |
| **Wendell** | | | | | |
| **Roy Tubbs** | | | | | |
| **Marguerite** | | | | | |

*Park vs Snag*

| | a wrong turn in Nebraska | a dead phone battery | a closed pass | a flat tire | a thunderstorm |
|---|---|---|---|---|---|
| **Olympic** | | | | | |
| **the Badlands** | | | | | |
| **Yellowstone** | | | | | |
| **Zion** | | | | | |
| **the Great Smoky Mountains** | | | | | |

## Solution

| Distance | Driver | Park | Snag |
|---|---|---|---|
| 200 miles | Marguerite | Yellowstone | a thunderstorm |
| 300 miles | Gil Ostrander | Olympic | a wrong turn in Nebraska |
| 400 miles | Roy Tubbs | the Great Smoky Mountains | a closed pass |
| 500 miles | Wendell | the Badlands | a dead phone battery |
| 600 miles | Hector Salas | Zion | a flat tire |

## How it falls out

1. [direct] from clue 3 snag:a closed pass: ruled out position(s) 1,2,4,5
2. [bijection] snag:a wrong turn in Nebraska: ruled out position(s) 3
3. [bijection] snag:a dead phone battery: ruled out position(s) 3
4. [bijection] snag:a flat tire: ruled out position(s) 3
5. [bijection] snag:a thunderstorm: ruled out position(s) 3
6. [order] from clue 9 driver:Wendell: ruled out position(s) 1,2,3,5
7. [order] from clue 8 park:Olympic: ruled out position(s) 1,3,4,5
8. [order] from clue 7 driver:Gil Ostrander: ruled out position(s) 5
9. [order] from clue 7 park:the Great Smoky Mountains: ruled out position(s) 1
10. [order] from clue 6 park:Zion: ruled out position(s) 1,2,4
11. [order] from clue 5 driver:Roy Tubbs: ruled out position(s) 1,2,5
12. [order] from clue 5 snag:a dead phone battery: ruled out position(s) 1,2
13. [order] from clue 4 snag:a thunderstorm: ruled out position(s) 5
14. [order] from clue 4 driver:Hector Salas: ruled out position(s) 1
15. [order] from clue 2 snag:a wrong turn in Nebraska: ruled out position(s) 1,5
16. [order] from clue 2 park:Yellowstone: ruled out position(s) 4
17. [bijection] driver:Gil Ostrander: ruled out position(s) 4
18. [bijection] driver:Hector Salas: ruled out position(s) 4
19. [bijection] driver:Roy Tubbs: ruled out position(s) 4
20. [bijection] driver:Marguerite: ruled out position(s) 4
21. [bijection] park:the Badlands: ruled out position(s) 2
22. [bijection] park:Yellowstone: ruled out position(s) 2
23. [bijection] park:the Great Smoky Mountains: ruled out position(s) 2
24. [order] from clue 1 snag:a flat tire: ruled out position(s) 1
25. [order] from clue 7 driver:Gil Ostrander: ruled out position(s) 1
26. [order] from clue 7 park:the Great Smoky Mountains: ruled out position(s) 5
27. [bijection] driver:Gil Ostrander: ruled out position(s) 3
28. [bijection] driver:Hector Salas: ruled out position(s) 3
29. [bijection] driver:Marguerite: ruled out position(s) 3
30. [bijection] driver:Marguerite: ruled out position(s) 2,5
31. [bijection] snag:a thunderstorm: ruled out position(s) 2,4
32. [order] from clue 7 park:the Great Smoky Mountains: ruled out position(s) 4
33. [bijection] driver:Hector Salas: ruled out position(s) 2
34. [bijection] park:the Badlands: ruled out position(s) 3
35. [bijection] park:Yellowstone: ruled out position(s) 3
36. [bijection] park:Zion: ruled out position(s) 3
37. [bijection] park:the Badlands: ruled out position(s) 1,5
38. [order] from clue 2 park:Yellowstone: ruled out position(s) 5
39. [order] from clue 1 snag:a flat tire: ruled out position(s) 2,4
40. [bijection] snag:a dead phone battery: ruled out position(s) 5
_... and 1 further steps._

---

<sub>seed `2026172973417` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
