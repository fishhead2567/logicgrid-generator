# The Medals Got Mixed Up

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `c5aa264afab3`

## Introduction

A volunteer handed out the medal boxes in the wrong order, and the scoreboard went dark an hour ago.
Five athletes are involved. Determine each athlete's placing and event.
- **Athlete**: Tobias Pike, Diego Vasquez, Camille Boyd, Ingrid Solheim and Rashad Ellery.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Event**: the long jump, the pole vault, the triple jump, the shot put and the 100 meter dash.
Every athlete has a different placing and event, so within each category every item is used exactly once.

## Clues

1. Ingrid Solheim finishes first. The athlete who competes in the pole vault finishes first.
2. The athlete who competes in the long jump does not finish fifth.
3. The athlete who competes in the triple jump is better than fourth in placing order.
4. Camille Boyd is worse than fourth in placing order.
5. The athlete who competes in the 100 meter dash is exactly one place better than Rashad Ellery, with no placing in between.
6. Tobias Pike is exactly one place better than the athlete who competes in the triple jump, with no placing in between.

## Solving chart

*Placing vs Athlete*

| | Tobias Pike | Diego Vasquez | Camille Boyd | Ingrid Solheim | Rashad Ellery |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Event*

| | the long jump | the pole vault | the triple jump | the shot put | the 100 meter dash |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Athlete vs Event*

| | the long jump | the pole vault | the triple jump | the shot put | the 100 meter dash |
|---|---|---|---|---|---|
| **Tobias Pike** | | | | | |
| **Diego Vasquez** | | | | | |
| **Camille Boyd** | | | | | |
| **Ingrid Solheim** | | | | | |
| **Rashad Ellery** | | | | | |

## Solution

| Placing | Athlete | Event |
|---|---|---|
| first | Ingrid Solheim | the pole vault |
| second | Tobias Pike | the 100 meter dash |
| third | Rashad Ellery | the triple jump |
| fourth | Diego Vasquez | the long jump |
| fifth | Camille Boyd | the shot put |

## How it falls out

1. [direct] from clue 7 event:the pole vault: ruled out position(s) 2,3,4,5
2. [direct] from clue 5 athlete:Ingrid Solheim: ruled out position(s) 2,3,4,5
3. [direct] from clue 3 event:the long jump: ruled out position(s) 5
4. [bijection] athlete:Tobias Pike: ruled out position(s) 1
5. [bijection] athlete:Diego Vasquez: ruled out position(s) 1
6. [bijection] athlete:Camille Boyd: ruled out position(s) 1
7. [bijection] athlete:Rashad Ellery: ruled out position(s) 1
8. [bijection] event:the long jump: ruled out position(s) 1
9. [bijection] event:the triple jump: ruled out position(s) 1
10. [bijection] event:the shot put: ruled out position(s) 1
11. [bijection] event:the 100 meter dash: ruled out position(s) 1
12. [order] from clue 6 event:the triple jump: ruled out position(s) 4,5
13. [order] from clue 4 event:the 100 meter dash: ruled out position(s) 5
14. [order] from clue 4 athlete:Rashad Ellery: ruled out position(s) 2
15. [order] from clue 2 athlete:Camille Boyd: ruled out position(s) 2,3,4
16. [order] from clue 1 athlete:Tobias Pike: ruled out position(s) 3,4,5
17. [order] from clue 1 event:the triple jump: ruled out position(s) 2
18. [bijection] athlete:Diego Vasquez: ruled out position(s) 2,5
19. [bijection] athlete:Rashad Ellery: ruled out position(s) 5
20. [bijection] event:the long jump: ruled out position(s) 3
21. [bijection] event:the shot put: ruled out position(s) 3
22. [bijection] event:the 100 meter dash: ruled out position(s) 3
23. [bijection] event:the shot put: ruled out position(s) 2,4
24. [order] from clue 4 event:the 100 meter dash: ruled out position(s) 4
25. [order] from clue 4 athlete:Rashad Ellery: ruled out position(s) 4
26. [bijection] athlete:Diego Vasquez: ruled out position(s) 3
27. [bijection] event:the long jump: ruled out position(s) 2

---

<sub>seed `2026172817981` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
