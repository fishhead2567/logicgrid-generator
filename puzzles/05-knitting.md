# The Ashfold Knitting Circle

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `2f742529c0b3`

## Introduction

The Ashfold Knitting Circle meets weekly and has not agreed on anything since 1998.
Four knitters are involved. Determine each knitter's day and project.
- **Knitter**: Ebba, Lionel, Maudie and Nkechi.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday and Thursday.
- **Project**: a cable-knit blanket, a dog coat, a pair of argyle socks and a fisherman's gansey.
Every knitter has a different day and project, so within each category every item is used exactly once.

## Clues

1. The knitter who is making a pair of argyle socks knits on Tuesday.
2. Nkechi knits on Monday.
3. Maudie is making a cable-knit blanket.
4. The knitter who is making a fisherman's gansey does not knit on Monday.
5. Lionel and the knitter who is making a pair of argyle socks are exactly one day apart in day order, in one direction or the other.

## Solving chart

*Day vs Knitter*

| | Ebba | Lionel | Maudie | Nkechi |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Project*

| | a cable-knit blanket | a dog coat | a pair of argyle socks | a fisherman's gansey |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Knitter vs Project*

| | a cable-knit blanket | a dog coat | a pair of argyle socks | a fisherman's gansey |
|---|---|---|---|---|
| **Ebba** | | | | |
| **Lionel** | | | | |
| **Maudie** | | | | |
| **Nkechi** | | | | |

## Solution

| Day | Knitter | Project |
|---|---|---|
| Monday | Nkechi | a dog coat |
| Tuesday | Ebba | a pair of argyle socks |
| Wednesday | Lionel | a fisherman's gansey |
| Thursday | Maudie | a cable-knit blanket |

## How it falls out

1. [direct] from clue 5 knitter:Nkechi: ruled out position(s) 2,3,4
2. [direct] from clue 4 project:a fisherman's gansey: ruled out position(s) 1
3. [direct] from clue 1 project:a pair of argyle socks: ruled out position(s) 1,3,4
4. [bijection] knitter:Ebba: ruled out position(s) 1
5. [bijection] knitter:Lionel: ruled out position(s) 1
6. [bijection] knitter:Maudie: ruled out position(s) 1
7. [bijection] project:a cable-knit blanket: ruled out position(s) 2
8. [bijection] project:a dog coat: ruled out position(s) 2
9. [bijection] project:a fisherman's gansey: ruled out position(s) 2
10. [direct] from clue 2 knitter:Maudie: ruled out position(s) 2
11. [direct] from clue 2 project:a cable-knit blanket: ruled out position(s) 1
12. [bijection] project:a dog coat: ruled out position(s) 3,4
13. [order] from clue 3 knitter:Lionel: ruled out position(s) 2,4
14. [bijection] knitter:Ebba: ruled out position(s) 3
15. [bijection] knitter:Maudie: ruled out position(s) 3
16. [bijection] knitter:Ebba: ruled out position(s) 4
17. [direct] from clue 2 project:a cable-knit blanket: ruled out position(s) 3
18. [bijection] project:a fisherman's gansey: ruled out position(s) 4

---

<sub>seed `2026172715034` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
