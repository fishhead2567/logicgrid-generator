# The Saltmarsh Light Rotation

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `f6783ebf8643`

## Introduction

The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.
Four keepers are involved. Determine each keeper's day, chore and weather.
- **Keeper**: Lucian, Clementine, Saoirse and Hollis.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday and Thursday.
- **Logged chore**: overhauling the foghorn, splicing the hoist rope, rebedding the storm glass and regrinding the lens.
- **Weather noted**: a flat calm, sleet, sea fog and drizzle.
Every keeper has a different day, chore and weather, so within each category every item is used exactly once.

## Clues

1. Clementine logs overhauling the foghorn.
2. The keeper who notes sleet falls somewhere between the keeper who logs regrinding the lens and Tuesday in day order.
3. The keeper who notes a flat calm is later than Wednesday in day order.
4. Hollis falls somewhere between the keeper who logs overhauling the foghorn and Monday in day order.
5. The keeper who logs splicing the hoist rope falls somewhere between Monday and Saoirse in day order.
6. The keeper who notes sea fog and Tuesday are exactly one day apart in day order, in one direction or the other.

## Solving chart

*Day vs Keeper*

| | Lucian | Clementine | Saoirse | Hollis |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Logged chore*

| | overhauling the foghorn | splicing the hoist rope | rebedding the storm glass | regrinding the lens |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Weather noted*

| | a flat calm | sleet | sea fog | drizzle |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Keeper vs Logged chore*

| | overhauling the foghorn | splicing the hoist rope | rebedding the storm glass | regrinding the lens |
|---|---|---|---|---|
| **Lucian** | | | | |
| **Clementine** | | | | |
| **Saoirse** | | | | |
| **Hollis** | | | | |

*Keeper vs Weather noted*

| | a flat calm | sleet | sea fog | drizzle |
|---|---|---|---|---|
| **Lucian** | | | | |
| **Clementine** | | | | |
| **Saoirse** | | | | |
| **Hollis** | | | | |

*Logged chore vs Weather noted*

| | a flat calm | sleet | sea fog | drizzle |
|---|---|---|---|---|
| **overhauling the foghorn** | | | | |
| **splicing the hoist rope** | | | | |
| **rebedding the storm glass** | | | | |
| **regrinding the lens** | | | | |

## Solution

| Day | Keeper | Logged chore | Weather noted |
|---|---|---|---|
| Monday | Lucian | rebedding the storm glass | sea fog |
| Tuesday | Hollis | splicing the hoist rope | drizzle |
| Wednesday | Clementine | overhauling the foghorn | sleet |
| Thursday | Saoirse | regrinding the lens | a flat calm |

## How it falls out

1. [order] from clue 5 weather:sleet: ruled out position(s) 1,2,4
2. [order] from clue 5 chore:regrinding the lens: ruled out position(s) 1,2,3
3. [order] from clue 4 chore:splicing the hoist rope: ruled out position(s) 1,4
4. [order] from clue 4 keeper:Saoirse: ruled out position(s) 1,2
5. [order] from clue 3 weather:sea fog: ruled out position(s) 2,4
6. [order] from clue 2 weather:a flat calm: ruled out position(s) 1,2,3
7. [order] from clue 1 keeper:Hollis: ruled out position(s) 1,4
8. [order] from clue 1 chore:overhauling the foghorn: ruled out position(s) 1,2
9. [direct] from clue 6 keeper:Clementine: ruled out position(s) 1,2
10. [bijection] chore:overhauling the foghorn: ruled out position(s) 4
11. [bijection] chore:rebedding the storm glass: ruled out position(s) 4
12. [bijection] chore:rebedding the storm glass: ruled out position(s) 2,3
13. [bijection] keeper:Lucian: ruled out position(s) 2,3,4
14. [bijection] weather:sea fog: ruled out position(s) 3
15. [bijection] weather:drizzle: ruled out position(s) 3,4
16. [bijection] weather:drizzle: ruled out position(s) 1
17. [direct] from clue 6 keeper:Clementine: ruled out position(s) 4
18. [order] from clue 1 keeper:Hollis: ruled out position(s) 3
19. [bijection] chore:splicing the hoist rope: ruled out position(s) 3
20. [bijection] keeper:Saoirse: ruled out position(s) 3

---

<sub>seed `2026172814788` &middot; score 5.13 &middot; atoms 6 &middot; positives 1 &middot; solved by order</sub>
