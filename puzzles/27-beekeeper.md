# The Honey Show Scandal

*The annual honey show has been judged, and at least two people are writing letters about it.*

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `1117445c02f0`

## Introduction

There are 5 exhibits. Each has exactly one entry fee and one item from every other category below, and within each category every item belongs to a different exhibit.
- **Entry fee** (listed in order): $2, $4, $6, $8 and $10.
- **Honey**: sea lavender honey, chestnut honey, clover honey, lime blossom honey and borage honey.
- **Hive type**: a long deep hive, a Langstroth hive, a skep, a WBC hive and a Warre hive.
- **Judge's note**: an unlabelled lid, a trace of wax, crystallised early, a cloudy jar and an overbearing aroma.
The fee steps above are listed in order, from $2 to $10.

## Clues

1. $10 goes with borage honey.
2. A Warre hive and crystallised early are next to each other in entry fee order, in one order or the other. Sea lavender honey goes with crystallised early.
3. $2 is immediately cheaper than a Warre hive's entry fee, with no entry fee in between. A trace of wax falls somewhere between $2 and a skep in entry fee order. An overbearing aroma falls somewhere between $6 and a skep in entry fee order.
4. $4 and chestnut honey are next to each other in entry fee order, in one order or the other.
5. A WBC hive falls somewhere between $8 and an unlabelled lid in entry fee order.
6. Clover honey's entry fee is immediately cheaper than a skep's entry fee, with no entry fee in between.
7. Sea lavender honey falls somewhere between a long deep hive and a cloudy jar in entry fee order.

## Solving chart

*Entry fee vs Honey*

| | sea lavender honey | chestnut honey | clover honey | lime blossom honey | borage honey |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Hive type*

| | a long deep hive | a Langstroth hive | a skep | a WBC hive | a Warre hive |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Judge's note*

| | an unlabelled lid | a trace of wax | crystallised early | a cloudy jar | an overbearing aroma |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Honey vs Hive type*

| | a long deep hive | a Langstroth hive | a skep | a WBC hive | a Warre hive |
|---|---|---|---|---|---|
| **sea lavender honey** | | | | | |
| **chestnut honey** | | | | | |
| **clover honey** | | | | | |
| **lime blossom honey** | | | | | |
| **borage honey** | | | | | |

*Honey vs Judge's note*

| | an unlabelled lid | a trace of wax | crystallised early | a cloudy jar | an overbearing aroma |
|---|---|---|---|---|---|
| **sea lavender honey** | | | | | |
| **chestnut honey** | | | | | |
| **clover honey** | | | | | |
| **lime blossom honey** | | | | | |
| **borage honey** | | | | | |

*Hive type vs Judge's note*

| | an unlabelled lid | a trace of wax | crystallised early | a cloudy jar | an overbearing aroma |
|---|---|---|---|---|---|
| **a long deep hive** | | | | | |
| **a Langstroth hive** | | | | | |
| **a skep** | | | | | |
| **a WBC hive** | | | | | |
| **a Warre hive** | | | | | |

## Solution

| Entry fee | Honey | Hive type | Judge's note |
|---|---|---|---|
| $2 | chestnut honey | a long deep hive | an unlabelled lid |
| $4 | lime blossom honey | a Warre hive | a trace of wax |
| $6 | sea lavender honey | a WBC hive | crystallised early |
| $8 | clover honey | a Langstroth hive | an overbearing aroma |
| $10 | borage honey | a skep | a cloudy jar |

## How it falls out

1. [direct] from clue 2 honey:borage honey: ruled out position(s) 1,2,3,4
2. [bijection] honey:sea lavender honey: ruled out position(s) 5
3. [bijection] honey:chestnut honey: ruled out position(s) 5
4. [bijection] honey:clover honey: ruled out position(s) 5
5. [bijection] honey:lime blossom honey: ruled out position(s) 5
6. [direct] from clue 5 verdict:crystallised early: ruled out position(s) 5
7. [order] from clue 10 verdict:an overbearing aroma: ruled out position(s) 1,3,5
8. [order] from clue 10 hive:a skep: ruled out position(s) 2,3,4
9. [order] from clue 8 hive:a WBC hive: ruled out position(s) 1,4,5
10. [order] from clue 8 verdict:an unlabelled lid: ruled out position(s) 3,4,5
11. [order] from clue 7 hive:a Warre hive: ruled out position(s) 1,3,4,5
12. [order] from clue 9 verdict:crystallised early: ruled out position(s) 2,4
13. [order] from clue 6 verdict:a trace of wax: ruled out position(s) 1,5
14. [order] from clue 6 hive:a skep: ruled out position(s) 1
15. [order] from clue 10 verdict:an overbearing aroma: ruled out position(s) 2
16. [order] from clue 4 honey:sea lavender honey: ruled out position(s) 1
17. [order] from clue 3 honey:chestnut honey: ruled out position(s) 2,4
18. [order] from clue 1 honey:clover honey: ruled out position(s) 1,2,3
19. [direct] from clue 5 honey:sea lavender honey: ruled out position(s) 2,4
20. [direct] from clue 5 verdict:crystallised early: ruled out position(s) 1
21. [order] from clue 4 hive:a long deep hive: ruled out position(s) 3
22. [order] from clue 4 verdict:a cloudy jar: ruled out position(s) 3
23. [bijection] hive:a long deep hive: ruled out position(s) 2,5
24. [bijection] hive:a Langstroth hive: ruled out position(s) 2,5
25. [bijection] hive:a WBC hive: ruled out position(s) 2
26. [bijection] honey:chestnut honey: ruled out position(s) 3
27. [bijection] honey:lime blossom honey: ruled out position(s) 3,4
28. [bijection] honey:lime blossom honey: ruled out position(s) 1
29. [bijection] verdict:a trace of wax: ruled out position(s) 3,4
30. [bijection] verdict:a cloudy jar: ruled out position(s) 4
31. [bijection] verdict:a cloudy jar: ruled out position(s) 1,2
32. [order] from clue 4 hive:a long deep hive: ruled out position(s) 4
33. [bijection] hive:a Langstroth hive: ruled out position(s) 1,3
34. [bijection] verdict:an unlabelled lid: ruled out position(s) 2

---

<sub>seed `2026172789249` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
