# The Graveyard Shift at WPKX

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `1b765d23b809`

## Introduction

Nobody at WPKX has met anyone on the overnight schedule, which is how the station likes it.
Five hosts are involved. Determine each host's slot, show and format.
- **Host**: Rusty Lamarr, Dustin Crowe, Bea Okonjo, Arlo Finch and Maribel Sosa.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Show**: Owls Calling; The Sleepless Hour; Coffee and Regrets; The Long Haul; and Signal Fade.
- **Format**: lost surf rock, trucker country, obscure jazz, forgotten soul and radio plays.
Every host has a different slot, show and format, so within each category every item is used exactly once.

## Clues

1. The host who plays forgotten soul broadcasts in slot three. One of Arlo Finch and slot three sits at an odd-numbered slot and the other at an even-numbered slot.
2. Maribel Sosa presents Signal Fade.
3. The host who presents Coffee and Regrets and slot five are exactly one slot apart in slot order, in one direction or the other.
4. Bea Okonjo and slot four are exactly one slot apart in slot order, in one direction or the other.
5. The host who plays radio plays is exactly one slot earlier than slot five, with no slot in between.
6. The host who plays radio plays is earlier than the host who presents Owls Calling in slot order.
7. The host who plays trucker country and Bea Okonjo are exactly one slot apart in slot order, in one direction or the other.
8. The host who plays radio plays falls somewhere between Dustin Crowe and the host who presents The Sleepless Hour in slot order.
9. The host who plays lost surf rock is earlier than the host who presents Signal Fade in slot order.
10. Bea Okonjo falls somewhere between the host who presents Owls Calling and the host who presents The Sleepless Hour in slot order.

## Solving chart

*Running order vs Host*

| | Rusty Lamarr | Dustin Crowe | Bea Okonjo | Arlo Finch | Maribel Sosa |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Show*

| | Owls Calling | The Sleepless Hour | Coffee and Regrets | The Long Haul | Signal Fade |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Format*

| | lost surf rock | trucker country | obscure jazz | forgotten soul | radio plays |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Host vs Show*

| | Owls Calling | The Sleepless Hour | Coffee and Regrets | The Long Haul | Signal Fade |
|---|---|---|---|---|---|
| **Rusty Lamarr** | | | | | |
| **Dustin Crowe** | | | | | |
| **Bea Okonjo** | | | | | |
| **Arlo Finch** | | | | | |
| **Maribel Sosa** | | | | | |

*Host vs Format*

| | lost surf rock | trucker country | obscure jazz | forgotten soul | radio plays |
|---|---|---|---|---|---|
| **Rusty Lamarr** | | | | | |
| **Dustin Crowe** | | | | | |
| **Bea Okonjo** | | | | | |
| **Arlo Finch** | | | | | |
| **Maribel Sosa** | | | | | |

*Show vs Format*

| | lost surf rock | trucker country | obscure jazz | forgotten soul | radio plays |
|---|---|---|---|---|---|
| **Owls Calling** | | | | | |
| **The Sleepless Hour** | | | | | |
| **Coffee and Regrets** | | | | | |
| **The Long Haul** | | | | | |
| **Signal Fade** | | | | | |

## Solution

| Running order | Host | Show | Format |
|---|---|---|---|
| slot one | Rusty Lamarr | The Sleepless Hour | lost surf rock |
| slot two | Maribel Sosa | Signal Fade | trucker country |
| slot three | Bea Okonjo | The Long Haul | forgotten soul |
| slot four | Arlo Finch | Coffee and Regrets | radio plays |
| slot five | Dustin Crowe | Owls Calling | obscure jazz |

## How it falls out

1. [direct] from clue 7 genre:forgotten soul: ruled out position(s) 1,2,4,5
2. [bijection] genre:lost surf rock: ruled out position(s) 3
3. [bijection] genre:trucker country: ruled out position(s) 3
4. [bijection] genre:obscure jazz: ruled out position(s) 3
5. [bijection] genre:radio plays: ruled out position(s) 3
6. [order] from clue 11 genre:radio plays: ruled out position(s) 1,5
7. [order] from clue 8 genre:lost surf rock: ruled out position(s) 5
8. [order] from clue 8 show:Signal Fade: ruled out position(s) 1
9. [order] from clue 6 host:Arlo Finch: ruled out position(s) 1,3,5
10. [order] from clue 5 show:Coffee and Regrets: ruled out position(s) 1,2,3,5
11. [order] from clue 4 host:Bea Okonjo: ruled out position(s) 1,2,4
12. [order] from clue 9 genre:trucker country: ruled out position(s) 1,5
13. [order] from clue 3 host:Bea Okonjo: ruled out position(s) 5
14. [order] from clue 3 show:Owls Calling: ruled out position(s) 3
15. [order] from clue 3 show:The Sleepless Hour: ruled out position(s) 3
16. [order] from clue 2 show:Owls Calling: ruled out position(s) 1,2
17. [order] from clue 3 show:The Sleepless Hour: ruled out position(s) 4,5
18. [order] from clue 11 host:Dustin Crowe: ruled out position(s) 1,2
19. [order] from clue 1 genre:radio plays: ruled out position(s) 2
20. [order] from clue 11 host:Dustin Crowe: ruled out position(s) 3,4
21. [order] from clue 2 show:Owls Calling: ruled out position(s) 4
22. [direct] from clue 10 host:Maribel Sosa: ruled out position(s) 1
23. [bijection] genre:lost surf rock: ruled out position(s) 4
24. [bijection] genre:trucker country: ruled out position(s) 4
25. [bijection] genre:obscure jazz: ruled out position(s) 4
26. [bijection] genre:obscure jazz: ruled out position(s) 1,2
27. [bijection] host:Rusty Lamarr: ruled out position(s) 3,5
28. [bijection] host:Maribel Sosa: ruled out position(s) 3,5
29. [bijection] host:Rusty Lamarr: ruled out position(s) 2,4
30. [bijection] show:The Long Haul: ruled out position(s) 4,5
31. [bijection] show:Signal Fade: ruled out position(s) 4,5
32. [direct] from clue 10 host:Maribel Sosa: ruled out position(s) 4
33. [direct] from clue 10 show:Signal Fade: ruled out position(s) 3
34. [order] from clue 8 genre:lost surf rock: ruled out position(s) 2
35. [bijection] host:Arlo Finch: ruled out position(s) 2
36. [bijection] show:The Sleepless Hour: ruled out position(s) 2
37. [bijection] show:The Long Haul: ruled out position(s) 2
38. [bijection] show:The Long Haul: ruled out position(s) 1

---

<sub>seed `2026172773411` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
