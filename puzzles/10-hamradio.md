# Field Day on Barrow Hill

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `b143dae5487e`

## Introduction

A club field day spread over a week, one operator a night, and a generator that has its own opinions.
Five operators are involved. Determine each operator's night and mode.
- **Operator**: Horace, Yusuf, Clementine, Bartholomew and Nkem.
- **Night** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Mode**: CW, RTTY, FT8, AM and SSB.
Every operator has a different night and mode, so within each category every item is used exactly once.

## Clues

1. The operator who operates SSB operates on Friday.
2. The operator who operates RTTY operates on Monday.
3. Nkem does not operate on Wednesday. The operator who operates AM and Wednesday are exactly one day apart in night order, in one direction or the other.
4. Horace is earlier than Tuesday in night order.
5. Horace is exactly one day earlier than the operator who operates CW, with no night in between.
6. The operator who operates FT8 and Yusuf are exactly one day apart in night order, in one direction or the other.
7. Bartholomew is exactly one day earlier than the operator who operates SSB, with no night in between.

## Solving chart

*Night vs Operator*

| | Horace | Yusuf | Clementine | Bartholomew | Nkem |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Night vs Mode*

| | CW | RTTY | FT8 | AM | SSB |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Operator vs Mode*

| | CW | RTTY | FT8 | AM | SSB |
|---|---|---|---|---|---|
| **Horace** | | | | | |
| **Yusuf** | | | | | |
| **Clementine** | | | | | |
| **Bartholomew** | | | | | |
| **Nkem** | | | | | |

## Solution

| Night | Operator | Mode |
|---|---|---|
| Monday | Horace | RTTY |
| Tuesday | Yusuf | CW |
| Wednesday | Clementine | FT8 |
| Thursday | Bartholomew | AM |
| Friday | Nkem | SSB |

## How it falls out

1. [direct] from clue 5 operator:Nkem: ruled out position(s) 3
2. [direct] from clue 2 mode:SSB: ruled out position(s) 1,2,3,4
3. [direct] from clue 1 mode:RTTY: ruled out position(s) 2,3,4,5
4. [bijection] mode:CW: ruled out position(s) 1,5
5. [bijection] mode:FT8: ruled out position(s) 1,5
6. [bijection] mode:AM: ruled out position(s) 1,5
7. [order] from clue 8 operator:Horace: ruled out position(s) 2,3,4,5
8. [order] from clue 6 operator:Bartholomew: ruled out position(s) 1,2,3,5
9. [order] from clue 4 mode:AM: ruled out position(s) 3
10. [order] from clue 3 mode:CW: ruled out position(s) 3,4
11. [bijection] mode:FT8: ruled out position(s) 2
12. [bijection] mode:AM: ruled out position(s) 2
13. [bijection] mode:FT8: ruled out position(s) 4
14. [bijection] operator:Yusuf: ruled out position(s) 1,4
15. [bijection] operator:Clementine: ruled out position(s) 1,4
16. [bijection] operator:Nkem: ruled out position(s) 1,4
17. [order] from clue 7 operator:Yusuf: ruled out position(s) 3,5
18. [bijection] operator:Clementine: ruled out position(s) 2
19. [bijection] operator:Nkem: ruled out position(s) 2
20. [bijection] operator:Clementine: ruled out position(s) 5

---

<sub>seed `2026172754629` &middot; score 4.62 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
