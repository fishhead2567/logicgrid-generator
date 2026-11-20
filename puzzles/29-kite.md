# The Wind Is Free, the Field Is Not

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `55e247ecaf19`

## Introduction

The Dunnage Kite Festival charges by the kite, which has produced some creative definitions of 'one kite'.
Five fliers are involved. Determine each flier's entry fee, kite and line.
- **Flier**: Kipling, Tansy, Blaise, Morwenna and Gunnar.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6, $8 and $10.
- **Kite**: a rokkaku fighter, a box kite, a delta wing, a paper sled kite and a hand-painted dragon.
- **Line**: nylon twine, braided dacron, hemp cord, kevlar thread and fishing monofilament.
Every flier has a different entry fee, kite and line, so within each category every item is used exactly once.

## Clues

1. The flier who uses braided dacron and $6 are exactly one fee step apart in entry fee order, in one direction or the other. The flier who flies a delta wing does not pay $6.
2. Blaise and $10 are exactly one fee step apart in entry fee order, in one direction or the other.
3. The flier who uses nylon twine is exactly one fee step cheaper than $6, with no entry fee in between.
4. The flier who uses hemp cord is cheaper than the flier who flies a paper sled kite in entry fee order.
5. The flier who flies a box kite is exactly one fee step cheaper than Tansy, with no entry fee in between.
6. Tansy falls somewhere between the flier who uses fishing monofilament and the flier who uses kevlar thread in entry fee order. Gunnar does not use kevlar thread.
7. The flier who flies a rokkaku fighter is exactly one fee step cheaper than the flier who uses fishing monofilament, with no entry fee in between.
8. Morwenna is exactly one fee step cheaper than the flier who flies a hand-painted dragon, with no entry fee in between.

## Solving chart

*Entry fee vs Flier*

| | Kipling | Tansy | Blaise | Morwenna | Gunnar |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Kite*

| | a rokkaku fighter | a box kite | a delta wing | a paper sled kite | a hand-painted dragon |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Line*

| | nylon twine | braided dacron | hemp cord | kevlar thread | fishing monofilament |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Flier vs Kite*

| | a rokkaku fighter | a box kite | a delta wing | a paper sled kite | a hand-painted dragon |
|---|---|---|---|---|---|
| **Kipling** | | | | | |
| **Tansy** | | | | | |
| **Blaise** | | | | | |
| **Morwenna** | | | | | |
| **Gunnar** | | | | | |

*Flier vs Line*

| | nylon twine | braided dacron | hemp cord | kevlar thread | fishing monofilament |
|---|---|---|---|---|---|
| **Kipling** | | | | | |
| **Tansy** | | | | | |
| **Blaise** | | | | | |
| **Morwenna** | | | | | |
| **Gunnar** | | | | | |

*Kite vs Line*

| | nylon twine | braided dacron | hemp cord | kevlar thread | fishing monofilament |
|---|---|---|---|---|---|
| **a rokkaku fighter** | | | | | |
| **a box kite** | | | | | |
| **a delta wing** | | | | | |
| **a paper sled kite** | | | | | |
| **a hand-painted dragon** | | | | | |

## Solution

| Entry fee | Flier | Kite | Line |
|---|---|---|---|
| $2 | Kipling | a delta wing | kevlar thread |
| $4 | Morwenna | a box kite | nylon twine |
| $6 | Tansy | a hand-painted dragon | hemp cord |
| $8 | Blaise | a rokkaku fighter | braided dacron |
| $10 | Gunnar | a paper sled kite | fishing monofilament |

## How it falls out

1. [direct] from clue 8 kite:a delta wing: ruled out position(s) 3
2. [order] from clue 10 kite:a rokkaku fighter: ruled out position(s) 5
3. [order] from clue 10 line:fishing monofilament: ruled out position(s) 1
4. [order] from clue 9 line:braided dacron: ruled out position(s) 1,3,5
5. [order] from clue 7 line:nylon twine: ruled out position(s) 1,3,4,5
6. [order] from clue 6 flier:Blaise: ruled out position(s) 1,2,3,5
7. [order] from clue 5 flier:Morwenna: ruled out position(s) 5
8. [order] from clue 5 kite:a hand-painted dragon: ruled out position(s) 1
9. [order] from clue 4 flier:Tansy: ruled out position(s) 1,5
10. [order] from clue 2 line:hemp cord: ruled out position(s) 5
11. [order] from clue 2 kite:a paper sled kite: ruled out position(s) 1
12. [order] from clue 1 kite:a box kite: ruled out position(s) 4,5
13. [bijection] flier:Kipling: ruled out position(s) 4
14. [bijection] flier:Tansy: ruled out position(s) 4
15. [bijection] flier:Morwenna: ruled out position(s) 4
16. [bijection] flier:Gunnar: ruled out position(s) 4
17. [bijection] line:braided dacron: ruled out position(s) 2
18. [bijection] line:hemp cord: ruled out position(s) 2
19. [bijection] line:kevlar thread: ruled out position(s) 2
20. [bijection] line:fishing monofilament: ruled out position(s) 2
21. [order] from clue 10 kite:a rokkaku fighter: ruled out position(s) 1
22. [order] from clue 5 kite:a hand-painted dragon: ruled out position(s) 5
23. [order] from clue 4 line:kevlar thread: ruled out position(s) 3,4,5
24. [direct] from clue 3 flier:Gunnar: ruled out position(s) 1
25. [order] from clue 1 kite:a box kite: ruled out position(s) 3
26. [bijection] line:hemp cord: ruled out position(s) 1,4
27. [bijection] line:fishing monofilament: ruled out position(s) 4
28. [bijection] line:fishing monofilament: ruled out position(s) 3
29. [order] from clue 10 kite:a rokkaku fighter: ruled out position(s) 2,3
30. [order] from clue 2 kite:a paper sled kite: ruled out position(s) 2,3
31. [bijection] kite:a delta wing: ruled out position(s) 4
32. [bijection] kite:a paper sled kite: ruled out position(s) 4
33. [bijection] kite:a hand-painted dragon: ruled out position(s) 4
34. [bijection] kite:a hand-painted dragon: ruled out position(s) 2
35. [order] from clue 5 flier:Morwenna: ruled out position(s) 1,3
36. [bijection] flier:Kipling: ruled out position(s) 2
37. [bijection] flier:Tansy: ruled out position(s) 2
38. [bijection] flier:Gunnar: ruled out position(s) 2
39. [bijection] flier:Kipling: ruled out position(s) 3,5
40. [bijection] kite:a delta wing: ruled out position(s) 5
_... and 3 further steps._

---

<sub>seed `2026173105096` &middot; score 5.675 &middot; atoms 10 &middot; positives 0 &middot; solved by order</sub>
