# The Night Shift at Coldwater Hall

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `7a5280b32e26`

## Introduction

Coldwater Hall Aquarium keeps a night rota of tanks, and one keeper who is definitely feeding the wrong things.
Four keepers are involved. Determine each keeper's slot, feed and incident.
- **Keeper**: Rhiannon, Agnetha, Marisol and Bartolo.
- **Running order** (listed from earlier to later): slot one, slot two, slot three and slot four.
- **Feed**: brine shrimp, live mysis, chopped squid and nori sheets.
- **Logged incident**: a visitor's dropped phone, an escapee, a failed chiller and an algal bloom.
Every keeper has a different slot, feed and incident, so within each category every item is used exactly once.

## Clues

1. The keeper who logs a visitor's dropped phone works slot three.
2. The keeper who feeds brine shrimp is earlier than the keeper who logs a failed chiller in slot order. Rhiannon logs a failed chiller.
3. Agnetha does not feed live mysis. Marisol falls somewhere between the keeper who feeds live mysis and slot four in slot order.
4. Slot two falls somewhere between the keeper who logs a failed chiller and the keeper who logs an escapee in slot order.
5. Marisol does not log an algal bloom.
6. The keeper who feeds brine shrimp and the keeper who logs an escapee are exactly one slot apart in slot order, in one direction or the other.
7. The keeper who feeds chopped squid and Marisol are exactly one slot apart in slot order, in one direction or the other.

## Solving chart

*Running order vs Keeper*

| | Rhiannon | Agnetha | Marisol | Bartolo |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Running order vs Feed*

| | brine shrimp | live mysis | chopped squid | nori sheets |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Running order vs Logged incident*

| | a visitor's dropped phone | an escapee | a failed chiller | an algal bloom |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Keeper vs Feed*

| | brine shrimp | live mysis | chopped squid | nori sheets |
|---|---|---|---|---|
| **Rhiannon** | | | | |
| **Agnetha** | | | | |
| **Marisol** | | | | |
| **Bartolo** | | | | |

*Keeper vs Logged incident*

| | a visitor's dropped phone | an escapee | a failed chiller | an algal bloom |
|---|---|---|---|---|
| **Rhiannon** | | | | |
| **Agnetha** | | | | |
| **Marisol** | | | | |
| **Bartolo** | | | | |

*Feed vs Logged incident*

| | a visitor's dropped phone | an escapee | a failed chiller | an algal bloom |
|---|---|---|---|---|
| **brine shrimp** | | | | |
| **live mysis** | | | | |
| **chopped squid** | | | | |
| **nori sheets** | | | | |

## Solution

| Running order | Keeper | Feed | Logged incident |
|---|---|---|---|
| slot one | Bartolo | live mysis | an escapee |
| slot two | Agnetha | brine shrimp | an algal bloom |
| slot three | Marisol | nori sheets | a visitor's dropped phone |
| slot four | Rhiannon | chopped squid | a failed chiller |

## How it falls out

1. [direct] from clue 8 incident:a visitor's dropped phone: ruled out position(s) 1,2,4
2. [bijection] incident:an escapee: ruled out position(s) 3
3. [bijection] incident:a failed chiller: ruled out position(s) 3
4. [bijection] incident:an algal bloom: ruled out position(s) 3
5. [direct] from clue 5 keeper:Rhiannon: ruled out position(s) 3
6. [order] from clue 9 feed:brine shrimp: ruled out position(s) 4
7. [order] from clue 4 keeper:Marisol: ruled out position(s) 1,4
8. [order] from clue 4 feed:live mysis: ruled out position(s) 3,4
9. [order] from clue 3 incident:a failed chiller: ruled out position(s) 1
10. [order] from clue 2 incident:a failed chiller: ruled out position(s) 2
11. [order] from clue 2 incident:an escapee: ruled out position(s) 2,4
12. [order] from clue 9 feed:brine shrimp: ruled out position(s) 1,3
13. [direct] from clue 5 keeper:Rhiannon: ruled out position(s) 1,2
14. [bijection] feed:live mysis: ruled out position(s) 2
15. [bijection] feed:chopped squid: ruled out position(s) 2
16. [bijection] feed:nori sheets: ruled out position(s) 2
17. [bijection] incident:an algal bloom: ruled out position(s) 1,4
18. [bijection] keeper:Agnetha: ruled out position(s) 4
19. [bijection] keeper:Bartolo: ruled out position(s) 4
20. [direct] from clue 7 keeper:Marisol: ruled out position(s) 2
21. [order] from clue 1 feed:chopped squid: ruled out position(s) 1,3
22. [direct] from clue 6 keeper:Agnetha: ruled out position(s) 1
23. [bijection] feed:nori sheets: ruled out position(s) 1,4
24. [bijection] keeper:Agnetha: ruled out position(s) 3
25. [bijection] keeper:Bartolo: ruled out position(s) 3
26. [bijection] keeper:Bartolo: ruled out position(s) 2

---

<sub>seed `2026172791031` &middot; score 4.93 &middot; atoms 9 &middot; positives 2 &middot; solved by order</sub>
