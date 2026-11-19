# The Night Shift at Coldwater Hall

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `bfce7b725169`

## Introduction

Coldwater Hall Aquarium keeps a night rota of tanks, and one keeper who is definitely feeding the wrong things.
Five keepers are involved. Determine each keeper's slot, tank and incident.
- **Keeper**: Marisol, Bartolo, Fitzwilliam, Oskar and Agnetha.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Tank**: the octopus enclosure, the kelp tank, the deep reef, the touch pool and the jellyfish column.
- **Logged incident**: an algal bloom, a blocked skimmer, a visitor's dropped phone, a failed chiller and an unexplained pH swing.
Every keeper has a different slot, tank and incident, so within each category every item is used exactly once.

## Clues

1. The keeper who logs a failed chiller and slot two are exactly one slot apart in slot order, in one direction or the other. Marisol works slot two.
2. Slot one is exactly one slot earlier than the keeper who tends the kelp tank, with no slot in between.
3. Agnetha is exactly one slot earlier than slot two, with no slot in between.
4. The keeper who tends the deep reef is exactly one slot earlier than slot two, with no slot in between.
5. One of the keeper who logs an unexplained pH swing and Marisol sits at an odd-numbered slot and the other at an even-numbered slot.
6. The keeper who logs an algal bloom is exactly one slot earlier than Bartolo, with no slot in between.
7. The keeper who logs a blocked skimmer is earlier than the keeper who tends the kelp tank in slot order.
8. Fitzwilliam and the keeper who tends the touch pool are exactly two slots apart in slot order.
9. The keeper who tends the octopus enclosure falls somewhere between Agnetha and Fitzwilliam in slot order.

## Solving chart

*Running order vs Keeper*

| | Marisol | Bartolo | Fitzwilliam | Oskar | Agnetha |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Tank*

| | the octopus enclosure | the kelp tank | the deep reef | the touch pool | the jellyfish column |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Logged incident*

| | an algal bloom | a blocked skimmer | a visitor's dropped phone | a failed chiller | an unexplained pH swing |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Keeper vs Tank*

| | the octopus enclosure | the kelp tank | the deep reef | the touch pool | the jellyfish column |
|---|---|---|---|---|---|
| **Marisol** | | | | | |
| **Bartolo** | | | | | |
| **Fitzwilliam** | | | | | |
| **Oskar** | | | | | |
| **Agnetha** | | | | | |

*Keeper vs Logged incident*

| | an algal bloom | a blocked skimmer | a visitor's dropped phone | a failed chiller | an unexplained pH swing |
|---|---|---|---|---|---|
| **Marisol** | | | | | |
| **Bartolo** | | | | | |
| **Fitzwilliam** | | | | | |
| **Oskar** | | | | | |
| **Agnetha** | | | | | |

*Tank vs Logged incident*

| | an algal bloom | a blocked skimmer | a visitor's dropped phone | a failed chiller | an unexplained pH swing |
|---|---|---|---|---|---|
| **the octopus enclosure** | | | | | |
| **the kelp tank** | | | | | |
| **the deep reef** | | | | | |
| **the touch pool** | | | | | |
| **the jellyfish column** | | | | | |

## Solution

| Running order | Keeper | Tank | Logged incident |
|---|---|---|---|
| slot one | Agnetha | the deep reef | a blocked skimmer |
| slot two | Marisol | the kelp tank | an algal bloom |
| slot three | Bartolo | the touch pool | a failed chiller |
| slot four | Oskar | the octopus enclosure | a visitor's dropped phone |
| slot five | Fitzwilliam | the jellyfish column | an unexplained pH swing |

## How it falls out

1. [direct] from clue 9 keeper:Marisol: ruled out position(s) 1,3,4,5
2. [bijection] keeper:Bartolo: ruled out position(s) 2
3. [bijection] keeper:Fitzwilliam: ruled out position(s) 2
4. [bijection] keeper:Oskar: ruled out position(s) 2
5. [bijection] keeper:Agnetha: ruled out position(s) 2
6. [order] from clue 10 incident:an algal bloom: ruled out position(s) 1,5
7. [order] from clue 10 keeper:Bartolo: ruled out position(s) 1
8. [order] from clue 8 tank:the kelp tank: ruled out position(s) 1,3,4,5
9. [order] from clue 7 tank:the touch pool: ruled out position(s) 4
10. [order] from clue 6 incident:a failed chiller: ruled out position(s) 2,4,5
11. [order] from clue 5 keeper:Agnetha: ruled out position(s) 3,4,5
12. [order] from clue 4 incident:an unexplained pH swing: ruled out position(s) 2,4
13. [order] from clue 3 tank:the octopus enclosure: ruled out position(s) 1,5
14. [order] from clue 3 keeper:Fitzwilliam: ruled out position(s) 1
15. [order] from clue 2 incident:a blocked skimmer: ruled out position(s) 2,3,4,5
16. [order] from clue 1 tank:the deep reef: ruled out position(s) 2,3,4,5
17. [bijection] incident:a visitor's dropped phone: ruled out position(s) 1
18. [bijection] incident:a failed chiller: ruled out position(s) 1
19. [bijection] incident:an unexplained pH swing: ruled out position(s) 1
20. [bijection] keeper:Oskar: ruled out position(s) 1
21. [bijection] tank:the octopus enclosure: ruled out position(s) 2
22. [bijection] tank:the touch pool: ruled out position(s) 1,2
23. [bijection] tank:the jellyfish column: ruled out position(s) 1,2
24. [order] from clue 7 keeper:Fitzwilliam: ruled out position(s) 4
25. [order] from clue 3 keeper:Fitzwilliam: ruled out position(s) 3
26. [order] from clue 7 tank:the touch pool: ruled out position(s) 5
27. [bijection] incident:an algal bloom: ruled out position(s) 3
28. [bijection] incident:a visitor's dropped phone: ruled out position(s) 3
29. [bijection] incident:an unexplained pH swing: ruled out position(s) 3
30. [bijection] keeper:Bartolo: ruled out position(s) 5
31. [bijection] keeper:Oskar: ruled out position(s) 5
32. [bijection] tank:the octopus enclosure: ruled out position(s) 3
33. [bijection] tank:the jellyfish column: ruled out position(s) 3
34. [bijection] tank:the jellyfish column: ruled out position(s) 4
35. [order] from clue 10 incident:an algal bloom: ruled out position(s) 4
36. [order] from clue 10 keeper:Bartolo: ruled out position(s) 4
37. [bijection] incident:a visitor's dropped phone: ruled out position(s) 2,5
38. [bijection] keeper:Oskar: ruled out position(s) 3

---

<sub>seed `2026172873414` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
