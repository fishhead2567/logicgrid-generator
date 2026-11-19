# The Saltmarsh Light Rotation

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `f8e494d9163f`

## Introduction

The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.
Four keepers are involved. Determine each keeper's day and weather.
- **Keeper**: Lucian, Barnaby, Hollis and Perpetua.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday and Thursday.
- **Weather noted**: thunder, a gale, drizzle and sea fog.
Every keeper has a different day and weather, so within each category every item is used exactly once.

## Clues

1. The keeper who notes a gale works on Wednesday.
2. Perpetua notes thunder.
3. Lucian notes drizzle.
4. The keeper who notes drizzle does not work on Tuesday.
5. Hollis and Wednesday are exactly one day apart in day order, in one direction or the other.
6. Wednesday is exactly one day earlier than the keeper who notes sea fog, with no day in between.

## Solving chart

*Day vs Keeper*

| | Lucian | Barnaby | Hollis | Perpetua |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Weather noted*

| | thunder | a gale | drizzle | sea fog |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Keeper vs Weather noted*

| | thunder | a gale | drizzle | sea fog |
|---|---|---|---|---|
| **Lucian** | | | | |
| **Barnaby** | | | | |
| **Hollis** | | | | |
| **Perpetua** | | | | |

## Solution

| Day | Keeper | Weather noted |
|---|---|---|
| Monday | Lucian | drizzle |
| Tuesday | Perpetua | thunder |
| Wednesday | Barnaby | a gale |
| Thursday | Hollis | sea fog |

## How it falls out

1. [direct] from clue 5 weather:a gale: ruled out position(s) 1,2,4
2. [direct] from clue 1 weather:drizzle: ruled out position(s) 2
3. [direct] from clue 4 keeper:Lucian: ruled out position(s) 2
4. [bijection] weather:thunder: ruled out position(s) 3
5. [bijection] weather:drizzle: ruled out position(s) 3
6. [bijection] weather:sea fog: ruled out position(s) 3
7. [direct] from clue 4 keeper:Lucian: ruled out position(s) 3
8. [direct] from clue 3 keeper:Perpetua: ruled out position(s) 3
9. [order] from clue 6 keeper:Hollis: ruled out position(s) 1,3
10. [order] from clue 2 weather:sea fog: ruled out position(s) 1,2
11. [bijection] keeper:Barnaby: ruled out position(s) 1,2,4
12. [bijection] weather:thunder: ruled out position(s) 4
13. [bijection] weather:drizzle: ruled out position(s) 4
14. [bijection] weather:thunder: ruled out position(s) 1
15. [direct] from clue 4 keeper:Lucian: ruled out position(s) 4
16. [direct] from clue 3 keeper:Perpetua: ruled out position(s) 1,4
17. [bijection] keeper:Hollis: ruled out position(s) 2

---

<sub>seed `2026172691277` &middot; score 3.97 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
