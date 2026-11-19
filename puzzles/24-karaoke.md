# Tuesday Night at the Dented Bell

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `f93ca7baec7d`

## Introduction

The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; talent is not.
Five singers are involved. Determine each singer's slot, drink and reception.
- **Singer**: Deshawn, Caitriona, Pernilla, Vikram and Bogdan.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Drink**: a rum and coke; a lime and soda; a double whisky; tap water; and a glass of the house red.
- **Reception**: a singalong, polite silence, a standing ovation, scattered applause and a request for an encore nobody wanted.
Every singer has a different slot, drink and reception, so within each category every item is used exactly once.

## Clues

1. Pernilla is earlier than slot three in slot order. The singer who gets a request for an encore nobody wanted sings in slot three.
2. Deshawn and slot five are exactly one slot apart in slot order, in one direction or the other.
3. The singer who orders a glass of the house red and slot five are exactly four slots apart in slot order.
4. The singer who gets polite silence falls somewhere between Bogdan and Caitriona in slot order.
5. The singer who orders a rum and coke falls somewhere between the singer who gets a singalong and the singer who gets scattered applause in slot order.
6. Bogdan is exactly one slot earlier than the singer who orders a double whisky, with no slot in between.
7. The singer who orders a lime and soda is earlier than the singer who gets a request for an encore nobody wanted in slot order.
8. The singer who gets a singalong is exactly one slot earlier than the singer who orders a double whisky, with no slot in between.

## Solving chart

*Running order vs Singer*

| | Deshawn | Caitriona | Pernilla | Vikram | Bogdan |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Drink*

| | a rum and coke | a lime and soda | a double whisky | tap water | a glass of the house red |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Reception*

| | a singalong | polite silence | a standing ovation | scattered applause | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Singer vs Drink*

| | a rum and coke | a lime and soda | a double whisky | tap water | a glass of the house red |
|---|---|---|---|---|---|
| **Deshawn** | | | | | |
| **Caitriona** | | | | | |
| **Pernilla** | | | | | |
| **Vikram** | | | | | |
| **Bogdan** | | | | | |

*Singer vs Reception*

| | a singalong | polite silence | a standing ovation | scattered applause | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **Deshawn** | | | | | |
| **Caitriona** | | | | | |
| **Pernilla** | | | | | |
| **Vikram** | | | | | |
| **Bogdan** | | | | | |

*Drink vs Reception*

| | a singalong | polite silence | a standing ovation | scattered applause | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **a rum and coke** | | | | | |
| **a lime and soda** | | | | | |
| **a double whisky** | | | | | |
| **tap water** | | | | | |
| **a glass of the house red** | | | | | |

## Solution

| Running order | Singer | Drink | Reception |
|---|---|---|---|
| slot one | Pernilla | a glass of the house red | a standing ovation |
| slot two | Bogdan | a lime and soda | a singalong |
| slot three | Vikram | a double whisky | a request for an encore nobody wanted |
| slot four | Deshawn | a rum and coke | polite silence |
| slot five | Caitriona | tap water | scattered applause |

## How it falls out

1. [direct] from clue 5 reception:a request for an encore nobody wanted: ruled out position(s) 1,2,4,5
2. [bijection] reception:a singalong: ruled out position(s) 3
3. [bijection] reception:polite silence: ruled out position(s) 3
4. [bijection] reception:a standing ovation: ruled out position(s) 3
5. [bijection] reception:scattered applause: ruled out position(s) 3
6. [order] from clue 9 singer:Pernilla: ruled out position(s) 3,4,5
7. [order] from clue 8 drink:a glass of the house red: ruled out position(s) 2,3,4,5
8. [order] from clue 7 reception:polite silence: ruled out position(s) 1,5
9. [order] from clue 6 drink:a lime and soda: ruled out position(s) 3,4,5
10. [order] from clue 4 singer:Deshawn: ruled out position(s) 1,2,3,5
11. [order] from clue 3 drink:a rum and coke: ruled out position(s) 1,5
12. [order] from clue 2 singer:Bogdan: ruled out position(s) 5
13. [order] from clue 2 drink:a double whisky: ruled out position(s) 1
14. [order] from clue 7 singer:Caitriona: ruled out position(s) 2
15. [order] from clue 1 reception:a singalong: ruled out position(s) 5
16. [order] from clue 1 drink:a double whisky: ruled out position(s) 4
17. [order] from clue 2 singer:Bogdan: ruled out position(s) 3
18. [bijection] drink:a lime and soda: ruled out position(s) 1
19. [bijection] drink:tap water: ruled out position(s) 1
20. [bijection] singer:Caitriona: ruled out position(s) 4
21. [bijection] singer:Vikram: ruled out position(s) 4
22. [bijection] singer:Bogdan: ruled out position(s) 4
23. [order] from clue 2 drink:a double whisky: ruled out position(s) 5
24. [order] from clue 1 reception:a singalong: ruled out position(s) 4
25. [order] from clue 3 reception:scattered applause: ruled out position(s) 1,2
26. [order] from clue 7 singer:Caitriona: ruled out position(s) 1
27. [bijection] drink:a rum and coke: ruled out position(s) 2
28. [bijection] drink:a double whisky: ruled out position(s) 2
29. [bijection] drink:tap water: ruled out position(s) 2
30. [bijection] drink:tap water: ruled out position(s) 3,4
31. [order] from clue 2 singer:Bogdan: ruled out position(s) 1
32. [order] from clue 7 reception:polite silence: ruled out position(s) 2
33. [order] from clue 7 singer:Caitriona: ruled out position(s) 3
34. [order] from clue 1 reception:a singalong: ruled out position(s) 1
35. [bijection] drink:a rum and coke: ruled out position(s) 3
36. [bijection] reception:a standing ovation: ruled out position(s) 2,4
37. [bijection] reception:scattered applause: ruled out position(s) 4
38. [bijection] reception:a standing ovation: ruled out position(s) 5
39. [bijection] singer:Pernilla: ruled out position(s) 2
40. [bijection] singer:Vikram: ruled out position(s) 2,5
_... and 1 further steps._

---

<sub>seed `2026172865495` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
