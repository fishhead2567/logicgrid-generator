# The Great American Road Trip

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `b560796acebb`

## Introduction

Everybody set out the same weekend, each for a different national park, each certain theirs is the better drive.
Four drivers are involved. Determine each driver's distance, ride and snag.
- **Driver**: Gil Ostrander, Hector Salas, Simone and Wendell.
- **Distance** (listed from shorter to longer): 200 miles, 300 miles, 400 miles and 500 miles.
- **Ride**: a hybrid sedan, an old convertible, a rented camper and a minivan with a roof box.
- **Snag**: nothing at all, a thunderstorm, a long line at the gate and a closed pass.
Every driver has a different distance, ride and snag, so within each category every item is used exactly once.

## Clues

1. The driver who drives a hybrid sedan covers 400 miles.
2. The driver who is delayed by a long line at the gate covers 300 miles.
3. Gil Ostrander and 500 miles are exactly one hundred miles apart in distance order, in one direction or the other.
4. The driver who is delayed by a thunderstorm falls somewhere between the driver who drives a minivan with a roof box and the driver who drives an old convertible in distance order.
5. Hector Salas does not drive a minivan with a roof box. Hector Salas is not delayed by nothing at all.
6. Wendell is not delayed by a closed pass.
7. Wendell is shorter than the driver who is delayed by nothing at all in distance order.
8. The driver who drives a rented camper is not delayed by a closed pass.

## Solving chart

*Distance vs Driver*

| | Gil Ostrander | Hector Salas | Simone | Wendell |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Ride*

| | a hybrid sedan | an old convertible | a rented camper | a minivan with a roof box |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Snag*

| | nothing at all | a thunderstorm | a long line at the gate | a closed pass |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Driver vs Ride*

| | a hybrid sedan | an old convertible | a rented camper | a minivan with a roof box |
|---|---|---|---|---|
| **Gil Ostrander** | | | | |
| **Hector Salas** | | | | |
| **Simone** | | | | |
| **Wendell** | | | | |

*Driver vs Snag*

| | nothing at all | a thunderstorm | a long line at the gate | a closed pass |
|---|---|---|---|---|
| **Gil Ostrander** | | | | |
| **Hector Salas** | | | | |
| **Simone** | | | | |
| **Wendell** | | | | |

*Ride vs Snag*

| | nothing at all | a thunderstorm | a long line at the gate | a closed pass |
|---|---|---|---|---|
| **a hybrid sedan** | | | | |
| **an old convertible** | | | | |
| **a rented camper** | | | | |
| **a minivan with a roof box** | | | | |

## Solution

| Distance | Driver | Ride | Snag |
|---|---|---|---|
| 200 miles | Hector Salas | an old convertible | a closed pass |
| 300 miles | Wendell | a rented camper | a long line at the gate |
| 400 miles | Gil Ostrander | a hybrid sedan | a thunderstorm |
| 500 miles | Simone | a minivan with a roof box | nothing at all |

## How it falls out

1. [direct] from clue 9 snag:a long line at the gate: ruled out position(s) 1,3,4
2. [direct] from clue 2 ride:a hybrid sedan: ruled out position(s) 1,2,4
3. [bijection] ride:an old convertible: ruled out position(s) 3
4. [bijection] ride:a rented camper: ruled out position(s) 3
5. [bijection] ride:a minivan with a roof box: ruled out position(s) 3
6. [bijection] snag:nothing at all: ruled out position(s) 2
7. [bijection] snag:a thunderstorm: ruled out position(s) 2
8. [bijection] snag:a closed pass: ruled out position(s) 2
9. [order] from clue 8 driver:Wendell: ruled out position(s) 4
10. [order] from clue 8 snag:nothing at all: ruled out position(s) 1
11. [order] from clue 7 snag:a thunderstorm: ruled out position(s) 1,4
12. [order] from clue 4 driver:Gil Ostrander: ruled out position(s) 1,2,4
13. [bijection] driver:Hector Salas: ruled out position(s) 3
14. [bijection] driver:Simone: ruled out position(s) 3
15. [bijection] driver:Wendell: ruled out position(s) 3
16. [bijection] snag:nothing at all: ruled out position(s) 3
17. [bijection] snag:a closed pass: ruled out position(s) 3
18. [bijection] snag:a closed pass: ruled out position(s) 4
19. [direct] from clue 1 ride:a rented camper: ruled out position(s) 1
20. [direct] from clue 3 driver:Wendell: ruled out position(s) 1
21. [direct] from clue 6 driver:Hector Salas: ruled out position(s) 4
22. [bijection] driver:Hector Salas: ruled out position(s) 2
23. [bijection] driver:Simone: ruled out position(s) 2
24. [bijection] driver:Simone: ruled out position(s) 1
25. [direct] from clue 5 ride:a minivan with a roof box: ruled out position(s) 1
26. [bijection] ride:an old convertible: ruled out position(s) 2,4
27. [order] from clue 7 ride:a minivan with a roof box: ruled out position(s) 2
28. [bijection] ride:a rented camper: ruled out position(s) 4

---

<sub>seed `2026172970473` &middot; score 4.93 &middot; atoms 9 &middot; positives 2 &middot; solved by order</sub>
