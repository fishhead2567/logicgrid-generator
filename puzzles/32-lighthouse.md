# The Saltmarsh Light Rotation

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 14 &nbsp;&nbsp; **id** `4c1b468385fd`

## Introduction

The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.
Five keepers are involved. Determine each keeper's day, lighthouse, chore and weather.
- **Keeper**: Hollis, Lucian, Perpetua, Emmerich and Clementine.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Lighthouse**: Thimble Reef, Mawes Point, Gannet Rock, Pelter Head and Cold Harbour.
- **Logged chore**: splicing the hoist rope, rebedding the storm glass, rewiring the beacon, repainting the gallery and overhauling the foghorn.
- **Weather noted**: sea fog, a gale, drizzle, thunder and sleet.
Every keeper has a different day, lighthouse, chore and weather, so within each category every item is used exactly once.

## Clues

1. The keeper who is stationed at Gannet Rock works on Wednesday.
2. The keeper who notes a gale and Friday are exactly four days apart in day order.
3. Clementine falls somewhere between Thursday and the keeper who is stationed at Thimble Reef in day order.
4. Lucian is exactly one day earlier than Friday, with no day in between.
5. At least one of the following holds, and possibly more than one: (a) The keeper who is stationed at Mawes Point and Wednesday are exactly two days apart in day order. (b) Clementine notes sleet.
6. Clementine is exactly one day earlier than the keeper who logs repainting the gallery, with no day in between.
7. The keeper who is stationed at Gannet Rock is exactly one day earlier than the keeper who logs rewiring the beacon, with no day in between.
8. The keeper who logs rewiring the beacon does not note sleet.
9. The keeper who notes sea fog falls somewhere between Perpetua and the keeper who is stationed at Gannet Rock in day order.
10. The keeper who logs splicing the hoist rope is not stationed at Mawes Point.
11. At least one of the following holds, and possibly more than one: (a) The keeper who is stationed at Cold Harbour and the keeper who notes drizzle are exactly one day apart in day order, in one direction or the other. (b) Clementine notes sleet.
12. The keeper who logs repainting the gallery and Hollis are exactly two days apart in day order.
13. The keeper who logs overhauling the foghorn and Perpetua are exactly one day apart in day order, in one direction or the other.
14. At least one of the following holds, and possibly more than one: (a) The keeper who logs rebedding the storm glass and Hollis are exactly one day apart in day order, in one direction or the other. (b) The keeper who is stationed at Pelter Head is exactly one day earlier than Hollis, with no day in between.

## Solving chart

*Day vs Keeper*

| | Hollis | Lucian | Perpetua | Emmerich | Clementine |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Lighthouse*

| | Thimble Reef | Mawes Point | Gannet Rock | Pelter Head | Cold Harbour |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Logged chore*

| | splicing the hoist rope | rebedding the storm glass | rewiring the beacon | repainting the gallery | overhauling the foghorn |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Weather noted*

| | sea fog | a gale | drizzle | thunder | sleet |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Keeper vs Lighthouse*

| | Thimble Reef | Mawes Point | Gannet Rock | Pelter Head | Cold Harbour |
|---|---|---|---|---|---|
| **Hollis** | | | | | |
| **Lucian** | | | | | |
| **Perpetua** | | | | | |
| **Emmerich** | | | | | |
| **Clementine** | | | | | |

*Keeper vs Logged chore*

| | splicing the hoist rope | rebedding the storm glass | rewiring the beacon | repainting the gallery | overhauling the foghorn |
|---|---|---|---|---|---|
| **Hollis** | | | | | |
| **Lucian** | | | | | |
| **Perpetua** | | | | | |
| **Emmerich** | | | | | |
| **Clementine** | | | | | |

*Keeper vs Weather noted*

| | sea fog | a gale | drizzle | thunder | sleet |
|---|---|---|---|---|---|
| **Hollis** | | | | | |
| **Lucian** | | | | | |
| **Perpetua** | | | | | |
| **Emmerich** | | | | | |
| **Clementine** | | | | | |

*Lighthouse vs Logged chore*

| | splicing the hoist rope | rebedding the storm glass | rewiring the beacon | repainting the gallery | overhauling the foghorn |
|---|---|---|---|---|---|
| **Thimble Reef** | | | | | |
| **Mawes Point** | | | | | |
| **Gannet Rock** | | | | | |
| **Pelter Head** | | | | | |
| **Cold Harbour** | | | | | |

*Lighthouse vs Weather noted*

