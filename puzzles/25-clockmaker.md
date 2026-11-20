# A Benchful of Clocks, and No Agreement

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `6d3e215e8024`

## Introduction

Mr Halloran repairs clocks. Those on the bench are all insisting on a different hour.
Five clocks are involved. Determine each clock's shelf, owner, fault and chime.
- **Clock**: a ship's chronometer, a carriage clock, a longcase clock, a cuckoo clock and an anniversary clock.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Owner**: Mr Dziedzic, Dr Vasquez, Father Brennan, Ms Trevino and Mrs Oyelaran.
- **Fault**: a bent pendulum rod, a snapped mainspring, a cracked suspension spring, a gummed-up pivot and a worn escape wheel.
- **Chime**: Westminster; a single strike; no chime at all; a ship's bell; and a bell and gong.
Every clock has a different shelf, owner, fault and chime, so within each category every item is used exactly once.

## Clues

1. The clock that suffers from a bent pendulum rod sits on the third shelf. The clock that suffers from a snapped mainspring is lower than the third shelf in shelf order.
2. The clock that sounds no chime at all sits on the second shelf.
3. The clock that belongs to Dr Vasquez and the fourth shelf are exactly one shelf apart in shelf order, in one direction or the other.
4. A cuckoo clock is exactly one shelf lower than the third shelf, with no shelf in between.
5. The clock that sounds a ship's bell falls somewhere between the clock that suffers from a gummed-up pivot and the fourth shelf in shelf order.
6. The clock that sounds a single strike is exactly one shelf lower than the clock that belongs to Mr Dziedzic, with no shelf in between.
7. The clock that sounds Westminster and the clock that suffers from a worn escape wheel are exactly four shelves apart in shelf order.
8. The clock that suffers from a snapped mainspring and the clock that belongs to Ms Trevino are exactly two shelves apart in shelf order.
9. The clock that suffers from a snapped mainspring falls somewhere between an anniversary clock and the clock that belongs to Mr Dziedzic in shelf order.
10. A carriage clock is lower than the clock that sounds a single strike in shelf order.
11. A longcase clock and the clock that belongs to Father Brennan are exactly four shelves apart in shelf order.

## Solving chart

*Shelf vs Clock*

| | a ship's chronometer | a carriage clock | a longcase clock | a cuckoo clock | an anniversary clock |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Owner*

| | Mr Dziedzic | Dr Vasquez | Father Brennan | Ms Trevino | Mrs Oyelaran |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Fault*

| | a bent pendulum rod | a snapped mainspring | a cracked suspension spring | a gummed-up pivot | a worn escape wheel |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Chime*

| | Westminster | a single strike | no chime at all | a ship's bell | a bell and gong |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Clock vs Owner*

| | Mr Dziedzic | Dr Vasquez | Father Brennan | Ms Trevino | Mrs Oyelaran |
|---|---|---|---|---|---|
| **a ship's chronometer** | | | | | |
| **a carriage clock** | | | | | |
| **a longcase clock** | | | | | |
| **a cuckoo clock** | | | | | |
| **an anniversary clock** | | | | | |

*Clock vs Fault*

| | a bent pendulum rod | a snapped mainspring | a cracked suspension spring | a gummed-up pivot | a worn escape wheel |
|---|---|---|---|---|---|
| **a ship's chronometer** | | | | | |
| **a carriage clock** | | | | | |
| **a longcase clock** | | | | | |
| **a cuckoo clock** | | | | | |
| **an anniversary clock** | | | | | |

*Clock vs Chime*

| | Westminster | a single strike | no chime at all | a ship's bell | a bell and gong |
|---|---|---|---|---|---|
| **a ship's chronometer** | | | | | |
| **a carriage clock** | | | | | |
| **a longcase clock** | | | | | |
| **a cuckoo clock** | | | | | |
| **an anniversary clock** | | | | | |

*Owner vs Fault*

| | a bent pendulum rod | a snapped mainspring | a cracked suspension spring | a gummed-up pivot | a worn escape wheel |
|---|---|---|---|---|---|
| **Mr Dziedzic** | | | | | |
| **Dr Vasquez** | | | | | |
| **Father Brennan** | | | | | |
| **Ms Trevino** | | | | | |
| **Mrs Oyelaran** | | | | | |

*Owner vs Chime*

| | Westminster | a single strike | no chime at all | a ship's bell | a bell and gong |
|---|---|---|---|---|---|
| **Mr Dziedzic** | | | | | |
| **Dr Vasquez** | | | | | |
| **Father Brennan** | | | | | |
| **Ms Trevino** | | | | | |
| **Mrs Oyelaran** | | | | | |

