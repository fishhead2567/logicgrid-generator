# A Benchful of Clocks, and No Agreement

*Mr Halloran repairs clocks. Those on the bench are all insisting on a different hour.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `48344831bdb4`

## Introduction

There are 4 repair jobs. Each has exactly one shelf and one item from every other category below, and within each category every item belongs to a different repair job.
- **Shelf** (listed in order): the bottom shelf, the second shelf, the third shelf and the fourth shelf.
- **Clock**: a ship's chronometer, a cuckoo clock, a station clock and a mantel clock under glass.
- **Owner**: Dr Vasquez, Mr Dziedzic, Captain Mott and Miss Trevelyan.
- **Chime**: a cuckoo call, Westminster, no chime at all and Whittington.
The shelves above are listed in order, from the bottom shelf to the fourth shelf.

## Clues

1. A cuckoo clock goes with the second shelf.
2. Miss Trevelyan's shelf is lower than the second shelf.
3. The bottom shelf is immediately lower than Dr Vasquez's shelf, with no shelf in between.
4. Whittington's shelf is immediately lower than a ship's chronometer's shelf, with no shelf in between.
5. Westminster's shelf is immediately lower than a cuckoo clock's shelf, with no shelf in between.
6. A cuckoo call and a station clock are next to each other in shelf order, in one order or the other. Captain Mott's shelf is immediately lower than a cuckoo call's shelf, with no shelf in between.

## Solving chart

*Shelf vs Clock*

| | a ship's chronometer | a cuckoo clock | a station clock | a mantel clock under glass |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Owner*

| | Dr Vasquez | Mr Dziedzic | Captain Mott | Miss Trevelyan |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Chime*

| | a cuckoo call | Westminster | no chime at all | Whittington |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Clock vs Owner*

| | Dr Vasquez | Mr Dziedzic | Captain Mott | Miss Trevelyan |
|---|---|---|---|---|
| **a ship's chronometer** | | | | |
| **a cuckoo clock** | | | | |
| **a station clock** | | | | |
| **a mantel clock under glass** | | | | |

*Clock vs Chime*

| | a cuckoo call | Westminster | no chime at all | Whittington |
|---|---|---|---|---|
| **a ship's chronometer** | | | | |
| **a cuckoo clock** | | | | |
| **a station clock** | | | | |
| **a mantel clock under glass** | | | | |

*Owner vs Chime*

| | a cuckoo call | Westminster | no chime at all | Whittington |
|---|---|---|---|---|
| **Dr Vasquez** | | | | |
| **Mr Dziedzic** | | | | |
| **Captain Mott** | | | | |
| **Miss Trevelyan** | | | | |

## Solution

| Shelf | Clock | Owner | Chime |
|---|---|---|---|
| the bottom shelf | a mantel clock under glass | Miss Trevelyan | Westminster |
| the second shelf | a cuckoo clock | Dr Vasquez | no chime at all |
| the third shelf | a station clock | Captain Mott | Whittington |
| the fourth shelf | a ship's chronometer | Mr Dziedzic | a cuckoo call |

## How it falls out

1. [direct] from clue 2 clock:a cuckoo clock: ruled out position(s) 1,3,4
2. [bijection] clock:a ship's chronometer: ruled out position(s) 2
3. [bijection] clock:a station clock: ruled out position(s) 2
4. [bijection] clock:a mantel clock under glass: ruled out position(s) 2
5. [order] from clue 7 owner:Captain Mott: ruled out position(s) 4
6. [order] from clue 7 chime:a cuckoo call: ruled out position(s) 1
7. [order] from clue 6 chime:Westminster: ruled out position(s) 2,3,4
8. [order] from clue 4 owner:Dr Vasquez: ruled out position(s) 1,3,4
9. [order] from clue 3 chime:Whittington: ruled out position(s) 1,4
10. [order] from clue 3 clock:a ship's chronometer: ruled out position(s) 1
11. [order] from clue 1 owner:Miss Trevelyan: ruled out position(s) 2,3,4
12. [bijection] chime:no chime at all: ruled out position(s) 1
13. [bijection] owner:Mr Dziedzic: ruled out position(s) 1,2
14. [bijection] owner:Captain Mott: ruled out position(s) 1,2
15. [bijection] owner:Mr Dziedzic: ruled out position(s) 3
16. [order] from clue 7 chime:a cuckoo call: ruled out position(s) 2,3
17. [order] from clue 5 clock:a station clock: ruled out position(s) 1,4
18. [bijection] chime:no chime at all: ruled out position(s) 4
19. [bijection] clock:a ship's chronometer: ruled out position(s) 3
20. [bijection] clock:a mantel clock under glass: ruled out position(s) 3
21. [bijection] clock:a mantel clock under glass: ruled out position(s) 4
22. [order] from clue 3 chime:Whittington: ruled out position(s) 2
23. [bijection] chime:no chime at all: ruled out position(s) 3

---

<sub>seed `2026172654626` &middot; score 5.13 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
