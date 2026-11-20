# The Autumn Show at Kiyosumi

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `06058ad8d8c5`

## Introduction

Trees on stands, judged on a hundred-point sheet, and the wiring marks are what everybody is looking for.
Five exhibitors are involved. Determine each exhibitor's judged score and species.
- **Exhibitor**: Noriko Hase, Keiko Tanabe, Hiroshi Mita, Emi Tsuchida and Jun Kawabe.
- **Judged score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Species**: a hinoki cypress, a zelkova, a satsuki azalea, a Chinese quince and a trident maple.
Every exhibitor has a different judged score and species, so within each category every item is used exactly once.

## Clues

1. The exhibitor who has grown a Chinese quince is lower than 64 points in judged score order.
2. The exhibitor who has grown a satsuki azalea and 70 points are exactly one score step apart in judged score order, in one direction or the other.
3. Hiroshi Mita is lower than 67 points in judged score order.
4. Emi Tsuchida and 73 points are exactly one score step apart in judged score order, in one direction or the other.
5. Jun Kawabe and the exhibitor who has grown a hinoki cypress are exactly one score step apart in judged score order, in one direction or the other.
6. Keiko Tanabe and the exhibitor who has grown a Chinese quince are exactly one score step apart in judged score order, in one direction or the other.
7. Emi Tsuchida falls somewhere between the exhibitor who has grown a hinoki cypress and the exhibitor who has grown a zelkova in judged score order.

## Solving chart

*Judged score vs Exhibitor*

| | Noriko Hase | Keiko Tanabe | Hiroshi Mita | Emi Tsuchida | Jun Kawabe |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Judged score vs Species*

| | a hinoki cypress | a zelkova | a satsuki azalea | a Chinese quince | a trident maple |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Exhibitor vs Species*

| | a hinoki cypress | a zelkova | a satsuki azalea | a Chinese quince | a trident maple |
|---|---|---|---|---|---|
| **Noriko Hase** | | | | | |
| **Keiko Tanabe** | | | | | |
| **Hiroshi Mita** | | | | | |
| **Emi Tsuchida** | | | | | |
| **Jun Kawabe** | | | | | |

## Solution

| Judged score | Exhibitor | Species |
|---|---|---|
| 61 points | Hiroshi Mita | a Chinese quince |
| 64 points | Keiko Tanabe | a hinoki cypress |
| 67 points | Jun Kawabe | a satsuki azalea |
| 70 points | Emi Tsuchida | a trident maple |
| 73 points | Noriko Hase | a zelkova |

## How it falls out

1. [order] from clue 7 species:a satsuki azalea: ruled out position(s) 1,2,4
2. [order] from clue 5 exhibitor:Emi Tsuchida: ruled out position(s) 1,5
3. [order] from clue 4 exhibitor:Emi Tsuchida: ruled out position(s) 2,3
4. [order] from clue 5 species:a hinoki cypress: ruled out position(s) 4
5. [order] from clue 5 species:a zelkova: ruled out position(s) 4
6. [order] from clue 3 exhibitor:Jun Kawabe: ruled out position(s) 5
7. [order] from clue 2 exhibitor:Hiroshi Mita: ruled out position(s) 3,4,5
8. [order] from clue 1 species:a Chinese quince: ruled out position(s) 2,3,4,5
9. [order] from clue 6 exhibitor:Keiko Tanabe: ruled out position(s) 1,3,4,5
10. [bijection] exhibitor:Noriko Hase: ruled out position(s) 2,4
11. [bijection] exhibitor:Hiroshi Mita: ruled out position(s) 2
12. [bijection] exhibitor:Jun Kawabe: ruled out position(s) 2,4
13. [bijection] exhibitor:Noriko Hase: ruled out position(s) 1,3
14. [bijection] species:a hinoki cypress: ruled out position(s) 1
15. [bijection] species:a zelkova: ruled out position(s) 1
16. [bijection] species:a trident maple: ruled out position(s) 1
17. [bijection] species:a trident maple: ruled out position(s) 2,3,5
18. [order] from clue 3 species:a hinoki cypress: ruled out position(s) 3,5
19. [order] from clue 5 species:a zelkova: ruled out position(s) 2,3
20. [bijection] exhibitor:Jun Kawabe: ruled out position(s) 1
21. [bijection] species:a satsuki azalea: ruled out position(s) 5

---

<sub>seed `2026172862551` &middot; score 5.1 &middot; atoms 7 &middot; positives 0 &middot; solved by order</sub>
