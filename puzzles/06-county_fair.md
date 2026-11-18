# The Hollow Creek Pie Judging

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `7aaf4179e86b`

## Introduction

The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.
Four bakers are involved. Determine each baker's placing and filling.
- **Baker**: Thaddeus, Bramwell, Caspian and Marigold.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Filling**: rhubarb, green tomato, sour cherry and blackberry.
Every baker has a different placing and filling, so within each category every item is used exactly once.

## Clues

1. The baker who bakes sour cherry places second. Second is exactly one place better than the baker who bakes blackberry, with no placing in between.
2. Thaddeus places second.
3. Caspian places third.
4. Bramwell bakes rhubarb.
5. Marigold does not place first.

## Solving chart

*Placing vs Baker*

| | Thaddeus | Bramwell | Caspian | Marigold |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Filling*

| | rhubarb | green tomato | sour cherry | blackberry |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Baker vs Filling*

| | rhubarb | green tomato | sour cherry | blackberry |
|---|---|---|---|---|
| **Thaddeus** | | | | |
| **Bramwell** | | | | |
| **Caspian** | | | | |
| **Marigold** | | | | |

## Solution

| Placing | Baker | Filling |
|---|---|---|
| first | Bramwell | rhubarb |
| second | Thaddeus | sour cherry |
| third | Caspian | blackberry |
| fourth | Marigold | green tomato |

## How it falls out

1. [direct] from clue 4 baker:Thaddeus: ruled out position(s) 1,3,4
2. [direct] from clue 3 baker:Marigold: ruled out position(s) 1
3. [direct] from clue 2 filling:sour cherry: ruled out position(s) 1,3,4
4. [direct] from clue 1 baker:Caspian: ruled out position(s) 1,2,4
5. [bijection] baker:Bramwell: ruled out position(s) 2,3
6. [bijection] baker:Marigold: ruled out position(s) 2,3
7. [bijection] baker:Bramwell: ruled out position(s) 4
8. [bijection] filling:rhubarb: ruled out position(s) 2
9. [bijection] filling:green tomato: ruled out position(s) 2
10. [bijection] filling:blackberry: ruled out position(s) 2
11. [direct] from clue 5 filling:rhubarb: ruled out position(s) 3,4
12. [bijection] filling:green tomato: ruled out position(s) 1
13. [bijection] filling:blackberry: ruled out position(s) 1
14. [order] from clue 6 filling:blackberry: ruled out position(s) 4
15. [bijection] filling:green tomato: ruled out position(s) 3

---

<sub>seed `2026172622950` &middot; score 3.67 &middot; atoms 6 &middot; positives 4 &middot; solved by order</sub>
