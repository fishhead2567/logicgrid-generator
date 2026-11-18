# The Ravelston Chess Club Ladder

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `f782eaae65a4`

## Introduction

The Ravelston Chess Club ladder is recalculated monthly and disputed continuously.
Four players are involved. Determine each player's placing, clock and habit.
- **Player**: Yevgenia, Casimir, Dermot and Hieronyma.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Clock**: a phone app, a hotel alarm clock, a tournament DGT clock and a chipped BHB clock.
- **Table habit**: rearranging the captured pieces, leaving between moves, narrating in a whisper and removing their shoes.
Every player has a different placing, clock and habit, so within each category every item is used exactly once.

## Clues

1. The player who uses a hotel alarm clock is known for narrating in a whisper.
2. The player who is known for removing their shoes is worse than second in placing order.
3. Second falls somewhere between the player who uses a phone app and Dermot in placing order.
4. Casimir falls somewhere between the player who is known for leaving between moves and first in placing order. Yevgenia is not known for leaving between moves.
5. The player who uses a hotel alarm clock and third are exactly one place apart in placing order, in one direction or the other.
6. The player who is known for removing their shoes and Hieronyma are exactly one place apart in placing order, in one direction or the other.
7. The player who uses a chipped BHB clock falls somewhere between the player who is known for rearranging the captured pieces and Yevgenia in placing order.

## Solving chart

*Placing vs Player*

| | Yevgenia | Casimir | Dermot | Hieronyma |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Clock*

| | a phone app | a hotel alarm clock | a tournament DGT clock | a chipped BHB clock |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Table habit*

| | rearranging the captured pieces | leaving between moves | narrating in a whisper | removing their shoes |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Player vs Clock*

| | a phone app | a hotel alarm clock | a tournament DGT clock | a chipped BHB clock |
|---|---|---|---|---|
| **Yevgenia** | | | | |
| **Casimir** | | | | |
| **Dermot** | | | | |
| **Hieronyma** | | | | |

*Player vs Table habit*

| | rearranging the captured pieces | leaving between moves | narrating in a whisper | removing their shoes |
|---|---|---|---|---|
| **Yevgenia** | | | | |
| **Casimir** | | | | |
| **Dermot** | | | | |
| **Hieronyma** | | | | |

*Clock vs Table habit*

| | rearranging the captured pieces | leaving between moves | narrating in a whisper | removing their shoes |
|---|---|---|---|---|
| **a phone app** | | | | |
| **a hotel alarm clock** | | | | |
| **a tournament DGT clock** | | | | |
| **a chipped BHB clock** | | | | |

## Solution

| Placing | Player | Clock | Table habit |
|---|---|---|---|
| first | Dermot | a tournament DGT clock | rearranging the captured pieces |
| second | Casimir | a hotel alarm clock | narrating in a whisper |
| third | Hieronyma | a chipped BHB clock | leaving between moves |
| fourth | Yevgenia | a phone app | removing their shoes |

## How it falls out

1. [order] from clue 8 clock:a phone app: ruled out position(s) 2
2. [order] from clue 8 player:Dermot: ruled out position(s) 2
3. [order] from clue 5 clock:a chipped BHB clock: ruled out position(s) 1,4
4. [order] from clue 4 habit:removing their shoes: ruled out position(s) 1,2
5. [order] from clue 7 player:Hieronyma: ruled out position(s) 1
6. [order] from clue 3 player:Casimir: ruled out position(s) 1,4
7. [order] from clue 3 habit:leaving between moves: ruled out position(s) 1,2
8. [order] from clue 1 clock:a hotel alarm clock: ruled out position(s) 1,3
9. [direct] from clue 2 habit:narrating in a whisper: ruled out position(s) 1,3
10. [bijection] habit:rearranging the captured pieces: ruled out position(s) 2,3,4
11. [order] from clue 5 player:Yevgenia: ruled out position(s) 1,2
12. [bijection] habit:narrating in a whisper: ruled out position(s) 4
13. [bijection] player:Dermot: ruled out position(s) 3,4
14. [order] from clue 8 clock:a phone app: ruled out position(s) 1
15. [direct] from clue 2 clock:a hotel alarm clock: ruled out position(s) 4
16. [bijection] clock:a tournament DGT clock: ruled out position(s) 2
17. [bijection] clock:a chipped BHB clock: ruled out position(s) 2
18. [bijection] clock:a tournament DGT clock: ruled out position(s) 3,4
19. [order] from clue 5 player:Yevgenia: ruled out position(s) 3
20. [direct] from clue 6 habit:leaving between moves: ruled out position(s) 4
21. [order] from clue 3 player:Casimir: ruled out position(s) 3
22. [bijection] clock:a phone app: ruled out position(s) 3
23. [bijection] habit:removing their shoes: ruled out position(s) 3
24. [bijection] player:Hieronyma: ruled out position(s) 2,4

---

<sub>seed `2026172646707` &middot; score 5.13 &middot; atoms 8 &middot; positives 1 &middot; solved by order</sub>
