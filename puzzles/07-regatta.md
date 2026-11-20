# The Mudflat Regatta

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `fef8acc74c12`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Five crews are involved. Determine each crew's placing and boat.
- **Crew**: the Tannery crew, the Customs crew, the Gasworks crew, the Brickworks crew and the Seminary crew.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Boat**: the Obstinate, the Peregrine, the Gilded Eel, the Dauntless and the Wet Hen.
Every crew has a different placing and boat, so within each category every item is used exactly once.

## Clues

1. The crew who rows the Peregrine finishes first. The Tannery crew does not row the Peregrine.
2. The Customs crew rows the Obstinate.
3. The Seminary crew rows the Gilded Eel.
4. The crew who rows the Gilded Eel is worse than fourth in placing order.
5. The crew who rows the Obstinate is better than third in placing order.
6. The Gasworks crew and third are exactly one place apart in placing order, in one direction or the other. The Gasworks crew does not row the Wet Hen.

## Solving chart

*Placing vs Crew*

| | the Tannery crew | the Customs crew | the Gasworks crew | the Brickworks crew | the Seminary crew |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Boat*

| | the Obstinate | the Peregrine | the Gilded Eel | the Dauntless | the Wet Hen |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Crew vs Boat*

| | the Obstinate | the Peregrine | the Gilded Eel | the Dauntless | the Wet Hen |
|---|---|---|---|---|---|
| **the Tannery crew** | | | | | |
| **the Customs crew** | | | | | |
| **the Gasworks crew** | | | | | |
| **the Brickworks crew** | | | | | |
| **the Seminary crew** | | | | | |

## Solution

| Placing | Crew | Boat |
|---|---|---|
| first | the Brickworks crew | the Peregrine |
| second | the Customs crew | the Obstinate |
| third | the Tannery crew | the Wet Hen |
| fourth | the Gasworks crew | the Dauntless |
| fifth | the Seminary crew | the Gilded Eel |

## How it falls out

1. [direct] from clue 4 boat:the Peregrine: ruled out position(s) 2,3,4,5
2. [direct] from clue 1 crew:the Tannery crew: ruled out position(s) 1
3. [bijection] boat:the Obstinate: ruled out position(s) 1
4. [bijection] boat:the Gilded Eel: ruled out position(s) 1
5. [bijection] boat:the Dauntless: ruled out position(s) 1
6. [bijection] boat:the Wet Hen: ruled out position(s) 1
7. [direct] from clue 3 crew:the Seminary crew: ruled out position(s) 1
8. [direct] from clue 6 crew:the Customs crew: ruled out position(s) 1
9. [order] from clue 8 crew:the Gasworks crew: ruled out position(s) 1,3,5
10. [order] from clue 7 boat:the Obstinate: ruled out position(s) 3,4,5
11. [order] from clue 2 boat:the Gilded Eel: ruled out position(s) 2,3,4
12. [direct] from clue 6 crew:the Customs crew: ruled out position(s) 3,4,5
13. [direct] from clue 3 crew:the Seminary crew: ruled out position(s) 2,3,4
14. [bijection] boat:the Dauntless: ruled out position(s) 2,5
15. [bijection] boat:the Wet Hen: ruled out position(s) 2,5
16. [bijection] crew:the Tannery crew: ruled out position(s) 2,5
17. [bijection] crew:the Gasworks crew: ruled out position(s) 2
18. [bijection] crew:the Brickworks crew: ruled out position(s) 2,5
19. [bijection] crew:the Brickworks crew: ruled out position(s) 3,4
20. [direct] from clue 5 boat:the Wet Hen: ruled out position(s) 4
21. [bijection] boat:the Dauntless: ruled out position(s) 3
22. [bijection] crew:the Tannery crew: ruled out position(s) 4

---

<sub>seed `2026172830875` &middot; score 4.38 &middot; atoms 8 &middot; positives 3 &middot; solved by order</sub>
