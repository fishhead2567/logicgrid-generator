# The Saltmarsh Light Rotation

*The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `604c15777ca6`

## Introduction

There are 4 shifts. Each has exactly one day and one item from every other category below, and within each category every item belongs to a different shift.
- **Day** (listed in order): Monday, Tuesday, Wednesday and Thursday.
- **Keeper**: Barnaby, Perpetua, Hollis and Lucian.
- **Logged chore**: whitewashing the base, rebedding the storm glass, splicing the hoist rope and repainting the gallery.
- **Weather noted**: a gale, sea fog, sleet and drizzle.
The days above are listed in order, from Monday to Thursday.

## Clues

1. Lucian goes with drizzle. Repainting the gallery falls somewhere between Barnaby and drizzle in day order.
2. Wednesday falls somewhere between splicing the hoist rope and sea fog in day order. Splicing the hoist rope's day is immediately earlier than a gale's day, with no day in between.
3. Whitewashing the base's day is earlier than Thursday.
4. Tuesday does not go with a gale.
5. Perpetua's day is immediately earlier than repainting the gallery's day, with no day in between.

## Solving chart

*Day vs Keeper*

| | Barnaby | Perpetua | Hollis | Lucian |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Logged chore*

| | whitewashing the base | rebedding the storm glass | splicing the hoist rope | repainting the gallery |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Day vs Weather noted*

| | a gale | sea fog | sleet | drizzle |
|---|---|---|---|---|
| **Monday** | | | | |
| **Tuesday** | | | | |
| **Wednesday** | | | | |
| **Thursday** | | | | |

*Keeper vs Logged chore*

| | whitewashing the base | rebedding the storm glass | splicing the hoist rope | repainting the gallery |
|---|---|---|---|---|
| **Barnaby** | | | | |
| **Perpetua** | | | | |
| **Hollis** | | | | |
| **Lucian** | | | | |

*Keeper vs Weather noted*

| | a gale | sea fog | sleet | drizzle |
|---|---|---|---|---|
| **Barnaby** | | | | |
| **Perpetua** | | | | |
| **Hollis** | | | | |
| **Lucian** | | | | |

*Logged chore vs Weather noted*

| | a gale | sea fog | sleet | drizzle |
|---|---|---|---|---|
| **whitewashing the base** | | | | |
| **rebedding the storm glass** | | | | |
| **splicing the hoist rope** | | | | |
| **repainting the gallery** | | | | |

## Solution

| Day | Keeper | Logged chore | Weather noted |
|---|---|---|---|
| Monday | Lucian | whitewashing the base | drizzle |
| Tuesday | Perpetua | splicing the hoist rope | sleet |
| Wednesday | Hollis | repainting the gallery | a gale |
| Thursday | Barnaby | rebedding the storm glass | sea fog |

## How it falls out

1. [direct] from clue 5 weather:a gale: ruled out position(s) 2
2. [order] from clue 7 chore:whitewashing the base: ruled out position(s) 4
3. [order] from clue 4 chore:splicing the hoist rope: ruled out position(s) 3
4. [order] from clue 4 weather:sea fog: ruled out position(s) 3
5. [order] from clue 3 keeper:Perpetua: ruled out position(s) 4
6. [order] from clue 3 chore:repainting the gallery: ruled out position(s) 1
7. [order] from clue 2 chore:splicing the hoist rope: ruled out position(s) 1,4
8. [order] from clue 2 weather:a gale: ruled out position(s) 1,4
9. [order] from clue 4 weather:sea fog: ruled out position(s) 1,2
10. [order] from clue 1 chore:repainting the gallery: ruled out position(s) 4
11. [order] from clue 3 keeper:Perpetua: ruled out position(s) 3
12. [bijection] chore:whitewashing the base: ruled out position(s) 2
13. [bijection] chore:rebedding the storm glass: ruled out position(s) 2
14. [bijection] chore:repainting the gallery: ruled out position(s) 2
15. [bijection] chore:rebedding the storm glass: ruled out position(s) 1,3
16. [bijection] weather:sleet: ruled out position(s) 3,4
17. [bijection] weather:drizzle: ruled out position(s) 3,4
18. [direct] from clue 6 keeper:Lucian: ruled out position(s) 3,4
19. [order] from clue 3 keeper:Perpetua: ruled out position(s) 1
20. [order] from clue 1 keeper:Barnaby: ruled out position(s) 1,2,3
21. [bijection] chore:whitewashing the base: ruled out position(s) 3
22. [bijection] keeper:Hollis: ruled out position(s) 2,4
23. [bijection] keeper:Lucian: ruled out position(s) 2
24. [bijection] keeper:Hollis: ruled out position(s) 1
25. [direct] from clue 6 weather:drizzle: ruled out position(s) 2
26. [bijection] weather:sleet: ruled out position(s) 1

---

<sub>seed `2026172702140` &middot; score 5.13 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
