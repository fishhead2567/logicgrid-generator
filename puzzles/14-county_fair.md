# The Hollow Creek Pie Judging

*The Hollow Creek county fair runs its pie judging with more ceremony than the state legislature.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `b49583c97e83`

## Introduction

There are 4 entries. Each has exactly one placing and one item from every other category below, and within each category every item belongs to a different entry.
- **Placing** (listed in order): first, second, third and fourth.
- **Filling**: rhubarb, sour cherry, blackberry and buttermilk.
- **Home county**: Ardmore, Little Pell, Sweetwater and Dunmore.
- **Crust**: a lattice top, a cut-out star top, a fluted rim and a double crust.
The places above are listed in order, from first to fourth.

## Clues

1. Second is immediately better than a lattice top's placing, with no placing in between. Ardmore goes with a lattice top.
2. Rhubarb's placing is better than a cut-out star top's placing. Dunmore goes with rhubarb.
3. First is better than Little Pell's placing. First is immediately better than a double crust's placing, with no placing in between.
4. Blackberry's placing is better than second.
5. Third is immediately better than buttermilk's placing, with no placing in between.

## Solving chart

*Placing vs Filling*

| | rhubarb | sour cherry | blackberry | buttermilk |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Home county*

| | Ardmore | Little Pell | Sweetwater | Dunmore |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Crust*

| | a lattice top | a cut-out star top | a fluted rim | a double crust |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Filling vs Home county*

| | Ardmore | Little Pell | Sweetwater | Dunmore |
|---|---|---|---|---|
| **rhubarb** | | | | |
| **sour cherry** | | | | |
| **blackberry** | | | | |
| **buttermilk** | | | | |

*Filling vs Crust*

| | a lattice top | a cut-out star top | a fluted rim | a double crust |
|---|---|---|---|---|
| **rhubarb** | | | | |
| **sour cherry** | | | | |
| **blackberry** | | | | |
| **buttermilk** | | | | |

*Home county vs Crust*

| | a lattice top | a cut-out star top | a fluted rim | a double crust |
|---|---|---|---|---|
| **Ardmore** | | | | |
| **Little Pell** | | | | |
| **Sweetwater** | | | | |
| **Dunmore** | | | | |

## Solution

| Placing | Filling | Home county | Crust |
|---|---|---|---|
| first | blackberry | Sweetwater | a fluted rim |
| second | rhubarb | Dunmore | a double crust |
| third | sour cherry | Ardmore | a lattice top |
| fourth | buttermilk | Little Pell | a cut-out star top |

## How it falls out

1. [order] from clue 7 crust:a double crust: ruled out position(s) 1,3,4
2. [order] from clue 6 filling:rhubarb: ruled out position(s) 4
3. [order] from clue 6 crust:a cut-out star top: ruled out position(s) 1
4. [order] from clue 5 county:Little Pell: ruled out position(s) 1
5. [order] from clue 4 crust:a lattice top: ruled out position(s) 1,2,4
6. [order] from clue 2 filling:buttermilk: ruled out position(s) 1,2,3
7. [order] from clue 1 filling:blackberry: ruled out position(s) 2,3,4
8. [direct] from clue 8 county:Ardmore: ruled out position(s) 1,2,4
9. [direct] from clue 3 county:Dunmore: ruled out position(s) 4
10. [bijection] county:Little Pell: ruled out position(s) 3
11. [bijection] county:Sweetwater: ruled out position(s) 3
12. [bijection] county:Dunmore: ruled out position(s) 3
13. [bijection] crust:a cut-out star top: ruled out position(s) 2,3
14. [bijection] crust:a fluted rim: ruled out position(s) 2,3
15. [bijection] crust:a fluted rim: ruled out position(s) 4
16. [bijection] filling:rhubarb: ruled out position(s) 1
17. [bijection] filling:sour cherry: ruled out position(s) 1,4
18. [direct] from clue 3 county:Dunmore: ruled out position(s) 1
19. [direct] from clue 3 filling:rhubarb: ruled out position(s) 3
20. [bijection] county:Little Pell: ruled out position(s) 2
21. [bijection] county:Sweetwater: ruled out position(s) 2
22. [bijection] county:Sweetwater: ruled out position(s) 4
23. [bijection] filling:sour cherry: ruled out position(s) 2

---

<sub>seed `2026172686302` &middot; score 4.93 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
