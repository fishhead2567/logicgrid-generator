# The Dream Garage

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `90aff8119e2d`

## Introduction

Kids turned loose at the auto show, each one certain they have found the only car worth owning.
Five kids are involved. Determine each kid's top speed and make.
- **Kid**: Imani, Benicio, Dov, Harriet and Cormac.
- **Top speed** (listed from slower to faster): 120 mph, 130 mph, 140 mph, 150 mph and 160 mph.
- **Make**: a Harrier Coupe, a Vulcan 500, a Trailhawk Pickup, a Comet GT and a Lark Hatchback.
Every kid has a different top speed and make, so within each category every item is used exactly once.

## Clues

1. 150 mph is exactly one speed step slower than the kid who is set on a Comet GT, with no top speed in between. Benicio does not want a car that does 150 mph.
2. The kid who is set on a Harrier Coupe does not want a car that does 120 mph.
3. Harriet is exactly one speed step slower than 140 mph, with no top speed in between. The kid who is set on a Lark Hatchback falls somewhere between Cormac and Harriet in top speed order.
4. The kid who is set on a Harrier Coupe and 130 mph are exactly one speed step apart in top speed order, in one direction or the other.
5. Benicio does not want a car that does 120 mph.
6. Imani and the kid who is set on a Vulcan 500 are exactly one speed step apart in top speed order, in one direction or the other.

## Solving chart

*Top speed vs Kid*

| | Imani | Benicio | Dov | Harriet | Cormac |
|---|---|---|---|---|---|
| **120 mph** | | | | | |
| **130 mph** | | | | | |
| **140 mph** | | | | | |
| **150 mph** | | | | | |
| **160 mph** | | | | | |

*Top speed vs Make*

| | a Harrier Coupe | a Vulcan 500 | a Trailhawk Pickup | a Comet GT | a Lark Hatchback |
|---|---|---|---|---|---|
| **120 mph** | | | | | |
| **130 mph** | | | | | |
| **140 mph** | | | | | |
| **150 mph** | | | | | |
| **160 mph** | | | | | |

*Kid vs Make*

| | a Harrier Coupe | a Vulcan 500 | a Trailhawk Pickup | a Comet GT | a Lark Hatchback |
|---|---|---|---|---|---|
| **Imani** | | | | | |
| **Benicio** | | | | | |
| **Dov** | | | | | |
| **Harriet** | | | | | |
| **Cormac** | | | | | |

## Solution

| Top speed | Kid | Make |
|---|---|---|
| 120 mph | Imani | a Trailhawk Pickup |
| 130 mph | Harriet | a Vulcan 500 |
| 140 mph | Benicio | a Harrier Coupe |
| 150 mph | Dov | a Lark Hatchback |
| 160 mph | Cormac | a Comet GT |

## How it falls out

1. [direct] from clue 5 kid:Benicio: ruled out position(s) 1
2. [direct] from clue 4 make:a Harrier Coupe: ruled out position(s) 1
3. [direct] from clue 3 kid:Benicio: ruled out position(s) 4
4. [order] from clue 8 make:a Harrier Coupe: ruled out position(s) 2,4,5
5. [order] from clue 7 kid:Harriet: ruled out position(s) 1,3,4,5
6. [order] from clue 6 make:a Lark Hatchback: ruled out position(s) 1,2,5
7. [order] from clue 6 kid:Cormac: ruled out position(s) 1,2,3
8. [order] from clue 2 make:a Comet GT: ruled out position(s) 1,2,3,4
9. [bijection] kid:Imani: ruled out position(s) 2
10. [bijection] kid:Benicio: ruled out position(s) 2
11. [bijection] kid:Dov: ruled out position(s) 2
12. [bijection] make:a Vulcan 500: ruled out position(s) 3,5
13. [bijection] make:a Trailhawk Pickup: ruled out position(s) 3,5
14. [bijection] make:a Lark Hatchback: ruled out position(s) 3
15. [order] from clue 6 kid:Cormac: ruled out position(s) 4
16. [order] from clue 1 kid:Imani: ruled out position(s) 4
17. [order] from clue 1 make:a Vulcan 500: ruled out position(s) 1
18. [bijection] kid:Imani: ruled out position(s) 5
19. [bijection] kid:Benicio: ruled out position(s) 5
20. [bijection] kid:Dov: ruled out position(s) 5
21. [bijection] kid:Dov: ruled out position(s) 1,3
22. [bijection] make:a Vulcan 500: ruled out position(s) 4
23. [bijection] make:a Trailhawk Pickup: ruled out position(s) 4
24. [bijection] make:a Trailhawk Pickup: ruled out position(s) 2
25. [bijection] kid:Imani: ruled out position(s) 3

---

<sub>seed `2026172870470` &middot; score 5.1 &middot; atoms 8 &middot; positives 0 &middot; solved by order</sub>
