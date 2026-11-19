# The Dream Garage

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `f5db7c635d5e`

## Introduction

Kids turned loose at the auto show, each one certain they have found the only car worth owning.
Five kids are involved. Determine each kid's top speed and paint.
- **Kid**: Harriet, Imani, Svetlana, Cormac and Jalen.
- **Top speed** (listed from slower to faster): 120 mph, 130 mph, 140 mph, 150 mph and 160 mph.
- **Paint**: candy-apple red, sea-foam green, burnt orange, matte black and deep purple.
Every kid has a different top speed and paint, so within each category every item is used exactly once.

## Clues

1. The kid who picks candy-apple red wants a car that does 160 mph.
2. Jalen wants a car that does 130 mph.
3. Jalen picks sea-foam green.
4. Svetlana picks matte black.
5. Imani does not pick deep purple. Imani is slower than 130 mph in top speed order.
6. Cormac and 130 mph are exactly one speed step apart in top speed order, in one direction or the other.

## Solving chart

*Top speed vs Kid*

| | Harriet | Imani | Svetlana | Cormac | Jalen |
|---|---|---|---|---|---|
| **120 mph** | | | | | |
| **130 mph** | | | | | |
| **140 mph** | | | | | |
| **150 mph** | | | | | |
| **160 mph** | | | | | |

*Top speed vs Paint*

| | candy-apple red | sea-foam green | burnt orange | matte black | deep purple |
|---|---|---|---|---|---|
| **120 mph** | | | | | |
| **130 mph** | | | | | |
| **140 mph** | | | | | |
| **150 mph** | | | | | |
| **160 mph** | | | | | |

*Kid vs Paint*

| | candy-apple red | sea-foam green | burnt orange | matte black | deep purple |
|---|---|---|---|---|---|
| **Harriet** | | | | | |
| **Imani** | | | | | |
| **Svetlana** | | | | | |
| **Cormac** | | | | | |
| **Jalen** | | | | | |

## Solution

| Top speed | Kid | Paint |
|---|---|---|
| 120 mph | Imani | burnt orange |
| 130 mph | Jalen | sea-foam green |
| 140 mph | Cormac | deep purple |
| 150 mph | Svetlana | matte black |
| 160 mph | Harriet | candy-apple red |

## How it falls out

1. [direct] from clue 5 paint:candy-apple red: ruled out position(s) 1,2,3,4
2. [direct] from clue 3 kid:Jalen: ruled out position(s) 1,3,4,5
3. [direct] from clue 6 paint:sea-foam green: ruled out position(s) 1,3,4,5
4. [bijection] kid:Harriet: ruled out position(s) 2
5. [bijection] kid:Imani: ruled out position(s) 2
6. [bijection] kid:Svetlana: ruled out position(s) 2
7. [bijection] kid:Cormac: ruled out position(s) 2
8. [bijection] paint:burnt orange: ruled out position(s) 2,5
9. [bijection] paint:matte black: ruled out position(s) 2,5
10. [bijection] paint:deep purple: ruled out position(s) 2,5
11. [direct] from clue 2 kid:Svetlana: ruled out position(s) 5
12. [order] from clue 4 kid:Cormac: ruled out position(s) 4,5
13. [order] from clue 1 kid:Imani: ruled out position(s) 3,4,5
14. [direct] from clue 7 paint:deep purple: ruled out position(s) 1
15. [bijection] kid:Harriet: ruled out position(s) 1
16. [bijection] kid:Svetlana: ruled out position(s) 1
17. [bijection] kid:Cormac: ruled out position(s) 1
18. [bijection] kid:Harriet: ruled out position(s) 3,4
19. [direct] from clue 2 paint:matte black: ruled out position(s) 1
20. [bijection] kid:Svetlana: ruled out position(s) 3
21. [bijection] paint:burnt orange: ruled out position(s) 3,4
22. [direct] from clue 2 paint:matte black: ruled out position(s) 3
23. [bijection] paint:deep purple: ruled out position(s) 4

---

<sub>seed `2026172707115` &middot; score 4.14 &middot; atoms 7 &middot; positives 4 &middot; solved by order</sub>
