# A Benchful of Clocks, and No Agreement

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `d64671372003`

## Introduction

Mr Halloran repairs clocks. Those on the bench are all insisting on a different hour.
Five clocks are involved. Determine each clock's shelf, owner and fault.
- **Clock**: a mantel clock under glass, a carriage clock, a station clock, a cuckoo clock and an anniversary clock.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Owner**: Miss Trevelyan, Father Brennan, Mr Dziedzic, Captain Mott and Ms Abernathy.
- **Fault**: a missing click spring, a snapped mainspring, a gummed-up pivot, a seized fusee and a bent pendulum rod.
Every clock has a different shelf, owner and fault, so within each category every item is used exactly once.

## Clues

1. The clock that belongs to Ms Abernathy sits on the fifth shelf. A station clock and the fifth shelf both sit at odd-numbered shelves or both at even-numbered shelves.
2. The fourth shelf falls somewhere between the clock that suffers from a missing click spring and the clock that suffers from a seized fusee in shelf order.
3. A carriage clock and the clock that suffers from a snapped mainspring are exactly three shelves apart in shelf order.
4. A station clock does not suffer from a bent pendulum rod. The clock that suffers from a missing click spring is exactly one shelf lower than a station clock, with no shelf in between.
5. A mantel clock under glass falls somewhere between the clock that suffers from a bent pendulum rod and the clock that belongs to Miss Trevelyan in shelf order.
6. An anniversary clock is lower than the clock that belongs to Mr Dziedzic in shelf order.
7. The clock that belongs to Captain Mott is exactly one shelf lower than the clock that suffers from a bent pendulum rod, with no shelf in between.
8. The clock that belongs to Mr Dziedzic is exactly one shelf lower than the clock that suffers from a gummed-up pivot, with no shelf in between.

## Solving chart

*Shelf vs Clock*

| | a mantel clock under glass | a carriage clock | a station clock | a cuckoo clock | an anniversary clock |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Owner*

| | Miss Trevelyan | Father Brennan | Mr Dziedzic | Captain Mott | Ms Abernathy |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Fault*

| | a missing click spring | a snapped mainspring | a gummed-up pivot | a seized fusee | a bent pendulum rod |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Clock vs Owner*

| | Miss Trevelyan | Father Brennan | Mr Dziedzic | Captain Mott | Ms Abernathy |
|---|---|---|---|---|---|
| **a mantel clock under glass** | | | | | |
| **a carriage clock** | | | | | |
| **a station clock** | | | | | |
| **a cuckoo clock** | | | | | |
| **an anniversary clock** | | | | | |

*Clock vs Fault*

| | a missing click spring | a snapped mainspring | a gummed-up pivot | a seized fusee | a bent pendulum rod |
|---|---|---|---|---|---|
| **a mantel clock under glass** | | | | | |
| **a carriage clock** | | | | | |
| **a station clock** | | | | | |
| **a cuckoo clock** | | | | | |
| **an anniversary clock** | | | | | |

*Owner vs Fault*

| | a missing click spring | a snapped mainspring | a gummed-up pivot | a seized fusee | a bent pendulum rod |
|---|---|---|---|---|---|
| **Miss Trevelyan** | | | | | |
| **Father Brennan** | | | | | |
| **Mr Dziedzic** | | | | | |
| **Captain Mott** | | | | | |
| **Ms Abernathy** | | | | | |

## Solution

| Shelf | Clock | Owner | Fault |
|---|---|---|---|
| the bottom shelf | an anniversary clock | Miss Trevelyan | a snapped mainspring |
| the second shelf | a mantel clock under glass | Mr Dziedzic | a missing click spring |
| the third shelf | a station clock | Captain Mott | a gummed-up pivot |
| the fourth shelf | a carriage clock | Father Brennan | a bent pendulum rod |
| the fifth shelf | a cuckoo clock | Ms Abernathy | a seized fusee |

## How it falls out

1. [direct] from clue 5 owner:Ms Abernathy: ruled out position(s) 1,2,3,4
2. [bijection] owner:Miss Trevelyan: ruled out position(s) 5
3. [bijection] owner:Father Brennan: ruled out position(s) 5
4. [bijection] owner:Mr Dziedzic: ruled out position(s) 5
5. [bijection] owner:Captain Mott: ruled out position(s) 5
6. [order] from clue 10 clock:a carriage clock: ruled out position(s) 3
7. [order] from clue 10 fault:a snapped mainspring: ruled out position(s) 3
8. [order] from clue 9 fault:a missing click spring: ruled out position(s) 5
9. [order] from clue 9 clock:a station clock: ruled out position(s) 1
10. [order] from clue 8 clock:an anniversary clock: ruled out position(s) 4,5
11. [order] from clue 8 owner:Mr Dziedzic: ruled out position(s) 1
12. [order] from clue 7 fault:a missing click spring: ruled out position(s) 4
13. [order] from clue 7 fault:a seized fusee: ruled out position(s) 1,2,3,4
14. [order] from clue 9 clock:a station clock: ruled out position(s) 5
15. [order] from clue 6 fault:a gummed-up pivot: ruled out position(s) 1,2
16. [order] from clue 3 fault:a bent pendulum rod: ruled out position(s) 1
17. [order] from clue 2 clock:a mantel clock under glass: ruled out position(s) 1,5
18. [order] from clue 1 clock:a station clock: ruled out position(s) 2,4
19. [order] from clue 9 fault:a missing click spring: ruled out position(s) 1,3
20. [direct] from clue 4 fault:a bent pendulum rod: ruled out position(s) 3
21. [order] from clue 3 owner:Captain Mott: ruled out position(s) 2
22. [bijection] clock:a mantel clock under glass: ruled out position(s) 3
23. [bijection] clock:a cuckoo clock: ruled out position(s) 3
24. [bijection] clock:an anniversary clock: ruled out position(s) 3
25. [bijection] fault:a snapped mainspring: ruled out position(s) 2,5
26. [bijection] fault:a gummed-up pivot: ruled out position(s) 5
27. [bijection] fault:a bent pendulum rod: ruled out position(s) 2,5
28. [bijection] fault:a snapped mainspring: ruled out position(s) 4
29. [bijection] fault:a gummed-up pivot: ruled out position(s) 4
30. [order] from clue 3 owner:Captain Mott: ruled out position(s) 1,4
31. [order] from clue 6 owner:Mr Dziedzic: ruled out position(s) 3,4
32. [order] from clue 10 clock:a carriage clock: ruled out position(s) 1,2,5
33. [order] from clue 8 clock:an anniversary clock: ruled out position(s) 2
34. [order] from clue 2 clock:a mantel clock under glass: ruled out position(s) 4
35. [order] from clue 2 owner:Miss Trevelyan: ruled out position(s) 2,3,4
36. [bijection] clock:a cuckoo clock: ruled out position(s) 1,2,4
37. [bijection] owner:Father Brennan: ruled out position(s) 1,2,3

---

<sub>seed `2026172725897` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
