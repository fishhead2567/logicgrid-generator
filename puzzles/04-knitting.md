# The Thornwood Knitting Circle

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `fd2b2cc374e3`

## Introduction

The Thornwood Knitting Circle meets weekly and has not agreed on anything since 1998.
Five knitters are involved. Determine each knitter's day and yarn.
- **Knitter**: Willem, Maddie, Ebba, Angus and Serafina.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Yarn**: mohair of great expense, nettle fiber, mill-end acrylic, undyed Shetland and recycled sari silk.
Every knitter has a different day and yarn, so within each category every item is used exactly once.

## Clues

1. Ebba knits on Tuesday.
2. Serafina knits on Friday.
3. Maddie knits on Thursday.
4. Monday is exactly one day earlier than the knitter who works in recycled sari silk, with no day in between. The knitter who works in mill-end acrylic does not knit on Monday.
5. Ebba is exactly one day earlier than the knitter who works in mohair of great expense, with no day in between.
6. Angus is exactly one day earlier than the knitter who works in nettle fiber, with no day in between.

## Solving chart

*Day vs Knitter*

| | Willem | Maddie | Ebba | Angus | Serafina |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Yarn*

| | mohair of great expense | nettle fiber | mill-end acrylic | undyed Shetland | recycled sari silk |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Knitter vs Yarn*

| | mohair of great expense | nettle fiber | mill-end acrylic | undyed Shetland | recycled sari silk |
|---|---|---|---|---|---|
| **Willem** | | | | | |
| **Maddie** | | | | | |
| **Ebba** | | | | | |
| **Angus** | | | | | |
| **Serafina** | | | | | |

## Solution

| Day | Knitter | Yarn |
|---|---|---|
| Monday | Willem | undyed Shetland |
| Tuesday | Ebba | recycled sari silk |
| Wednesday | Angus | mohair of great expense |
| Thursday | Maddie | nettle fiber |
| Friday | Serafina | mill-end acrylic |

## How it falls out

1. [direct] from clue 6 knitter:Maddie: ruled out position(s) 1,2,3,5
2. [direct] from clue 5 knitter:Ebba: ruled out position(s) 1,3,4,5
3. [direct] from clue 3 yarn:mill-end acrylic: ruled out position(s) 1
4. [direct] from clue 2 knitter:Serafina: ruled out position(s) 1,2,3,4
5. [bijection] knitter:Willem: ruled out position(s) 2,4,5
6. [bijection] knitter:Angus: ruled out position(s) 2,4,5
7. [order] from clue 7 yarn:recycled sari silk: ruled out position(s) 1,3,4,5
8. [order] from clue 4 yarn:nettle fiber: ruled out position(s) 1,3,5
9. [order] from clue 1 yarn:mohair of great expense: ruled out position(s) 1,2,4,5
10. [bijection] yarn:nettle fiber: ruled out position(s) 2
11. [bijection] yarn:mill-end acrylic: ruled out position(s) 2,3
12. [bijection] yarn:undyed Shetland: ruled out position(s) 2,3
13. [bijection] yarn:undyed Shetland: ruled out position(s) 4,5
14. [order] from clue 4 knitter:Angus: ruled out position(s) 1
15. [bijection] knitter:Willem: ruled out position(s) 3
16. [bijection] yarn:mill-end acrylic: ruled out position(s) 4

---

<sub>seed `2026172907121` &middot; score 4.38 &middot; atoms 7 &middot; positives 3 &middot; solved by order</sub>
