# The Mudflat Regatta

*The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.*

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `04c3bbd982d4`

## Introduction

There are 5 entries. Each has exactly one placing and one item from every other category below, and within each category every item belongs to a different entry.
- **Placing** (listed in order): first, second, third, fourth and fifth.
- **Crew**: the Brickworks crew, the Seminary crew, the Gasworks crew, the Creamery crew and the Customs crew.
- **Boat**: the Mudlark, the Wet Hen, the Last Resort, the Dauntless and the Obstinate.
- **Colours**: cherry and grey, mustard and black, navy with a white band, bottle green and lilac and bronze.
The places above are listed in order, from first to fifth.

## Clues

1. The Last Resort and second are next to each other in placing order, in one order or the other. The Dauntless goes with second. Second falls somewhere between navy with a white band and the Creamery crew in placing order.
2. The Wet Hen falls somewhere between mustard and black and fifth in placing order. Navy with a white band's placing is better than fifth.
3. At least one of the following holds, and possibly more than one: (a) Lilac and bronze and fifth are next to each other in placing order, in one order or the other. (b) The Brickworks crew and fifth are next to each other in placing order, in one order or the other.
4. The Customs crew and fourth are next to each other in placing order, in one order or the other.
5. Mustard and black, the Gasworks crew and first are three different entries. The Last Resort does not go with the Gasworks crew. The Last Resort does not go with the Customs crew.
6. Bottle green's placing is better than the Last Resort's placing.
7. The Seminary crew's placing is immediately better than the Mudlark's placing, with no placing in between.

## Solving chart

*Placing vs Crew*

| | the Brickworks crew | the Seminary crew | the Gasworks crew | the Creamery crew | the Customs crew |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Boat*

| | the Mudlark | the Wet Hen | the Last Resort | the Dauntless | the Obstinate |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Colours*

| | cherry and grey | mustard and black | navy with a white band | bottle green | lilac and bronze |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Crew vs Boat*

| | the Mudlark | the Wet Hen | the Last Resort | the Dauntless | the Obstinate |
|---|---|---|---|---|---|
| **the Brickworks crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Gasworks crew** | | | | | |
| **the Creamery crew** | | | | | |
| **the Customs crew** | | | | | |

*Crew vs Colours*

| | cherry and grey | mustard and black | navy with a white band | bottle green | lilac and bronze |
|---|---|---|---|---|---|
| **the Brickworks crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Gasworks crew** | | | | | |
| **the Creamery crew** | | | | | |
| **the Customs crew** | | | | | |

*Boat vs Colours*

| | cherry and grey | mustard and black | navy with a white band | bottle green | lilac and bronze |
|---|---|---|---|---|---|
| **the Mudlark** | | | | | |
| **the Wet Hen** | | | | | |
| **the Last Resort** | | | | | |
| **the Dauntless** | | | | | |
| **the Obstinate** | | | | | |

## Solution

| Placing | Crew | Boat | Colours |
|---|---|---|---|
| first | the Brickworks crew | the Obstinate | navy with a white band |
| second | the Gasworks crew | the Dauntless | bottle green |
| third | the Creamery crew | the Last Resort | mustard and black |
| fourth | the Seminary crew | the Wet Hen | lilac and bronze |
| fifth | the Customs crew | the Mudlark | cherry and grey |

## How it falls out

1. [direct] from clue 11 boat:the Dauntless: ruled out position(s) 1,3,4,5
2. [bijection] from clue 7 colours:mustard and black: ruled out position(s) 1
3. [bijection] from clue 7 crew:the Gasworks crew: ruled out position(s) 1
4. [bijection] boat:the Mudlark: ruled out position(s) 2
5. [bijection] boat:the Wet Hen: ruled out position(s) 2
6. [bijection] boat:the Last Resort: ruled out position(s) 2
7. [bijection] boat:the Obstinate: ruled out position(s) 2
8. [order] from clue 12 crew:the Customs crew: ruled out position(s) 1,2,4
9. [order] from clue 9 colours:bottle green: ruled out position(s) 5
10. [order] from clue 9 boat:the Last Resort: ruled out position(s) 1
11. [order] from clue 8 crew:the Seminary crew: ruled out position(s) 1,5
12. [order] from clue 8 boat:the Mudlark: ruled out position(s) 1
13. [order] from clue 5 boat:the Wet Hen: ruled out position(s) 1,5
14. [order] from clue 5 colours:mustard and black: ruled out position(s) 4,5
15. [order] from clue 4 boat:the Last Resort: ruled out position(s) 4,5
16. [order] from clue 9 colours:bottle green: ruled out position(s) 3,4
17. [order] from clue 3 colours:navy with a white band: ruled out position(s) 2
18. [order] from clue 3 crew:the Creamery crew: ruled out position(s) 2
19. [order] from clue 1 colours:navy with a white band: ruled out position(s) 5
20. [direct] from clue 10 crew:the Customs crew: ruled out position(s) 3
21. [direct] from clue 6 crew:the Gasworks crew: ruled out position(s) 3
22. [bijection] boat:the Mudlark: ruled out position(s) 3
23. [bijection] boat:the Wet Hen: ruled out position(s) 3
24. [bijection] boat:the Obstinate: ruled out position(s) 3
25. [bijection] boat:the Obstinate: ruled out position(s) 4,5
26. [bijection] crew:the Brickworks crew: ruled out position(s) 5
27. [bijection] crew:the Gasworks crew: ruled out position(s) 5
28. [bijection] crew:the Creamery crew: ruled out position(s) 5
29. [order] from clue 8 crew:the Seminary crew: ruled out position(s) 2
30. [bijection] boat:the Mudlark: ruled out position(s) 4
31. [order] from clue 8 crew:the Seminary crew: ruled out position(s) 3
32. [bijection] crew:the Brickworks crew: ruled out position(s) 4
33. [bijection] crew:the Gasworks crew: ruled out position(s) 4
34. [bijection] crew:the Creamery crew: ruled out position(s) 4
35. [bijection] from clue 7 colours:mustard and black: ruled out position(s) 2
36. [bijection] colours:cherry and grey: ruled out position(s) 3
37. [bijection] colours:navy with a white band: ruled out position(s) 3
38. [bijection] colours:lilac and bronze: ruled out position(s) 3
39. [bijection] crew:the Brickworks crew: ruled out position(s) 2
40. [disjunction] from clue 2 colours:lilac and bronze: ruled out position(s) 1,2,5
_... and 6 further steps._

---

<sub>seed `2026173012763` &middot; score 8.5792 &middot; atoms 12 &middot; positives 1 &middot; solved by disjunction</sub>
