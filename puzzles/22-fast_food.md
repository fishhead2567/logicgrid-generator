# The Food Court Standoff

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `7a4e51aa64aa`

## Introduction

One food court, and a shared conviction that everybody else ordered wrong.
Five friends are involved. Determine each friend's total, main and drink.
- **Friend**: Hank, Dmitri, Noor, Aaliyah and Paloma.
- **Total** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Main**: a bean burrito, a chicken sandwich, a personal pepperoni, a double cheeseburger and three crunchy tacos.
- **Drink**: a blue slushie, a root beer, a lemonade, an orange soda and a chocolate shake.
Every friend has a different total, main and drink, so within each category every item is used exactly once.

## Clues

1. The friend who drinks a lemonade and $9 are exactly one price step apart in total order, in one direction or the other. Aaliyah falls somewhere between $3 and $9 in total order.
2. Dmitri and $9 are exactly one price step apart in total order, in one direction or the other.
3. The friend who orders three crunchy tacos and $3 are exactly one price step apart in total order, in one direction or the other.
4. The friend who drinks an orange soda is cheaper than Noor in total order.
5. Hank is exactly one price step cheaper than the friend who drinks a blue slushie, with no total in between.
6. The friend who orders a chicken sandwich is exactly one price step cheaper than the friend who drinks an orange soda, with no total in between.
7. Paloma and the friend who orders a bean burrito are exactly one price step apart in total order, in one direction or the other.
8. The friend who orders a personal pepperoni falls somewhere between the friend who drinks a blue slushie and the friend who drinks a chocolate shake in total order.

## Solving chart

*Total vs Friend*

| | Hank | Dmitri | Noor | Aaliyah | Paloma |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Total vs Main*

| | a bean burrito | a chicken sandwich | a personal pepperoni | a double cheeseburger | three crunchy tacos |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Total vs Drink*

| | a blue slushie | a root beer | a lemonade | an orange soda | a chocolate shake |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Friend vs Main*

| | a bean burrito | a chicken sandwich | a personal pepperoni | a double cheeseburger | three crunchy tacos |
|---|---|---|---|---|---|
| **Hank** | | | | | |
| **Dmitri** | | | | | |
| **Noor** | | | | | |
| **Aaliyah** | | | | | |
| **Paloma** | | | | | |

*Friend vs Drink*

| | a blue slushie | a root beer | a lemonade | an orange soda | a chocolate shake |
|---|---|---|---|---|---|
| **Hank** | | | | | |
| **Dmitri** | | | | | |
| **Noor** | | | | | |
| **Aaliyah** | | | | | |
| **Paloma** | | | | | |

*Main vs Drink*

| | a blue slushie | a root beer | a lemonade | an orange soda | a chocolate shake |
|---|---|---|---|---|---|
| **a bean burrito** | | | | | |
| **a chicken sandwich** | | | | | |
| **a personal pepperoni** | | | | | |
| **a double cheeseburger** | | | | | |
| **three crunchy tacos** | | | | | |

## Solution

| Total | Friend | Main | Drink |
|---|---|---|---|
| $3 | Hank | a double cheeseburger | a root beer |
| $5 | Aaliyah | three crunchy tacos | a blue slushie |
| $7 | Dmitri | a chicken sandwich | a lemonade |
| $9 | Paloma | a personal pepperoni | an orange soda |
| $11 | Noor | a bean burrito | a chocolate shake |

## How it falls out

1. [order] from clue 9 friend:Dmitri: ruled out position(s) 1,2,4
2. [order] from clue 8 main:a chicken sandwich: ruled out position(s) 5
3. [order] from clue 8 drink:an orange soda: ruled out position(s) 1
4. [order] from clue 7 friend:Hank: ruled out position(s) 5
5. [order] from clue 7 drink:a blue slushie: ruled out position(s) 1
6. [order] from clue 6 drink:a lemonade: ruled out position(s) 1,2,4
7. [order] from clue 5 main:a personal pepperoni: ruled out position(s) 1,5
8. [order] from clue 4 friend:Aaliyah: ruled out position(s) 1,4,5
9. [order] from clue 2 main:three crunchy tacos: ruled out position(s) 1,3,4,5
10. [order] from clue 1 drink:an orange soda: ruled out position(s) 5
11. [order] from clue 1 friend:Noor: ruled out position(s) 1,2
12. [order] from clue 8 main:a chicken sandwich: ruled out position(s) 4
13. [bijection] main:a bean burrito: ruled out position(s) 2
14. [bijection] main:a chicken sandwich: ruled out position(s) 2
15. [bijection] main:a personal pepperoni: ruled out position(s) 2
16. [bijection] main:a double cheeseburger: ruled out position(s) 2
17. [order] from clue 8 drink:an orange soda: ruled out position(s) 3
18. [order] from clue 3 friend:Paloma: ruled out position(s) 1
19. [bijection] friend:Hank: ruled out position(s) 2,3,4
20. [order] from clue 7 drink:a blue slushie: ruled out position(s) 3,4,5
21. [order] from clue 5 drink:a chocolate shake: ruled out position(s) 1,2,3
22. [bijection] drink:a root beer: ruled out position(s) 2
23. [bijection] drink:an orange soda: ruled out position(s) 2
24. [bijection] drink:a root beer: ruled out position(s) 3,4,5
25. [order] from clue 8 main:a chicken sandwich: ruled out position(s) 1
26. [order] from clue 1 friend:Noor: ruled out position(s) 3,4
27. [bijection] drink:a chocolate shake: ruled out position(s) 4
28. [bijection] drink:a lemonade: ruled out position(s) 5
29. [bijection] friend:Dmitri: ruled out position(s) 5
30. [bijection] friend:Paloma: ruled out position(s) 5
31. [bijection] friend:Paloma: ruled out position(s) 2,3
32. [bijection] main:a bean burrito: ruled out position(s) 3
33. [bijection] main:a personal pepperoni: ruled out position(s) 3
34. [bijection] main:a double cheeseburger: ruled out position(s) 3
35. [order] from clue 3 main:a bean burrito: ruled out position(s) 1,4
36. [bijection] friend:Aaliyah: ruled out position(s) 3
37. [bijection] main:a double cheeseburger: ruled out position(s) 4,5

---

<sub>seed `2026173049663` &middot; score 5.675 &middot; atoms 9 &middot; positives 0 &middot; solved by order</sub>
