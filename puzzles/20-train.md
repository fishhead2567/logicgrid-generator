# The Loft Layout Dispute

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `b17bdaedfe62`

## Introduction

The members of the model railway society share one loft layout and a deep well of resentment.
Five modellers are involved. Determine each modeller's shelf, stock and scenery.
- **Modeller**: Rosamond, Gilbert, Abiodun, Cuthbert and Hendrik.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Rolling stock**: a scratch-built crane wagon, a brass pannier tank, a rake of milk tankers, a battered autocoach and a kit-built brake van.
- **Scenery**: a plaster tunnel mouth, a coal staithe, a cardboard viaduct, a flocked cutting and a working level crossing.
Every modeller has a different shelf, stock and scenery, so within each category every item is used exactly once.

## Clues

1. Hendrik and the fifth shelf are exactly one shelf apart in shelf order, in one direction or the other. The modeller who builds a flocked cutting stores on the fifth shelf.
2. Abiodun builds a plaster tunnel mouth.
3. The modeller who builds a cardboard viaduct is exactly one shelf lower than the fifth shelf, with no shelf in between.
4. The fourth shelf is exactly one shelf lower than Rosamond, with no shelf in between.
5. Cuthbert and the modeller who owns a brass pannier tank are exactly four shelves apart in shelf order.
6. Abiodun and the modeller who owns a rake of milk tankers are exactly one shelf apart in shelf order, in one direction or the other.
7. The modeller who builds a cardboard viaduct and the modeller who owns a battered autocoach are exactly two shelves apart in shelf order.
8. The modeller who owns a kit-built brake van is exactly one shelf lower than the modeller who builds a coal staithe, with no shelf in between.

## Solving chart

*Shelf vs Modeller*

| | Rosamond | Gilbert | Abiodun | Cuthbert | Hendrik |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Rolling stock*

| | a scratch-built crane wagon | a brass pannier tank | a rake of milk tankers | a battered autocoach | a kit-built brake van |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Scenery*

| | a plaster tunnel mouth | a coal staithe | a cardboard viaduct | a flocked cutting | a working level crossing |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Modeller vs Rolling stock*

| | a scratch-built crane wagon | a brass pannier tank | a rake of milk tankers | a battered autocoach | a kit-built brake van |
|---|---|---|---|---|---|
| **Rosamond** | | | | | |
| **Gilbert** | | | | | |
| **Abiodun** | | | | | |
| **Cuthbert** | | | | | |
| **Hendrik** | | | | | |

*Modeller vs Scenery*

| | a plaster tunnel mouth | a coal staithe | a cardboard viaduct | a flocked cutting | a working level crossing |
|---|---|---|---|---|---|
| **Rosamond** | | | | | |
| **Gilbert** | | | | | |
| **Abiodun** | | | | | |
| **Cuthbert** | | | | | |
| **Hendrik** | | | | | |

*Rolling stock vs Scenery*

| | a plaster tunnel mouth | a coal staithe | a cardboard viaduct | a flocked cutting | a working level crossing |
|---|---|---|---|---|---|
| **a scratch-built crane wagon** | | | | | |
| **a brass pannier tank** | | | | | |
| **a rake of milk tankers** | | | | | |
| **a battered autocoach** | | | | | |
| **a kit-built brake van** | | | | | |

## Solution

| Shelf | Modeller | Rolling stock | Scenery |
|---|---|---|---|
| the bottom shelf | Cuthbert | a kit-built brake van | a working level crossing |
| the second shelf | Gilbert | a battered autocoach | a coal staithe |
| the third shelf | Abiodun | a scratch-built crane wagon | a plaster tunnel mouth |
| the fourth shelf | Hendrik | a rake of milk tankers | a cardboard viaduct |
| the fifth shelf | Rosamond | a brass pannier tank | a flocked cutting |

## How it falls out

1. [direct] from clue 3 scenery:a flocked cutting: ruled out position(s) 1,2,3,4
2. [bijection] scenery:a plaster tunnel mouth: ruled out position(s) 5
3. [bijection] scenery:a coal staithe: ruled out position(s) 5
4. [bijection] scenery:a cardboard viaduct: ruled out position(s) 5
5. [bijection] scenery:a working level crossing: ruled out position(s) 5
6. [direct] from clue 2 modeller:Abiodun: ruled out position(s) 5
7. [order] from clue 9 modeller:Cuthbert: ruled out position(s) 2,3,4
8. [order] from clue 9 stock:a brass pannier tank: ruled out position(s) 2,3,4
9. [order] from clue 8 scenery:a cardboard viaduct: ruled out position(s) 1,2,3
10. [order] from clue 7 stock:a kit-built brake van: ruled out position(s) 4,5
11. [order] from clue 7 scenery:a coal staithe: ruled out position(s) 1
12. [order] from clue 6 modeller:Hendrik: ruled out position(s) 1,2,3,5
13. [order] from clue 4 stock:a battered autocoach: ruled out position(s) 1,3,4,5
14. [order] from clue 1 modeller:Rosamond: ruled out position(s) 1,2,3,4
15. [bijection] modeller:Gilbert: ruled out position(s) 4,5
16. [bijection] modeller:Abiodun: ruled out position(s) 4
17. [bijection] modeller:Cuthbert: ruled out position(s) 5
18. [bijection] scenery:a plaster tunnel mouth: ruled out position(s) 4
19. [bijection] scenery:a coal staithe: ruled out position(s) 4
20. [bijection] scenery:a working level crossing: ruled out position(s) 4
21. [bijection] stock:a scratch-built crane wagon: ruled out position(s) 2
22. [bijection] stock:a rake of milk tankers: ruled out position(s) 2
23. [bijection] stock:a kit-built brake van: ruled out position(s) 2
24. [order] from clue 7 stock:a kit-built brake van: ruled out position(s) 3
25. [order] from clue 7 scenery:a coal staithe: ruled out position(s) 3
26. [order] from clue 9 stock:a brass pannier tank: ruled out position(s) 1
27. [order] from clue 5 modeller:Abiodun: ruled out position(s) 1
28. [order] from clue 5 stock:a rake of milk tankers: ruled out position(s) 5
29. [direct] from clue 2 scenery:a plaster tunnel mouth: ruled out position(s) 1
30. [bijection] modeller:Gilbert: ruled out position(s) 1
31. [bijection] scenery:a plaster tunnel mouth: ruled out position(s) 2
32. [bijection] scenery:a working level crossing: ruled out position(s) 2
33. [bijection] scenery:a working level crossing: ruled out position(s) 3
34. [bijection] stock:a scratch-built crane wagon: ruled out position(s) 1,5
35. [bijection] stock:a rake of milk tankers: ruled out position(s) 1
36. [direct] from clue 2 modeller:Abiodun: ruled out position(s) 2
37. [order] from clue 5 stock:a rake of milk tankers: ruled out position(s) 3
38. [bijection] modeller:Gilbert: ruled out position(s) 3
39. [bijection] stock:a scratch-built crane wagon: ruled out position(s) 4

---

<sub>seed `2026172733816` &middot; score 5.355 &middot; atoms 9 &middot; positives 2 &middot; solved by order</sub>
