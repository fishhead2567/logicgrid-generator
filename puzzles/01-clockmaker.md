# A Benchful of Clocks, and No Agreement

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `07db40d70730`

## Introduction

Mr Halloran repairs clocks. Those on the bench are all insisting on a different hour.
Four clocks are involved. Determine each clock's shelf and owner.
- **Clock**: a carriage clock, a station clock, a mantel clock under glass and an anniversary clock.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf and the fourth shelf.
- **Owner**: Ms Abernathy, Miss Trevelyan, Father Brennan and Dr Vasquez.
Every clock has a different shelf and owner, so within each category every item is used exactly once.

## Clues

1. A mantel clock under glass sits on the fourth shelf.
2. The clock that belongs to Miss Trevelyan sits on the bottom shelf.
3. The clock that belongs to Dr Vasquez does not sit on the fourth shelf.
4. The second shelf is exactly one shelf lower than a carriage clock, with no shelf in between.
5. An anniversary clock and the clock that belongs to Father Brennan are exactly one shelf apart in shelf order, in one direction or the other.
6. An anniversary clock and the clock that belongs to Miss Trevelyan are exactly one shelf apart in shelf order, in one direction or the other.

## Solving chart

*Shelf vs Clock*

| | a carriage clock | a station clock | a mantel clock under glass | an anniversary clock |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Owner*

| | Ms Abernathy | Miss Trevelyan | Father Brennan | Dr Vasquez |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Clock vs Owner*

| | Ms Abernathy | Miss Trevelyan | Father Brennan | Dr Vasquez |
|---|---|---|---|---|
| **a carriage clock** | | | | |
| **a station clock** | | | | |
| **a mantel clock under glass** | | | | |
| **an anniversary clock** | | | | |

## Solution

| Shelf | Clock | Owner |
|---|---|---|
| the bottom shelf | a station clock | Miss Trevelyan |
| the second shelf | an anniversary clock | Dr Vasquez |
| the third shelf | a carriage clock | Father Brennan |
| the fourth shelf | a mantel clock under glass | Ms Abernathy |

## How it falls out

1. [direct] from clue 5 owner:Dr Vasquez: ruled out position(s) 4
2. [direct] from clue 4 clock:a mantel clock under glass: ruled out position(s) 1,2,3
3. [direct] from clue 2 owner:Miss Trevelyan: ruled out position(s) 2,3,4
4. [bijection] clock:a carriage clock: ruled out position(s) 4
5. [bijection] clock:a station clock: ruled out position(s) 4
6. [bijection] clock:an anniversary clock: ruled out position(s) 4
7. [bijection] owner:Ms Abernathy: ruled out position(s) 1
8. [bijection] owner:Father Brennan: ruled out position(s) 1
9. [bijection] owner:Dr Vasquez: ruled out position(s) 1
10. [order] from clue 3 clock:an anniversary clock: ruled out position(s) 1,3
11. [order] from clue 6 owner:Father Brennan: ruled out position(s) 2,4
12. [order] from clue 1 clock:a carriage clock: ruled out position(s) 1,2
13. [bijection] clock:a station clock: ruled out position(s) 2,3
14. [bijection] owner:Ms Abernathy: ruled out position(s) 3
15. [bijection] owner:Dr Vasquez: ruled out position(s) 3
16. [bijection] owner:Ms Abernathy: ruled out position(s) 2

---

<sub>seed `2026172783361` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
