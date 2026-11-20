# Trivia Night at the Public Library

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `8eaea97a1465`

## Introduction

The library runs trivia on the first Thursday of the month, and the scorekeeper will not be hurried.
Five players are involved. Determine each player's score, team and category.
- **Player**: Odalys, Lou Ann, Takeshi, Vikram and Darby.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Team**: the Wi-Fighters, the Library Cards, Nacho Average Team, the Smarty Pants and the Quizzard of Oz.
- **Category**: state capitals, breakfast cereals, one-hit wonders, cloud formations and 90s cartoons.
Every player has a different score, team and category, so within each category every item is used exactly once.

## Clues

1. The player who takes the questions on state capitals scores 67 points.
2. The player who plays for the Library Cards is lower than 70 points in score order.
3. The player who plays for the Smarty Pants falls somewhere between Vikram and 64 points in score order.
4. 64 points is exactly one score step lower than Lou Ann, with no score in between.
5. Vikram falls somewhere between the player who takes the questions on breakfast cereals and the player who plays for the Wi-Fighters in score order.
6. The player who plays for the Smarty Pants is lower than Takeshi in score order.
7. The player who plays for the Quizzard of Oz is exactly one score step lower than the player who takes the questions on state capitals, with no score in between.
8. The player who takes the questions on one-hit wonders is exactly one score step lower than Darby, with no score in between.
9. The player who takes the questions on cloud formations and the player who plays for Nacho Average Team are exactly one score step apart in score order, in one direction or the other.

## Solving chart

*Score vs Player*

| | Odalys | Lou Ann | Takeshi | Vikram | Darby |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Team*

| | the Wi-Fighters | the Library Cards | Nacho Average Team | the Smarty Pants | the Quizzard of Oz |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Category*

| | state capitals | breakfast cereals | one-hit wonders | cloud formations | 90s cartoons |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Player vs Team*

| | the Wi-Fighters | the Library Cards | Nacho Average Team | the Smarty Pants | the Quizzard of Oz |
|---|---|---|---|---|---|
| **Odalys** | | | | | |
| **Lou Ann** | | | | | |
| **Takeshi** | | | | | |
| **Vikram** | | | | | |
| **Darby** | | | | | |

*Player vs Category*

| | state capitals | breakfast cereals | one-hit wonders | cloud formations | 90s cartoons |
|---|---|---|---|---|---|
| **Odalys** | | | | | |
| **Lou Ann** | | | | | |
| **Takeshi** | | | | | |
| **Vikram** | | | | | |
| **Darby** | | | | | |

*Team vs Category*

| | state capitals | breakfast cereals | one-hit wonders | cloud formations | 90s cartoons |
|---|---|---|---|---|---|
| **the Wi-Fighters** | | | | | |
| **the Library Cards** | | | | | |
| **Nacho Average Team** | | | | | |
| **the Smarty Pants** | | | | | |
| **the Quizzard of Oz** | | | | | |

## Solution

| Score | Player | Team | Category |
|---|---|---|---|
| 61 points | Odalys | the Library Cards | one-hit wonders |
| 64 points | Darby | the Quizzard of Oz | breakfast cereals |
| 67 points | Lou Ann | the Smarty Pants | state capitals |
| 70 points | Vikram | Nacho Average Team | 90s cartoons |
| 73 points | Takeshi | the Wi-Fighters | cloud formations |

## How it falls out

1. [direct] from clue 8 category:state capitals: ruled out position(s) 1,2,4,5
2. [bijection] category:breakfast cereals: ruled out position(s) 3
3. [bijection] category:one-hit wonders: ruled out position(s) 3
4. [bijection] category:cloud formations: ruled out position(s) 3
5. [bijection] category:90s cartoons: ruled out position(s) 3
6. [order] from clue 9 team:the Library Cards: ruled out position(s) 4,5
7. [order] from clue 7 team:the Smarty Pants: ruled out position(s) 5
8. [order] from clue 7 player:Takeshi: ruled out position(s) 1
9. [order] from clue 6 player:Vikram: ruled out position(s) 1,5
10. [order] from clue 4 player:Lou Ann: ruled out position(s) 1,2,4,5
11. [order] from clue 3 team:the Smarty Pants: ruled out position(s) 1,2,4
12. [order] from clue 3 player:Vikram: ruled out position(s) 2,3
13. [order] from clue 6 category:breakfast cereals: ruled out position(s) 4
14. [order] from clue 6 team:the Wi-Fighters: ruled out position(s) 4
15. [order] from clue 7 player:Takeshi: ruled out position(s) 2,3
16. [order] from clue 2 team:the Quizzard of Oz: ruled out position(s) 1,3,4,5
17. [order] from clue 1 category:one-hit wonders: ruled out position(s) 5
18. [order] from clue 1 player:Darby: ruled out position(s) 1,4
19. [bijection] player:Odalys: ruled out position(s) 3,4
20. [bijection] player:Takeshi: ruled out position(s) 4
21. [bijection] player:Darby: ruled out position(s) 3
22. [bijection] player:Odalys: ruled out position(s) 2,5
23. [bijection] team:the Wi-Fighters: ruled out position(s) 2,3
24. [bijection] team:the Library Cards: ruled out position(s) 2,3
25. [bijection] team:Nacho Average Team: ruled out position(s) 2,3
26. [bijection] team:Nacho Average Team: ruled out position(s) 1,5
27. [order] from clue 5 category:cloud formations: ruled out position(s) 1,2,4
28. [order] from clue 1 category:one-hit wonders: ruled out position(s) 2
29. [bijection] category:breakfast cereals: ruled out position(s) 5
30. [bijection] category:90s cartoons: ruled out position(s) 5
31. [bijection] player:Darby: ruled out position(s) 5
32. [bijection] team:the Wi-Fighters: ruled out position(s) 1
33. [order] from clue 1 category:one-hit wonders: ruled out position(s) 4
34. [bijection] category:breakfast cereals: ruled out position(s) 1
35. [bijection] category:90s cartoons: ruled out position(s) 1
36. [bijection] category:90s cartoons: ruled out position(s) 2

---

<sub>seed `2026173097177` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
