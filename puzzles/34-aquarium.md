# The Night Shift at Harbor Point

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `4713cc02058c`

## Introduction

The Harbor Point Aquarium keeps a night rotation of tanks, and one keeper who is definitely feeding the wrong things.
Five keepers are involved. Determine each keeper's slot, tank and incident.
- **Keeper**: Everett, Chiamaka, Oskar, Bartolo and Marisol.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Tank**: the jellyfish column, the deep reef, the touch pool, the octopus enclosure and the estuary tank.
- **Logged incident**: a failed chiller, an escapee, a visitor's dropped phone, a cracked viewing pane and an algal bloom.
Every keeper has a different slot, tank and incident, so within each category every item is used exactly once.

## Clues

1. The keeper who logs a failed chiller and slot four are exactly three slots apart in slot order.
2. At least one of the following holds, and possibly more than one: (a) The keeper who logs an algal bloom and Chiamaka are exactly one slot apart in slot order, in one direction or the other. (b) Chiamaka does not work slot two.
3. The keeper who tends the octopus enclosure is exactly one slot earlier than slot three, with no slot in between.
4. One of Everett and slot two sits at an odd-numbered slot and the other at an even-numbered slot.
5. The keeper who tends the estuary tank and slot one are exactly two slots apart in slot order.
6. The keeper who logs an escapee and Oskar are exactly one slot apart in slot order, in one direction or the other.
7. The keeper who tends the touch pool falls somewhere between Marisol and Oskar in slot order.
8. Chiamaka and the keeper who tends the jellyfish column are exactly one slot apart in slot order, in one direction or the other.
9. At least one of the following holds, and possibly more than one: (a) The keeper who tends the octopus enclosure is exactly one slot earlier than the keeper who logs a visitor's dropped phone, with no slot in between. (b) The keeper who logs a visitor's dropped phone tends the deep reef.
10. Oskar falls somewhere between the keeper who logs an algal bloom and the keeper who logs an escapee in slot order.
11. The keeper who logs an algal bloom and the keeper who tends the touch pool are exactly two slots apart in slot order.

## Solving chart

*Running order vs Keeper*

| | Everett | Chiamaka | Oskar | Bartolo | Marisol |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Tank*

| | the jellyfish column | the deep reef | the touch pool | the octopus enclosure | the estuary tank |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Logged incident*

| | a failed chiller | an escapee | a visitor's dropped phone | a cracked viewing pane | an algal bloom |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Keeper vs Tank*

| | the jellyfish column | the deep reef | the touch pool | the octopus enclosure | the estuary tank |
|---|---|---|---|---|---|
| **Everett** | | | | | |
| **Chiamaka** | | | | | |
| **Oskar** | | | | | |
| **Bartolo** | | | | | |
| **Marisol** | | | | | |

*Keeper vs Logged incident*

| | a failed chiller | an escapee | a visitor's dropped phone | a cracked viewing pane | an algal bloom |
|---|---|---|---|---|---|
| **Everett** | | | | | |
| **Chiamaka** | | | | | |
| **Oskar** | | | | | |
| **Bartolo** | | | | | |
| **Marisol** | | | | | |

*Tank vs Logged incident*

| | a failed chiller | an escapee | a visitor's dropped phone | a cracked viewing pane | an algal bloom |
|---|---|---|---|---|---|
| **the jellyfish column** | | | | | |
| **the deep reef** | | | | | |
| **the touch pool** | | | | | |
| **the octopus enclosure** | | | | | |
| **the estuary tank** | | | | | |

## Solution

| Running order | Keeper | Tank | Logged incident |
|---|---|---|---|
| slot one | Everett | the deep reef | a failed chiller |
| slot two | Bartolo | the octopus enclosure | an algal bloom |
| slot three | Oskar | the estuary tank | a visitor's dropped phone |
| slot four | Chiamaka | the touch pool | an escapee |
| slot five | Marisol | the jellyfish column | a cracked viewing pane |

## How it falls out

1. [order] from clue 11 tank:the octopus enclosure: ruled out position(s) 1,3,4,5
2. [order] from clue 10 keeper:Oskar: ruled out position(s) 1,5
3. [order] from clue 8 tank:the touch pool: ruled out position(s) 1,5
4. [order] from clue 8 keeper:Marisol: ruled out position(s) 3
5. [order] from clue 9 incident:an algal bloom: ruled out position(s) 3
6. [order] from clue 4 keeper:Everett: ruled out position(s) 2,4
7. [order] from clue 2 tank:the estuary tank: ruled out position(s) 1,2,4,5
8. [order] from clue 1 incident:a failed chiller: ruled out position(s) 2,3,4,5
9. [bijection] incident:an escapee: ruled out position(s) 1
10. [bijection] incident:a visitor's dropped phone: ruled out position(s) 1
11. [bijection] incident:a cracked viewing pane: ruled out position(s) 1
12. [bijection] incident:an algal bloom: ruled out position(s) 1
13. [bijection] tank:the jellyfish column: ruled out position(s) 2,3
14. [bijection] tank:the deep reef: ruled out position(s) 2,3
15. [bijection] tank:the touch pool: ruled out position(s) 2,3
16. [order] from clue 8 keeper:Marisol: ruled out position(s) 1,2,4
17. [order] from clue 8 keeper:Oskar: ruled out position(s) 4
18. [order] from clue 6 keeper:Chiamaka: ruled out position(s) 1
19. [order] from clue 9 incident:an algal bloom: ruled out position(s) 4,5
20. [order] from clue 10 keeper:Oskar: ruled out position(s) 2
21. [order] from clue 10 incident:an escapee: ruled out position(s) 2,3
22. [order] from clue 5 incident:an escapee: ruled out position(s) 5
23. [bijection] incident:a visitor's dropped phone: ruled out position(s) 2,4
24. [bijection] incident:a cracked viewing pane: ruled out position(s) 2,4
25. [bijection] keeper:Everett: ruled out position(s) 3,5
26. [bijection] keeper:Chiamaka: ruled out position(s) 3,5
27. [bijection] keeper:Bartolo: ruled out position(s) 3,5
28. [bijection] tank:the jellyfish column: ruled out position(s) 4
29. [bijection] tank:the deep reef: ruled out position(s) 4
30. [bijection] keeper:Bartolo: ruled out position(s) 1
31. [disjunction] from clue 7 keeper:Chiamaka: ruled out position(s) 2
32. [order] from clue 6 tank:the jellyfish column: ruled out position(s) 1
33. [bijection] keeper:Bartolo: ruled out position(s) 4
34. [bijection] tank:the deep reef: ruled out position(s) 5
35. [disjunction] from clue 3 incident:a visitor's dropped phone: ruled out position(s) 5
36. [bijection] incident:a cracked viewing pane: ruled out position(s) 3

---

<sub>seed `2026173144691` &middot; score 9.2622 &middot; atoms 11 &middot; positives 0 &middot; solved by disjunction</sub>
