# A Benchful of Clocks, and No Agreement

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `36e5510439ef`

## Introduction

Mr Halloran repairs clocks. Those on the bench are all insisting on a different hour.
Four clocks are involved. Determine each clock's shelf, owner and fault.
- **Clock**: a carriage clock, a ship's chronometer, a cuckoo clock and a mantel clock under glass.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf and the fourth shelf.
- **Owner**: Dr Vasquez, Mr Dziedzic, Miss Trevelyan and Captain Mott.
- **Fault**: a cracked suspension spring, a snapped mainspring, a gummed-up pivot and a bent pendulum rod.
Every clock has a different shelf, owner and fault, so within each category every item is used exactly once.

## Clues

1. A mantel clock under glass sits on the bottom shelf. A ship's chronometer falls somewhere between the bottom shelf and the third shelf in shelf order.
2. The clock that suffers from a snapped mainspring belongs to Captain Mott.
3. The clock that suffers from a gummed-up pivot is exactly one shelf lower than the third shelf, with no shelf in between.
4. The clock that suffers from a gummed-up pivot does not belong to Miss Trevelyan.
5. A cuckoo clock does not belong to Captain Mott. A cuckoo clock is exactly one shelf lower than the clock that belongs to Mr Dziedzic, with no shelf in between.
6. The clock that belongs to Miss Trevelyan is lower than the clock that suffers from a cracked suspension spring in shelf order.

## Solving chart

*Shelf vs Clock*

| | a carriage clock | a ship's chronometer | a cuckoo clock | a mantel clock under glass |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Owner*

| | Dr Vasquez | Mr Dziedzic | Miss Trevelyan | Captain Mott |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Fault*

| | a cracked suspension spring | a snapped mainspring | a gummed-up pivot | a bent pendulum rod |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Clock vs Owner*

| | Dr Vasquez | Mr Dziedzic | Miss Trevelyan | Captain Mott |
|---|---|---|---|---|
| **a carriage clock** | | | | |
| **a ship's chronometer** | | | | |
| **a cuckoo clock** | | | | |
| **a mantel clock under glass** | | | | |

*Clock vs Fault*

| | a cracked suspension spring | a snapped mainspring | a gummed-up pivot | a bent pendulum rod |
|---|---|---|---|---|
| **a carriage clock** | | | | |
| **a ship's chronometer** | | | | |
| **a cuckoo clock** | | | | |
| **a mantel clock under glass** | | | | |

*Owner vs Fault*

| | a cracked suspension spring | a snapped mainspring | a gummed-up pivot | a bent pendulum rod |
|---|---|---|---|---|
| **Dr Vasquez** | | | | |
| **Mr Dziedzic** | | | | |
| **Miss Trevelyan** | | | | |
| **Captain Mott** | | | | |

## Solution

| Shelf | Clock | Owner | Fault |
|---|---|---|---|
| the bottom shelf | a mantel clock under glass | Captain Mott | a snapped mainspring |
| the second shelf | a ship's chronometer | Dr Vasquez | a gummed-up pivot |
| the third shelf | a cuckoo clock | Miss Trevelyan | a bent pendulum rod |
| the fourth shelf | a carriage clock | Mr Dziedzic | a cracked suspension spring |

## How it falls out

1. [direct] from clue 3 clock:a mantel clock under glass: ruled out position(s) 2,3,4
2. [bijection] clock:a carriage clock: ruled out position(s) 1
3. [bijection] clock:a ship's chronometer: ruled out position(s) 1
4. [bijection] clock:a cuckoo clock: ruled out position(s) 1
5. [order] from clue 7 clock:a ship's chronometer: ruled out position(s) 3,4
6. [order] from clue 6 owner:Miss Trevelyan: ruled out position(s) 4
7. [order] from clue 6 fault:a cracked suspension spring: ruled out position(s) 1
8. [order] from clue 5 clock:a cuckoo clock: ruled out position(s) 4
9. [order] from clue 5 owner:Mr Dziedzic: ruled out position(s) 1,2
10. [order] from clue 1 fault:a gummed-up pivot: ruled out position(s) 1,3,4
11. [direct] from clue 4 owner:Miss Trevelyan: ruled out position(s) 2
12. [bijection] clock:a carriage clock: ruled out position(s) 2
13. [bijection] clock:a cuckoo clock: ruled out position(s) 2
14. [bijection] clock:a carriage clock: ruled out position(s) 3
15. [bijection] fault:a cracked suspension spring: ruled out position(s) 2
16. [bijection] fault:a snapped mainspring: ruled out position(s) 2
17. [bijection] fault:a bent pendulum rod: ruled out position(s) 2
18. [direct] from clue 2 owner:Captain Mott: ruled out position(s) 2
19. [direct] from clue 8 owner:Captain Mott: ruled out position(s) 3
20. [direct] from clue 2 fault:a snapped mainspring: ruled out position(s) 3
21. [order] from clue 5 owner:Mr Dziedzic: ruled out position(s) 3
22. [bijection] owner:Dr Vasquez: ruled out position(s) 4
23. [bijection] owner:Captain Mott: ruled out position(s) 4
24. [bijection] owner:Dr Vasquez: ruled out position(s) 1,3
25. [direct] from clue 2 fault:a snapped mainspring: ruled out position(s) 4
26. [bijection] fault:a bent pendulum rod: ruled out position(s) 1
27. [bijection] owner:Miss Trevelyan: ruled out position(s) 1
28. [order] from clue 6 fault:a cracked suspension spring: ruled out position(s) 3
29. [bijection] fault:a bent pendulum rod: ruled out position(s) 4

---

<sub>seed `2026172654626` &middot; score 4.93 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
