# The Night Shift at Coldwater Hall

*Coldwater Hall Aquarium keeps a night rota of tanks, and one keeper who is definitely feeding the wrong things.*

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `9bf6b156c99a`

## Introduction

There are 5 shifts. Each has exactly one slot and one item from every other category below, and within each category every item belongs to a different shift.
- **Running order** (listed in order): slot one, slot two, slot three, slot four and slot five.
- **Keeper**: Marisol, Chiamaka, Oskar, Fitzwilliam and Rhiannon.
- **Tank**: the touch pool, the deep reef, the octopus enclosure, the jellyfish column and the seahorse nursery.
- **Logged incident**: an algal bloom, an unexplained pH swing, a visitor's dropped phone, a failed chiller and an escapee.
The slots above are listed in order, from slot one to slot five.

## Clues

1. An escapee goes with slot two. An escapee's slot is immediately earlier than the touch pool's slot, with no slot in between.
2. The seahorse nursery falls somewhere between Oskar and slot five in slot order.
3. A failed chiller and the octopus enclosure are exactly three slots apart in slot order. The octopus enclosure falls somewhere between Marisol and slot four in slot order.
4. Rhiannon and slot one are exactly four slots apart in slot order.
5. A visitor's dropped phone does not go with Fitzwilliam.
6. An unexplained pH swing, Rhiannon and the jellyfish column are three different shifts.
7. A visitor's dropped phone's slot is immediately earlier than the deep reef's slot, with no slot in between.
8. Fitzwilliam does not go with the touch pool.

## Solving chart

*Running order vs Keeper*

| | Marisol | Chiamaka | Oskar | Fitzwilliam | Rhiannon |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Tank*

| | the touch pool | the deep reef | the octopus enclosure | the jellyfish column | the seahorse nursery |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Logged incident*

| | an algal bloom | an unexplained pH swing | a visitor's dropped phone | a failed chiller | an escapee |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Keeper vs Tank*

| | the touch pool | the deep reef | the octopus enclosure | the jellyfish column | the seahorse nursery |
|---|---|---|---|---|---|
| **Marisol** | | | | | |
| **Chiamaka** | | | | | |
| **Oskar** | | | | | |
| **Fitzwilliam** | | | | | |
| **Rhiannon** | | | | | |

*Keeper vs Logged incident*

| | an algal bloom | an unexplained pH swing | a visitor's dropped phone | a failed chiller | an escapee |
|---|---|---|---|---|---|
| **Marisol** | | | | | |
| **Chiamaka** | | | | | |
| **Oskar** | | | | | |
| **Fitzwilliam** | | | | | |
| **Rhiannon** | | | | | |

*Tank vs Logged incident*

| | an algal bloom | an unexplained pH swing | a visitor's dropped phone | a failed chiller | an escapee |
|---|---|---|---|---|---|
| **the touch pool** | | | | | |
| **the deep reef** | | | | | |
| **the octopus enclosure** | | | | | |
| **the jellyfish column** | | | | | |
| **the seahorse nursery** | | | | | |

## Solution

| Running order | Keeper | Tank | Logged incident |
|---|---|---|---|
| slot one | Marisol | the jellyfish column | an algal bloom |
| slot two | Fitzwilliam | the octopus enclosure | an escapee |
| slot three | Oskar | the touch pool | an unexplained pH swing |
| slot four | Chiamaka | the seahorse nursery | a visitor's dropped phone |
| slot five | Rhiannon | the deep reef | a failed chiller |

## How it falls out

1. [direct] from clue 8 incident:an escapee: ruled out position(s) 1,3,4,5
2. [bijection] incident:an algal bloom: ruled out position(s) 2
3. [bijection] incident:an unexplained pH swing: ruled out position(s) 2
4. [bijection] incident:a visitor's dropped phone: ruled out position(s) 2
5. [bijection] incident:a failed chiller: ruled out position(s) 2
6. [order] from clue 9 keeper:Rhiannon: ruled out position(s) 1,2,3,4
7. [order] from clue 7 tank:the seahorse nursery: ruled out position(s) 1,5
8. [order] from clue 7 keeper:Oskar: ruled out position(s) 4,5
9. [order] from clue 6 incident:a failed chiller: ruled out position(s) 3
10. [order] from clue 6 tank:the octopus enclosure: ruled out position(s) 3,5
11. [order] from clue 4 tank:the touch pool: ruled out position(s) 1,2,4,5
12. [order] from clue 3 tank:the octopus enclosure: ruled out position(s) 1,4
13. [order] from clue 3 keeper:Marisol: ruled out position(s) 2,3,4,5
14. [order] from clue 6 incident:a failed chiller: ruled out position(s) 1,4
15. [order] from clue 1 incident:a visitor's dropped phone: ruled out position(s) 5
16. [order] from clue 1 tank:the deep reef: ruled out position(s) 1,3
17. [bijection] from clue 2 incident:an unexplained pH swing: ruled out position(s) 5
18. [bijection] from clue 2 tank:the jellyfish column: ruled out position(s) 5
19. [direct] from clue 5 keeper:Fitzwilliam: ruled out position(s) 3
20. [bijection] incident:an algal bloom: ruled out position(s) 5
21. [bijection] keeper:Chiamaka: ruled out position(s) 1,5
22. [bijection] keeper:Oskar: ruled out position(s) 1
23. [bijection] keeper:Fitzwilliam: ruled out position(s) 1,5
24. [bijection] tank:the deep reef: ruled out position(s) 2
25. [bijection] tank:the jellyfish column: ruled out position(s) 2,3
26. [bijection] tank:the seahorse nursery: ruled out position(s) 2,3
27. [bijection] tank:the jellyfish column: ruled out position(s) 4
28. [bijection] tank:the deep reef: ruled out position(s) 4
29. [bijection] from clue 2 incident:an unexplained pH swing: ruled out position(s) 1
30. [order] from clue 1 incident:a visitor's dropped phone: ruled out position(s) 1,3
31. [direct] from clue 10 keeper:Fitzwilliam: ruled out position(s) 4
32. [bijection] incident:an algal bloom: ruled out position(s) 4
33. [bijection] incident:an unexplained pH swing: ruled out position(s) 4
34. [bijection] incident:an algal bloom: ruled out position(s) 3
35. [bijection] keeper:Chiamaka: ruled out position(s) 2
36. [bijection] keeper:Oskar: ruled out position(s) 2
37. [bijection] keeper:Chiamaka: ruled out position(s) 3

---

<sub>seed `2026172741735` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
