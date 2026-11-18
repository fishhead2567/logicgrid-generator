# The Ravelston Chess Club Ladder

*The Ravelston Chess Club ladder is recalculated monthly and disputed continuously.*

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `699e7962de70`

## Introduction

There are 5 entries. Each has exactly one placing and one item from every other category below, and within each category every item belongs to a different entry.
- **Placing** (listed in order): first, second, third, fourth and fifth.
- **Player**: Hieronyma, Olumide, Yevgenia, Birgitta and Adaeze.
- **Clock**: a tournament DGT clock, a chipped BHB clock, a borrowed digital clock, a hotel alarm clock and a phone app.
- **Table habit**: leaving between moves, removing their shoes, rearranging the captured pieces, eating boiled sweets and narrating in a whisper.
The places above are listed in order, from first to fifth.

## Clues

1. Leaving between moves goes with second.
2. Narrating in a whisper goes with fourth.
3. A hotel alarm clock, rearranging the captured pieces and Adaeze are three different entries. Rearranging the captured pieces' placing is immediately better than a phone app's placing, with no placing in between. Yevgenia falls somewhere between rearranging the captured pieces and third in placing order.
4. A borrowed digital clock and Birgitta are exactly four places apart in placing order.
5. A tournament DGT clock and Birgitta are exactly three places apart in placing order.
6. Eating boiled sweets' placing is immediately better than Olumide's placing, with no placing in between.

## Solving chart

*Placing vs Player*

| | Hieronyma | Olumide | Yevgenia | Birgitta | Adaeze |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Clock*

| | a tournament DGT clock | a chipped BHB clock | a borrowed digital clock | a hotel alarm clock | a phone app |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Table habit*

| | leaving between moves | removing their shoes | rearranging the captured pieces | eating boiled sweets | narrating in a whisper |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Player vs Clock*

| | a tournament DGT clock | a chipped BHB clock | a borrowed digital clock | a hotel alarm clock | a phone app |
|---|---|---|---|---|---|
| **Hieronyma** | | | | | |
| **Olumide** | | | | | |
| **Yevgenia** | | | | | |
| **Birgitta** | | | | | |
| **Adaeze** | | | | | |

*Player vs Table habit*

| | leaving between moves | removing their shoes | rearranging the captured pieces | eating boiled sweets | narrating in a whisper |
|---|---|---|---|---|---|
| **Hieronyma** | | | | | |
| **Olumide** | | | | | |
| **Yevgenia** | | | | | |
| **Birgitta** | | | | | |
| **Adaeze** | | | | | |

*Clock vs Table habit*

| | leaving between moves | removing their shoes | rearranging the captured pieces | eating boiled sweets | narrating in a whisper |
|---|---|---|---|---|---|
| **a tournament DGT clock** | | | | | |
| **a chipped BHB clock** | | | | | |
| **a borrowed digital clock** | | | | | |
| **a hotel alarm clock** | | | | | |
| **a phone app** | | | | | |

## Solution

| Placing | Player | Clock | Table habit |
|---|---|---|---|
| first | Birgitta | a chipped BHB clock | rearranging the captured pieces |
| second | Yevgenia | a phone app | leaving between moves |
| third | Hieronyma | a hotel alarm clock | eating boiled sweets |
| fourth | Olumide | a tournament DGT clock | narrating in a whisper |
| fifth | Adaeze | a borrowed digital clock | removing their shoes |

## How it falls out

1. [direct] from clue 3 habit:narrating in a whisper: ruled out position(s) 1,2,3,5
2. [direct] from clue 1 habit:leaving between moves: ruled out position(s) 1,3,4,5
3. [bijection] habit:removing their shoes: ruled out position(s) 2,4
4. [bijection] habit:rearranging the captured pieces: ruled out position(s) 2,4
5. [bijection] habit:eating boiled sweets: ruled out position(s) 2,4
6. [order] from clue 8 habit:eating boiled sweets: ruled out position(s) 5
7. [order] from clue 8 player:Olumide: ruled out position(s) 1,3,5
8. [order] from clue 6 player:Yevgenia: ruled out position(s) 1,3,5
9. [order] from clue 6 habit:rearranging the captured pieces: ruled out position(s) 3
10. [order] from clue 5 habit:rearranging the captured pieces: ruled out position(s) 5
11. [order] from clue 5 clock:a phone app: ruled out position(s) 1,3,4,5
12. [order] from clue 6 player:Yevgenia: ruled out position(s) 4
13. [order] from clue 4 clock:a borrowed digital clock: ruled out position(s) 2,3,4
14. [order] from clue 4 player:Birgitta: ruled out position(s) 2,3,4
15. [order] from clue 2 clock:a tournament DGT clock: ruled out position(s) 1,3,5
16. [bijection] from clue 7 clock:a hotel alarm clock: ruled out position(s) 1
17. [bijection] from clue 7 player:Adaeze: ruled out position(s) 1
18. [bijection] clock:a tournament DGT clock: ruled out position(s) 2
19. [bijection] clock:a chipped BHB clock: ruled out position(s) 2
20. [bijection] clock:a hotel alarm clock: ruled out position(s) 2
21. [bijection] habit:removing their shoes: ruled out position(s) 1
22. [bijection] habit:eating boiled sweets: ruled out position(s) 1
23. [bijection] habit:removing their shoes: ruled out position(s) 3
24. [bijection] player:Hieronyma: ruled out position(s) 2
25. [bijection] player:Olumide: ruled out position(s) 2
26. [bijection] player:Adaeze: ruled out position(s) 2
27. [order] from clue 2 player:Birgitta: ruled out position(s) 5
28. [order] from clue 4 clock:a borrowed digital clock: ruled out position(s) 1
29. [bijection] clock:a chipped BHB clock: ruled out position(s) 4,5
30. [bijection] clock:a hotel alarm clock: ruled out position(s) 4,5
31. [bijection] clock:a chipped BHB clock: ruled out position(s) 3
32. [bijection] player:Hieronyma: ruled out position(s) 1,4
33. [bijection] player:Adaeze: ruled out position(s) 4
34. [bijection] from clue 7 player:Adaeze: ruled out position(s) 3
35. [bijection] player:Hieronyma: ruled out position(s) 5

---

<sub>seed `2026172725897` &middot; score 5.355 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
