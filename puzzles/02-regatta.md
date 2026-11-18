# The Mudflat Regatta

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 4 &nbsp;&nbsp; **id** `4e6bca5074dc`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Four crews are involved. Determine each crew's placing and boat.
- **Crew**: the Tannery crew, the Brickworks crew, the Customs crew and the Almshouse crew.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Boat**: the Gilded Eel, the Last Resort, the Dauntless and the Obstinate.
Every crew has a different placing and boat, so within each category every item is used exactly once.

## Clues

1. The Customs crew finishes first.
2. The Almshouse crew rows the Last Resort.
3. The Tannery crew rows the Gilded Eel. The crew who rows the Last Resort is better than the Tannery crew in placing order.
4. Second is exactly one place better than the crew who rows the Obstinate, with no placing in between.

## Solving chart

*Placing vs Crew*

| | the Tannery crew | the Brickworks crew | the Customs crew | the Almshouse crew |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Boat*

| | the Gilded Eel | the Last Resort | the Dauntless | the Obstinate |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Crew vs Boat*

| | the Gilded Eel | the Last Resort | the Dauntless | the Obstinate |
|---|---|---|---|---|
| **the Tannery crew** | | | | |
| **the Brickworks crew** | | | | |
| **the Customs crew** | | | | |
| **the Almshouse crew** | | | | |

## Solution

| Placing | Crew | Boat |
|---|---|---|
| first | the Customs crew | the Dauntless |
| second | the Almshouse crew | the Last Resort |
| third | the Brickworks crew | the Obstinate |
| fourth | the Tannery crew | the Gilded Eel |

## How it falls out

1. [direct] from clue 1 crew:the Customs crew: ruled out position(s) 2,3,4
2. [bijection] crew:the Tannery crew: ruled out position(s) 1
3. [bijection] crew:the Brickworks crew: ruled out position(s) 1
4. [bijection] crew:the Almshouse crew: ruled out position(s) 1
5. [direct] from clue 5 boat:the Last Resort: ruled out position(s) 1
6. [direct] from clue 3 boat:the Gilded Eel: ruled out position(s) 1
7. [order] from clue 4 boat:the Obstinate: ruled out position(s) 1,2,4
8. [order] from clue 2 boat:the Last Resort: ruled out position(s) 4
9. [order] from clue 2 crew:the Tannery crew: ruled out position(s) 2
10. [direct] from clue 5 crew:the Almshouse crew: ruled out position(s) 4
11. [direct] from clue 3 boat:the Gilded Eel: ruled out position(s) 2
12. [bijection] boat:the Gilded Eel: ruled out position(s) 3
13. [bijection] boat:the Last Resort: ruled out position(s) 3
14. [bijection] boat:the Dauntless: ruled out position(s) 3
15. [bijection] boat:the Dauntless: ruled out position(s) 2,4
16. [direct] from clue 5 crew:the Almshouse crew: ruled out position(s) 3
17. [direct] from clue 3 crew:the Tannery crew: ruled out position(s) 3
18. [bijection] crew:the Brickworks crew: ruled out position(s) 2,4

---

<sub>seed `2026172591274` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