| | sea fog | a gale | drizzle | thunder | sleet |
|---|---|---|---|---|---|
| **Thimble Reef** | | | | | |
| **Mawes Point** | | | | | |
| **Gannet Rock** | | | | | |
| **Pelter Head** | | | | | |
| **Cold Harbour** | | | | | |

*Logged chore vs Weather noted*

| | sea fog | a gale | drizzle | thunder | sleet |
|---|---|---|---|---|---|
| **splicing the hoist rope** | | | | | |
| **rebedding the storm glass** | | | | | |
| **rewiring the beacon** | | | | | |
| **repainting the gallery** | | | | | |
| **overhauling the foghorn** | | | | | |

## Solution

| Day | Keeper | Lighthouse | Logged chore | Weather noted |
|---|---|---|---|---|
| Monday | Perpetua | Thimble Reef | splicing the hoist rope | a gale |
| Tuesday | Clementine | Cold Harbour | overhauling the foghorn | sea fog |
| Wednesday | Emmerich | Gannet Rock | repainting the gallery | drizzle |
| Thursday | Lucian | Pelter Head | rewiring the beacon | thunder |
| Friday | Hollis | Mawes Point | rebedding the storm glass | sleet |

## How it falls out

1. [direct] from clue 7 light:Gannet Rock: ruled out position(s) 1,2,4,5
2. [bijection] light:Thimble Reef: ruled out position(s) 3
3. [bijection] light:Mawes Point: ruled out position(s) 3
4. [bijection] light:Pelter Head: ruled out position(s) 3
5. [bijection] light:Cold Harbour: ruled out position(s) 3
6. [order] from clue 13 weather:sea fog: ruled out position(s) 1,3,5
7. [order] from clue 13 keeper:Perpetua: ruled out position(s) 2,3,4
8. [order] from clue 11 chore:rewiring the beacon: ruled out position(s) 1,2,3,5
9. [order] from clue 9 keeper:Clementine: ruled out position(s) 1,4,5
10. [order] from clue 9 light:Thimble Reef: ruled out position(s) 4,5
11. [order] from clue 8 weather:a gale: ruled out position(s) 2,3,4,5
12. [order] from clue 5 chore:overhauling the foghorn: ruled out position(s) 1,3,5
13. [order] from clue 2 keeper:Lucian: ruled out position(s) 1,2,3,5
14. [order] from clue 1 chore:repainting the gallery: ruled out position(s) 1,2,5
15. [order] from clue 14 keeper:Hollis: ruled out position(s) 3,4
16. [direct] from clue 12 weather:sleet: ruled out position(s) 4
17. [bijection] chore:splicing the hoist rope: ruled out position(s) 4
18. [bijection] chore:rebedding the storm glass: ruled out position(s) 4
19. [bijection] chore:repainting the gallery: ruled out position(s) 4
20. [bijection] chore:overhauling the foghorn: ruled out position(s) 4
21. [bijection] keeper:Emmerich: ruled out position(s) 4
22. [bijection] weather:drizzle: ruled out position(s) 1
23. [bijection] weather:thunder: ruled out position(s) 1
24. [bijection] weather:sleet: ruled out position(s) 1
25. [order] from clue 5 keeper:Perpetua: ruled out position(s) 5
26. [order] from clue 13 weather:sea fog: ruled out position(s) 4
27. [order] from clue 14 keeper:Hollis: ruled out position(s) 2
28. [order] from clue 1 keeper:Clementine: ruled out position(s) 3
29. [order] from clue 9 light:Thimble Reef: ruled out position(s) 2
30. [bijection] chore:splicing the hoist rope: ruled out position(s) 2,3
31. [bijection] chore:rebedding the storm glass: ruled out position(s) 2,3
32. [bijection] keeper:Hollis: ruled out position(s) 1
33. [bijection] keeper:Emmerich: ruled out position(s) 1,2
34. [bijection] keeper:Emmerich: ruled out position(s) 5
35. [bijection] light:Mawes Point: ruled out position(s) 1
36. [bijection] light:Pelter Head: ruled out position(s) 1
37. [bijection] light:Cold Harbour: ruled out position(s) 1
38. [bijection] weather:drizzle: ruled out position(s) 2
39. [bijection] weather:thunder: ruled out position(s) 2
40. [bijection] weather:sleet: ruled out position(s) 2
_... and 8 further steps._

---

<sub>seed `2026172828844` &middot; score 10.3003 &middot; atoms 14 &middot; positives 1 &middot; solved by disjunction</sub>
