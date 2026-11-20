# The Cannon Beach Sandcastle Open

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `8566d97f1849`

## Introduction

The Cannon Beach Open is judged at four o'clock, whatever the tide is doing.
Five builders are involved. Determine each builder's placing and tool.
- **Builder**: Hartley, Harper, Bridget, Khalid and Wes.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Chief tool**: a bucket with no handle, a paint scraper, a pastry brush, a soup spoon and a cake server.
Every builder has a different placing and tool, so within each category every item is used exactly once.

## Clues

1. Harper places fifth. The builder who works with a soup spoon places fifth.
2. Hartley falls somewhere between first and fourth in placing order.
3. The builder who works with a paint scraper is exactly one place better than second, with no placing in between.
4. Khalid falls somewhere between the builder who works with a cake server and the builder who works with a paint scraper in placing order.
5. The builder who works with a bucket with no handle is exactly one place better than Wes, with no placing in between.
6. Khalid is better than the builder who works with a bucket with no handle in placing order.

## Solving chart

*Placing vs Builder*

| | Hartley | Harper | Bridget | Khalid | Wes |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Chief tool*

| | a bucket with no handle | a paint scraper | a pastry brush | a soup spoon | a cake server |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Builder vs Chief tool*

| | a bucket with no handle | a paint scraper | a pastry brush | a soup spoon | a cake server |
|---|---|---|---|---|---|
| **Hartley** | | | | | |
| **Harper** | | | | | |
| **Bridget** | | | | | |
| **Khalid** | | | | | |
| **Wes** | | | | | |

## Solution

| Placing | Builder | Chief tool |
|---|---|---|
| first | Bridget | a paint scraper |
| second | Khalid | a pastry brush |
| third | Hartley | a bucket with no handle |
| fourth | Wes | a cake server |
| fifth | Harper | a soup spoon |

## How it falls out

1. [direct] from clue 4 builder:Harper: ruled out position(s) 1,2,3,4
2. [direct] from clue 3 tool:a soup spoon: ruled out position(s) 1,2,3,4
3. [bijection] builder:Hartley: ruled out position(s) 5
4. [bijection] builder:Bridget: ruled out position(s) 5
5. [bijection] builder:Khalid: ruled out position(s) 5
6. [bijection] builder:Wes: ruled out position(s) 5
7. [bijection] tool:a bucket with no handle: ruled out position(s) 5
8. [bijection] tool:a paint scraper: ruled out position(s) 5
9. [bijection] tool:a pastry brush: ruled out position(s) 5
10. [bijection] tool:a cake server: ruled out position(s) 5
11. [order] from clue 7 builder:Hartley: ruled out position(s) 1,4
12. [order] from clue 6 builder:Khalid: ruled out position(s) 1,4
13. [order] from clue 5 tool:a bucket with no handle: ruled out position(s) 4
14. [order] from clue 5 builder:Wes: ruled out position(s) 1
15. [order] from clue 2 builder:Khalid: ruled out position(s) 3
16. [order] from clue 2 tool:a bucket with no handle: ruled out position(s) 1,2
17. [order] from clue 5 builder:Wes: ruled out position(s) 2,3
18. [order] from clue 6 tool:a cake server: ruled out position(s) 2
19. [order] from clue 6 tool:a paint scraper: ruled out position(s) 2
20. [order] from clue 1 tool:a paint scraper: ruled out position(s) 3,4
21. [order] from clue 6 tool:a cake server: ruled out position(s) 1
22. [bijection] builder:Hartley: ruled out position(s) 2
23. [bijection] builder:Bridget: ruled out position(s) 2,4
24. [bijection] builder:Bridget: ruled out position(s) 3
25. [bijection] tool:a pastry brush: ruled out position(s) 1,3
26. [bijection] tool:a cake server: ruled out position(s) 3
27. [bijection] tool:a pastry brush: ruled out position(s) 4

---

<sub>seed `2026173002149` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