*Fault vs Chime*

| | Westminster | a single strike | no chime at all | a ship's bell | a bell and gong |
|---|---|---|---|---|---|
| **a bent pendulum rod** | | | | | |
| **a snapped mainspring** | | | | | |
| **a cracked suspension spring** | | | | | |
| **a gummed-up pivot** | | | | | |
| **a worn escape wheel** | | | | | |

## Solution

| Shelf | Clock | Owner | Fault | Chime |
|---|---|---|---|---|
| the bottom shelf | an anniversary clock | Father Brennan | a gummed-up pivot | Westminster |
| the second shelf | a cuckoo clock | Mrs Oyelaran | a snapped mainspring | no chime at all |
| the third shelf | a carriage clock | Dr Vasquez | a bent pendulum rod | a ship's bell |
| the fourth shelf | a ship's chronometer | Ms Trevino | a cracked suspension spring | a single strike |
| the fifth shelf | a longcase clock | Mr Dziedzic | a worn escape wheel | a bell and gong |

## How it falls out

1. [direct] from clue 2 chime:no chime at all: ruled out position(s) 1,3,4,5
2. [direct] from clue 1 fault:a bent pendulum rod: ruled out position(s) 1,2,4,5
3. [bijection] chime:Westminster: ruled out position(s) 2
4. [bijection] chime:a single strike: ruled out position(s) 2
5. [bijection] chime:a ship's bell: ruled out position(s) 2
6. [bijection] chime:a bell and gong: ruled out position(s) 2
7. [bijection] fault:a snapped mainspring: ruled out position(s) 3
8. [bijection] fault:a cracked suspension spring: ruled out position(s) 3
9. [bijection] fault:a gummed-up pivot: ruled out position(s) 3
10. [bijection] fault:a worn escape wheel: ruled out position(s) 3
11. [order] from clue 12 chime:Westminster: ruled out position(s) 3,4
12. [order] from clue 12 fault:a worn escape wheel: ruled out position(s) 2,4
13. [order] from clue 11 chime:a single strike: ruled out position(s) 5
14. [order] from clue 11 owner:Mr Dziedzic: ruled out position(s) 1,3
15. [order] from clue 10 clock:a carriage clock: ruled out position(s) 4,5
16. [order] from clue 10 chime:a single strike: ruled out position(s) 1
17. [order] from clue 11 owner:Mr Dziedzic: ruled out position(s) 2
18. [order] from clue 9 owner:Dr Vasquez: ruled out position(s) 1,2,4
19. [order] from clue 8 chime:a ship's bell: ruled out position(s) 1,4,5
20. [order] from clue 8 fault:a gummed-up pivot: ruled out position(s) 4,5
21. [order] from clue 7 clock:a longcase clock: ruled out position(s) 2,3,4
22. [order] from clue 7 owner:Father Brennan: ruled out position(s) 2,3,4
23. [order] from clue 6 owner:Ms Trevino: ruled out position(s) 1,5
24. [order] from clue 5 fault:a snapped mainspring: ruled out position(s) 4,5
25. [order] from clue 6 owner:Ms Trevino: ruled out position(s) 2
26. [order] from clue 4 fault:a snapped mainspring: ruled out position(s) 1
27. [order] from clue 4 clock:an anniversary clock: ruled out position(s) 2,3,4,5
28. [order] from clue 6 owner:Ms Trevino: ruled out position(s) 3
29. [order] from clue 3 clock:a cuckoo clock: ruled out position(s) 1,3,4,5
30. [bijection] chime:a single strike: ruled out position(s) 3
31. [bijection] chime:a bell and gong: ruled out position(s) 3
32. [bijection] clock:a ship's chronometer: ruled out position(s) 1,2
33. [bijection] clock:a carriage clock: ruled out position(s) 1,2
34. [bijection] clock:a longcase clock: ruled out position(s) 1
35. [bijection] clock:a ship's chronometer: ruled out position(s) 3,5
36. [bijection] fault:a cracked suspension spring: ruled out position(s) 2
37. [bijection] fault:a gummed-up pivot: ruled out position(s) 2
38. [bijection] fault:a cracked suspension spring: ruled out position(s) 1,5
39. [bijection] owner:Mr Dziedzic: ruled out position(s) 4
40. [bijection] owner:Mrs Oyelaran: ruled out position(s) 4
_... and 7 further steps._

---

<sub>seed `2026173073420` &middot; score 6.01 &middot; atoms 12 &middot; positives 2 &middot; solved by order</sub>
