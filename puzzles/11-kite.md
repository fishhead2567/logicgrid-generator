# The Wind Is Free, the Field Is Not

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `3b108afe321d`

## Introduction

The Dunnage Kite Festival charges by the kite, which has produced some creative definitions of 'one kite'.
Four fliers are involved. Determine each flier's entry fee, kite and line.
- **Flier**: Ifeoma, Tansy, Gunnar and Kipling.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6 and $8.
- **Kite**: a parafoil, a rokkaku fighter, a delta wing and a box kite.
- **Line**: nylon twine, fishing monofilament, parcel string and braided dacron.
Every flier has a different entry fee, kite and line, so within each category every item is used exactly once.

## Clues

1. Kipling uses parcel string.
2. The flier who flies a box kite and $6 are exactly one fee step apart in entry fee order, in one direction or the other.
3. $4 falls somewhere between Gunnar and Kipling in entry fee order. The flier who flies a delta wing is cheaper than Kipling in entry fee order.
4. $4 falls somewhere between the flier who uses fishing monofilament and the flier who uses nylon twine in entry fee order.
5. The flier who flies a parafoil falls somewhere between Kipling and Tansy in entry fee order.
6. The flier who flies a box kite is cheaper than the flier who uses nylon twine in entry fee order.

## Solving chart

*Entry fee vs Flier*

| | Ifeoma | Tansy | Gunnar | Kipling |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Entry fee vs Kite*

| | a parafoil | a rokkaku fighter | a delta wing | a box kite |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Entry fee vs Line*

| | nylon twine | fishing monofilament | parcel string | braided dacron |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Flier vs Kite*

| | a parafoil | a rokkaku fighter | a delta wing | a box kite |
|---|---|---|---|---|
| **Ifeoma** | | | | |
| **Tansy** | | | | |
| **Gunnar** | | | | |
| **Kipling** | | | | |

*Flier vs Line*

| | nylon twine | fishing monofilament | parcel string | braided dacron |
|---|---|---|---|---|
| **Ifeoma** | | | | |
| **Tansy** | | | | |
| **Gunnar** | | | | |
| **Kipling** | | | | |

*Kite vs Line*

| | nylon twine | fishing monofilament | parcel string | braided dacron |
|---|---|---|---|---|
| **a parafoil** | | | | |
| **a rokkaku fighter** | | | | |
| **a delta wing** | | | | |
| **a box kite** | | | | |

## Solution

| Entry fee | Flier | Kite | Line |
|---|---|---|---|
| $2 | Gunnar | a delta wing | fishing monofilament |
| $4 | Tansy | a box kite | braided dacron |
| $6 | Ifeoma | a parafoil | nylon twine |
| $8 | Kipling | a rokkaku fighter | parcel string |

## How it falls out

1. [order] from clue 7 kite:a box kite: ruled out position(s) 4
2. [order] from clue 7 line:nylon twine: ruled out position(s) 1
3. [order] from clue 6 flier:Gunnar: ruled out position(s) 2
4. [order] from clue 6 flier:Kipling: ruled out position(s) 2
5. [order] from clue 5 kite:a delta wing: ruled out position(s) 4
6. [order] from clue 5 flier:Kipling: ruled out position(s) 1
7. [order] from clue 6 flier:Gunnar: ruled out position(s) 3,4
8. [order] from clue 4 line:fishing monofilament: ruled out position(s) 2,3,4
9. [order] from clue 4 line:nylon twine: ruled out position(s) 2
10. [order] from clue 2 kite:a box kite: ruled out position(s) 1,3
11. [order] from clue 1 kite:a parafoil: ruled out position(s) 1,4
12. [order] from clue 1 flier:Tansy: ruled out position(s) 3,4
13. [direct] from clue 3 line:parcel string: ruled out position(s) 1,2
14. [bijection] flier:Ifeoma: ruled out position(s) 1
15. [bijection] flier:Tansy: ruled out position(s) 1
16. [bijection] kite:a parafoil: ruled out position(s) 2
17. [bijection] kite:a rokkaku fighter: ruled out position(s) 2
18. [bijection] kite:a delta wing: ruled out position(s) 2
19. [bijection] kite:a rokkaku fighter: ruled out position(s) 1,3
20. [bijection] line:braided dacron: ruled out position(s) 1
21. [bijection] line:braided dacron: ruled out position(s) 3,4
22. [order] from clue 1 flier:Kipling: ruled out position(s) 3
23. [direct] from clue 3 line:parcel string: ruled out position(s) 3
24. [bijection] flier:Ifeoma: ruled out position(s) 2,4
25. [bijection] kite:a delta wing: ruled out position(s) 3
26. [bijection] line:nylon twine: ruled out position(s) 4

---

<sub>seed `2026172762548` &middot; score 5.13 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
