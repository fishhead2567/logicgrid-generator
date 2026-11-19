# The Build Server Contest

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `84157d3818a1`

## Introduction

A creative-mode server, one weekend, and a block limit everybody swore they would stay under.
Five builders are involved. Determine each builder's score and biome.
- **Builder**: Milo, Thandiwe, Keiko, Nadine and Rafferty.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Biome**: a jungle, a snowy tundra, a badlands mesa, a cherry grove and a mushroom field.
Every builder has a different score and biome, so within each category every item is used exactly once.

## Clues

1. 70 points is exactly one score step lower than Thandiwe, with no score in between. Nadine scores 70 points.
2. Milo scores 61 points. The builder who builds in a badlands mesa falls somewhere between Milo and Rafferty in score order.
3. 64 points falls somewhere between the builder who builds in a jungle and the builder who builds in a snowy tundra in score order.
4. 70 points falls somewhere between the builder who builds in a snowy tundra and Rafferty in score order.
5. Rafferty is lower than the builder who builds in a mushroom field in score order.

## Solving chart

*Score vs Builder*

| | Milo | Thandiwe | Keiko | Nadine | Rafferty |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Biome*

| | a jungle | a snowy tundra | a badlands mesa | a cherry grove | a mushroom field |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Builder vs Biome*

| | a jungle | a snowy tundra | a badlands mesa | a cherry grove | a mushroom field |
|---|---|---|---|---|---|
| **Milo** | | | | | |
| **Thandiwe** | | | | | |
| **Keiko** | | | | | |
| **Nadine** | | | | | |
| **Rafferty** | | | | | |

## Solution

| Score | Builder | Biome |
|---|---|---|
| 61 points | Milo | a jungle |
| 64 points | Keiko | a badlands mesa |
| 67 points | Rafferty | a cherry grove |
| 70 points | Nadine | a mushroom field |
| 73 points | Thandiwe | a snowy tundra |

## How it falls out

1. [direct] from clue 4 builder:Milo: ruled out position(s) 2,3,4,5
2. [direct] from clue 2 builder:Nadine: ruled out position(s) 1,2,3,5
3. [bijection] builder:Thandiwe: ruled out position(s) 1,4
4. [bijection] builder:Keiko: ruled out position(s) 1,4
5. [bijection] builder:Rafferty: ruled out position(s) 1,4
6. [order] from clue 7 biome:a badlands mesa: ruled out position(s) 1,5
7. [order] from clue 7 builder:Rafferty: ruled out position(s) 2
8. [order] from clue 6 builder:Thandiwe: ruled out position(s) 2,3
9. [order] from clue 5 builder:Rafferty: ruled out position(s) 5
10. [order] from clue 5 biome:a mushroom field: ruled out position(s) 1,2,3
11. [order] from clue 7 biome:a badlands mesa: ruled out position(s) 3,4
12. [order] from clue 3 biome:a jungle: ruled out position(s) 2
13. [order] from clue 3 biome:a snowy tundra: ruled out position(s) 2
14. [order] from clue 1 biome:a snowy tundra: ruled out position(s) 1,3,4
15. [order] from clue 3 biome:a jungle: ruled out position(s) 3,4,5
16. [bijection] biome:a cherry grove: ruled out position(s) 1,2,5
17. [bijection] biome:a mushroom field: ruled out position(s) 5
18. [bijection] biome:a cherry grove: ruled out position(s) 4
19. [bijection] builder:Keiko: ruled out position(s) 3,5

---

<sub>seed `2026172746710` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
