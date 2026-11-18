# The Hollow Creek Pie Judging

*The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.*

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `5fc5504ad617`

## Introduction

There are 4 entries. Each has exactly one placing and one item from every other category below, and within each category every item belongs to a different entry.
- **Placing** (listed in order): first, second, third and fourth.
- **Filling**: mincemeat, sour cherry, buttermilk and green tomato.
- **Home county**: Fenwick, Quarry Hill, Ardmore and Sweetwater.
The places above are listed in order, from first to fourth.

## Clues

1. Ardmore goes with second. Second is immediately better than Sweetwater's placing, with no placing in between.
2. Mincemeat goes with second.
3. Buttermilk goes with third.
4. Fenwick goes with sour cherry.
5. Green tomato does not go with first.

## Solving chart

*Placing vs Filling*

| | mincemeat | sour cherry | buttermilk | green tomato |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Home county*

| | Fenwick | Quarry Hill | Ardmore | Sweetwater |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Filling vs Home county*

| | Fenwick | Quarry Hill | Ardmore | Sweetwater |
|---|---|---|---|---|
| **mincemeat** | | | | |
| **sour cherry** | | | | |
| **buttermilk** | | | | |
| **green tomato** | | | | |

## Solution

| Placing | Filling | Home county |
|---|---|---|
| first | sour cherry | Fenwick |
| second | mincemeat | Ardmore |
| third | buttermilk | Sweetwater |
| fourth | green tomato | Quarry Hill |

## How it falls out

1. [direct] from clue 4 filling:mincemeat: ruled out position(s) 1,3,4
2. [direct] from clue 3 filling:green tomato: ruled out position(s) 1
3. [direct] from clue 2 county:Ardmore: ruled out position(s) 1,3,4
4. [direct] from clue 1 filling:buttermilk: ruled out position(s) 1,2,4
5. [bijection] county:Fenwick: ruled out position(s) 2
6. [bijection] county:Quarry Hill: ruled out position(s) 2
7. [bijection] county:Sweetwater: ruled out position(s) 2
8. [bijection] filling:sour cherry: ruled out position(s) 2,3
9. [bijection] filling:green tomato: ruled out position(s) 2,3
10. [bijection] filling:sour cherry: ruled out position(s) 4
11. [direct] from clue 5 county:Fenwick: ruled out position(s) 3,4
12. [bijection] county:Quarry Hill: ruled out position(s) 1
13. [bijection] county:Sweetwater: ruled out position(s) 1
14. [order] from clue 6 county:Sweetwater: ruled out position(s) 4
15. [bijection] county:Quarry Hill: ruled out position(s) 3

---

<sub>seed `2026172622950` &middot; score 3.67 &middot; atoms 6 &middot; positives 4 &middot; solved by order</sub>
