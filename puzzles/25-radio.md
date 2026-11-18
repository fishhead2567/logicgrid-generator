# The Graveyard Shift at WPKX

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `1b765d23b809`

## Introduction

Nobody at WPKX has met anyone on the overnight schedule, which is how the station likes it.
Five hosts are involved. Determine each host's slot, show and format.
- **Host**: Rusty Lamarr, Dustin Crowe, Bea Okonjo, Arlo Finch and Maribel Sosa.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Show**: Owls Calling; The Sleepless Hour; Coffee and Regrets; The Long Haul; and Signal Fade.
- **Format**: lost surf rock, trucker country, obscure jazz, forgotten soul and radio plays.
Every host has a different slot, show and format, so within each category every item is used exactly once.

## Clues

1. The host who plays radio plays broadcasts in slot four. The host who presents Owls Calling is later than slot four in slot order.
2. Dustin Crowe broadcasts in slot five.
3. The host who presents The Long Haul does not broadcast in slot two. The host who presents The Long Haul does not broadcast in slot one.
4. Maribel Sosa falls somewhere between the host who plays lost surf rock and slot three in slot order.
5. The host who plays forgotten soul falls somewhere between Arlo Finch and Rusty Lamarr in slot order.
6. Dustin Crowe and the host who presents Coffee and Regrets are exactly one slot apart in slot order, in one direction or the other.
7. The host who presents Signal Fade falls somewhere between the host who plays forgotten soul and Rusty Lamarr in slot order.
8. The host who plays trucker country and Rusty Lamarr are exactly one slot apart in slot order, in one direction or the other.

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

1. [direct] from clue 9 show:The Long Haul: ruled out position(s) 1
2. [direct] from clue 8 host:Dustin Crowe: ruled out position(s) 1,2,3,4
3. [direct] from clue 5 genre:radio plays: ruled out position(s) 1,2,3,5
4. [direct] from clue 4 show:The Long Haul: ruled out position(s) 2
5. [bijection] genre:lost surf rock: ruled out position(s) 4
6. [bijection] genre:trucker country: ruled out position(s) 4
7. [bijection] genre:obscure jazz: ruled out position(s) 4
8. [bijection] genre:forgotten soul: ruled out position(s) 4
9. [bijection] host:Rusty Lamarr: ruled out position(s) 5
10. [bijection] host:Bea Okonjo: ruled out position(s) 5
11. [bijection] host:Arlo Finch: ruled out position(s) 5
12. [bijection] host:Maribel Sosa: ruled out position(s) 5
13. [order] from clue 10 show:Owls Calling: ruled out position(s) 1,2,3,4
14. [order] from clue 7 show:Signal Fade: ruled out position(s) 1,5
15. [order] from clue 6 host:Maribel Sosa: ruled out position(s) 1,3
16. [order] from clue 6 genre:lost surf rock: ruled out position(s) 2,3
17. [order] from clue 2 show:Coffee and Regrets: ruled out position(s) 1,2,3,5
18. [order] from clue 1 genre:forgotten soul: ruled out position(s) 1,5
19. [order] from clue 7 show:Signal Fade: ruled out position(s) 4
20. [order] from clue 7 host:Rusty Lamarr: ruled out position(s) 2,3
21. [order] from clue 3 genre:trucker country: ruled out position(s) 1
22. [bijection] show:The Sleepless Hour: ruled out position(s) 4,5
23. [bijection] show:The Long Haul: ruled out position(s) 4,5
24. [bijection] show:The Sleepless Hour: ruled out position(s) 2,3
25. [bijection] show:Signal Fade: ruled out position(s) 3
26. [order] from clue 7 genre:forgotten soul: ruled out position(s) 2
27. [order] from clue 7 host:Rusty Lamarr: ruled out position(s) 4
28. [order] from clue 3 genre:trucker country: ruled out position(s) 3,5
29. [order] from clue 1 host:Arlo Finch: ruled out position(s) 1,2,3
30. [bijection] genre:obscure jazz: ruled out position(s) 2,3
31. [bijection] host:Bea Okonjo: ruled out position(s) 1,4
32. [bijection] host:Maribel Sosa: ruled out position(s) 4
33. [bijection] host:Bea Okonjo: ruled out position(s) 2
34. [order] from clue 6 genre:lost surf rock: ruled out position(s) 5
35. [bijection] genre:obscure jazz: ruled out position(s) 1

---

<sub>seed `2026172773411` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
