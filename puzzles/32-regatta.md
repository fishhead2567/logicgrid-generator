# The Mudflat Regatta

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `6beff5f46fbb`

## Introduction

The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.
Five crews are involved. Determine each crew's placing, boat and colours.
- **Crew**: the Almshouse crew, the Creamery crew, the Tannery crew, the Seminary crew and the Gasworks crew.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Boat**: the Peregrine, the Gilded Eel, the Obstinate, the Mudlark and the Last Resort.
- **Colours**: bottle green; navy with a white band; cherry and grey; pink and cream; and lilac and bronze.
Every crew has a different placing, boat and colours, so within each category every item is used exactly once.

## Clues

1. The crew who rows the Obstinate and first are exactly three places apart in placing order.
2. At least one of the following holds, and possibly more than one: (a) The Almshouse crew rows the Gilded Eel. (b) The Creamery crew and fourth both sit at odd-numbered places or both at even-numbered places.
3. The following two do NOT both hold; either one alone may hold, and so may neither: (a) The Tannery crew does not finish fifth. (b) One of the crew who rows the Last Resort and the Creamery crew sits at an odd-numbered placing and the other at an even-numbered placing.
4. The crew who wears pink and cream is exactly one place better than fifth, with no placing in between.
5. The crew who rows the Peregrine and the Almshouse crew are exactly one place apart in placing order, in one direction or the other.
6. The crew who wears bottle green is better than the Seminary crew in placing order.
7. The crew who rows the Gilded Eel and the crew who wears cherry and grey are exactly one place apart in placing order, in one direction or the other.
8. The crew who wears pink and cream is better than the crew who rows the Peregrine in placing order.
9. The crew who rows the Last Resort and the crew who wears lilac and bronze are exactly four places apart in placing order.
10. The crew who rows the Last Resort is exactly one place better than the crew who wears cherry and grey, with no placing in between.

## Solving chart

*Placing vs Crew*

| | the Almshouse crew | the Creamery crew | the Tannery crew | the Seminary crew | the Gasworks crew |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Boat*

| | the Peregrine | the Gilded Eel | the Obstinate | the Mudlark | the Last Resort |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Colours*

| | bottle green | navy with a white band | cherry and grey | pink and cream | lilac and bronze |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Crew vs Boat*

| | the Peregrine | the Gilded Eel | the Obstinate | the Mudlark | the Last Resort |
|---|---|---|---|---|---|
| **the Almshouse crew** | | | | | |
| **the Creamery crew** | | | | | |
| **the Tannery crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Gasworks crew** | | | | | |

*Crew vs Colours*

| | bottle green | navy with a white band | cherry and grey | pink and cream | lilac and bronze |
|---|---|---|---|---|---|
| **the Almshouse crew** | | | | | |
| **the Creamery crew** | | | | | |
| **the Tannery crew** | | | | | |
| **the Seminary crew** | | | | | |
| **the Gasworks crew** | | | | | |

*Boat vs Colours*

| | bottle green | navy with a white band | cherry and grey | pink and cream | lilac and bronze |
|---|---|---|---|---|---|
| **the Peregrine** | | | | | |
| **the Gilded Eel** | | | | | |
| **the Obstinate** | | | | | |
| **the Mudlark** | | | | | |
| **the Last Resort** | | | | | |

## Solution

| Placing | Crew | Boat | Colours |
|---|---|---|---|
| first | the Gasworks crew | the Last Resort | bottle green |
| second | the Creamery crew | the Mudlark | cherry and grey |
| third | the Seminary crew | the Gilded Eel | navy with a white band |
| fourth | the Almshouse crew | the Obstinate | pink and cream |
| fifth | the Tannery crew | the Peregrine | lilac and bronze |

## How it falls out

1. [order] from clue 10 boat:the Obstinate: ruled out position(s) 1,2,3,5
2. [order] from clue 9 colours:pink and cream: ruled out position(s) 5
3. [order] from clue 9 boat:the Peregrine: ruled out position(s) 1
4. [order] from clue 7 colours:pink and cream: ruled out position(s) 1,2,3
5. [order] from clue 9 boat:the Peregrine: ruled out position(s) 2,3,4
6. [order] from clue 6 boat:the Last Resort: ruled out position(s) 5
7. [order] from clue 6 colours:cherry and grey: ruled out position(s) 1
8. [order] from clue 4 boat:the Last Resort: ruled out position(s) 2,3,4
9. [order] from clue 4 colours:lilac and bronze: ruled out position(s) 1,2,3,4
10. [order] from clue 6 colours:cherry and grey: ruled out position(s) 3,4,5
11. [order] from clue 8 boat:the Gilded Eel: ruled out position(s) 2,4,5
12. [order] from clue 3 crew:the Almshouse crew: ruled out position(s) 1,2,3,5
13. [order] from clue 2 colours:bottle green: ruled out position(s) 5
14. [order] from clue 2 crew:the Seminary crew: ruled out position(s) 1
15. [bijection] boat:the Gilded Eel: ruled out position(s) 1
16. [bijection] boat:the Mudlark: ruled out position(s) 1,4,5
17. [bijection] boat:the Mudlark: ruled out position(s) 3
18. [bijection] colours:bottle green: ruled out position(s) 2,4
19. [bijection] colours:navy with a white band: ruled out position(s) 2,4,5
20. [bijection] crew:the Creamery crew: ruled out position(s) 4
21. [bijection] crew:the Tannery crew: ruled out position(s) 4
22. [bijection] crew:the Seminary crew: ruled out position(s) 4
23. [bijection] crew:the Gasworks crew: ruled out position(s) 4
24. [disjunction] from clue 1 crew:the Creamery crew: ruled out position(s) 1,3,5
25. [disjunction] from clue 5 crew:the Tannery crew: ruled out position(s) 1,2,3
26. [bijection] crew:the Seminary crew: ruled out position(s) 2,5
27. [bijection] crew:the Gasworks crew: ruled out position(s) 2,5
28. [bijection] crew:the Gasworks crew: ruled out position(s) 3
29. [order] from clue 2 colours:bottle green: ruled out position(s) 3
30. [bijection] colours:navy with a white band: ruled out position(s) 1

---

<sub>seed `2026172828844` &middot; score 9.2622 &middot; atoms 10 &middot; positives 0 &middot; solved by disjunction</sub>
