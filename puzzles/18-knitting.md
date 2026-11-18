# The Ashfold Knitting Circle

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `e969a5749303`

## Introduction

The Ashfold Knitting Circle meets weekly and has not agreed on anything since 1998.
Four knitters are involved. Determine each knitter's day, project and yarn.
- **Knitter**: Ebba, Lionel, Angus and Maudie.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday and Thursday.
- **Project**: a shawl of impossible lace, a fisherman's gansey, a cable-knit blanket and a Fair Isle tam.
- **Yarn**: undyed Shetland, recycled sari silk, mohair of great expense and hand-spun alpaca.
Every knitter has a different day, project and yarn, so within each category every item is used exactly once.

## Clues

1. The knitter who is making a cable-knit blanket knits on Wednesday.
2. The knitter who is making a Fair Isle tam works in mohair of great expense.
3. Wednesday is exactly one day earlier than the knitter who is making a shawl of impossible lace, with no day in between.
4. Lionel does not knit on Wednesday.
5. Maudie is exactly one day earlier than the knitter who works in mohair of great expense, with no day in between.
6. Angus is not making a Fair Isle tam. The knitter who is making a Fair Isle tam is earlier than Lionel in day order.
7. Angus does not work in recycled sari silk.
8. The knitter who works in hand-spun alpaca is exactly one day earlier than the knitter who is making a Fair Isle tam, with no day in between.

## Solving chart

*Day vs Knitter*

| | Ebba | Lionel | Angus | Maudie |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Project*

| | a shawl of impossible lace | a fisherman's gansey | a cable-knit blanket | a Fair Isle tam |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Yarn*

| | undyed Shetland | recycled sari silk | mohair of great expense | hand-spun alpaca |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Knitter vs Project*

| | a shawl of impossible lace | a fisherman's gansey | a cable-knit blanket | a Fair Isle tam |
|---|---|---|---|---|
| **Ebba** | | | | |
| **Lionel** | | | | |
| **Angus** | | | | |
| **Maudie** | | | | |

*Knitter vs Yarn*

| | undyed Shetland | recycled sari silk | mohair of great expense | hand-spun alpaca |
|---|---|---|---|---|
| **Ebba** | | | | |
| **Lionel** | | | | |
| **Angus** | | | | |
| **Maudie** | | | | |

*Project vs Yarn*

| | undyed Shetland | recycled sari silk | mohair of great expense | hand-spun alpaca |
|---|---|---|---|---|
| **a shawl of impossible lace** | | | | |
| **a fisherman's gansey** | | | | |
| **a cable-knit blanket** | | | | |
| **a Fair Isle tam** | | | | |

## Solution

| Day | Knitter | Project | Yarn |
|---|---|---|---|
| Monday | Maudie | a fisherman's gansey | hand-spun alpaca |
| Tuesday | Ebba | a Fair Isle tam | mohair of great expense |
| Wednesday | Angus | a cable-knit blanket | undyed Shetland |
| Thursday | Lionel | a shawl of impossible lace | recycled sari silk |

## How it falls out

1. [direct] from clue 8 knitter:Lionel: ruled out position(s) 3
2. [direct] from clue 2 project:a cable-knit blanket: ruled out position(s) 1,2,4
3. [bijection] project:a shawl of impossible lace: ruled out position(s) 3
4. [bijection] project:a fisherman's gansey: ruled out position(s) 3
5. [bijection] project:a Fair Isle tam: ruled out position(s) 3
6. [direct] from clue 1 yarn:mohair of great expense: ruled out position(s) 3
7. [order] from clue 9 knitter:Maudie: ruled out position(s) 2,4
8. [order] from clue 9 yarn:mohair of great expense: ruled out position(s) 1
9. [order] from clue 7 project:a Fair Isle tam: ruled out position(s) 4
10. [order] from clue 7 knitter:Lionel: ruled out position(s) 1
11. [order] from clue 5 project:a shawl of impossible lace: ruled out position(s) 1,2
12. [order] from clue 4 yarn:hand-spun alpaca: ruled out position(s) 2,3,4
13. [order] from clue 4 project:a Fair Isle tam: ruled out position(s) 1
14. [order] from clue 7 knitter:Lionel: ruled out position(s) 2
15. [direct] from clue 3 knitter:Angus: ruled out position(s) 2
16. [direct] from clue 1 yarn:mohair of great expense: ruled out position(s) 4
17. [order] from clue 9 knitter:Maudie: ruled out position(s) 3
18. [bijection] knitter:Ebba: ruled out position(s) 1,4
19. [bijection] knitter:Angus: ruled out position(s) 1,4
20. [bijection] knitter:Ebba: ruled out position(s) 3
21. [bijection] project:a fisherman's gansey: ruled out position(s) 2,4
22. [bijection] yarn:undyed Shetland: ruled out position(s) 1,2
23. [bijection] yarn:recycled sari silk: ruled out position(s) 1,2
24. [direct] from clue 6 yarn:recycled sari silk: ruled out position(s) 3
25. [bijection] yarn:undyed Shetland: ruled out position(s) 4

---

<sub>seed `2026172717978` &middot; score 4.93 &middot; atoms 9 &middot; positives 2 &middot; solved by order</sub>
