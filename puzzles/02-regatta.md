# The Mudflat Regatta

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 4 &nbsp;&nbsp; **id** `4e6bca5074dc`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Four crews are involved. Determine each crew's placing and boat.
- **Crew**: the Tannery crew, the Brickworks crew, the Customs crew and the Almshouse crew.
- **Placing** (listed from better to worse): first, second, third and fourth.
- **Boat**: the Gilded Eel, the Last Resort, the Dauntless and the Obstinate.
Every crew has a different placing and boat, so within each category every item is used exactly once.

## Clues

1. The Brickworks crew finishes third. The Brickworks crew rows the Obstinate.
2. The crew who rows the Last Resort is better than fourth in placing order.
3. The Customs crew is better than the crew who rows the Last Resort in placing order.
4. The crew who rows the Dauntless is exactly one place better than the Almshouse crew, with no placing in between.

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

1. [direct] from clue 4 crew:the Brickworks crew: ruled out position(s) 1,2,4
2. [direct] from clue 2 boat:the Obstinate: ruled out position(s) 1,2,4
3. [bijection] boat:the Gilded Eel: ruled out position(s) 3
4. [bijection] boat:the Last Resort: ruled out position(s) 3
5. [bijection] boat:the Dauntless: ruled out position(s) 3
6. [bijection] crew:the Tannery crew: ruled out position(s) 3
7. [bijection] crew:the Customs crew: ruled out position(s) 3
8. [bijection] crew:the Almshouse crew: ruled out position(s) 3
9. [order] from clue 5 crew:the Customs crew: ruled out position(s) 4
10. [order] from clue 5 boat:the Last Resort: ruled out position(s) 1
11. [order] from clue 3 boat:the Dauntless: ruled out position(s) 2,4
12. [order] from clue 3 crew:the Almshouse crew: ruled out position(s) 1,4
13. [order] from clue 1 boat:the Last Resort: ruled out position(s) 4
14. [order] from clue 5 crew:the Customs crew: ruled out position(s) 2
15. [bijection] boat:the Gilded Eel: ruled out position(s) 1,2
16. [bijection] crew:the Tannery crew: ruled out position(s) 1,2

---

<sub>seed `2026172591274` &middot; score 4.27 &middot; atoms 5 &middot; positives 2 &middot; solved by order</sub>
