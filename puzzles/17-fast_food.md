# The Food Court Standoff

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `a43c2dabee9a`

## Introduction

One food court, and a shared conviction that everybody else ordered wrong.
Four friends are involved. Determine each friend's total, stand and main.
- **Friend**: Paloma, Dmitri, Reggie and Colton.
- **Total** (listed from cheaper to dearer): $3, $5, $7 and $9.
- **Stand**: the Noodle Cart, Burger Barn, Taco Tower and the Fry Shack.
- **Main**: a foot-long sub, a personal pepperoni, three crunchy tacos and a chicken sandwich.
Every friend has a different total, stand and main, so within each category every item is used exactly once.

## Clues

1. The friend who orders a personal pepperoni spends $5. The friend who eats at Taco Tower does not spend $5.
2. Colton spends $3. $3 is exactly one price step cheaper than Dmitri, with no total in between.
3. The friend who orders a chicken sandwich eats at the Fry Shack.
4. The friend who orders a chicken sandwich is exactly one price step cheaper than the friend who eats at Burger Barn, with no total in between.
5. Reggie is exactly one price step cheaper than the friend who orders a foot-long sub, with no total in between. The friend who eats at Taco Tower is cheaper than Reggie in total order.

## Solving chart

*Total vs Friend*

| | Paloma | Dmitri | Reggie | Colton |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Total vs Stand*

| | the Noodle Cart | Burger Barn | Taco Tower | the Fry Shack |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Total vs Main*

| | a foot-long sub | a personal pepperoni | three crunchy tacos | a chicken sandwich |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Friend vs Stand*

| | the Noodle Cart | Burger Barn | Taco Tower | the Fry Shack |
|---|---|---|---|---|
| **Paloma** | | | | |
| **Dmitri** | | | | |
| **Reggie** | | | | |
| **Colton** | | | | |

*Friend vs Main*

| | a foot-long sub | a personal pepperoni | three crunchy tacos | a chicken sandwich |
|---|---|---|---|---|
| **Paloma** | | | | |
| **Dmitri** | | | | |
| **Reggie** | | | | |
| **Colton** | | | | |

*Stand vs Main*

| | a foot-long sub | a personal pepperoni | three crunchy tacos | a chicken sandwich |
|---|---|---|---|---|
| **the Noodle Cart** | | | | |
| **Burger Barn** | | | | |
| **Taco Tower** | | | | |
| **the Fry Shack** | | | | |

## Solution

| Total | Friend | Stand | Main |
|---|---|---|---|
| $3 | Colton | Taco Tower | three crunchy tacos |
| $5 | Dmitri | the Noodle Cart | a personal pepperoni |
| $7 | Reggie | the Fry Shack | a chicken sandwich |
| $9 | Paloma | Burger Barn | a foot-long sub |

## How it falls out

1. [direct] from clue 6 friend:Colton: ruled out position(s) 2,3,4
2. [direct] from clue 4 stand:Taco Tower: ruled out position(s) 2
3. [direct] from clue 3 main:a personal pepperoni: ruled out position(s) 1,3,4
4. [bijection] friend:Paloma: ruled out position(s) 1
5. [bijection] friend:Dmitri: ruled out position(s) 1
6. [bijection] friend:Reggie: ruled out position(s) 1
7. [bijection] main:a foot-long sub: ruled out position(s) 2
8. [bijection] main:three crunchy tacos: ruled out position(s) 2
9. [bijection] main:a chicken sandwich: ruled out position(s) 2
10. [direct] from clue 7 stand:the Fry Shack: ruled out position(s) 2
11. [order] from clue 8 friend:Dmitri: ruled out position(s) 3,4
12. [order] from clue 5 friend:Reggie: ruled out position(s) 4
13. [order] from clue 5 main:a foot-long sub: ruled out position(s) 1
14. [order] from clue 2 stand:Taco Tower: ruled out position(s) 3,4
15. [order] from clue 1 main:a chicken sandwich: ruled out position(s) 4
16. [order] from clue 1 stand:Burger Barn: ruled out position(s) 1,3
17. [direct] from clue 7 stand:the Fry Shack: ruled out position(s) 4
18. [bijection] friend:Paloma: ruled out position(s) 2
19. [bijection] friend:Reggie: ruled out position(s) 2
20. [bijection] friend:Paloma: ruled out position(s) 3
21. [bijection] stand:the Noodle Cart: ruled out position(s) 1
22. [bijection] stand:the Fry Shack: ruled out position(s) 1
23. [direct] from clue 7 main:a chicken sandwich: ruled out position(s) 1
24. [order] from clue 1 stand:Burger Barn: ruled out position(s) 2
25. [order] from clue 5 main:a foot-long sub: ruled out position(s) 3
26. [bijection] main:three crunchy tacos: ruled out position(s) 3,4
27. [bijection] stand:the Noodle Cart: ruled out position(s) 3,4

---

<sub>seed `2026172910065` &middot; score 4.73 &middot; atoms 8 &middot; positives 3 &middot; solved by order</sub>
