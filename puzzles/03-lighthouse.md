# The Saltmarsh Light Rotation

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 3 &nbsp;&nbsp; **id** `74e84d425b39`

## Introduction

The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.
Four keepers are involved. Determine each keeper's day and chore.
- **Keeper**: Clementine, Emmerich, Perpetua and Lucian.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday and Thursday.
- **Logged chore**: rewiring the beacon, regrinding the lens, splicing the hoist rope and overhauling the foghorn.
Every keeper has a different day and chore, so within each category every item is used exactly once.

## Clues

1. The keeper who logs splicing the hoist rope works on Monday. Lucian logs splicing the hoist rope.
2. The keeper who logs overhauling the foghorn and Thursday are exactly one day apart in day order, in one direction or the other. Clementine does not work on Thursday.
3. The keeper who logs regrinding the lens is exactly one day earlier than Emmerich, with no day in between.

## Solving chart

*Day vs Keeper*

| | Clementine | Emmerich | Perpetua | Lucian |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Logged chore*

| | rewiring the beacon | regrinding the lens | splicing the hoist rope | overhauling the foghorn |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Keeper vs Logged chore*

| | rewiring the beacon | regrinding the lens | splicing the hoist rope | overhauling the foghorn |
|---|---|---|---|---|
| **Clementine** | | | | |
| **Emmerich** | | | | |
| **Perpetua** | | | | |
| **Lucian** | | | | |

## Solution

| Day | Keeper | Logged chore |
|---|---|---|
| Monday | Lucian | splicing the hoist rope |
| Tuesday | Clementine | regrinding the lens |
| Wednesday | Emmerich | overhauling the foghorn |
| Thursday | Perpetua | rewiring the beacon |

## How it falls out

1. [direct] from clue 2 keeper:Clementine: ruled out position(s) 4
2. [direct] from clue 1 chore:splicing the hoist rope: ruled out position(s) 2,3,4
3. [direct] from clue 3 keeper:Lucian: ruled out position(s) 2,3,4
4. [bijection] chore:rewiring the beacon: ruled out position(s) 1
5. [bijection] chore:regrinding the lens: ruled out position(s) 1
6. [bijection] chore:overhauling the foghorn: ruled out position(s) 1
7. [bijection] keeper:Clementine: ruled out position(s) 1
8. [bijection] keeper:Emmerich: ruled out position(s) 1
9. [bijection] keeper:Perpetua: ruled out position(s) 1
10. [order] from clue 5 chore:overhauling the foghorn: ruled out position(s) 2,4
11. [order] from clue 4 chore:regrinding the lens: ruled out position(s) 4
12. [order] from clue 4 keeper:Emmerich: ruled out position(s) 2
13. [bijection] chore:rewiring the beacon: ruled out position(s) 3
14. [bijection] chore:regrinding the lens: ruled out position(s) 3
15. [bijection] chore:rewiring the beacon: ruled out position(s) 2
16. [order] from clue 4 keeper:Emmerich: ruled out position(s) 4
17. [bijection] keeper:Clementine: ruled out position(s) 3
18. [bijection] keeper:Perpetua: ruled out position(s) 3
19. [bijection] keeper:Perpetua: ruled out position(s) 2

---

<sub>seed `2026172799199` &middot; score 4.27 &middot; atoms 5 &middot; positives 2 &middot; solved by order</sub>
