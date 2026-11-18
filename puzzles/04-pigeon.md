# Andy's Swiftest Birds

*Andy races pigeons, and each bird is bred for a different combination of stubbornness and speed.*

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `5a84c8f6c609`

## Introduction

There are 4 races. Each has exactly one distance and one item from every other category below, and within each category every item belongs to a different race.
- **Distance** (listed in order): 200 miles, 300 miles, 400 miles and 500 miles.
- **Breed**: a Vandenabeele, a Van Loon, a Delbar and a Janssen.
- **Loft**: the garage loft, the orchard loft, the allotment loft and the canal loft.
The hundred mileses above are listed in order, from 200 miles to 500 miles.

## Clues

1. A Janssen goes with 200 miles.
2. A Vandenabeele goes with the canal loft. A Vandenabeele goes with 300 miles.
3. A Delbar goes with the orchard loft.
4. A Van Loon does not go with 500 miles.
5. 400 miles does not go with the garage loft.

## Solving chart

*Distance vs Breed*

| | a Vandenabeele | a Van Loon | a Delbar | a Janssen |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Loft*

| | the garage loft | the orchard loft | the allotment loft | the canal loft |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Breed vs Loft*

| | the garage loft | the orchard loft | the allotment loft | the canal loft |
|---|---|---|---|---|
| **a Vandenabeele** | | | | |
| **a Van Loon** | | | | |
| **a Delbar** | | | | |
| **a Janssen** | | | | |

## Solution

| Distance | Breed | Loft |
|---|---|---|
| 200 miles | a Janssen | the garage loft |
| 300 miles | a Vandenabeele | the canal loft |
| 400 miles | a Van Loon | the allotment loft |
| 500 miles | a Delbar | the orchard loft |

## How it falls out

1. [direct] from clue 6 breed:a Van Loon: ruled out position(s) 4
2. [direct] from clue 4 breed:a Janssen: ruled out position(s) 2,3,4
3. [direct] from clue 3 loft:the garage loft: ruled out position(s) 3
4. [direct] from clue 1 breed:a Vandenabeele: ruled out position(s) 1,3,4
5. [direct] from clue 2 loft:the canal loft: ruled out position(s) 1,3,4
6. [bijection] breed:a Van Loon: ruled out position(s) 1,2
7. [bijection] breed:a Delbar: ruled out position(s) 1,2
8. [bijection] breed:a Delbar: ruled out position(s) 3
9. [bijection] loft:the garage loft: ruled out position(s) 2
10. [bijection] loft:the orchard loft: ruled out position(s) 2
11. [bijection] loft:the allotment loft: ruled out position(s) 2
12. [direct] from clue 5 loft:the orchard loft: ruled out position(s) 1,3
13. [bijection] loft:the garage loft: ruled out position(s) 4
14. [bijection] loft:the allotment loft: ruled out position(s) 4
15. [bijection] loft:the allotment loft: ruled out position(s) 1

---

<sub>seed `2026172607112` &middot; score 2.585 &middot; atoms 6 &middot; positives 4 &middot; solved by bijection</sub>
