# Tuesday Night at the Rusty Anchor

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `b9cd504a1392`

## Introduction

The Rusty Anchor runs karaoke on Tuesdays. Attendance is loyal; talent is not.
Five singers are involved. Determine each singer's slot, drink and reception.
- **Singer**: Bogdan, Caitriona, Vikram, Mercy and Pernilla.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Drink**: a hard cider in a plastic cup; a double bourbon; a rum and coke; a pitcher of light beer; and tap water.
- **Reception**: one heckler, a singalong, the manager cutting the power, a request for an encore nobody wanted and scattered applause.
Every singer has a different slot, drink and reception, so within each category every item is used exactly once.

## Clues

1. The singer who gets the manager cutting the power falls somewhere between slot four and slot two in slot order.
2. Slot one is exactly one slot earlier than the singer who orders a double bourbon, with no slot in between.
3. Mercy and slot four are exactly one slot apart in slot order, in one direction or the other.
4. The singer who orders a pitcher of light beer is earlier than the singer who gets the manager cutting the power in slot order.
5. The singer who orders a rum and coke and the singer who gets one heckler are exactly one slot apart in slot order, in one direction or the other.
6. One of the singer who gets a request for an encore nobody wanted and Mercy sits at an odd-numbered slot and the other at an even-numbered slot.
7. The singer who orders a double bourbon and Vikram are exactly one slot apart in slot order, in one direction or the other.
8. Bogdan is exactly one slot earlier than the singer who orders a double bourbon, with no slot in between.
9. The singer who gets one heckler is earlier than Pernilla in slot order.
10. The singer who orders tap water and the singer who gets a singalong are exactly one slot apart in slot order, in one direction or the other.

## Solving chart

*Running order vs Singer*

| | Bogdan | Caitriona | Vikram | Mercy | Pernilla |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Drink*

| | a hard cider in a plastic cup | a double bourbon | a rum and coke | a pitcher of light beer | tap water |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Reception*

| | one heckler | a singalong | the manager cutting the power | a request for an encore nobody wanted | scattered applause |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Singer vs Drink*

| | a hard cider in a plastic cup | a double bourbon | a rum and coke | a pitcher of light beer | tap water |
|---|---|---|---|---|---|
| **Bogdan** | | | | | |
| **Caitriona** | | | | | |
| **Vikram** | | | | | |
| **Mercy** | | | | | |
| **Pernilla** | | | | | |

*Singer vs Reception*

| | one heckler | a singalong | the manager cutting the power | a request for an encore nobody wanted | scattered applause |
|---|---|---|---|---|---|
| **Bogdan** | | | | | |
| **Caitriona** | | | | | |
| **Vikram** | | | | | |
| **Mercy** | | | | | |
| **Pernilla** | | | | | |

*Drink vs Reception*

| | one heckler | a singalong | the manager cutting the power | a request for an encore nobody wanted | scattered applause |
|---|---|---|---|---|---|
| **a hard cider in a plastic cup** | | | | | |
| **a double bourbon** | | | | | |
| **a rum and coke** | | | | | |
| **a pitcher of light beer** | | | | | |
| **tap water** | | | | | |

## Solution

| Running order | Singer | Drink | Reception |
|---|---|---|---|
| slot one | Bogdan | a pitcher of light beer | scattered applause |
| slot two | Caitriona | a double bourbon | one heckler |
| slot three | Vikram | a rum and coke | the manager cutting the power |
| slot four | Pernilla | tap water | a request for an encore nobody wanted |
| slot five | Mercy | a hard cider in a plastic cup | a singalong |

## How it falls out

1. [order] from clue 6 singer:Mercy: ruled out position(s) 1,2,4
2. [order] from clue 8 reception:a request for an encore nobody wanted: ruled out position(s) 1,3,5
3. [order] from clue 5 drink:a pitcher of light beer: ruled out position(s) 5
4. [order] from clue 5 reception:the manager cutting the power: ruled out position(s) 1
5. [order] from clue 4 singer:Bogdan: ruled out position(s) 5
6. [order] from clue 4 drink:a double bourbon: ruled out position(s) 1
7. [order] from clue 3 drink:a double bourbon: ruled out position(s) 3,4,5
8. [order] from clue 9 singer:Vikram: ruled out position(s) 2,4,5
9. [order] from clue 4 singer:Bogdan: ruled out position(s) 2,3,4
10. [order] from clue 2 reception:one heckler: ruled out position(s) 5
11. [order] from clue 2 singer:Pernilla: ruled out position(s) 1
12. [order] from clue 1 reception:the manager cutting the power: ruled out position(s) 2,4,5
13. [order] from clue 5 drink:a pitcher of light beer: ruled out position(s) 3,4
14. [bijection] drink:a hard cider in a plastic cup: ruled out position(s) 2
15. [bijection] drink:a rum and coke: ruled out position(s) 2
16. [bijection] drink:a pitcher of light beer: ruled out position(s) 2
17. [bijection] drink:tap water: ruled out position(s) 2
18. [bijection] reception:one heckler: ruled out position(s) 3
19. [bijection] reception:a singalong: ruled out position(s) 3
20. [bijection] reception:scattered applause: ruled out position(s) 3
21. [bijection] singer:Caitriona: ruled out position(s) 1
22. [bijection] singer:Vikram: ruled out position(s) 1
23. [order] from clue 7 reception:a singalong: ruled out position(s) 1
24. [order] from clue 10 drink:a rum and coke: ruled out position(s) 4
25. [order] from clue 10 reception:one heckler: ruled out position(s) 1
26. [order] from clue 2 singer:Pernilla: ruled out position(s) 2
27. [bijection] drink:a hard cider in a plastic cup: ruled out position(s) 1
28. [bijection] drink:a rum and coke: ruled out position(s) 1
29. [bijection] drink:tap water: ruled out position(s) 1
30. [bijection] reception:scattered applause: ruled out position(s) 2,4,5
31. [bijection] singer:Caitriona: ruled out position(s) 3
32. [bijection] singer:Mercy: ruled out position(s) 3
33. [bijection] singer:Pernilla: ruled out position(s) 3
34. [bijection] singer:Caitriona: ruled out position(s) 4,5
35. [bijection] reception:a singalong: ruled out position(s) 2,4
36. [bijection] singer:Pernilla: ruled out position(s) 5
37. [order] from clue 2 reception:one heckler: ruled out position(s) 4
38. [order] from clue 10 drink:a rum and coke: ruled out position(s) 5
39. [order] from clue 7 drink:tap water: ruled out position(s) 3,5
40. [bijection] drink:a hard cider in a plastic cup: ruled out position(s) 3,4
_... and 1 further steps._

---

<sub>seed `2026173065501` &middot; score 5.675 &middot; atoms 10 &middot; positives 0 &middot; solved by order</sub>
