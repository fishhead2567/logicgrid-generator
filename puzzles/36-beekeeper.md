# The Honey Show Scandal

*The annual honey show has been judged, and at least two people are writing letters about it.*

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `6eecf8d1c272`

## Introduction

There are 5 exhibits. Each has exactly one entry fee and one item from every other category below, and within each category every item belongs to a different exhibit.
- **Entry fee** (listed in order): $2, $4, $6, $8 and $10.
- **Beekeeper**: Antonina, Priya, Breda, Mungo and Wilhelmina.
- **Honey**: heather honey, chestnut honey, ivy honey, sea lavender honey and borage honey.
- **Judge's note**: a cloudy jar, exemplary clarity, an unlabelled lid, slightly over-filtered and a trace of wax.
The fee steps above are listed in order, from $2 to $10.

## Clues

1. Ivy honey goes with exemplary clarity.
2. $2 does not go with Priya, and $2 does not go with slightly over-filtered.
3. $10 and Mungo are next to each other in entry fee order, in one order or the other.
4. At least one of the following holds, and possibly more than one: (a) $6 goes with exemplary clarity. (b) Breda goes with a cloudy jar.
5. Heather honey's entry fee is cheaper than Breda's entry fee.
6. Chestnut honey's entry fee is immediately cheaper than a trace of wax's entry fee, with no entry fee in between.
7. Borage honey does not go with an unlabelled lid. Borage honey's entry fee is immediately cheaper than Wilhelmina's entry fee, with no entry fee in between.
8. Ivy honey and Antonina are next to each other in entry fee order, in one order or the other.

## Solving chart

*Entry fee vs Beekeeper*

| | Antonina | Priya | Breda | Mungo | Wilhelmina |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Honey*

| | heather honey | chestnut honey | ivy honey | sea lavender honey | borage honey |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Judge's note*

| | a cloudy jar | exemplary clarity | an unlabelled lid | slightly over-filtered | a trace of wax |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Beekeeper vs Honey*

| | heather honey | chestnut honey | ivy honey | sea lavender honey | borage honey |
|---|---|---|---|---|---|
| **Antonina** | | | | | |
| **Priya** | | | | | |
| **Breda** | | | | | |
| **Mungo** | | | | | |
| **Wilhelmina** | | | | | |

*Beekeeper vs Judge's note*

| | a cloudy jar | exemplary clarity | an unlabelled lid | slightly over-filtered | a trace of wax |
|---|---|---|---|---|---|
| **Antonina** | | | | | |
| **Priya** | | | | | |
| **Breda** | | | | | |
| **Mungo** | | | | | |
| **Wilhelmina** | | | | | |

*Honey vs Judge's note*

| | a cloudy jar | exemplary clarity | an unlabelled lid | slightly over-filtered | a trace of wax |
|---|---|---|---|---|---|
| **heather honey** | | | | | |
| **chestnut honey** | | | | | |
| **ivy honey** | | | | | |
| **sea lavender honey** | | | | | |
| **borage honey** | | | | | |

## Solution

| Entry fee | Beekeeper | Honey | Judge's note |
|---|---|---|---|
| $2 | Antonina | heather honey | an unlabelled lid |
| $4 | Priya | ivy honey | exemplary clarity |
| $6 | Breda | chestnut honey | a cloudy jar |
| $8 | Mungo | borage honey | a trace of wax |
| $10 | Wilhelmina | sea lavender honey | slightly over-filtered |

## How it falls out

1. [direct] from clue 8 keeper:Priya: ruled out position(s) 1
2. [direct] from clue 2 verdict:slightly over-filtered: ruled out position(s) 1
3. [order] from clue 7 honey:borage honey: ruled out position(s) 5
4. [order] from clue 7 keeper:Wilhelmina: ruled out position(s) 1
5. [order] from clue 5 keeper:Mungo: ruled out position(s) 1,2,3,5
6. [order] from clue 4 honey:chestnut honey: ruled out position(s) 5
7. [order] from clue 4 verdict:a trace of wax: ruled out position(s) 1
8. [order] from clue 3 honey:heather honey: ruled out position(s) 5
9. [order] from clue 3 keeper:Breda: ruled out position(s) 1
10. [bijection] keeper:Antonina: ruled out position(s) 4
11. [bijection] keeper:Priya: ruled out position(s) 4
12. [bijection] keeper:Breda: ruled out position(s) 4
13. [bijection] keeper:Wilhelmina: ruled out position(s) 4
14. [bijection] keeper:Antonina: ruled out position(s) 2,3,5
15. [order] from clue 7 honey:borage honey: ruled out position(s) 3
16. [order] from clue 1 honey:ivy honey: ruled out position(s) 1,3,4,5
17. [direct] from clue 10 verdict:exemplary clarity: ruled out position(s) 1,3,4,5
18. [bijection] honey:heather honey: ruled out position(s) 2
19. [bijection] honey:chestnut honey: ruled out position(s) 2
20. [bijection] honey:sea lavender honey: ruled out position(s) 2
21. [bijection] honey:borage honey: ruled out position(s) 2
22. [bijection] honey:sea lavender honey: ruled out position(s) 1,3,4
23. [bijection] verdict:a cloudy jar: ruled out position(s) 2
24. [bijection] verdict:an unlabelled lid: ruled out position(s) 2
25. [bijection] verdict:slightly over-filtered: ruled out position(s) 2
26. [bijection] verdict:a trace of wax: ruled out position(s) 2
27. [order] from clue 7 keeper:Wilhelmina: ruled out position(s) 3
28. [order] from clue 4 honey:chestnut honey: ruled out position(s) 1
29. [order] from clue 4 verdict:a trace of wax: ruled out position(s) 3
30. [disjunction] from clue 9 keeper:Breda: ruled out position(s) 2
31. [disjunction] from clue 9 verdict:a cloudy jar: ruled out position(s) 1,4
32. [bijection] verdict:an unlabelled lid: ruled out position(s) 3,4,5
33. [direct] from clue 6 honey:borage honey: ruled out position(s) 1
34. [order] from clue 7 keeper:Wilhelmina: ruled out position(s) 2
35. [bijection] honey:heather honey: ruled out position(s) 4
36. [bijection] honey:chestnut honey: ruled out position(s) 4
37. [bijection] honey:heather honey: ruled out position(s) 3
38. [bijection] keeper:Priya: ruled out position(s) 5
39. [bijection] keeper:Breda: ruled out position(s) 5
40. [bijection] keeper:Priya: ruled out position(s) 3
_... and 3 further steps._

---

<sub>seed `2026172860520` &middot; score 9.2376 &middot; atoms 10 &middot; positives 1 &middot; solved by disjunction</sub>
