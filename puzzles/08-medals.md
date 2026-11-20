# The Medals Got Mixed Up

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `89345a199be6`

## Introduction

A volunteer handed out the medal boxes in the wrong order, and the scoreboard went dark an hour ago.
Four athletes are involved. Determine each athlete's placing and jersey.
- **Athlete**: Wren Abernathy, Ingrid Solheim, Nadia Kell and Tobias Pike.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Jersey**: a teal jersey, a silver jersey, a navy jersey and a maroon jersey.
Every athlete has a different placing and jersey, so within each category every item is used exactly once.

## Clues

1. The athlete who wears a silver jersey finishes second.
2. Ingrid Solheim wears a silver jersey.
3. Wren Abernathy wears a navy jersey.
4. Nadia Kell and third are exactly one place apart in placing order, in one direction or the other.
5. The athlete who wears a teal jersey is exactly one place better than fourth, with no placing in between.

## Solving chart

*Placing vs Athlete*

| | Wren Abernathy | Ingrid Solheim | Nadia Kell | Tobias Pike |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Jersey*

| | a teal jersey | a silver jersey | a navy jersey | a maroon jersey |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Athlete vs Jersey*

| | a teal jersey | a silver jersey | a navy jersey | a maroon jersey |
|---|---|---|---|---|
| **Wren Abernathy** | | | | |
| **Ingrid Solheim** | | | | |
| **Nadia Kell** | | | | |
| **Tobias Pike** | | | | |

## Solution

| Placing | Athlete | Jersey |
|---|---|---|
| first | Wren Abernathy | a navy jersey |
| second | Ingrid Solheim | a silver jersey |
| third | Tobias Pike | a teal jersey |
| fourth | Nadia Kell | a maroon jersey |

## How it falls out

1. [direct] from clue 4 jersey:a silver jersey: ruled out position(s) 1,3,4
2. [direct] from clue 3 athlete:Ingrid Solheim: ruled out position(s) 1,3,4
3. [bijection] athlete:Wren Abernathy: ruled out position(s) 2
4. [bijection] athlete:Nadia Kell: ruled out position(s) 2
5. [bijection] athlete:Tobias Pike: ruled out position(s) 2
6. [bijection] jersey:a teal jersey: ruled out position(s) 2
7. [bijection] jersey:a navy jersey: ruled out position(s) 2
8. [bijection] jersey:a maroon jersey: ruled out position(s) 2
9. [order] from clue 2 athlete:Nadia Kell: ruled out position(s) 1,3
10. [order] from clue 1 jersey:a teal jersey: ruled out position(s) 1,4
11. [bijection] athlete:Wren Abernathy: ruled out position(s) 4
12. [bijection] athlete:Tobias Pike: ruled out position(s) 4
13. [bijection] jersey:a navy jersey: ruled out position(s) 3
14. [bijection] jersey:a maroon jersey: ruled out position(s) 3
15. [direct] from clue 5 athlete:Wren Abernathy: ruled out position(s) 3
16. [direct] from clue 5 jersey:a navy jersey: ruled out position(s) 4
17. [bijection] athlete:Tobias Pike: ruled out position(s) 1
18. [bijection] jersey:a maroon jersey: ruled out position(s) 1

---

<sub>seed `2026172838794` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
