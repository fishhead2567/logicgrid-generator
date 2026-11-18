# The Grindle Bay Sandcastle Open

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `bc2b8118b14a`

## Introduction

The Grindle Bay Open is judged at four o'clock, whatever the tide is doing.
Five builders are involved. Determine each builder's placing and cause.
- **Builder**: Aleksy, Fenwick, Khalid, Juniper and Hartley.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Undone by**: a cricket ball, a sudden shower, the incoming tide, structural overreach and a loose dog.
Every builder has a different placing and cause, so within each category every item is used exactly once.

## Clues

1. Hartley places third.
2. The builder who is undone by a sudden shower places fourth.
3. Juniper falls somewhere between second and the builder who is undone by a loose dog in placing order.
4. Juniper and the builder who is undone by structural overreach are exactly one place apart in placing order, in one direction or the other.
5. The builder who is undone by a cricket ball is exactly one place better than Fenwick, with no placing in between.
6. Aleksy is better than the builder who is undone by a loose dog in placing order.

## Solving chart

*Placing vs Builder*

| | Aleksy | Fenwick | Khalid | Juniper | Hartley |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Undone by*

| | a cricket ball | a sudden shower | the incoming tide | structural overreach | a loose dog |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Builder vs Undone by*

| | a cricket ball | a sudden shower | the incoming tide | structural overreach | a loose dog |
|---|---|---|---|---|---|
| **Aleksy** | | | | | |
| **Fenwick** | | | | | |
| **Khalid** | | | | | |
| **Juniper** | | | | | |
| **Hartley** | | | | | |

## Solution

| Placing | Builder | Undone by |
|---|---|---|
| first | Aleksy | a cricket ball |
| second | Fenwick | the incoming tide |
| third | Hartley | structural overreach |
| fourth | Juniper | a sudden shower |
| fifth | Khalid | a loose dog |

## How it falls out

1. [direct] from clue 4 ruin:a sudden shower: ruled out position(s) 1,2,3,5
2. [direct] from clue 3 builder:Hartley: ruled out position(s) 1,2,4,5
3. [bijection] builder:Aleksy: ruled out position(s) 3
4. [bijection] builder:Fenwick: ruled out position(s) 3
5. [bijection] builder:Khalid: ruled out position(s) 3
6. [bijection] builder:Juniper: ruled out position(s) 3
7. [bijection] ruin:a cricket ball: ruled out position(s) 4
8. [bijection] ruin:the incoming tide: ruled out position(s) 4
9. [bijection] ruin:structural overreach: ruled out position(s) 4
10. [bijection] ruin:a loose dog: ruled out position(s) 4
11. [order] from clue 6 builder:Aleksy: ruled out position(s) 5
12. [order] from clue 6 ruin:a loose dog: ruled out position(s) 1
13. [order] from clue 5 builder:Juniper: ruled out position(s) 1,2,5
14. [order] from clue 5 ruin:a loose dog: ruled out position(s) 2,3
15. [order] from clue 2 ruin:structural overreach: ruled out position(s) 1,2
16. [order] from clue 1 ruin:a cricket ball: ruled out position(s) 2,5
17. [order] from clue 1 builder:Fenwick: ruled out position(s) 1,5
18. [bijection] builder:Aleksy: ruled out position(s) 4
19. [bijection] builder:Fenwick: ruled out position(s) 4
20. [bijection] builder:Khalid: ruled out position(s) 4
21. [bijection] builder:Khalid: ruled out position(s) 1,2
22. [bijection] ruin:the incoming tide: ruled out position(s) 5
23. [bijection] ruin:structural overreach: ruled out position(s) 5
24. [bijection] ruin:the incoming tide: ruled out position(s) 1,3
25. [order] from clue 1 ruin:a cricket ball: ruled out position(s) 3
26. [bijection] builder:Aleksy: ruled out position(s) 2

---

<sub>seed `2026172887841` &middot; score 4.62 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
