# The Lakeshore Esports Bracket

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 12 &nbsp;&nbsp; **id** `8ff2c5f8c382`

## Introduction

The school esports club booked the library after hours: a double-elimination bracket, and a very long argument about seeding.
Five players are involved. Determine each player's exit round, gear and tag.
- **Player**: Tyrell, Gus Villalobos, Saoirse, Oksana and Mina.
- **Exit round** (listed from earlier to later): round one, round two, round three, round four and round five.
- **Gear**: a borrowed controller, a split keyboard, an arcade stick, a wireless headset and the club's old mouse.
- **Tag**: BlueHeron, Nine Lives, Sparrow, Pocketwatch and Marmalade.
Every player has a different exit round, gear and tag, so within each category every item is used exactly once.

## Clues

1. Tyrell is knocked out in round five.
2. The player who plays with an arcade stick goes by BlueHeron.
3. The player who goes by Sparrow is not knocked out in round two. The player who goes by Sparrow is not knocked out in round five.
4. Gus Villalobos is not knocked out in round two.
5. The player who plays with the club's old mouse does not go by Marmalade. The player who goes by Marmalade is not knocked out in round five.
6. The player who plays with a split keyboard and round three are exactly one round apart in exit round order, in one direction or the other.
7. Round two is exactly one round earlier than Saoirse, with no exit round in between.
8. The player who plays with the club's old mouse is earlier than the player who goes by Sparrow in exit round order.
9. Mina is exactly one round earlier than the player who plays with a wireless headset, with no exit round in between.
10. Saoirse is exactly one round earlier than the player who plays with an arcade stick, with no exit round in between.
11. Tyrell does not go by Nine Lives.
12. Gus Villalobos does not go by Nine Lives.

## Solving chart

*Exit round vs Player*

| | Tyrell | Gus Villalobos | Saoirse | Oksana | Mina |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Exit round vs Gear*

| | a borrowed controller | a split keyboard | an arcade stick | a wireless headset | the club's old mouse |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Exit round vs Tag*

| | BlueHeron | Nine Lives | Sparrow | Pocketwatch | Marmalade |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Player vs Gear*

| | a borrowed controller | a split keyboard | an arcade stick | a wireless headset | the club's old mouse |
|---|---|---|---|---|---|
| **Tyrell** | | | | | |
| **Gus Villalobos** | | | | | |
| **Saoirse** | | | | | |
| **Oksana** | | | | | |
| **Mina** | | | | | |

*Player vs Tag*

| | BlueHeron | Nine Lives | Sparrow | Pocketwatch | Marmalade |
|---|---|---|---|---|---|
| **Tyrell** | | | | | |
| **Gus Villalobos** | | | | | |
| **Saoirse** | | | | | |
| **Oksana** | | | | | |
| **Mina** | | | | | |

*Gear vs Tag*

| | BlueHeron | Nine Lives | Sparrow | Pocketwatch | Marmalade |
|---|---|---|---|---|---|
| **a borrowed controller** | | | | | |
| **a split keyboard** | | | | | |
| **an arcade stick** | | | | | |
| **a wireless headset** | | | | | |
| **the club's old mouse** | | | | | |

## Solution

| Exit round | Player | Gear | Tag |
|---|---|---|---|
| round one | Oksana | the club's old mouse | Nine Lives |
| round two | Mina | a split keyboard | Marmalade |
| round three | Saoirse | a wireless headset | Sparrow |
| round four | Gus Villalobos | an arcade stick | BlueHeron |
| round five | Tyrell | a borrowed controller | Pocketwatch |

## How it falls out

1. [direct] from clue 11 tag:Sparrow: ruled out position(s) 5
2. [direct] from clue 8 player:Tyrell: ruled out position(s) 1,2,3,4
3. [direct] from clue 9 tag:Nine Lives: ruled out position(s) 5
4. [direct] from clue 6 tag:Sparrow: ruled out position(s) 2
5. [direct] from clue 3 tag:Marmalade: ruled out position(s) 5
6. [direct] from clue 1 player:Gus Villalobos: ruled out position(s) 2
7. [bijection] player:Gus Villalobos: ruled out position(s) 5
8. [bijection] player:Saoirse: ruled out position(s) 5
9. [bijection] player:Oksana: ruled out position(s) 5
10. [bijection] player:Mina: ruled out position(s) 5
11. [order] from clue 13 player:Saoirse: ruled out position(s) 1,2,4
12. [order] from clue 12 gear:a wireless headset: ruled out position(s) 1
13. [order] from clue 10 gear:a split keyboard: ruled out position(s) 1,3,5
14. [order] from clue 5 gear:the club's old mouse: ruled out position(s) 4,5
15. [order] from clue 5 tag:Sparrow: ruled out position(s) 1
16. [order] from clue 4 gear:an arcade stick: ruled out position(s) 1,2,3,5
17. [direct] from clue 2 tag:BlueHeron: ruled out position(s) 1,2,3,5
18. [bijection] gear:a borrowed controller: ruled out position(s) 4
19. [bijection] gear:a split keyboard: ruled out position(s) 4
20. [bijection] gear:a wireless headset: ruled out position(s) 4
21. [bijection] player:Gus Villalobos: ruled out position(s) 3
22. [bijection] player:Oksana: ruled out position(s) 3
23. [bijection] player:Mina: ruled out position(s) 3
24. [bijection] tag:Nine Lives: ruled out position(s) 4
25. [bijection] tag:Sparrow: ruled out position(s) 4
26. [bijection] tag:Pocketwatch: ruled out position(s) 4
27. [bijection] tag:Marmalade: ruled out position(s) 4
28. [bijection] tag:Pocketwatch: ruled out position(s) 1,2,3
29. [order] from clue 5 gear:the club's old mouse: ruled out position(s) 3
30. [bijection] gear:a borrowed controller: ruled out position(s) 2
31. [bijection] gear:a wireless headset: ruled out position(s) 2
32. [bijection] gear:the club's old mouse: ruled out position(s) 2
33. [bijection] tag:Nine Lives: ruled out position(s) 3
34. [bijection] tag:Marmalade: ruled out position(s) 3
35. [direct] from clue 14 tag:Marmalade: ruled out position(s) 1
36. [order] from clue 12 player:Mina: ruled out position(s) 1
37. [bijection] gear:a borrowed controller: ruled out position(s) 1
38. [bijection] tag:Nine Lives: ruled out position(s) 2
39. [direct] from clue 7 player:Gus Villalobos: ruled out position(s) 1
40. [bijection] player:Oksana: ruled out position(s) 4
_... and 4 further steps._

---

<sub>seed `2026172978392` &middot; score 5.355 &middot; atoms 14 &middot; positives 2 &middot; solved by order</sub>
