# The Hollow Creek Pie Judging

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `65dfd2b93c53`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Four bakers are involved. Determine each baker's placing and crust.
- **Baker**: Bramwell, Odette, Caspian and Winnie.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Crust**: a cut-out star top, a crumb topping, a double crust and a lattice top.
Every baker has a different placing and crust, so within each category every item is used exactly once.

## Clues

1. Bramwell places first.
2. Odette places third.
3. Caspian uses a lattice top.
4. Bramwell uses a crumb topping.
5. The baker who uses a double crust is exactly one place better than Winnie, with no placing in between.

## Solving chart

*Placing vs Baker*

| | Bramwell | Odette | Caspian | Winnie |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Crust*

| | a cut-out star top | a crumb topping | a double crust | a lattice top |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Baker vs Crust*

| | a cut-out star top | a crumb topping | a double crust | a lattice top |
|---|---|---|---|---|
| **Bramwell** | | | | |
| **Odette** | | | | |
| **Caspian** | | | | |
| **Winnie** | | | | |

## Solution

| Placing | Baker | Crust |
|---|---|---|
| first | Bramwell | a crumb topping |
| second | Caspian | a lattice top |
| third | Odette | a double crust |
| fourth | Winnie | a cut-out star top |

## How it falls out

1. [direct] from clue 5 baker:Odette: ruled out position(s) 1,2,4
2. [direct] from clue 4 baker:Bramwell: ruled out position(s) 2,3,4
3. [direct] from clue 3 crust:a crumb topping: ruled out position(s) 2,3,4
4. [bijection] baker:Caspian: ruled out position(s) 1,3
5. [bijection] baker:Winnie: ruled out position(s) 1,3
6. [bijection] crust:a cut-out star top: ruled out position(s) 1
7. [bijection] crust:a double crust: ruled out position(s) 1
8. [bijection] crust:a lattice top: ruled out position(s) 1
9. [direct] from clue 1 crust:a lattice top: ruled out position(s) 3
10. [order] from clue 2 crust:a double crust: ruled out position(s) 2,4
11. [order] from clue 2 baker:Winnie: ruled out position(s) 2
12. [bijection] baker:Caspian: ruled out position(s) 4
13. [bijection] crust:a cut-out star top: ruled out position(s) 3
14. [direct] from clue 1 crust:a lattice top: ruled out position(s) 4
15. [bijection] crust:a cut-out star top: ruled out position(s) 2

---

<sub>seed `2026172808651` &middot; score 3.67 &middot; atoms 5 &middot; positives 4 &middot; solved by order</sub>
