# The Saltmarsh Light Rotation

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `cb6cea28f93e`

## Introduction

The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.
Four keepers are involved. Determine each keeper's day and lighthouse.
- **Keeper**: Hollis, Barnaby, Lucian and Clementine.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday and Thursday.
- **Lighthouse**: Gannet Rock, Cold Harbour, Mawes Point and Pelter Head.
Every keeper has a different day and lighthouse, so within each category every item is used exactly once.

## Clues

1. Clementine works on Monday.
2. The keeper who is stationed at Gannet Rock works on Monday.
3. The keeper who is stationed at Mawes Point does not work on Thursday.
4. The keeper who is stationed at Pelter Head is exactly one day earlier than Barnaby, with no day in between.
5. Lucian is exactly one day earlier than the keeper who is stationed at Cold Harbour, with no day in between.

## Solving chart

*Day vs Keeper*

| | Hollis | Barnaby | Lucian | Clementine |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Lighthouse*

| | Gannet Rock | Cold Harbour | Mawes Point | Pelter Head |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Keeper vs Lighthouse*

| | Gannet Rock | Cold Harbour | Mawes Point | Pelter Head |
|---|---|---|---|---|
| **Hollis** | | | | |
| **Barnaby** | | | | |
| **Lucian** | | | | |
| **Clementine** | | | | |

## Solution

| Day | Keeper | Lighthouse |
|---|---|---|
| Monday | Clementine | Gannet Rock |
| Tuesday | Hollis | Mawes Point |
| Wednesday | Lucian | Pelter Head |
| Thursday | Barnaby | Cold Harbour |

## How it falls out

1. [direct] from clue 4 light:Gannet Rock: ruled out position(s) 2,3,4
2. [direct] from clue 3 light:Mawes Point: ruled out position(s) 4
3. [direct] from clue 1 keeper:Clementine: ruled out position(s) 2,3,4
4. [bijection] keeper:Hollis: ruled out position(s) 1
5. [bijection] keeper:Barnaby: ruled out position(s) 1
6. [bijection] keeper:Lucian: ruled out position(s) 1
7. [bijection] light:Cold Harbour: ruled out position(s) 1
8. [bijection] light:Mawes Point: ruled out position(s) 1
9. [bijection] light:Pelter Head: ruled out position(s) 1
10. [order] from clue 5 keeper:Lucian: ruled out position(s) 4
11. [order] from clue 5 light:Cold Harbour: ruled out position(s) 2
12. [order] from clue 2 light:Pelter Head: ruled out position(s) 4
13. [order] from clue 2 keeper:Barnaby: ruled out position(s) 2
14. [bijection] light:Cold Harbour: ruled out position(s) 3
15. [order] from clue 5 keeper:Lucian: ruled out position(s) 2
16. [bijection] keeper:Hollis: ruled out position(s) 3
17. [bijection] keeper:Barnaby: ruled out position(s) 3
18. [bijection] keeper:Hollis: ruled out position(s) 4
19. [order] from clue 2 light:Pelter Head: ruled out position(s) 2
20. [bijection] light:Mawes Point: ruled out position(s) 3

---

<sub>seed `2026172930878` &middot; score 4.27 &middot; atoms 5 &middot; positives 2 &middot; solved by order</sub>
