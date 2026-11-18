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

1. The crew who rows the Wet Hen finishes second.
2. The crew who is stroked by Thomasina is exactly one place better than fourth, with no placing in between.
3. The crew who rows the Obstinate is not stroked by Yusuf. The Customs crew falls somewhere between the crew who rows the Obstinate and the crew who rows the Wet Hen in placing order.
4. The crew who is stroked by Crispin is exactly one place better than the Almshouse crew, with no placing in between. The Creamery crew is not stroked by Crispin.
5. The Seminary crew does not row the Gilded Eel.

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

1. [direct] from clue 1 boat:the Wet Hen: ruled out position(s) 1,3,4
2. [bijection] boat:the Peregrine: ruled out position(s) 2
3. [bijection] boat:the Gilded Eel: ruled out position(s) 2
4. [bijection] boat:the Obstinate: ruled out position(s) 2
5. [order] from clue 7 crew:the Customs crew: ruled out position(s) 1,2,4
6. [order] from clue 7 boat:the Obstinate: ruled out position(s) 1,3
7. [order] from clue 6 stroke:Thomasina: ruled out position(s) 1,2,4
8. [order] from clue 5 stroke:Crispin: ruled out position(s) 4
9. [order] from clue 5 crew:the Almshouse crew: ruled out position(s) 1
10. [direct] from clue 2 stroke:Yusuf: ruled out position(s) 4
11. [bijection] boat:the Peregrine: ruled out position(s) 4
12. [bijection] boat:the Gilded Eel: ruled out position(s) 4
13. [bijection] crew:the Seminary crew: ruled out position(s) 3
14. [bijection] crew:the Creamery crew: ruled out position(s) 3
15. [bijection] crew:the Almshouse crew: ruled out position(s) 3
16. [bijection] stroke:Bartholomew: ruled out position(s) 3
17. [bijection] stroke:Crispin: ruled out position(s) 3
18. [bijection] stroke:Yusuf: ruled out position(s) 3
19. [bijection] stroke:Bartholomew: ruled out position(s) 1,2
20. [order] from clue 5 stroke:Crispin: ruled out position(s) 2
21. [order] from clue 5 crew:the Almshouse crew: ruled out position(s) 4
22. [direct] from clue 4 crew:the Creamery crew: ruled out position(s) 1
23. [bijection] crew:the Seminary crew: ruled out position(s) 2
24. [bijection] crew:the Creamery crew: ruled out position(s) 2
25. [bijection] crew:the Seminary crew: ruled out position(s) 4
26. [bijection] stroke:Yusuf: ruled out position(s) 1
27. [direct] from clue 3 boat:the Gilded Eel: ruled out position(s) 1
28. [bijection] boat:the Peregrine: ruled out position(s) 3

---

<sub>seed `2026172670464` &middot; score 5.13 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
