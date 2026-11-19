# Mrs Pell's Impossible Shelves

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `c25568d60cc1`

## Introduction

Mrs Pell's secondhand bookshop shelves by a system she alone understands, and she has gone to Margate for a fortnight.
Five volumes are involved. Determine each volume's shelf and keepsake.
- **Volume**: a treatise on clocks, a water-stained atlas, a beekeeping manual, a guide to fungi and a book of sea shanties.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Found inside**: a lock of hair, a recipe for quince jelly, a postcard from Hull, a tram ticket and a laundry list.
Every volume has a different shelf and keepsake, so within each category every item is used exactly once.

## Clues

1. The volume that contains a recipe for quince jelly sits on the second shelf. The second shelf is exactly one shelf lower than the volume that contains a tram ticket, with no shelf in between.
2. A beekeeping manual sits on the bottom shelf.
3. The volume that contains a laundry list sits on the bottom shelf.
4. The volume that contains a lock of hair and the fourth shelf are exactly one shelf apart in shelf order, in one direction or the other.
5. The second shelf is exactly one shelf lower than a treatise on clocks, with no shelf in between.
6. The fourth shelf is exactly one shelf lower than a book of sea shanties, with no shelf in between.
7. A guide to fungi does not contain a postcard from Hull.

## Solving chart

*Shelf vs Volume*

| | a treatise on clocks | a water-stained atlas | a beekeeping manual | a guide to fungi | a book of sea shanties |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Found inside*

| | a lock of hair | a recipe for quince jelly | a postcard from Hull | a tram ticket | a laundry list |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Volume vs Found inside*

| | a lock of hair | a recipe for quince jelly | a postcard from Hull | a tram ticket | a laundry list |
|---|---|---|---|---|---|
| **a treatise on clocks** | | | | | |
| **a water-stained atlas** | | | | | |
| **a beekeeping manual** | | | | | |
| **a guide to fungi** | | | | | |
| **a book of sea shanties** | | | | | |

## Solution

| Shelf | Volume | Found inside |
|---|---|---|
| the bottom shelf | a beekeeping manual | a laundry list |
| the second shelf | a guide to fungi | a recipe for quince jelly |
| the third shelf | a treatise on clocks | a tram ticket |
| the fourth shelf | a water-stained atlas | a postcard from Hull |
| the fifth shelf | a book of sea shanties | a lock of hair |

## How it falls out

1. [direct] from clue 4 bookmark:a laundry list: ruled out position(s) 2,3,4,5
2. [direct] from clue 2 bookmark:a recipe for quince jelly: ruled out position(s) 1,3,4,5
3. [direct] from clue 1 book:a beekeeping manual: ruled out position(s) 2,3,4,5
4. [bijection] book:a treatise on clocks: ruled out position(s) 1
5. [bijection] book:a water-stained atlas: ruled out position(s) 1
6. [bijection] book:a guide to fungi: ruled out position(s) 1
7. [bijection] book:a book of sea shanties: ruled out position(s) 1
8. [bijection] bookmark:a lock of hair: ruled out position(s) 1,2
9. [bijection] bookmark:a postcard from Hull: ruled out position(s) 1,2
10. [bijection] bookmark:a tram ticket: ruled out position(s) 1,2
11. [order] from clue 8 book:a treatise on clocks: ruled out position(s) 2,4,5
12. [order] from clue 7 bookmark:a lock of hair: ruled out position(s) 4
13. [order] from clue 6 bookmark:a tram ticket: ruled out position(s) 4,5
14. [order] from clue 5 book:a book of sea shanties: ruled out position(s) 2,3,4
15. [bijection] book:a water-stained atlas: ruled out position(s) 3,5
16. [bijection] book:a guide to fungi: ruled out position(s) 3,5
17. [bijection] bookmark:a lock of hair: ruled out position(s) 3
18. [bijection] bookmark:a postcard from Hull: ruled out position(s) 3
19. [bijection] bookmark:a postcard from Hull: ruled out position(s) 5
20. [direct] from clue 3 book:a guide to fungi: ruled out position(s) 4
21. [bijection] book:a water-stained atlas: ruled out position(s) 2

---

<sub>seed `2026172683358` &middot; score 4.38 &middot; atoms 8 &middot; positives 3 &middot; solved by order</sub>
