# The Mudflat Regatta

*The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.*

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `9996ef4afd32`

## Introduction

There are 5 entries. Each has exactly one placing and one item from every other category below, and within each category every item belongs to a different entry.
- **Placing** (listed in order): first, second, third, fourth and fifth.
- **Stroke**: Everard, Bartholomew, Yusuf, Ondine and Maeve.
- **Boat**: the Gilded Eel, the Wet Hen, the Mudlark, the Last Resort and the Peregrine.
The places above are listed in order, from first to fifth.

## Clues

1. Fifth goes with Ondine.
2. The Mudlark goes with second.
3. First is immediately better than Everard's placing, with no placing in between.
4. Second is immediately better than the Wet Hen's placing, with no placing in between.
5. The Last Resort and third are next to each other in placing order, in one order or the other. The Last Resort does not go with Maeve.
6. Bartholomew's placing is immediately better than fourth, with no placing in between.
7. Fourth is immediately better than the Gilded Eel's placing, with no placing in between.

## Solving chart

*Placing vs Stroke*

| | Everard | Bartholomew | Yusuf | Ondine | Maeve |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Boat*

| | the Gilded Eel | the Wet Hen | the Mudlark | the Last Resort | the Peregrine |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Stroke vs Boat*

| | the Gilded Eel | the Wet Hen | the Mudlark | the Last Resort | the Peregrine |
|---|---|---|---|---|---|
| **Everard** | | | | | |
| **Bartholomew** | | | | | |
| **Yusuf** | | | | | |
| **Ondine** | | | | | |
| **Maeve** | | | | | |

## Solution

| Placing | Stroke | Boat |
|---|---|---|
| first | Maeve | the Peregrine |
| second | Everard | the Mudlark |
| third | Bartholomew | the Wet Hen |
| fourth | Yusuf | the Last Resort |
| fifth | Ondine | the Gilded Eel |

## How it falls out

1. [direct] from clue 8 stroke:Ondine: ruled out position(s) 1,2,3,4
2. [direct] from clue 1 boat:the Mudlark: ruled out position(s) 1,3,4,5
3. [bijection] boat:the Gilded Eel: ruled out position(s) 2
4. [bijection] boat:the Wet Hen: ruled out position(s) 2
5. [bijection] boat:the Last Resort: ruled out position(s) 2
6. [bijection] boat:the Peregrine: ruled out position(s) 2
7. [bijection] stroke:Everard: ruled out position(s) 5
8. [bijection] stroke:Bartholomew: ruled out position(s) 5
9. [bijection] stroke:Yusuf: ruled out position(s) 5
10. [bijection] stroke:Maeve: ruled out position(s) 5
11. [order] from clue 7 stroke:Bartholomew: ruled out position(s) 1,2,4
12. [order] from clue 5 boat:the Gilded Eel: ruled out position(s) 1,3,4
13. [order] from clue 4 boat:the Last Resort: ruled out position(s) 1,3,5
14. [order] from clue 3 stroke:Everard: ruled out position(s) 1,3,4
15. [order] from clue 2 boat:the Wet Hen: ruled out position(s) 1,4,5
16. [direct] from clue 6 stroke:Maeve: ruled out position(s) 4
17. [bijection] boat:the Peregrine: ruled out position(s) 3,4,5
18. [bijection] stroke:Yusuf: ruled out position(s) 2,3
19. [bijection] stroke:Maeve: ruled out position(s) 2,3
20. [bijection] stroke:Yusuf: ruled out position(s) 1

---

<sub>seed `2026172919517` &middot; score 4.62 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
