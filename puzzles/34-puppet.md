# A Fortnight at the Little Vesper Theatre

*The Little Vesper Theatre seats forty people and employs a company of puppeteers who will not be in the same room together.*

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `1f743b265280`

## Introduction

There are 5 performances. Each has exactly one slot and one item from every other category below, and within each category every item belongs to a different performance.
- **Running order** (listed in order): slot one, slot two, slot three, slot four and slot five.
- **Puppeteer**: Quentin, Halima, Stellan, Josefa and Mirabel.
- **Play**: Hollowmas, The Glass Tide, The Clockwork Orchard, Winterling and Six Spoons.
- **Accompaniment**: a bowed psaltery, a hurdy-gurdy, a pump organ, a glass harmonica and two kettle drums.
The slots above are listed in order, from slot one to slot five.

## Clues

1. The Glass Tide falls somewhere between Halima and Josefa in slot order. Halima falls somewhere between Hollowmas and slot four in slot order. Slot four is earlier than Stellan's slot.
2. Quentin's slot is immediately earlier than slot four, with no slot in between.
3. At least one of the following holds, and possibly more than one: (a) A hurdy-gurdy and Josefa are next to each other in slot order, in one order or the other. (b) Slot three is immediately earlier than a bowed psaltery's slot, with no slot in between.
4. A glass harmonica's slot is immediately earlier than slot two, with no slot in between.
5. A pump organ's slot is immediately earlier than Winterling's slot, with no slot in between.
6. One of Six Spoons and Halima sits at an odd-numbered slot and the other at an even-numbered slot. A hurdy-gurdy, Six Spoons and Mirabel are three different performances.

## Solving chart

*Running order vs Puppeteer*

| | Quentin | Halima | Stellan | Josefa | Mirabel |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Play*

| | Hollowmas | The Glass Tide | The Clockwork Orchard | Winterling | Six Spoons |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Accompaniment*

| | a bowed psaltery | a hurdy-gurdy | a pump organ | a glass harmonica | two kettle drums |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Puppeteer vs Play*

| | Hollowmas | The Glass Tide | The Clockwork Orchard | Winterling | Six Spoons |
|---|---|---|---|---|---|
| **Quentin** | | | | | |
| **Halima** | | | | | |
| **Stellan** | | | | | |
| **Josefa** | | | | | |
| **Mirabel** | | | | | |

*Puppeteer vs Accompaniment*

| | a bowed psaltery | a hurdy-gurdy | a pump organ | a glass harmonica | two kettle drums |
|---|---|---|---|---|---|
| **Quentin** | | | | | |
| **Halima** | | | | | |
| **Stellan** | | | | | |
| **Josefa** | | | | | |
| **Mirabel** | | | | | |

*Play vs Accompaniment*

| | a bowed psaltery | a hurdy-gurdy | a pump organ | a glass harmonica | two kettle drums |
|---|---|---|---|---|---|
| **Hollowmas** | | | | | |
| **The Glass Tide** | | | | | |
| **The Clockwork Orchard** | | | | | |
| **Winterling** | | | | | |
| **Six Spoons** | | | | | |

## Solution

| Running order | Puppeteer | Play | Accompaniment |
|---|---|---|---|
| slot one | Mirabel | Hollowmas | a glass harmonica |
| slot two | Halima | The Clockwork Orchard | a hurdy-gurdy |
| slot three | Quentin | The Glass Tide | a pump organ |
| slot four | Josefa | Winterling | a bowed psaltery |
| slot five | Stellan | Six Spoons | two kettle drums |

## How it falls out

1. [order] from clue 8 puppeteer:Stellan: ruled out position(s) 1,2,3,4
2. [order] from clue 7 puppeteer:Quentin: ruled out position(s) 1,2,4,5
3. [order] from clue 6 play:The Glass Tide: ruled out position(s) 1,5
4. [order] from clue 4 puppeteer:Halima: ruled out position(s) 1,4,5
5. [order] from clue 4 play:Hollowmas: ruled out position(s) 3,4,5
6. [order] from clue 6 puppeteer:Josefa: ruled out position(s) 2,3
7. [order] from clue 3 music:a glass harmonica: ruled out position(s) 2,3,4,5
8. [order] from clue 1 music:a pump organ: ruled out position(s) 5
9. [order] from clue 1 play:Winterling: ruled out position(s) 1
10. [bijection] music:a bowed psaltery: ruled out position(s) 1
11. [bijection] music:a hurdy-gurdy: ruled out position(s) 1
12. [bijection] music:a pump organ: ruled out position(s) 1
13. [bijection] music:two kettle drums: ruled out position(s) 1
14. [bijection] puppeteer:Halima: ruled out position(s) 3
15. [bijection] puppeteer:Josefa: ruled out position(s) 5
16. [bijection] puppeteer:Mirabel: ruled out position(s) 3,5
17. [order] from clue 9 play:Six Spoons: ruled out position(s) 2,4
18. [order] from clue 6 play:The Glass Tide: ruled out position(s) 2,4
19. [order] from clue 6 puppeteer:Josefa: ruled out position(s) 1
20. [order] from clue 4 play:Hollowmas: ruled out position(s) 2
21. [order] from clue 1 play:Winterling: ruled out position(s) 2
22. [bijection] play:The Clockwork Orchard: ruled out position(s) 1,3
23. [bijection] play:Winterling: ruled out position(s) 3
24. [bijection] play:Six Spoons: ruled out position(s) 1,3
25. [bijection] play:The Clockwork Orchard: ruled out position(s) 4,5
26. [bijection] puppeteer:Mirabel: ruled out position(s) 2,4
27. [bijection] from clue 5 music:a hurdy-gurdy: ruled out position(s) 5
28. [order] from clue 1 music:a pump organ: ruled out position(s) 2
29. [bijection] play:Winterling: ruled out position(s) 5
30. [order] from clue 1 music:a pump organ: ruled out position(s) 4
31. [bijection] music:a bowed psaltery: ruled out position(s) 3
32. [bijection] music:a hurdy-gurdy: ruled out position(s) 3
33. [bijection] music:two kettle drums: ruled out position(s) 3
34. [disjunction] from clue 2 music:a hurdy-gurdy: ruled out position(s) 4
35. [disjunction] from clue 2 music:a bowed psaltery: ruled out position(s) 2,5
36. [bijection] music:two kettle drums: ruled out position(s) 2,4

---

<sub>seed `2026172844682` &middot; score 9.1244 &middot; atoms 9 &middot; positives 0 &middot; solved by disjunction</sub>
