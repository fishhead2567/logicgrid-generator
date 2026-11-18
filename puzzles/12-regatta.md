# The Mudflat Regatta

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `6031b36e1684`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Four crews are involved. Determine each crew's placing, stroke and boat.
- **Crew**: the Customs crew, the Seminary crew, the Creamery crew and the Almshouse crew.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Stroke**: Bartholomew, Crispin, Thomasina and Yusuf.
- **Boat**: the Peregrine, the Wet Hen, the Gilded Eel and the Obstinate.
Every crew has a different placing, stroke and boat, so within each category every item is used exactly once.

## Clues

1. The crew who rows the Wet Hen is exactly one place better than third, with no placing in between.
2. The crew who is stroked by Thomasina does not finish second.
3. The crew who rows the Obstinate is not stroked by Yusuf. The Customs crew falls somewhere between the crew who rows the Obstinate and the crew who rows the Wet Hen in placing order.
4. The Creamery crew is not stroked by Crispin. The crew who is stroked by Crispin is exactly one place better than the Almshouse crew, with no placing in between.
5. The crew who is stroked by Thomasina falls somewhere between the crew who rows the Obstinate and the crew who rows the Peregrine in placing order.

## Solving chart

*Placing vs Crew*

| | the Customs crew | the Seminary crew | the Creamery crew | the Almshouse crew |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Stroke*

| | Bartholomew | Crispin | Thomasina | Yusuf |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Boat*

| | the Peregrine | the Wet Hen | the Gilded Eel | the Obstinate |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Crew vs Stroke*

| | Bartholomew | Crispin | Thomasina | Yusuf |
|---|---|---|---|---|
| **the Customs crew** | | | | |
| **the Seminary crew** | | | | |
| **the Creamery crew** | | | | |
| **the Almshouse crew** | | | | |

*Crew vs Boat*

| | the Peregrine | the Wet Hen | the Gilded Eel | the Obstinate |
|---|---|---|---|---|
| **the Customs crew** | | | | |
| **the Seminary crew** | | | | |
| **the Creamery crew** | | | | |
| **the Almshouse crew** | | | | |

*Stroke vs Boat*

| | the Peregrine | the Wet Hen | the Gilded Eel | the Obstinate |
|---|---|---|---|---|
| **Bartholomew** | | | | |
| **Crispin** | | | | |
| **Thomasina** | | | | |
| **Yusuf** | | | | |

## Solution

| Placing | Crew | Stroke | Boat |
|---|---|---|---|
| first | the Seminary crew | Crispin | the Peregrine |
| second | the Almshouse crew | Yusuf | the Wet Hen |
| third | the Customs crew | Thomasina | the Gilded Eel |
| fourth | the Creamery crew | Bartholomew | the Obstinate |

## How it falls out

1. [direct] from clue 3 stroke:Thomasina: ruled out position(s) 2
2. [order] from clue 7 crew:the Customs crew: ruled out position(s) 1,4
3. [order] from clue 6 stroke:Crispin: ruled out position(s) 4
4. [order] from clue 6 crew:the Almshouse crew: ruled out position(s) 1
5. [order] from clue 4 stroke:Thomasina: ruled out position(s) 1,4
6. [order] from clue 4 boat:the Obstinate: ruled out position(s) 3
7. [order] from clue 4 boat:the Peregrine: ruled out position(s) 3
8. [order] from clue 2 boat:the Wet Hen: ruled out position(s) 1,3,4
9. [order] from clue 7 crew:the Customs crew: ruled out position(s) 2
10. [order] from clue 7 boat:the Obstinate: ruled out position(s) 1,2
11. [order] from clue 4 boat:the Peregrine: ruled out position(s) 4
12. [direct] from clue 1 stroke:Yusuf: ruled out position(s) 4
13. [bijection] boat:the Peregrine: ruled out position(s) 2
14. [bijection] boat:the Gilded Eel: ruled out position(s) 2,4
15. [bijection] boat:the Gilded Eel: ruled out position(s) 1
16. [bijection] crew:the Seminary crew: ruled out position(s) 3
17. [bijection] crew:the Creamery crew: ruled out position(s) 3
18. [bijection] crew:the Almshouse crew: ruled out position(s) 3
19. [bijection] stroke:Bartholomew: ruled out position(s) 3
20. [bijection] stroke:Crispin: ruled out position(s) 3
21. [bijection] stroke:Yusuf: ruled out position(s) 3
22. [bijection] stroke:Bartholomew: ruled out position(s) 1,2
23. [order] from clue 6 stroke:Crispin: ruled out position(s) 2
24. [order] from clue 6 crew:the Almshouse crew: ruled out position(s) 4
25. [direct] from clue 5 crew:the Creamery crew: ruled out position(s) 1
26. [bijection] crew:the Seminary crew: ruled out position(s) 2
27. [bijection] crew:the Creamery crew: ruled out position(s) 2
28. [bijection] crew:the Seminary crew: ruled out position(s) 4
29. [bijection] stroke:Yusuf: ruled out position(s) 1

---

<sub>seed `2026172670464` &middot; score 5.33 &middot; atoms 7 &middot; positives 0 &middot; solved by order</sub>
