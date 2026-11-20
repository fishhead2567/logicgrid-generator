# The Riverside Chess Club Ladder

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 13 &nbsp;&nbsp; **id** `50633fd57c4b`

## Introduction

The Riverside Chess Club ladder is recalculated monthly and disputed continuously.
Five players are involved. Determine each player's placing, opening and clock.
- **Player**: Hannah, Birgitta, Olumide, Dermot and Casimir.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Favourite opening**: the Grunfeld, the Dutch Defence, the London System, the Bird's Opening and the Catalan.
- **Clock**: a hotel alarm clock, a wooden analog clock, a chipped BHB clock, no clock at all and a borrowed digital clock.
Every player has a different placing, opening and clock, so within each category every item is used exactly once.

## Clues

1. The player who uses a hotel alarm clock favours the Grunfeld.
2. The player who favours the Dutch Defence and second are exactly two places apart in placing order.
3. At least one of the following holds, and possibly more than one: (a) The player who uses a chipped BHB clock is better than the player who favours the Dutch Defence in placing order. (b) The player who favours the London System places third.
4. The player who uses a wooden analog clock and first are exactly two places apart in placing order.
5. At least one of the following holds, and possibly more than one: (a) The player who uses a chipped BHB clock and second are exactly one place apart in placing order, in one direction or the other. (b) The player who uses a chipped BHB clock and Olumide are exactly one place apart in placing order, in one direction or the other.
6. One of the player who uses no clock at all and first sits at an odd-numbered placing and the other at an even-numbered placing.
7. Olumide falls somewhere between the player who favours the Dutch Defence and the player who favours the London System in placing order.
8. The player who uses a wooden analog clock does not favour the Bird's Opening.
9. The player who favours the Bird's Opening and Birgitta are exactly two places apart in placing order.
10. The player who uses a wooden analog clock and Hannah are exactly two places apart in placing order.
11. At least one of the following holds, and possibly more than one: (a) The player who favours the Dutch Defence and Dermot are exactly one place apart in placing order, in one direction or the other. (b) The player who favours the Bird's Opening is better than Casimir in placing order.
12. One of the player who uses a chipped BHB clock and the player who favours the Catalan sits at an odd-numbered placing and the other at an even-numbered placing.
13. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The player who favours the Dutch Defence and Dermot are exactly one place apart in placing order, in one direction or the other. (b) Dermot does not favour the Bird's Opening.

## Solving chart

*Placing vs Player*

| | Hannah | Birgitta | Olumide | Dermot | Casimir |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Favourite opening*

| | the Grunfeld | the Dutch Defence | the London System | the Bird's Opening | the Catalan |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Clock*

| | a hotel alarm clock | a wooden analog clock | a chipped BHB clock | no clock at all | a borrowed digital clock |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Player vs Favourite opening*

| | the Grunfeld | the Dutch Defence | the London System | the Bird's Opening | the Catalan |
|---|---|---|---|---|---|
| **Hannah** | | | | | |
| **Birgitta** | | | | | |
| **Olumide** | | | | | |
| **Dermot** | | | | | |
| **Casimir** | | | | | |

*Player vs Clock*

| | a hotel alarm clock | a wooden analog clock | a chipped BHB clock | no clock at all | a borrowed digital clock |
|---|---|---|---|---|---|
| **Hannah** | | | | | |
| **Birgitta** | | | | | |
| **Olumide** | | | | | |
| **Dermot** | | | | | |
| **Casimir** | | | | | |

*Favourite opening vs Clock*

| | a hotel alarm clock | a wooden analog clock | a chipped BHB clock | no clock at all | a borrowed digital clock |
|---|---|---|---|---|---|
| **the Grunfeld** | | | | | |
| **the Dutch Defence** | | | | | |
| **the London System** | | | | | |
| **the Bird's Opening** | | | | | |
| **the Catalan** | | | | | |

## Solution

| Placing | Player | Favourite opening | Clock |
|---|---|---|---|
| first | Hannah | the London System | a borrowed digital clock |
| second | Dermot | the Bird's Opening | a chipped BHB clock |
| third | Olumide | the Catalan | a wooden analog clock |
| fourth | Birgitta | the Dutch Defence | no clock at all |
| fifth | Casimir | the Grunfeld | a hotel alarm clock |

## How it falls out

1. [order] from clue 10 clock:no clock at all: ruled out position(s) 1,3,5
2. [order] from clue 9 player:Olumide: ruled out position(s) 1,5
3. [order] from clue 5 opening:the Dutch Defence: ruled out position(s) 1,2,3,5
4. [order] from clue 9 player:Olumide: ruled out position(s) 4
5. [order] from clue 9 opening:the London System: ruled out position(s) 3,4,5
6. [order] from clue 2 clock:a wooden analog clock: ruled out position(s) 1,2,4,5
7. [order] from clue 12 player:Hannah: ruled out position(s) 2,3,4
8. [direct] from clue 7 opening:the Bird's Opening: ruled out position(s) 3
9. [order] from clue 13 player:Birgitta: ruled out position(s) 1,5
10. [bijection] clock:a hotel alarm clock: ruled out position(s) 3
11. [bijection] clock:a chipped BHB clock: ruled out position(s) 3
12. [bijection] clock:a borrowed digital clock: ruled out position(s) 3
13. [bijection] opening:the Grunfeld: ruled out position(s) 4
14. [bijection] opening:the Bird's Opening: ruled out position(s) 4
15. [bijection] opening:the Catalan: ruled out position(s) 4
16. [order] from clue 13 player:Birgitta: ruled out position(s) 2
17. [direct] from clue 4 clock:a hotel alarm clock: ruled out position(s) 4
18. [direct] from clue 4 opening:the Grunfeld: ruled out position(s) 3
19. [bijection] opening:the Catalan: ruled out position(s) 1,2,5
20. [order] from clue 11 clock:a chipped BHB clock: ruled out position(s) 1,5
21. [disjunction] from clue 8 player:Olumide: ruled out position(s) 2
22. [disjunction] from clue 3 player:Dermot: ruled out position(s) 3
23. [disjunction] from clue 1 clock:a chipped BHB clock: ruled out position(s) 4
24. [bijection] clock:a hotel alarm clock: ruled out position(s) 2
25. [bijection] clock:no clock at all: ruled out position(s) 2
26. [bijection] clock:a borrowed digital clock: ruled out position(s) 2
27. [bijection] player:Birgitta: ruled out position(s) 3
28. [bijection] player:Casimir: ruled out position(s) 3
29. [order] from clue 13 opening:the Bird's Opening: ruled out position(s) 1,5
30. [disjunction] from clue 3 player:Dermot: ruled out position(s) 5
31. [disjunction] from clue 6 player:Casimir: ruled out position(s) 1,2
32. [direct] from clue 4 opening:the Grunfeld: ruled out position(s) 2
33. [bijection] clock:a borrowed digital clock: ruled out position(s) 4
34. [bijection] opening:the London System: ruled out position(s) 2
35. [bijection] opening:the Grunfeld: ruled out position(s) 1
36. [bijection] player:Dermot: ruled out position(s) 4
37. [bijection] player:Casimir: ruled out position(s) 4
38. [bijection] player:Dermot: ruled out position(s) 1
39. [direct] from clue 4 clock:a hotel alarm clock: ruled out position(s) 1
40. [bijection] clock:a borrowed digital clock: ruled out position(s) 5
_... and 1 further steps._

---

<sub>seed `2026173120934` &middot; score 9.9344 &middot; atoms 13 &middot; positives 1 &middot; solved by disjunction</sub>
