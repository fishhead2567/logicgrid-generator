# The Graveyard Shift at WPKX

*Nobody at WPKX has met anyone on the overnight schedule, which is how the station likes it.*

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `28c6e43e510b`

## Introduction

There are 5 programmes. Each has exactly one slot and one item from every other category below, and within each category every item belongs to a different programme.
- **Running order** (listed in order): slot one, slot two, slot three, slot four and slot five.
- **Host**: Rusty Lamarr, Dustin Crowe, Bea Okonjo, Arlo Finch and Maribel Sosa.
- **Format**: lost surf rock, obscure jazz, forgotten soul, radio plays and church organ recordings.
- **Sponsor**: a discount dentist, a mattress warehouse, a bail bondsman, a psychic hotline and a taxidermist.
The slots above are listed in order, from slot one to slot five.

## Clues

1. A taxidermist falls somewhere between Rusty Lamarr and slot five in slot order. Church organ recordings, Bea Okonjo and a taxidermist are three different programmes. Church organ recordings goes with slot two.
2. Radio plays goes with Bea Okonjo. Radio plays, Maribel Sosa and a bail bondsman are three different programmes. Obscure jazz's slot is earlier than a bail bondsman's slot.
3. Rusty Lamarr's slot is immediately earlier than slot two, with no slot in between. Slot two does not go with a discount dentist. Dustin Crowe does not go with slot two.
4. Forgotten soul's slot is immediately earlier than slot five, with no slot in between.
5. A psychic hotline's slot is immediately earlier than Arlo Finch's slot, with no slot in between. Slot four and a psychic hotline are next to each other in slot order, in one order or the other.

## Solving chart

*Running order vs Host*

| | Rusty Lamarr | Dustin Crowe | Bea Okonjo | Arlo Finch | Maribel Sosa |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Format*

| | lost surf rock | obscure jazz | forgotten soul | radio plays | church organ recordings |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Sponsor*

| | a discount dentist | a mattress warehouse | a bail bondsman | a psychic hotline | a taxidermist |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Host vs Format*

| | lost surf rock | obscure jazz | forgotten soul | radio plays | church organ recordings |
|---|---|---|---|---|---|
| **Rusty Lamarr** | | | | | |
| **Dustin Crowe** | | | | | |
| **Bea Okonjo** | | | | | |
| **Arlo Finch** | | | | | |
| **Maribel Sosa** | | | | | |

*Host vs Sponsor*

| | a discount dentist | a mattress warehouse | a bail bondsman | a psychic hotline | a taxidermist |
|---|---|---|---|---|---|
| **Rusty Lamarr** | | | | | |
| **Dustin Crowe** | | | | | |
| **Bea Okonjo** | | | | | |
| **Arlo Finch** | | | | | |
| **Maribel Sosa** | | | | | |

*Format vs Sponsor*

| | a discount dentist | a mattress warehouse | a bail bondsman | a psychic hotline | a taxidermist |
|---|---|---|---|---|---|
| **lost surf rock** | | | | | |
| **obscure jazz** | | | | | |
| **forgotten soul** | | | | | |
| **radio plays** | | | | | |
| **church organ recordings** | | | | | |

## Solution

| Running order | Host | Format | Sponsor |
|---|---|---|---|
| slot one | Rusty Lamarr | obscure jazz | a discount dentist |
| slot two | Maribel Sosa | church organ recordings | a mattress warehouse |
| slot three | Bea Okonjo | radio plays | a psychic hotline |
| slot four | Arlo Finch | forgotten soul | a taxidermist |
| slot five | Dustin Crowe | lost surf rock | a bail bondsman |

## How it falls out

1. [direct] from clue 12 sponsor:a discount dentist: ruled out position(s) 2
2. [direct] from clue 8 genre:church organ recordings: ruled out position(s) 1,3,4,5
3. [direct] from clue 4 host:Dustin Crowe: ruled out position(s) 2
4. [bijection] from clue 1 host:Bea Okonjo: ruled out position(s) 2
5. [bijection] from clue 1 sponsor:a taxidermist: ruled out position(s) 2
6. [direct] from clue 5 genre:radio plays: ruled out position(s) 2
7. [bijection] genre:lost surf rock: ruled out position(s) 2
8. [bijection] genre:obscure jazz: ruled out position(s) 2
9. [bijection] genre:forgotten soul: ruled out position(s) 2
10. [order] from clue 11 sponsor:a taxidermist: ruled out position(s) 1,5
11. [order] from clue 11 host:Rusty Lamarr: ruled out position(s) 4,5
12. [order] from clue 10 genre:obscure jazz: ruled out position(s) 5
13. [order] from clue 10 sponsor:a bail bondsman: ruled out position(s) 1
14. [order] from clue 9 host:Rusty Lamarr: ruled out position(s) 2,3
15. [order] from clue 6 sponsor:a psychic hotline: ruled out position(s) 1,2,4
16. [order] from clue 3 genre:forgotten soul: ruled out position(s) 1,3,5
17. [order] from clue 2 sponsor:a psychic hotline: ruled out position(s) 5
18. [order] from clue 2 host:Arlo Finch: ruled out position(s) 1,2,3,5
19. [bijection] genre:lost surf rock: ruled out position(s) 4
20. [bijection] genre:obscure jazz: ruled out position(s) 4
21. [bijection] genre:radio plays: ruled out position(s) 4
22. [bijection] host:Dustin Crowe: ruled out position(s) 1,4
23. [bijection] host:Bea Okonjo: ruled out position(s) 1,4
24. [bijection] host:Maribel Sosa: ruled out position(s) 1,4
25. [bijection] host:Maribel Sosa: ruled out position(s) 3,5
26. [bijection] sponsor:a discount dentist: ruled out position(s) 3
27. [bijection] sponsor:a mattress warehouse: ruled out position(s) 3
28. [bijection] sponsor:a bail bondsman: ruled out position(s) 3
29. [bijection] sponsor:a taxidermist: ruled out position(s) 3
30. [bijection] from clue 7 sponsor:a bail bondsman: ruled out position(s) 2
31. [direct] from clue 5 genre:radio plays: ruled out position(s) 1
32. [bijection] sponsor:a discount dentist: ruled out position(s) 4
33. [bijection] sponsor:a mattress warehouse: ruled out position(s) 4
34. [bijection] sponsor:a bail bondsman: ruled out position(s) 4
35. [bijection] sponsor:a mattress warehouse: ruled out position(s) 1,5
36. [bijection] from clue 7 genre:radio plays: ruled out position(s) 5
37. [direct] from clue 5 host:Bea Okonjo: ruled out position(s) 5
38. [bijection] genre:lost surf rock: ruled out position(s) 3
39. [bijection] genre:obscure jazz: ruled out position(s) 3
40. [bijection] genre:lost surf rock: ruled out position(s) 1
_... and 2 further steps._

---

<sub>seed `2026172773411` &middot; score 5.355 &middot; atoms 12 &middot; positives 2 &middot; solved by order</sub>
