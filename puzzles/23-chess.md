# The Ravelston Chess Club Ladder

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `302deb4f45d6`

## Introduction

The Ravelston Chess Club ladder is recalculated monthly and disputed continuously.
Five players are involved. Determine each player's placing, clock and habit.
- **Player**: Birgitta, Casimir, Yevgenia, Hieronyma and Olumide.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Clock**: a tournament DGT clock, a hotel alarm clock, a borrowed digital clock, a wooden analogue clock and a phone app.
- **Table habit**: removing their shoes, writing notation in pencil, humming, leaving between moves and eating boiled sweets.
Every player has a different placing, clock and habit, so within each category every item is used exactly once.

## Clues

1. The player who uses a borrowed digital clock is known for removing their shoes.
2. The player who uses a wooden analogue clock is known for humming.
3. The player who uses a tournament DGT clock falls somewhere between fifth and second in placing order.
4. The player who is known for removing their shoes and second are exactly one place apart in placing order, in one direction or the other.
5. The player who is known for leaving between moves and second are exactly one place apart in placing order, in one direction or the other.
6. First is exactly one place better than Casimir, with no placing in between.
7. Hieronyma is better than the player who uses a wooden analogue clock in placing order. The player who is known for humming falls somewhere between Hieronyma and Olumide in placing order.
8. Olumide is exactly one place better than the player who uses a hotel alarm clock, with no placing in between.
9. The player who is known for writing notation in pencil falls somewhere between Olumide and Yevgenia in placing order.

## Solving chart

*Placing vs Player*

| | Birgitta | Casimir | Yevgenia | Hieronyma | Olumide |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Clock*

| | a tournament DGT clock | a hotel alarm clock | a borrowed digital clock | a wooden analogue clock | a phone app |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Table habit*

| | removing their shoes | writing notation in pencil | humming | leaving between moves | eating boiled sweets |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Player vs Clock*

| | a tournament DGT clock | a hotel alarm clock | a borrowed digital clock | a wooden analogue clock | a phone app |
|---|---|---|---|---|---|
| **Birgitta** | | | | | |
| **Casimir** | | | | | |
| **Yevgenia** | | | | | |
| **Hieronyma** | | | | | |
| **Olumide** | | | | | |

*Player vs Table habit*

| | removing their shoes | writing notation in pencil | humming | leaving between moves | eating boiled sweets |
|---|---|---|---|---|---|
| **Birgitta** | | | | | |
| **Casimir** | | | | | |
| **Yevgenia** | | | | | |
| **Hieronyma** | | | | | |
| **Olumide** | | | | | |

*Clock vs Table habit*

| | removing their shoes | writing notation in pencil | humming | leaving between moves | eating boiled sweets |
|---|---|---|---|---|---|
| **a tournament DGT clock** | | | | | |
| **a hotel alarm clock** | | | | | |
| **a borrowed digital clock** | | | | | |
| **a wooden analogue clock** | | | | | |
| **a phone app** | | | | | |

## Solution

| Placing | Player | Clock | Table habit |
|---|---|---|---|
| first | Hieronyma | a borrowed digital clock | removing their shoes |
| second | Casimir | a wooden analogue clock | humming |
| third | Olumide | a tournament DGT clock | leaving between moves |
| fourth | Birgitta | a hotel alarm clock | writing notation in pencil |
| fifth | Yevgenia | a phone app | eating boiled sweets |

## How it falls out

1. [order] from clue 10 habit:writing notation in pencil: ruled out position(s) 1,5
2. [order] from clue 9 habit:leaving between moves: ruled out position(s) 2,4,5
3. [order] from clue 7 player:Olumide: ruled out position(s) 5
4. [order] from clue 7 clock:a hotel alarm clock: ruled out position(s) 1
5. [order] from clue 6 player:Casimir: ruled out position(s) 1,3,4,5
6. [order] from clue 5 habit:removing their shoes: ruled out position(s) 2,4,5
7. [order] from clue 4 habit:humming: ruled out position(s) 1,5
8. [order] from clue 3 clock:a tournament DGT clock: ruled out position(s) 1,2,5
9. [order] from clue 2 player:Hieronyma: ruled out position(s) 5
10. [order] from clue 2 clock:a wooden analogue clock: ruled out position(s) 1
11. [order] from clue 4 habit:humming: ruled out position(s) 4
12. [direct] from clue 8 clock:a wooden analogue clock: ruled out position(s) 4,5
13. [order] from clue 2 player:Hieronyma: ruled out position(s) 3,4
14. [order] from clue 4 player:Olumide: ruled out position(s) 1,2
15. [order] from clue 10 player:Yevgenia: ruled out position(s) 3,4
16. [order] from clue 7 clock:a hotel alarm clock: ruled out position(s) 2,3
17. [direct] from clue 1 clock:a borrowed digital clock: ruled out position(s) 2,4,5
18. [bijection] habit:eating boiled sweets: ruled out position(s) 1,2,3,4
19. [bijection] player:Birgitta: ruled out position(s) 2
20. [bijection] player:Yevgenia: ruled out position(s) 2
21. [bijection] player:Hieronyma: ruled out position(s) 2
22. [bijection] habit:writing notation in pencil: ruled out position(s) 2,3
23. [bijection] player:Birgitta: ruled out position(s) 1
24. [bijection] player:Yevgenia: ruled out position(s) 1
25. [order] from clue 10 player:Olumide: ruled out position(s) 4
26. [order] from clue 7 clock:a hotel alarm clock: ruled out position(s) 5
27. [order] from clue 4 habit:humming: ruled out position(s) 3
28. [direct] from clue 8 clock:a wooden analogue clock: ruled out position(s) 3
29. [bijection] clock:a tournament DGT clock: ruled out position(s) 4
30. [bijection] clock:a phone app: ruled out position(s) 2,4
31. [bijection] clock:a phone app: ruled out position(s) 1,3
32. [bijection] player:Birgitta: ruled out position(s) 3,5
33. [bijection] clock:a borrowed digital clock: ruled out position(s) 3
34. [direct] from clue 1 habit:removing their shoes: ruled out position(s) 3
35. [bijection] habit:leaving between moves: ruled out position(s) 1

---

<sub>seed `2026172957579` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
