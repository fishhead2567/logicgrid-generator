# The Autumn Show at Kiyosumi

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `6bf2861e1a74`

## Introduction

Trees on stands, judged on a hundred-point sheet, and the wiring marks are what everybody is looking for.
Five exhibitors are involved. Determine each exhibitor's judged score and flaw.
- **Exhibitor**: Noriko Hase, Keiko Tanabe, Takumi Ishii, Jun Kawabe and Hiroshi Mita.
- **Judged score** (listed from lower to higher): 61 points, 64 points, 67 points, 70 points and 73 points.
- **Flaw noted**: a weak nebari, a bar branch, reverse taper, visible wiring scars and an eye-poking branch.
Every exhibitor has a different judged score and flaw, so within each category every item is used exactly once.

## Clues

1. The exhibitor who is marked down for reverse taper is awarded 64 points. Noriko Hase is awarded 64 points.
2. The exhibitor who is marked down for a weak nebari and 73 points are exactly one score step apart in judged score order, in one direction or the other.
3. Takumi Ishii and the exhibitor who is marked down for a weak nebari are exactly one score step apart in judged score order, in one direction or the other.
4. The exhibitor who is marked down for an eye-poking branch is exactly one score step lower than Hiroshi Mita, with no judged score in between.
5. Jun Kawabe falls somewhere between the exhibitor who is marked down for a weak nebari and the exhibitor who is marked down for visible wiring scars in judged score order.

## Solving chart

*Judged score vs Exhibitor*

| | Noriko Hase | Keiko Tanabe | Takumi Ishii | Jun Kawabe | Hiroshi Mita |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Judged score vs Flaw noted*

| | a weak nebari | a bar branch | reverse taper | visible wiring scars | an eye-poking branch |
|---|---|---|---|---|---|
| **61 points** | | | | | |
| **64 points** | | | | | |
| **67 points** | | | | | |
| **70 points** | | | | | |
| **73 points** | | | | | |

*Exhibitor vs Flaw noted*

| | a weak nebari | a bar branch | reverse taper | visible wiring scars | an eye-poking branch |
|---|---|---|---|---|---|
| **Noriko Hase** | | | | | |
| **Keiko Tanabe** | | | | | |
| **Takumi Ishii** | | | | | |
| **Jun Kawabe** | | | | | |
| **Hiroshi Mita** | | | | | |

## Solution

| Judged score | Exhibitor | Flaw noted |
|---|---|---|
| 61 points | Keiko Tanabe | visible wiring scars |
| 64 points | Noriko Hase | reverse taper |
| 67 points | Jun Kawabe | an eye-poking branch |
| 70 points | Hiroshi Mita | a weak nebari |
| 73 points | Takumi Ishii | a bar branch |

## How it falls out

1. [direct] from clue 5 exhibitor:Noriko Hase: ruled out position(s) 1,3,4,5
2. [direct] from clue 1 flaw:reverse taper: ruled out position(s) 1,3,4,5
3. [bijection] exhibitor:Keiko Tanabe: ruled out position(s) 2
4. [bijection] exhibitor:Takumi Ishii: ruled out position(s) 2
5. [bijection] exhibitor:Jun Kawabe: ruled out position(s) 2
6. [bijection] exhibitor:Hiroshi Mita: ruled out position(s) 2
7. [bijection] flaw:a weak nebari: ruled out position(s) 2
8. [bijection] flaw:a bar branch: ruled out position(s) 2
9. [bijection] flaw:visible wiring scars: ruled out position(s) 2
10. [bijection] flaw:an eye-poking branch: ruled out position(s) 2
11. [order] from clue 6 flaw:an eye-poking branch: ruled out position(s) 1,5
12. [order] from clue 6 exhibitor:Hiroshi Mita: ruled out position(s) 1,3
13. [order] from clue 4 exhibitor:Takumi Ishii: ruled out position(s) 1
14. [order] from clue 4 flaw:a weak nebari: ruled out position(s) 1
15. [order] from clue 3 flaw:a weak nebari: ruled out position(s) 3,5
16. [order] from clue 4 exhibitor:Takumi Ishii: ruled out position(s) 4
17. [order] from clue 2 exhibitor:Jun Kawabe: ruled out position(s) 1,4,5
18. [order] from clue 2 flaw:visible wiring scars: ruled out position(s) 3,4,5
19. [bijection] exhibitor:Keiko Tanabe: ruled out position(s) 3
20. [bijection] exhibitor:Takumi Ishii: ruled out position(s) 3
21. [bijection] exhibitor:Keiko Tanabe: ruled out position(s) 4,5
22. [bijection] flaw:a bar branch: ruled out position(s) 1,4
23. [bijection] flaw:an eye-poking branch: ruled out position(s) 4
24. [bijection] flaw:a bar branch: ruled out position(s) 3
25. [order] from clue 6 exhibitor:Hiroshi Mita: ruled out position(s) 5

---

<sub>seed `2026172994230` &middot; score 4.62 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
