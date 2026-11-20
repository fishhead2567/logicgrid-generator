# A Fortnight at the Little Vesper Theatre

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `2ed0b598015f`

## Introduction

The Little Vesper Theatre seats forty people and employs a company of puppeteers who will not be in the same room together.
Four puppeteers are involved. Determine each puppeteer's slot and accompaniment.
- **Puppeteer**: Stellan, Halima, Bowen and Mirabel.
- **Running order** (listed from earlier to later): slot one, slot two, slot three and slot four.
- **Accompaniment**: a hurdy-gurdy, a bowed psaltery, two kettle drums and a prepared piano.
Every puppeteer has a different slot and accompaniment, so within each category every item is used exactly once.

## Clues

1. The puppeteer who is accompanied by a bowed psaltery is later than slot one in slot order. Bowen performs in slot one.
2. Halima is accompanied by a hurdy-gurdy.
3. The puppeteer who is accompanied by a bowed psaltery does not perform in slot two.
4. The puppeteer who is accompanied by two kettle drums is exactly one slot earlier than slot four, with no slot in between.
5. Mirabel is earlier than slot four in slot order.

## Solving chart

*Running order vs Puppeteer*

| | Stellan | Halima | Bowen | Mirabel |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Running order vs Accompaniment*

| | a hurdy-gurdy | a bowed psaltery | two kettle drums | a prepared piano |
|---|---|---|---|---|
| **slot one** | | | | |
| **slot two** | | | | |
| **slot three** | | | | |
| **slot four** | | | | |

*Puppeteer vs Accompaniment*

| | a hurdy-gurdy | a bowed psaltery | two kettle drums | a prepared piano |
|---|---|---|---|---|
| **Stellan** | | | | |
| **Halima** | | | | |
| **Bowen** | | | | |
| **Mirabel** | | | | |

## Solution

| Running order | Puppeteer | Accompaniment |
|---|---|---|
| slot one | Bowen | a prepared piano |
| slot two | Halima | a hurdy-gurdy |
| slot three | Mirabel | two kettle drums |
| slot four | Stellan | a bowed psaltery |

## How it falls out

1. [direct] from clue 6 music:a bowed psaltery: ruled out position(s) 2
2. [direct] from clue 3 puppeteer:Bowen: ruled out position(s) 2,3,4
3. [bijection] puppeteer:Stellan: ruled out position(s) 1
4. [bijection] puppeteer:Halima: ruled out position(s) 1
5. [bijection] puppeteer:Mirabel: ruled out position(s) 1
6. [direct] from clue 2 music:a hurdy-gurdy: ruled out position(s) 1
7. [order] from clue 5 music:two kettle drums: ruled out position(s) 1,2,4
8. [order] from clue 4 puppeteer:Mirabel: ruled out position(s) 4
9. [order] from clue 1 music:a bowed psaltery: ruled out position(s) 1
10. [bijection] music:a hurdy-gurdy: ruled out position(s) 3
11. [bijection] music:a bowed psaltery: ruled out position(s) 3
12. [bijection] music:a prepared piano: ruled out position(s) 3
13. [bijection] music:a prepared piano: ruled out position(s) 2,4
14. [direct] from clue 2 puppeteer:Halima: ruled out position(s) 3
15. [bijection] music:a hurdy-gurdy: ruled out position(s) 4
16. [direct] from clue 2 puppeteer:Halima: ruled out position(s) 4
17. [bijection] puppeteer:Stellan: ruled out position(s) 2
18. [bijection] puppeteer:Mirabel: ruled out position(s) 2
19. [bijection] puppeteer:Stellan: ruled out position(s) 3

---

<sub>seed `2026172915040` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
