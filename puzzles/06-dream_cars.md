# The Dream Garage

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `74c39b1cc634`

## Introduction

Kids turned loose at the auto show, each one certain they have found the only car worth owning.
Four kids are involved. Determine each kid's top speed and make.
- **Kid**: Imani, Svetlana, Jalen and Cormac.
- **Top speed** (listed from slower to faster): 120 mph, 130 mph, 140 mph and 150 mph.
- **Make**: a Comet GT, a Trailhawk Pickup, a Meridian Sedan and a Vulcan 500.
Every kid has a different top speed and make, so within each category every item is used exactly once.

## Clues

1. The kid who is set on a Vulcan 500 wants a car that does 120 mph.
2. Cormac is set on a Trailhawk Pickup.
3. Svetlana is slower than 130 mph in top speed order.
4. The kid who is set on a Trailhawk Pickup and 150 mph are exactly one speed step apart in top speed order, in one direction or the other.
5. The kid who is set on a Comet GT is slower than Imani in top speed order.

## Solving chart

*Top speed vs Kid*

| | Imani | Svetlana | Jalen | Cormac |
|---|---|---|---|---|
| **120 mph** | | | | |
| **130 mph** | | | | |
| **140 mph** | | | | |
| **150 mph** | | | | |

*Top speed vs Make*

| | a Comet GT | a Trailhawk Pickup | a Meridian Sedan | a Vulcan 500 |
|---|---|---|---|---|
| **120 mph** | | | | |
| **130 mph** | | | | |
| **140 mph** | | | | |
| **150 mph** | | | | |

*Kid vs Make*

| | a Comet GT | a Trailhawk Pickup | a Meridian Sedan | a Vulcan 500 |
|---|---|---|---|---|
| **Imani** | | | | |
| **Svetlana** | | | | |
| **Jalen** | | | | |
| **Cormac** | | | | |

## Solution

| Top speed | Kid | Make |
|---|---|---|
| 120 mph | Svetlana | a Vulcan 500 |
| 130 mph | Jalen | a Comet GT |
| 140 mph | Cormac | a Trailhawk Pickup |
| 150 mph | Imani | a Meridian Sedan |

## How it falls out

1. [direct] from clue 3 make:a Vulcan 500: ruled out position(s) 2,3,4
2. [bijection] make:a Comet GT: ruled out position(s) 1
3. [bijection] make:a Trailhawk Pickup: ruled out position(s) 1
4. [bijection] make:a Meridian Sedan: ruled out position(s) 1
5. [direct] from clue 2 kid:Cormac: ruled out position(s) 1
6. [order] from clue 5 make:a Comet GT: ruled out position(s) 4
7. [order] from clue 5 kid:Imani: ruled out position(s) 1,2
8. [order] from clue 4 kid:Svetlana: ruled out position(s) 2,3,4
9. [order] from clue 1 make:a Trailhawk Pickup: ruled out position(s) 2,4
10. [direct] from clue 2 kid:Cormac: ruled out position(s) 2,4
11. [bijection] kid:Imani: ruled out position(s) 3
12. [bijection] kid:Jalen: ruled out position(s) 1,3
13. [bijection] kid:Jalen: ruled out position(s) 4
14. [bijection] make:a Comet GT: ruled out position(s) 3
15. [bijection] make:a Meridian Sedan: ruled out position(s) 3
16. [bijection] make:a Meridian Sedan: ruled out position(s) 2

---

<sub>seed `2026172922959` &middot; score 4.27 &middot; atoms 5 &middot; positives 2 &middot; solved by order</sub>
