# The Mudflat Regatta

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `971594c4e5d7`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Five crews are involved. Determine each crew's placing, boat and colours.
- **Crew**: the Gasworks crew, the Creamery crew, the Seminary crew, the Customs crew and the Brickworks crew.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Boat**: the Gilded Eel, the Peregrine, the Wet Hen, the Last Resort and the Obstinate.
- **Colours**: cherry and grey; mustard and black; scarlet; lilac and bronze; and navy with a white band.
Every crew has a different placing, boat and colours, so within each category every item is used exactly once.

## Clues

1. The Customs crew finishes fifth.
2. The crew who rows the Obstinate falls somewhere between first and fourth in placing order.
3. The crew who rows the Peregrine is worse than third in placing order.
4. The crew who rows the Gilded Eel does not wear lilac and bronze. The crew who rows the Gilded Eel and fourth are exactly one place apart in placing order, in one direction or the other.
5. The crew who wears mustard and black is exactly one place better than second, with no placing in between.
6. The Gasworks crew and fifth are exactly one place apart in placing order, in one direction or the other.
7. The Creamery crew does not row the Wet Hen.
8. At least one of the following holds, and possibly more than one: (a) The crew who wears cherry and grey and the Creamery crew are exactly one place apart in placing order, in one direction or the other. (b) The crew who wears scarlet and the Brickworks crew are exactly one place apart in placing order, in one direction or the other.
9. The crew who wears cherry and grey is better than the Brickworks crew in placing order.
10. The crew who rows the Last Resort and the crew who wears mustard and black are exactly three places apart in placing order.

## Solving chart

*Placing vs Crew*

| | the Gasworks crew | the Creamery crew | the Seminary crew | the Customs crew | the Brickworks crew |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Boat*

| | the Gilded Eel | the Peregrine | the Wet Hen | the Last Resort | the Obstinate |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Colours*

| | cherry and grey | mustard and black | scarlet | lilac and bronze | navy with a white band |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Crew vs Boat*

| | the Gilded Eel | the Peregrine | the Wet Hen | the Last Resort | the Obstinate |
|---|---|---|---|---|---|
| **the Gasworks crew** | | | | | |
| **the Creamery crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Customs crew** | | | | | |
| **the Brickworks crew** | | | | | |

*Crew vs Colours*

| | cherry and grey | mustard and black | scarlet | lilac and bronze | navy with a white band |
|---|---|---|---|---|---|
| **the Gasworks crew** | | | | | |
| **the Creamery crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Customs crew** | | | | | |
| **the Brickworks crew** | | | | | |

*Boat vs Colours*

| | cherry and grey | mustard and black | scarlet | lilac and bronze | navy with a white band |
|---|---|---|---|---|---|
| **the Gilded Eel** | | | | | |
| **the Peregrine** | | | | | |
| **the Wet Hen** | | | | | |
| **the Last Resort** | | | | | |
| **the Obstinate** | | | | | |

## Solution

| Placing | Crew | Boat | Colours |
|---|---|---|---|
| first | the Seminary crew | the Wet Hen | mustard and black |
| second | the Creamery crew | the Obstinate | cherry and grey |
| third | the Brickworks crew | the Gilded Eel | navy with a white band |
| fourth | the Gasworks crew | the Last Resort | scarlet |
| fifth | the Customs crew | the Peregrine | lilac and bronze |

## How it falls out

1. [direct] from clue 8 crew:the Customs crew: ruled out position(s) 1,2,3,4
2. [bijection] crew:the Gasworks crew: ruled out position(s) 5
3. [bijection] crew:the Creamery crew: ruled out position(s) 5
4. [bijection] crew:the Seminary crew: ruled out position(s) 5
5. [bijection] crew:the Brickworks crew: ruled out position(s) 5
6. [order] from clue 11 boat:the Gilded Eel: ruled out position(s) 1,2,4
7. [order] from clue 9 colours:cherry and grey: ruled out position(s) 4,5
8. [order] from clue 9 crew:the Brickworks crew: ruled out position(s) 1
9. [order] from clue 6 colours:mustard and black: ruled out position(s) 2,3,4,5
10. [order] from clue 5 crew:the Gasworks crew: ruled out position(s) 1,2,3
11. [order] from clue 4 boat:the Last Resort: ruled out position(s) 1,2,3,5
12. [order] from clue 3 boat:the Peregrine: ruled out position(s) 1,2,3
13. [order] from clue 1 boat:the Obstinate: ruled out position(s) 1,4,5
14. [bijection] boat:the Peregrine: ruled out position(s) 4
15. [bijection] boat:the Wet Hen: ruled out position(s) 4
16. [bijection] boat:the Wet Hen: ruled out position(s) 2,3,5
17. [bijection] colours:cherry and grey: ruled out position(s) 1
18. [bijection] colours:scarlet: ruled out position(s) 1
19. [bijection] colours:lilac and bronze: ruled out position(s) 1
20. [bijection] colours:navy with a white band: ruled out position(s) 1
21. [bijection] crew:the Creamery crew: ruled out position(s) 4
22. [bijection] crew:the Seminary crew: ruled out position(s) 4
23. [bijection] crew:the Brickworks crew: ruled out position(s) 4
24. [order] from clue 9 colours:cherry and grey: ruled out position(s) 3
25. [order] from clue 9 crew:the Brickworks crew: ruled out position(s) 2
26. [direct] from clue 10 crew:the Creamery crew: ruled out position(s) 1
27. [bijection] boat:the Gilded Eel: ruled out position(s) 5
28. [bijection] boat:the Obstinate: ruled out position(s) 3
29. [bijection] colours:scarlet: ruled out position(s) 2
30. [bijection] colours:lilac and bronze: ruled out position(s) 2
31. [bijection] colours:navy with a white band: ruled out position(s) 2
32. [bijection] crew:the Creamery crew: ruled out position(s) 3
33. [bijection] crew:the Seminary crew: ruled out position(s) 3
34. [bijection] crew:the Seminary crew: ruled out position(s) 2
35. [direct] from clue 7 colours:lilac and bronze: ruled out position(s) 3
36. [disjunction] from clue 2 colours:scarlet: ruled out position(s) 3,5
37. [bijection] colours:lilac and bronze: ruled out position(s) 4
38. [bijection] colours:navy with a white band: ruled out position(s) 4
39. [bijection] colours:navy with a white band: ruled out position(s) 5

---

<sub>seed `2026173136772` &middot; score 8.5792 &middot; atoms 11 &middot; positives 1 &middot; solved by disjunction</sub>
