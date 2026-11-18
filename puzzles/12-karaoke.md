# Tuesday Night at the Dented Bell

*The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; talent is not.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `6ea8bbdad1cf`

## Introduction

There are 4 turns. Each has exactly one slot and one item from every other category below, and within each category every item belongs to a different turn.
- **Running order** (listed in order): slot one, slot two, slot three and slot four.
- **Singer**: Deshawn, Caitriona, Mercy and Bogdan.
- **Song**: a maudlin folk song, a disco standard, a rap performed entirely from memory and a power ballad.
- **Drink**: a cider in a plastic cup, a double whisky, a pint of mild and tap water.
The slots above are listed in order, from slot one to slot four.

## Clues

1. A double whisky goes with a power ballad.
2. Caitriona does not go with slot three.
3. A double whisky does not go with slot four.
4. Deshawn's slot is immediately earlier than slot three, with no slot in between.
5. A rap performed entirely from memory's slot is earlier than a cider in a plastic cup's slot. A cider in a plastic cup's slot is earlier than a maudlin folk song's slot.
6. Mercy's slot is earlier than a disco standard's slot.
7. A pint of mild's slot is immediately earlier than a power ballad's slot, with no slot in between.

## Solving chart

*Running order vs Singer*

| | Deshawn | Caitriona | Mercy | Bogdan |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Running order vs Song*

| | a maudlin folk song | a disco standard | a rap performed entirely from memory | a power ballad |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Running order vs Drink*

| | a cider in a plastic cup | a double whisky | a pint of mild | tap water |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Singer vs Song*

| | a maudlin folk song | a disco standard | a rap performed entirely from memory | a power ballad |
|---|---|---|---|---|
| **Deshawn** | | | | |
| **Caitriona** | | | | |
| **Mercy** | | | | |
| **Bogdan** | | | | |

*Singer vs Drink*

| | a cider in a plastic cup | a double whisky | a pint of mild | tap water |
|---|---|---|---|---|
| **Deshawn** | | | | |
| **Caitriona** | | | | |
| **Mercy** | | | | |
| **Bogdan** | | | | |

*Song vs Drink*

| | a cider in a plastic cup | a double whisky | a pint of mild | tap water |
|---|---|---|---|---|
| **a maudlin folk song** | | | | |
| **a disco standard** | | | | |
| **a rap performed entirely from memory** | | | | |
| **a power ballad** | | | | |

## Solution

| Running order | Singer | Song | Drink |
|---|---|---|---|
| slot one | Mercy | a rap performed entirely from memory | a pint of mild |
| slot two | Deshawn | a power ballad | a double whisky |
| slot three | Bogdan | a disco standard | a cider in a plastic cup |
| slot four | Caitriona | a maudlin folk song | tap water |

## How it falls out

1. [direct] from clue 4 singer:Caitriona: ruled out position(s) 3
2. [direct] from clue 1 drink:a double whisky: ruled out position(s) 4
3. [direct] from clue 6 song:a power ballad: ruled out position(s) 4
4. [order] from clue 8 song:a rap performed entirely from memory: ruled out position(s) 4
5. [order] from clue 8 drink:a cider in a plastic cup: ruled out position(s) 1
6. [order] from clue 7 drink:a cider in a plastic cup: ruled out position(s) 4
7. [order] from clue 7 song:a maudlin folk song: ruled out position(s) 1,2
8. [order] from clue 8 song:a rap performed entirely from memory: ruled out position(s) 3
9. [order] from clue 5 drink:a pint of mild: ruled out position(s) 3,4
10. [order] from clue 5 song:a power ballad: ruled out position(s) 1
11. [order] from clue 3 singer:Mercy: ruled out position(s) 4
12. [order] from clue 3 song:a disco standard: ruled out position(s) 1
13. [order] from clue 2 singer:Deshawn: ruled out position(s) 1,3,4
14. [direct] from clue 6 drink:a double whisky: ruled out position(s) 1
15. [bijection] drink:tap water: ruled out position(s) 1,2,3
16. [bijection] singer:Caitriona: ruled out position(s) 2
17. [bijection] singer:Mercy: ruled out position(s) 2
18. [bijection] singer:Bogdan: ruled out position(s) 2
19. [bijection] song:a rap performed entirely from memory: ruled out position(s) 2
20. [bijection] drink:a pint of mild: ruled out position(s) 2
21. [order] from clue 5 song:a power ballad: ruled out position(s) 3
22. [direct] from clue 6 drink:a double whisky: ruled out position(s) 3
23. [bijection] drink:a cider in a plastic cup: ruled out position(s) 2
24. [bijection] song:a disco standard: ruled out position(s) 2
25. [order] from clue 7 song:a maudlin folk song: ruled out position(s) 3
26. [bijection] song:a disco standard: ruled out position(s) 4
27. [order] from clue 3 singer:Mercy: ruled out position(s) 3
28. [bijection] singer:Caitriona: ruled out position(s) 1
29. [bijection] singer:Bogdan: ruled out position(s) 1
30. [bijection] singer:Bogdan: ruled out position(s) 4

---

<sub>seed `2026172670464` &middot; score 5.13 &middot; atoms 8 &middot; positives 1 &middot; solved by order</sub>
