# The Mudflat Regatta

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `51590a7afa8a`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Five crews are involved. Determine each crew's placing, stroke and boat.
- **Crew**: the Creamery crew, the Brickworks crew, the Customs crew, the Seminary crew and the Tannery crew.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Stroke**: Yusuf, Ondine, Bartholomew, Crispin and Everard.
- **Boat**: the Gilded Eel, the Wet Hen, the Obstinate, the Peregrine and the Dauntless.
Every crew has a different placing, stroke and boat, so within each category every item is used exactly once.

## Clues

1. Second falls somewhere between the Creamery crew and the crew who is stroked by Crispin in placing order.
2. The crew who rows the Gilded Eel is better than fourth in placing order.
3. The Seminary crew is better than the crew who is stroked by Yusuf in placing order. The crew who is stroked by Yusuf is better than fourth in placing order.
4. Third and the crew who is stroked by Everard both sit at odd-numbered places or both at even-numbered places.
5. One of the crew who rows the Dauntless and fifth sits at an odd-numbered placing and the other at an even-numbered placing.
6. The crew who is stroked by Ondine is worse than fourth in placing order.
7. The Customs crew falls somewhere between fourth and the crew who is stroked by Everard in placing order.
8. The Tannery crew is better than the crew who rows the Obstinate in placing order.
9. The Seminary crew is exactly one place better than the crew who rows the Peregrine, with no placing in between.
10. At least one of the following holds, and possibly more than one: (a) The Creamery crew is stroked by Bartholomew. (b) One of the crew who rows the Gilded Eel and the Creamery crew sits at an odd-numbered placing and the other at an even-numbered placing.

## Solving chart

*Placing vs Crew*

| | the Creamery crew | the Brickworks crew | the Customs crew | the Seminary crew | the Tannery crew |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Stroke*

| | Yusuf | Ondine | Bartholomew | Crispin | Everard |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Boat*

| | the Gilded Eel | the Wet Hen | the Obstinate | the Peregrine | the Dauntless |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Crew vs Stroke*

| | Yusuf | Ondine | Bartholomew | Crispin | Everard |
|---|---|---|---|---|---|
| **the Creamery crew** | | | | | |
| **the Brickworks crew** | | | | | |
| **the Customs crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Tannery crew** | | | | | |

*Crew vs Boat*

| | the Gilded Eel | the Wet Hen | the Obstinate | the Peregrine | the Dauntless |
|---|---|---|---|---|---|
| **the Creamery crew** | | | | | |
| **the Brickworks crew** | | | | | |
| **the Customs crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Tannery crew** | | | | | |

*Stroke vs Boat*

| | the Gilded Eel | the Wet Hen | the Obstinate | the Peregrine | the Dauntless |
|---|---|---|---|---|---|
| **Yusuf** | | | | | |
| **Ondine** | | | | | |
| **Bartholomew** | | | | | |
| **Crispin** | | | | | |
| **Everard** | | | | | |

## Solution

| Placing | Crew | Stroke | Boat |
|---|---|---|---|
| first | the Creamery crew | Everard | the Wet Hen |
| second | the Seminary crew | Bartholomew | the Gilded Eel |
| third | the Customs crew | Yusuf | the Peregrine |
| fourth | the Tannery crew | Crispin | the Dauntless |
| fifth | the Brickworks crew | Ondine | the Obstinate |

## How it falls out

1. [order] from clue 11 crew:the Seminary crew: ruled out position(s) 5
2. [order] from clue 11 boat:the Peregrine: ruled out position(s) 1
3. [order] from clue 10 crew:the Tannery crew: ruled out position(s) 5
4. [order] from clue 10 boat:the Obstinate: ruled out position(s) 1
5. [order] from clue 9 boat:the Gilded Eel: ruled out position(s) 4,5
6. [order] from clue 8 boat:the Dauntless: ruled out position(s) 1,3,5
7. [order] from clue 7 crew:the Creamery crew: ruled out position(s) 2
8. [order] from clue 7 stroke:Crispin: ruled out position(s) 2
9. [order] from clue 6 stroke:Everard: ruled out position(s) 2,4
10. [order] from clue 5 stroke:Ondine: ruled out position(s) 1,2,3,4
11. [order] from clue 3 stroke:Yusuf: ruled out position(s) 1
12. [order] from clue 2 crew:the Customs crew: ruled out position(s) 1,4,5
13. [order] from clue 2 stroke:Everard: ruled out position(s) 3,5
14. [order] from clue 1 stroke:Yusuf: ruled out position(s) 4,5
15. [order] from clue 3 crew:the Seminary crew: ruled out position(s) 3,4
16. [order] from clue 11 boat:the Peregrine: ruled out position(s) 4,5
17. [bijection] stroke:Bartholomew: ruled out position(s) 1,5
18. [bijection] stroke:Crispin: ruled out position(s) 1,5
19. [order] from clue 7 crew:the Creamery crew: ruled out position(s) 3,4,5
20. [bijection] crew:the Brickworks crew: ruled out position(s) 1
21. [bijection] crew:the Seminary crew: ruled out position(s) 1
22. [bijection] crew:the Tannery crew: ruled out position(s) 1
23. [bijection] crew:the Brickworks crew: ruled out position(s) 2,3,4
24. [order] from clue 10 boat:the Obstinate: ruled out position(s) 2
25. [order] from clue 11 boat:the Peregrine: ruled out position(s) 2
26. [order] from clue 3 stroke:Yusuf: ruled out position(s) 2
27. [bijection] boat:the Gilded Eel: ruled out position(s) 3
28. [bijection] boat:the Wet Hen: ruled out position(s) 3
29. [bijection] boat:the Obstinate: ruled out position(s) 3
30. [bijection] crew:the Customs crew: ruled out position(s) 2
31. [bijection] crew:the Tannery crew: ruled out position(s) 2
32. [bijection] crew:the Tannery crew: ruled out position(s) 3
33. [bijection] stroke:Bartholomew: ruled out position(s) 3
34. [bijection] stroke:Crispin: ruled out position(s) 3
35. [bijection] stroke:Bartholomew: ruled out position(s) 4
36. [order] from clue 10 boat:the Obstinate: ruled out position(s) 4
37. [bijection] boat:the Wet Hen: ruled out position(s) 5
38. [disjunction] from clue 4 boat:the Gilded Eel: ruled out position(s) 1
39. [bijection] boat:the Wet Hen: ruled out position(s) 2
40. [bijection] boat:the Dauntless: ruled out position(s) 2
_... and 1 further steps._

---

<sub>seed `2026172868439` &middot; score 8.7392 &middot; atoms 11 &middot; positives 0 &middot; solved by disjunction</sub>
