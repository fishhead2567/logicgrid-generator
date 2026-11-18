# A Bad Week at the Pinhole Observatory

*The Pinhole Amateur Astronomical Society has one good telescope and a great many strong opinions about who may point it where.*

**Difficulty** 2/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `9f6a7921bf75`

## Introduction

There are 5 sessions. Each has exactly one day and one item from every other category below, and within each category every item belongs to a different session.
- **Day** (listed in order): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Astronomer**: Niamh, Sunniva, Cornelius, Dmitri and Ingrid.
- **Mishap**: a dewed-up eyepiece, a neighbour's floodlight, a cracked filter, an unexpected cloud bank and a dropped lens cap.
The days above are listed in order, from Monday to Friday.

## Clues

1. Dmitri goes with Friday. Friday goes with an unexpected cloud bank.
2. Wednesday goes with a dropped lens cap.
3. Cornelius does not go with a cracked filter. Sunniva, Tuesday and a cracked filter are three different sessions.
4. Wednesday falls somewhere between Cornelius and Ingrid in day order.
5. Ingrid and a neighbour's floodlight are next to each other in day order, in one order or the other.

## Solving chart

*Day vs Astronomer*

| | Niamh | Sunniva | Cornelius | Dmitri | Ingrid |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Mishap*

| | a dewed-up eyepiece | a neighbour's floodlight | a cracked filter | an unexpected cloud bank | a dropped lens cap |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Astronomer vs Mishap*

| | a dewed-up eyepiece | a neighbour's floodlight | a cracked filter | an unexpected cloud bank | a dropped lens cap |
|---|---|---|---|---|---|
| **Niamh** | | | | | |
| **Sunniva** | | | | | |
| **Cornelius** | | | | | |
| **Dmitri** | | | | | |
| **Ingrid** | | | | | |

## Solution

| Day | Astronomer | Mishap |
|---|---|---|
| Monday | Ingrid | a cracked filter |
| Tuesday | Niamh | a neighbour's floodlight |
| Wednesday | Sunniva | a dropped lens cap |
| Thursday | Cornelius | a dewed-up eyepiece |
| Friday | Dmitri | an unexpected cloud bank |

## How it falls out

1. [direct] from clue 6 astronomer:Dmitri: ruled out position(s) 1,2,3,4
2. [direct] from clue 4 mishap:an unexpected cloud bank: ruled out position(s) 1,2,3,4
3. [direct] from clue 3 mishap:a dropped lens cap: ruled out position(s) 1,2,4,5
4. [bijection] from clue 2 astronomer:Sunniva: ruled out position(s) 2
5. [bijection] from clue 2 mishap:a cracked filter: ruled out position(s) 2
6. [bijection] astronomer:Niamh: ruled out position(s) 5
7. [bijection] astronomer:Sunniva: ruled out position(s) 5
8. [bijection] astronomer:Cornelius: ruled out position(s) 5
9. [bijection] astronomer:Ingrid: ruled out position(s) 5
10. [bijection] mishap:a dewed-up eyepiece: ruled out position(s) 3,5
11. [bijection] mishap:a neighbour's floodlight: ruled out position(s) 3,5
12. [bijection] mishap:a cracked filter: ruled out position(s) 3,5
13. [order] from clue 7 astronomer:Cornelius: ruled out position(s) 3
14. [order] from clue 7 astronomer:Ingrid: ruled out position(s) 3
15. [order] from clue 1 astronomer:Ingrid: ruled out position(s) 4
16. [order] from clue 1 mishap:a neighbour's floodlight: ruled out position(s) 4
17. [order] from clue 7 astronomer:Cornelius: ruled out position(s) 1,2
18. [direct] from clue 5 mishap:a cracked filter: ruled out position(s) 4
19. [bijection] from clue 2 astronomer:Sunniva: ruled out position(s) 1
20. [bijection] astronomer:Niamh: ruled out position(s) 4
21. [bijection] astronomer:Sunniva: ruled out position(s) 4
22. [bijection] mishap:a dewed-up eyepiece: ruled out position(s) 1
23. [bijection] mishap:a neighbour's floodlight: ruled out position(s) 1
24. [bijection] mishap:a dewed-up eyepiece: ruled out position(s) 2
25. [order] from clue 1 astronomer:Ingrid: ruled out position(s) 2
26. [bijection] astronomer:Niamh: ruled out position(s) 1,3

---

<sub>seed `2026172717978` &middot; score 4.38 &middot; atoms 7 &middot; positives 3 &middot; solved by order</sub>
