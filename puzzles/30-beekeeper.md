# The Honey Show Scandal

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `0d7d0fe6c620`

## Introduction

The annual honey show has been judged, and at least two people are writing letters about it.
Five beekeepers are involved. Determine each beekeeper's entry fee, honey and hive.
- **Beekeeper**: Wilhelmina, Breda, Mungo, Priya and Fausto.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6, $8 and $10.
- **Honey**: borage honey, ivy honey, lime blossom honey, sea lavender honey and chestnut honey.
- **Hive type**: a long deep hive, a Langstroth hive, a national hive, a Warre hive and a WBC hive.
Every beekeeper has a different entry fee, honey and hive, so within each category every item is used exactly once.

## Clues

1. $2 is exactly one fee step cheaper than Wilhelmina, with no entry fee in between. Fausto falls somewhere between $10 and $2 in entry fee order. The beekeeper who keeps a WBC hive pays $2.
2. The beekeeper who keeps a Warre hive falls somewhere between $2 and $6 in entry fee order. The beekeeper who enters chestnut honey does not pay $6.
3. $8 is exactly one fee step cheaper than the beekeeper who keeps a long deep hive, with no entry fee in between.
4. The beekeeper who enters ivy honey does not pay $6.
5. The beekeeper who enters sea lavender honey and Priya are exactly one fee step apart in entry fee order, in one direction or the other.
6. The beekeeper who keeps a WBC hive and the beekeeper who enters lime blossom honey are exactly one fee step apart in entry fee order, in one direction or the other.
7. Mungo does not enter ivy honey.
8. The beekeeper who keeps a Langstroth hive is exactly one fee step cheaper than Priya, with no entry fee in between.
9. The beekeeper who enters chestnut honey falls somewhere between Breda and Wilhelmina in entry fee order.

## Solving chart

*Entry fee vs Beekeeper*

| | Wilhelmina | Breda | Mungo | Priya | Fausto |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Honey*

| | borage honey | ivy honey | lime blossom honey | sea lavender honey | chestnut honey |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Hive type*

| | a long deep hive | a Langstroth hive | a national hive | a Warre hive | a WBC hive |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Beekeeper vs Honey*

| | borage honey | ivy honey | lime blossom honey | sea lavender honey | chestnut honey |
|---|---|---|---|---|---|
| **Wilhelmina** | | | | | |
| **Breda** | | | | | |
| **Mungo** | | | | | |
| **Priya** | | | | | |
| **Fausto** | | | | | |

*Beekeeper vs Hive type*

| | a long deep hive | a Langstroth hive | a national hive | a Warre hive | a WBC hive |
|---|---|---|---|---|---|
| **Wilhelmina** | | | | | |
| **Breda** | | | | | |
| **Mungo** | | | | | |
| **Priya** | | | | | |
| **Fausto** | | | | | |

*Honey vs Hive type*

| | a long deep hive | a Langstroth hive | a national hive | a Warre hive | a WBC hive |
|---|---|---|---|---|---|
| **borage honey** | | | | | |
| **ivy honey** | | | | | |
| **lime blossom honey** | | | | | |
| **sea lavender honey** | | | | | |
| **chestnut honey** | | | | | |

## Solution

| Entry fee | Beekeeper | Honey | Hive type |
|---|---|---|---|
| $2 | Mungo | borage honey | a WBC hive |
| $4 | Wilhelmina | lime blossom honey | a Warre hive |
| $6 | Fausto | sea lavender honey | a Langstroth hive |
| $8 | Priya | chestnut honey | a national hive |
| $10 | Breda | ivy honey | a long deep hive |

## How it falls out

1. [direct] from clue 10 honey:chestnut honey: ruled out position(s) 3
2. [direct] from clue 7 honey:ivy honey: ruled out position(s) 3
3. [direct] from clue 6 hive:a WBC hive: ruled out position(s) 2,3,4,5
4. [bijection] hive:a long deep hive: ruled out position(s) 1
5. [bijection] hive:a Langstroth hive: ruled out position(s) 1
6. [bijection] hive:a national hive: ruled out position(s) 1
7. [bijection] hive:a Warre hive: ruled out position(s) 1
8. [order] from clue 12 hive:a Warre hive: ruled out position(s) 3,4,5
9. [order] from clue 11 hive:a Langstroth hive: ruled out position(s) 5
10. [order] from clue 11 keeper:Priya: ruled out position(s) 1,2
11. [order] from clue 9 honey:sea lavender honey: ruled out position(s) 1
12. [order] from clue 8 keeper:Fausto: ruled out position(s) 1,5
13. [order] from clue 4 honey:chestnut honey: ruled out position(s) 1,5
14. [order] from clue 3 hive:a long deep hive: ruled out position(s) 2,3,4
15. [order] from clue 2 honey:lime blossom honey: ruled out position(s) 1,3,4,5
16. [order] from clue 1 keeper:Wilhelmina: ruled out position(s) 1,3,4,5
17. [order] from clue 4 honey:chestnut honey: ruled out position(s) 2
18. [order] from clue 4 keeper:Breda: ruled out position(s) 1,2,3,4
19. [bijection] hive:a Langstroth hive: ruled out position(s) 2
20. [bijection] hive:a national hive: ruled out position(s) 2,5
21. [bijection] honey:borage honey: ruled out position(s) 2,4
22. [bijection] honey:ivy honey: ruled out position(s) 2,4
23. [bijection] honey:sea lavender honey: ruled out position(s) 2,4
24. [bijection] keeper:Mungo: ruled out position(s) 2,5
25. [bijection] keeper:Priya: ruled out position(s) 5
26. [bijection] keeper:Fausto: ruled out position(s) 2
27. [bijection] keeper:Mungo: ruled out position(s) 3,4
28. [order] from clue 9 keeper:Priya: ruled out position(s) 3
29. [direct] from clue 5 honey:ivy honey: ruled out position(s) 1
30. [order] from clue 11 hive:a Langstroth hive: ruled out position(s) 4
31. [bijection] hive:a national hive: ruled out position(s) 3
32. [bijection] honey:borage honey: ruled out position(s) 5
33. [bijection] honey:sea lavender honey: ruled out position(s) 5
34. [bijection] honey:borage honey: ruled out position(s) 3
35. [bijection] keeper:Fausto: ruled out position(s) 4

---

<sub>seed `2026173113015` &middot; score 5.515 &middot; atoms 12 &middot; positives 1 &middot; solved by order</sub>
