# The Food Court Standoff

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `caced914c28a`

## Introduction

One food court, and a shared conviction that everybody else ordered wrong.
Five friends are involved. Determine each friend's total, stand and drink.
- **Friend**: Paloma, Colton, Hank, Reggie and Dmitri.
- **Total** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Stand**: Sub Stop, the Chicken Coop, Burger Barn, Taco Tower and Pizza Wheel.
- **Drink**: an iced tea, a chocolate shake, just water, a lemonade and a root beer.
Every friend has a different total, stand and drink, so within each category every item is used exactly once.

## Clues

1. The friend who drinks an iced tea is exactly one price step cheaper than $9, with no total in between.
2. The friend who eats at Burger Barn is exactly one price step cheaper than $11, with no total in between.
3. Colton and $7 are exactly one price step apart in total order, in one direction or the other.
4. At least one of the following holds, and possibly more than one: (a) The friend who drinks a lemonade spends $11. (b) The friend who drinks a root beer eats at Taco Tower.
5. The friend who drinks an iced tea falls somewhere between Dmitri and Reggie in total order.
6. The friend who drinks a chocolate shake falls somewhere between Colton and Reggie in total order.
7. At least one of the following holds, and possibly more than one: (a) The friend who drinks a chocolate shake is cheaper than the friend who eats at Pizza Wheel in total order. (b) The friend who drinks a root beer eats at Sub Stop.
8. The friend who drinks a root beer and the friend who eats at Burger Barn are exactly one price step apart in total order, in one direction or the other.
9. Hank and the friend who eats at Burger Barn are exactly one price step apart in total order, in one direction or the other.
10. The friend who drinks just water and the friend who eats at Sub Stop are exactly one price step apart in total order, in one direction or the other.

## Solving chart

*Total vs Friend*

| | Paloma | Colton | Hank | Reggie | Dmitri |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Total vs Stand*

| | Sub Stop | the Chicken Coop | Burger Barn | Taco Tower | Pizza Wheel |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Total vs Drink*

| | an iced tea | a chocolate shake | just water | a lemonade | a root beer |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Friend vs Stand*

| | Sub Stop | the Chicken Coop | Burger Barn | Taco Tower | Pizza Wheel |
|---|---|---|---|---|---|
| **Paloma** | | | | | |
| **Colton** | | | | | |
| **Hank** | | | | | |
| **Reggie** | | | | | |
| **Dmitri** | | | | | |

*Friend vs Drink*

| | an iced tea | a chocolate shake | just water | a lemonade | a root beer |
|---|---|---|---|---|---|
| **Paloma** | | | | | |
| **Colton** | | | | | |
| **Hank** | | | | | |
| **Reggie** | | | | | |
| **Dmitri** | | | | | |

*Stand vs Drink*

| | an iced tea | a chocolate shake | just water | a lemonade | a root beer |
|---|---|---|---|---|---|
| **Sub Stop** | | | | | |
| **the Chicken Coop** | | | | | |
| **Burger Barn** | | | | | |
| **Taco Tower** | | | | | |
| **Pizza Wheel** | | | | | |

## Solution

| Total | Friend | Stand | Drink |
|---|---|---|---|
| $3 | Reggie | the Chicken Coop | just water |
| $5 | Paloma | Sub Stop | a chocolate shake |
| $7 | Hank | Pizza Wheel | an iced tea |
| $9 | Colton | Burger Barn | a lemonade |
| $11 | Dmitri | Taco Tower | a root beer |

## How it falls out

1. [order] from clue 9 drink:a chocolate shake: ruled out position(s) 1,5
2. [order] from clue 6 stand:Burger Barn: ruled out position(s) 1,2,3,5
3. [order] from clue 10 drink:a root beer: ruled out position(s) 1,2,4
4. [order] from clue 5 friend:Colton: ruled out position(s) 1,3,5
5. [order] from clue 9 friend:Reggie: ruled out position(s) 3
6. [order] from clue 4 drink:an iced tea: ruled out position(s) 1,2,4,5
7. [order] from clue 3 friend:Dmitri: ruled out position(s) 3
8. [order] from clue 2 friend:Hank: ruled out position(s) 1,2,4
9. [bijection] drink:a chocolate shake: ruled out position(s) 3
10. [bijection] drink:just water: ruled out position(s) 3
11. [bijection] drink:a lemonade: ruled out position(s) 3
12. [bijection] drink:a root beer: ruled out position(s) 3
13. [bijection] stand:Sub Stop: ruled out position(s) 4
14. [bijection] stand:the Chicken Coop: ruled out position(s) 4
15. [bijection] stand:Taco Tower: ruled out position(s) 4
16. [bijection] stand:Pizza Wheel: ruled out position(s) 4
17. [order] from clue 8 drink:just water: ruled out position(s) 5
18. [order] from clue 9 friend:Reggie: ruled out position(s) 2,4
19. [bijection] drink:a lemonade: ruled out position(s) 5
20. [disjunction] from clue 1 stand:Taco Tower: ruled out position(s) 1,2,3
21. [bijection] stand:Sub Stop: ruled out position(s) 5
22. [bijection] stand:the Chicken Coop: ruled out position(s) 5
23. [bijection] stand:Pizza Wheel: ruled out position(s) 5
24. [disjunction] from clue 7 drink:a chocolate shake: ruled out position(s) 4
25. [disjunction] from clue 7 stand:Pizza Wheel: ruled out position(s) 1,2
26. [disjunction] from clue 7 stand:Sub Stop: ruled out position(s) 3
27. [order] from clue 8 drink:just water: ruled out position(s) 4
28. [order] from clue 9 friend:Colton: ruled out position(s) 2
29. [order] from clue 9 friend:Reggie: ruled out position(s) 5
30. [order] from clue 3 friend:Dmitri: ruled out position(s) 1,2
31. [bijection] drink:just water: ruled out position(s) 2
32. [bijection] drink:a lemonade: ruled out position(s) 2
33. [bijection] drink:a lemonade: ruled out position(s) 1
34. [bijection] friend:Paloma: ruled out position(s) 1,4
35. [bijection] friend:Dmitri: ruled out position(s) 4
36. [bijection] friend:Paloma: ruled out position(s) 3,5
37. [bijection] stand:the Chicken Coop: ruled out position(s) 3
38. [order] from clue 8 stand:Sub Stop: ruled out position(s) 1
39. [bijection] friend:Hank: ruled out position(s) 5
40. [bijection] stand:the Chicken Coop: ruled out position(s) 2

---

<sub>seed `2026172936766` &middot; score 9.7475 &middot; atoms 10 &middot; positives 0 &middot; solved by disjunction</sub>
