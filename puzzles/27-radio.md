# The Graveyard Shift at WPKX

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `6d43b4e36892`

## Introduction

Nobody at WPKX has met anyone on the overnight schedule, which is how the station likes it.
Five hosts are involved. Determine each host's slot, format and sponsor.
- **Host**: Dustin Crowe, Arlo Finch, Nadia Vell, Maribel Sosa and Rusty Lamarr.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Format**: lost surf rock, listener call-ins, church organ recordings, obscure jazz and forgotten soul.
- **Sponsor**: a discount dentist, a storage facility, a taxidermist, a psychic hotline and a mattress warehouse.
Every host has a different slot, format and sponsor, so within each category every item is used exactly once.

## Clues

1. The host who plays obscure jazz broadcasts in slot five. The host who is sponsored by a storage facility falls somewhere between slot five and slot three in slot order.
2. Arlo Finch and slot four are exactly one slot apart in slot order, in one direction or the other.
3. The host who is sponsored by a mattress warehouse is earlier than slot five in slot order.
4. Nadia Vell and slot five are exactly one slot apart in slot order, in one direction or the other.
5. The host who is sponsored by a discount dentist and slot two are exactly one slot apart in slot order, in one direction or the other.
6. The host who is sponsored by a taxidermist is exactly one slot earlier than the host who plays forgotten soul, with no slot in between.
7. The host who plays church organ recordings and Maribel Sosa are exactly one slot apart in slot order, in one direction or the other.
8. The host who plays listener call-ins is not sponsored by a taxidermist.
9. The host who plays lost surf rock and the host who is sponsored by a discount dentist are exactly three slots apart in slot order.
10. The host who is sponsored by a taxidermist is exactly one slot earlier than Dustin Crowe, with no slot in between.

## Solving chart

*Running order vs Host*

| | Dustin Crowe | Arlo Finch | Nadia Vell | Maribel Sosa | Rusty Lamarr |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Format*

| | lost surf rock | listener call-ins | church organ recordings | obscure jazz | forgotten soul |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Sponsor*

| | a discount dentist | a storage facility | a taxidermist | a psychic hotline | a mattress warehouse |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Host vs Format*

| | lost surf rock | listener call-ins | church organ recordings | obscure jazz | forgotten soul |
|---|---|---|---|---|---|
| **Dustin Crowe** | | | | | |
| **Arlo Finch** | | | | | |
| **Nadia Vell** | | | | | |
| **Maribel Sosa** | | | | | |
| **Rusty Lamarr** | | | | | |

*Host vs Sponsor*

| | a discount dentist | a storage facility | a taxidermist | a psychic hotline | a mattress warehouse |
|---|---|---|---|---|---|
| **Dustin Crowe** | | | | | |
| **Arlo Finch** | | | | | |
| **Nadia Vell** | | | | | |
| **Maribel Sosa** | | | | | |
| **Rusty Lamarr** | | | | | |

*Format vs Sponsor*

| | a discount dentist | a storage facility | a taxidermist | a psychic hotline | a mattress warehouse |
|---|---|---|---|---|---|
| **lost surf rock** | | | | | |
| **listener call-ins** | | | | | |
| **church organ recordings** | | | | | |
| **obscure jazz** | | | | | |
| **forgotten soul** | | | | | |

## Solution

| Running order | Host | Format | Sponsor |
|---|---|---|---|
| slot one | Maribel Sosa | listener call-ins | a discount dentist |
| slot two | Rusty Lamarr | church organ recordings | a taxidermist |
| slot three | Dustin Crowe | forgotten soul | a mattress warehouse |
| slot four | Nadia Vell | lost surf rock | a storage facility |
| slot five | Arlo Finch | obscure jazz | a psychic hotline |

## How it falls out

1. [direct] from clue 10 genre:obscure jazz: ruled out position(s) 1,2,3,4
2. [bijection] genre:lost surf rock: ruled out position(s) 5
3. [bijection] genre:listener call-ins: ruled out position(s) 5
4. [bijection] genre:church organ recordings: ruled out position(s) 5
5. [bijection] genre:forgotten soul: ruled out position(s) 5
6. [order] from clue 9 host:Nadia Vell: ruled out position(s) 1,2,3,5
7. [order] from clue 8 sponsor:a mattress warehouse: ruled out position(s) 5
8. [order] from clue 7 host:Arlo Finch: ruled out position(s) 1,2,4
9. [order] from clue 6 genre:lost surf rock: ruled out position(s) 3
10. [order] from clue 6 sponsor:a discount dentist: ruled out position(s) 2,3
11. [order] from clue 4 sponsor:a discount dentist: ruled out position(s) 4,5
12. [order] from clue 6 genre:lost surf rock: ruled out position(s) 1,2
13. [order] from clue 3 sponsor:a taxidermist: ruled out position(s) 5
14. [order] from clue 3 host:Dustin Crowe: ruled out position(s) 1
15. [order] from clue 2 sponsor:a storage facility: ruled out position(s) 1,2,3,5
16. [order] from clue 1 sponsor:a taxidermist: ruled out position(s) 4
17. [order] from clue 1 genre:forgotten soul: ruled out position(s) 1
18. [order] from clue 3 host:Dustin Crowe: ruled out position(s) 5
19. [bijection] genre:listener call-ins: ruled out position(s) 4
20. [bijection] genre:church organ recordings: ruled out position(s) 4
21. [bijection] genre:forgotten soul: ruled out position(s) 4
22. [bijection] host:Dustin Crowe: ruled out position(s) 4
23. [bijection] host:Maribel Sosa: ruled out position(s) 4
24. [bijection] host:Rusty Lamarr: ruled out position(s) 4
25. [bijection] sponsor:a taxidermist: ruled out position(s) 1
26. [bijection] sponsor:a psychic hotline: ruled out position(s) 1,4
27. [bijection] sponsor:a mattress warehouse: ruled out position(s) 1,4
28. [bijection] sponsor:a psychic hotline: ruled out position(s) 2,3
29. [order] from clue 3 sponsor:a taxidermist: ruled out position(s) 3
30. [order] from clue 3 host:Dustin Crowe: ruled out position(s) 2
31. [order] from clue 1 genre:forgotten soul: ruled out position(s) 2
32. [order] from clue 5 host:Maribel Sosa: ruled out position(s) 5
33. [direct] from clue 11 genre:listener call-ins: ruled out position(s) 2
34. [bijection] genre:listener call-ins: ruled out position(s) 3
35. [bijection] genre:church organ recordings: ruled out position(s) 3
36. [bijection] genre:church organ recordings: ruled out position(s) 1
37. [bijection] host:Arlo Finch: ruled out position(s) 3
38. [bijection] host:Maribel Sosa: ruled out position(s) 3
39. [bijection] host:Rusty Lamarr: ruled out position(s) 3
40. [bijection] sponsor:a mattress warehouse: ruled out position(s) 2
_... and 2 further steps._

---

<sub>seed `2026172989255` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
