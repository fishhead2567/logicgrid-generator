# Trivia Night at the Public Library

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `2e37a59d12c2`

## Introduction

The library runs trivia on the first Thursday of the month. Six regulars, six team names, and a scorekeeper who will not be hurried.
Five players are involved. Determine each player's score, team and category.
- **Player**: Takeshi, Priscilla, Darby, Vikram and Odalys.
- **Score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Team**: the Quizzard of Oz, Nacho Average Team, the Wi-Fighters, the Smarty Pants and the Library Cards.
- **Category**: world flags, dinosaurs, 90s cartoons, one-hit wonders and state capitals.
Every player has a different score, team and category, so within each category every item is used exactly once.

## Clues

1. Takeshi scores 70 points.
2. The player who takes the questions on dinosaurs falls somewhere between 61 points and the player who plays for Nacho Average Team in score order.
3. Priscilla is higher than 67 points in score order.
4. 70 points is exactly one score step lower than the player who takes the questions on 90s cartoons, with no score in between.
5. The player who takes the questions on state capitals is exactly one score step lower than Takeshi, with no score in between.
6. Darby is exactly one score step lower than the player who plays for the Quizzard of Oz, with no score in between.
7. The player who takes the questions on one-hit wonders falls somewhere between the player who plays for the Quizzard of Oz and the player who plays for the Smarty Pants in score order.
8. The player who takes the questions on one-hit wonders is lower than Vikram in score order.
9. The player who takes the questions on dinosaurs does not play for the Wi-Fighters.

## Solving chart

*Score vs Player*

| | Takeshi | Priscilla | Darby | Vikram | Odalys |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Team*

| | the Quizzard of Oz | Nacho Average Team | the Wi-Fighters | the Smarty Pants | the Library Cards |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Score vs Category*

| | world flags | dinosaurs | 90s cartoons | one-hit wonders | state capitals |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Player vs Team*

| | the Quizzard of Oz | Nacho Average Team | the Wi-Fighters | the Smarty Pants | the Library Cards |
|---|---|---|---|---|---|
| **Takeshi** | | | | | |
| **Priscilla** | | | | | |
| **Darby** | | | | | |
| **Vikram** | | | | | |
| **Odalys** | | | | | |

*Player vs Category*

| | world flags | dinosaurs | 90s cartoons | one-hit wonders | state capitals |
|---|---|---|---|---|---|
| **Takeshi** | | | | | |
| **Priscilla** | | | | | |
| **Darby** | | | | | |
| **Vikram** | | | | | |
| **Odalys** | | | | | |

*Team vs Category*

| | world flags | dinosaurs | 90s cartoons | one-hit wonders | state capitals |
|---|---|---|---|---|---|
| **the Quizzard of Oz** | | | | | |
| **Nacho Average Team** | | | | | |
| **the Wi-Fighters** | | | | | |
| **the Smarty Pants** | | | | | |
| **the Library Cards** | | | | | |

## Solution

| Score | Player | Team | Category |
|---|---|---|---|
| 61 points | Odalys | the Smarty Pants | world flags |
| 64 points | Darby | the Wi-Fighters | one-hit wonders |
| 67 points | Vikram | the Quizzard of Oz | state capitals |
| 70 points | Takeshi | the Library Cards | dinosaurs |
| 73 points | Priscilla | Nacho Average Team | 90s cartoons |

## How it falls out

1. [direct] from clue 2 player:Takeshi: ruled out position(s) 1,2,3,5
2. [bijection] player:Priscilla: ruled out position(s) 4
3. [bijection] player:Darby: ruled out position(s) 4
4. [bijection] player:Vikram: ruled out position(s) 4
5. [bijection] player:Odalys: ruled out position(s) 4
6. [order] from clue 8 category:dinosaurs: ruled out position(s) 1,5
7. [order] from clue 8 team:Nacho Average Team: ruled out position(s) 1,2
8. [order] from clue 7 category:one-hit wonders: ruled out position(s) 5
9. [order] from clue 7 player:Vikram: ruled out position(s) 1
10. [order] from clue 6 category:one-hit wonders: ruled out position(s) 1
11. [order] from clue 7 player:Vikram: ruled out position(s) 2
12. [order] from clue 5 player:Darby: ruled out position(s) 5
13. [order] from clue 5 team:the Quizzard of Oz: ruled out position(s) 1,5
14. [order] from clue 6 team:the Smarty Pants: ruled out position(s) 3
15. [order] from clue 4 player:Priscilla: ruled out position(s) 1,2,3
16. [order] from clue 3 category:90s cartoons: ruled out position(s) 1,2,3,4
17. [order] from clue 1 category:state capitals: ruled out position(s) 1,2,4,5
18. [bijection] category:world flags: ruled out position(s) 3,5
19. [bijection] category:dinosaurs: ruled out position(s) 3
20. [bijection] category:one-hit wonders: ruled out position(s) 3
21. [bijection] category:world flags: ruled out position(s) 2,4
22. [bijection] player:Vikram: ruled out position(s) 5
23. [bijection] player:Odalys: ruled out position(s) 5
24. [order] from clue 7 category:one-hit wonders: ruled out position(s) 4
25. [order] from clue 6 team:the Quizzard of Oz: ruled out position(s) 2
26. [order] from clue 6 team:the Smarty Pants: ruled out position(s) 2,4,5
27. [order] from clue 5 player:Darby: ruled out position(s) 1
28. [bijection] category:dinosaurs: ruled out position(s) 2
29. [bijection] player:Darby: ruled out position(s) 3
30. [bijection] player:Odalys: ruled out position(s) 3
31. [bijection] player:Odalys: ruled out position(s) 2
32. [bijection] team:the Wi-Fighters: ruled out position(s) 1
33. [bijection] team:the Library Cards: ruled out position(s) 1
34. [order] from clue 5 team:the Quizzard of Oz: ruled out position(s) 4
35. [direct] from clue 9 team:the Wi-Fighters: ruled out position(s) 4
36. [order] from clue 8 team:Nacho Average Team: ruled out position(s) 3,4
37. [bijection] team:the Wi-Fighters: ruled out position(s) 3,5
38. [bijection] team:the Library Cards: ruled out position(s) 3,5
39. [bijection] team:the Library Cards: ruled out position(s) 2

---

<sub>seed `2026172881333` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
