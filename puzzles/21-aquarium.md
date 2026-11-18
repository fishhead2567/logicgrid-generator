# The Night Shift at Coldwater Hall

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `8464a2b72386`

## Introduction

Coldwater Hall Aquarium keeps a night rota of tanks, and one keeper who is definitely feeding the wrong things.
Five keepers are involved. Determine each keeper's slot, tank and feed.
- **Keeper**: Oskar, Marisol, Chiamaka, Rhiannon and Fitzwilliam.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Tank**: the jellyfish column, the touch pool, the deep reef, the seahorse nursery and the kelp tank.
- **Feed**: live mysis, a gelatine cube of unclear provenance, mussel meat, nori sheets and chopped squid.
Every keeper has a different slot, tank and feed, so within each category every item is used exactly once.

## Clues

1. The keeper who tends the touch pool works slot five.
2. The keeper who feeds nori sheets does not work slot three.
3. The keeper who feeds chopped squid and slot one are exactly one slot apart in slot order, in one direction or the other.
4. The keeper who feeds mussel meat does not work slot five.
5. Slot one is exactly one slot earlier than Fitzwilliam, with no slot in between.
6. The keeper who feeds live mysis is earlier than the keeper who tends the deep reef in slot order. The keeper who tends the deep reef is earlier than Marisol in slot order.
7. The keeper who feeds chopped squid is earlier than the keeper who tends the kelp tank in slot order.
8. The keeper who feeds live mysis is earlier than Chiamaka in slot order.
9. The keeper who feeds mussel meat and Rhiannon are exactly one slot apart in slot order, in one direction or the other. Chiamaka is earlier than the keeper who feeds mussel meat in slot order.
10. The keeper who feeds mussel meat and the keeper who tends the jellyfish column are exactly one slot apart in slot order, in one direction or the other.

## Solving chart

*Running order vs Keeper*

| | Oskar | Marisol | Chiamaka | Rhiannon | Fitzwilliam |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Tank*

| | the jellyfish column | the touch pool | the deep reef | the seahorse nursery | the kelp tank |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Feed*

| | live mysis | a gelatine cube of unclear provenance | mussel meat | nori sheets | chopped squid |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Keeper vs Tank*

| | the jellyfish column | the touch pool | the deep reef | the seahorse nursery | the kelp tank |
|---|---|---|---|---|---|
| **Oskar** | | | | | |
| **Marisol** | | | | | |
| **Chiamaka** | | | | | |
| **Rhiannon** | | | | | |
| **Fitzwilliam** | | | | | |

*Keeper vs Feed*

| | live mysis | a gelatine cube of unclear provenance | mussel meat | nori sheets | chopped squid |
|---|---|---|---|---|---|
| **Oskar** | | | | | |
| **Marisol** | | | | | |
| **Chiamaka** | | | | | |
| **Rhiannon** | | | | | |
| **Fitzwilliam** | | | | | |

*Tank vs Feed*

| | live mysis | a gelatine cube of unclear provenance | mussel meat | nori sheets | chopped squid |
|---|---|---|---|---|---|
| **the jellyfish column** | | | | | |
| **the touch pool** | | | | | |
| **the deep reef** | | | | | |
| **the seahorse nursery** | | | | | |
| **the kelp tank** | | | | | |

## Solution

| Running order | Keeper | Tank | Feed |
|---|---|---|---|
| slot one | Oskar | the seahorse nursery | live mysis |
| slot two | Fitzwilliam | the deep reef | chopped squid |
| slot three | Chiamaka | the jellyfish column | a gelatine cube of unclear provenance |
| slot four | Marisol | the kelp tank | mussel meat |
| slot five | Rhiannon | the touch pool | nori sheets |

## How it falls out

1. [direct] from clue 11 feed:mussel meat: ruled out position(s) 5
2. [direct] from clue 4 tank:the touch pool: ruled out position(s) 1,2,3,4
3. [direct] from clue 2 feed:nori sheets: ruled out position(s) 3
4. [bijection] tank:the jellyfish column: ruled out position(s) 5
5. [bijection] tank:the deep reef: ruled out position(s) 5
6. [bijection] tank:the seahorse nursery: ruled out position(s) 5
7. [bijection] tank:the kelp tank: ruled out position(s) 5
8. [order] from clue 12 feed:live mysis: ruled out position(s) 5
9. [order] from clue 12 keeper:Chiamaka: ruled out position(s) 1
10. [order] from clue 10 feed:chopped squid: ruled out position(s) 1,3,4,5
11. [order] from clue 9 tank:the kelp tank: ruled out position(s) 1,2
12. [order] from clue 8 keeper:Fitzwilliam: ruled out position(s) 1,3,4,5
13. [order] from clue 7 feed:live mysis: ruled out position(s) 4
14. [order] from clue 7 tank:the deep reef: ruled out position(s) 1
15. [order] from clue 6 keeper:Marisol: ruled out position(s) 1,2
16. [order] from clue 1 keeper:Chiamaka: ruled out position(s) 4,5
17. [order] from clue 1 feed:mussel meat: ruled out position(s) 1,2
18. [order] from clue 5 keeper:Rhiannon: ruled out position(s) 1
19. [order] from clue 3 tank:the jellyfish column: ruled out position(s) 1
20. [order] from clue 12 feed:live mysis: ruled out position(s) 3
21. [bijection] feed:live mysis: ruled out position(s) 2
22. [bijection] feed:a gelatine cube of unclear provenance: ruled out position(s) 2
23. [bijection] feed:nori sheets: ruled out position(s) 2
24. [bijection] keeper:Oskar: ruled out position(s) 2
25. [bijection] keeper:Chiamaka: ruled out position(s) 2
26. [bijection] keeper:Rhiannon: ruled out position(s) 2
27. [bijection] keeper:Oskar: ruled out position(s) 3,4,5
28. [bijection] tank:the seahorse nursery: ruled out position(s) 2,3,4
29. [order] from clue 1 feed:mussel meat: ruled out position(s) 3
30. [order] from clue 5 keeper:Rhiannon: ruled out position(s) 4
31. [order] from clue 3 tank:the jellyfish column: ruled out position(s) 2,4
32. [bijection] feed:a gelatine cube of unclear provenance: ruled out position(s) 1,4
33. [bijection] feed:nori sheets: ruled out position(s) 1,4
34. [bijection] feed:a gelatine cube of unclear provenance: ruled out position(s) 5
35. [bijection] keeper:Marisol: ruled out position(s) 3
36. [bijection] keeper:Rhiannon: ruled out position(s) 3
37. [bijection] keeper:Marisol: ruled out position(s) 5
38. [bijection] tank:the deep reef: ruled out position(s) 3
39. [bijection] tank:the kelp tank: ruled out position(s) 3
40. [bijection] tank:the deep reef: ruled out position(s) 4

---

<sub>seed `2026172741735` &middot; score 5.515 &middot; atoms 12 &middot; positives 1 &middot; solved by order</sub>
