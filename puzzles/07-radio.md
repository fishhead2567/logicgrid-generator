# The Graveyard Shift at WPKX

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 4 &nbsp;&nbsp; **id** `b12da526c87b`

## Introduction

Nobody at WPKX has met anyone on the overnight schedule, which is how the station likes it.
Four hosts are involved. Determine each host's slot and show.
- **Host**: Dustin Crowe, Maribel Sosa, Bea Okonjo and Rusty Lamarr.
- **Running order** (listed from earlier to later): slot one, slot two, slot three and slot four.
- **Show**: Owls Calling, The Long Haul, The Sleepless Hour and Static & Sons.
Every host has a different slot and show, so within each category every item is used exactly once.

## Clues

1. The host who presents Owls Calling broadcasts in slot two. Bea Okonjo broadcasts in slot two.
2. Rusty Lamarr broadcasts in slot four. The host who presents Static & Sons and slot four are exactly one slot apart in slot order, in one direction or the other.
3. The host who presents The Long Haul and slot three are exactly one slot apart in slot order, in one direction or the other.
4. Dustin Crowe is exactly one slot earlier than the host who presents Owls Calling, with no slot in between.

## Solving chart

*Running order vs Host*

| | Dustin Crowe | Maribel Sosa | Bea Okonjo | Rusty Lamarr |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Running order vs Show*

| | Owls Calling | The Long Haul | The Sleepless Hour | Static & Sons |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Host vs Show*

| | Owls Calling | The Long Haul | The Sleepless Hour | Static & Sons |
|---|---|---|---|---|
| **Dustin Crowe** | | | | |
| **Maribel Sosa** | | | | |
| **Bea Okonjo** | | | | |
| **Rusty Lamarr** | | | | |

## Solution

| Running order | Host | Show |
|---|---|---|
| slot one | Dustin Crowe | The Sleepless Hour |
| slot two | Bea Okonjo | Owls Calling |
| slot three | Maribel Sosa | Static & Sons |
| slot four | Rusty Lamarr | The Long Haul |

## How it falls out

1. [direct] from clue 6 host:Rusty Lamarr: ruled out position(s) 1,2,3
2. [direct] from clue 5 show:Owls Calling: ruled out position(s) 1,3,4
3. [direct] from clue 4 host:Bea Okonjo: ruled out position(s) 1,3,4
4. [bijection] host:Dustin Crowe: ruled out position(s) 2,4
5. [bijection] host:Maribel Sosa: ruled out position(s) 2,4
6. [bijection] show:The Long Haul: ruled out position(s) 2
7. [bijection] show:The Sleepless Hour: ruled out position(s) 2
8. [bijection] show:Static & Sons: ruled out position(s) 2
9. [order] from clue 3 show:Static & Sons: ruled out position(s) 1,4
10. [order] from clue 2 show:The Long Haul: ruled out position(s) 1,3
11. [order] from clue 1 host:Dustin Crowe: ruled out position(s) 3
12. [bijection] host:Maribel Sosa: ruled out position(s) 1
13. [bijection] show:The Sleepless Hour: ruled out position(s) 3,4

---

<sub>seed `2026172730872` &middot; score 3.97 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
