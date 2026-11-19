# The Grindle Bay Sandcastle Open

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `9c31bad60a31`

## Introduction

The Grindle Bay Open is judged at four o'clock, whatever the tide is doing.
Four builders are involved. Determine each builder's placing and tool.
- **Builder**: Juniper, Aleksy, Hartley and Bronagh.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Chief tool**: a soup spoon, bare hands, a bucket with no handle and a cake slice.
Every builder has a different placing and tool, so within each category every item is used exactly once.

## Clues

1. Hartley places third.
2. Aleksy works with a cake slice.
3. Bronagh works with a bucket with no handle.
4. The builder who works with bare hands is better than third in placing order.
5. Aleksy is exactly one place better than second, with no placing in between.

## Solving chart

*Placing vs Builder*

| | Juniper | Aleksy | Hartley | Bronagh |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Chief tool*

| | a soup spoon | bare hands | a bucket with no handle | a cake slice |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Builder vs Chief tool*

| | a soup spoon | bare hands | a bucket with no handle | a cake slice |
|---|---|---|---|---|
| **Juniper** | | | | |
| **Aleksy** | | | | |
| **Hartley** | | | | |
| **Bronagh** | | | | |

## Solution

| Placing | Builder | Chief tool |
|---|---|---|
| first | Aleksy | a cake slice |
| second | Juniper | bare hands |
| third | Hartley | a soup spoon |
| fourth | Bronagh | a bucket with no handle |

## How it falls out

1. [direct] from clue 1 builder:Hartley: ruled out position(s) 1,2,4
2. [bijection] builder:Juniper: ruled out position(s) 3
3. [bijection] builder:Aleksy: ruled out position(s) 3
4. [bijection] builder:Bronagh: ruled out position(s) 3
5. [direct] from clue 2 tool:a bucket with no handle: ruled out position(s) 3
6. [direct] from clue 4 tool:a cake slice: ruled out position(s) 3
7. [order] from clue 5 builder:Aleksy: ruled out position(s) 2,4
8. [order] from clue 3 tool:bare hands: ruled out position(s) 3,4
9. [direct] from clue 4 tool:a cake slice: ruled out position(s) 2,4
10. [bijection] builder:Juniper: ruled out position(s) 1
11. [bijection] builder:Bronagh: ruled out position(s) 1
12. [bijection] tool:a soup spoon: ruled out position(s) 1
13. [bijection] tool:bare hands: ruled out position(s) 1
14. [bijection] tool:a bucket with no handle: ruled out position(s) 1
15. [bijection] tool:a soup spoon: ruled out position(s) 2,4
16. [bijection] tool:a bucket with no handle: ruled out position(s) 2
17. [direct] from clue 2 builder:Bronagh: ruled out position(s) 2
18. [bijection] builder:Juniper: ruled out position(s) 4

---

<sub>seed `2026172738791` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
