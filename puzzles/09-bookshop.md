# Mrs Pell's Impossible Shelves

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `ff457a01d66a`

## Introduction

Mrs Pell's secondhand bookshop shelves by a system she alone understands, and she has gone to Margate for a fortnight.
Five volumes are involved. Determine each volume's shelf and keepsake.
- **Volume**: a book of sea shanties, a guide to fungi, a water-stained atlas, an album of pressed ferns and a beekeeping manual.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Found inside**: a recipe for quince jelly, a tram ticket, a postcard from Hull, a pawn ticket and a pressed violet.
Every volume has a different shelf and keepsake, so within each category every item is used exactly once.

## Clues

1. A guide to fungi sits on the second shelf.
2. The volume that contains a tram ticket falls somewhere between a beekeeping manual and a water-stained atlas in shelf order. A beekeeping manual sits on the fifth shelf.
3. The bottom shelf is exactly one shelf lower than the volume that contains a postcard from Hull, with no shelf in between.
4. The fourth shelf falls somewhere between a water-stained atlas and the volume that contains a pressed violet in shelf order.
5. The volume that contains a tram ticket is lower than a book of sea shanties in shelf order.
6. An album of pressed ferns falls somewhere between the volume that contains a pressed violet and the volume that contains a recipe for quince jelly in shelf order.

## Solving chart

*Shelf vs Volume*

| | a book of sea shanties | a guide to fungi | a water-stained atlas | an album of pressed ferns | a beekeeping manual |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Found inside*

| | a recipe for quince jelly | a tram ticket | a postcard from Hull | a pawn ticket | a pressed violet |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Volume vs Found inside*

| | a recipe for quince jelly | a tram ticket | a postcard from Hull | a pawn ticket | a pressed violet |
|---|---|---|---|---|---|
| **a book of sea shanties** | | | | | |
| **a guide to fungi** | | | | | |
| **a water-stained atlas** | | | | | |
| **an album of pressed ferns** | | | | | |
| **a beekeeping manual** | | | | | |

## Solution

| Shelf | Volume | Found inside |
|---|---|---|
| the bottom shelf | a water-stained atlas | a recipe for quince jelly |
| the second shelf | a guide to fungi | a postcard from Hull |
| the third shelf | an album of pressed ferns | a tram ticket |
| the fourth shelf | a book of sea shanties | a pawn ticket |
| the fifth shelf | a beekeeping manual | a pressed violet |

## How it falls out

1. [direct] from clue 7 book:a guide to fungi: ruled out position(s) 1,3,4,5
2. [direct] from clue 5 book:a beekeeping manual: ruled out position(s) 1,2,3,4
3. [bijection] book:a book of sea shanties: ruled out position(s) 2,5
4. [bijection] book:a water-stained atlas: ruled out position(s) 2,5
5. [bijection] book:an album of pressed ferns: ruled out position(s) 2,5
6. [order] from clue 6 bookmark:a tram ticket: ruled out position(s) 4,5
7. [order] from clue 6 book:a book of sea shanties: ruled out position(s) 1
8. [order] from clue 4 book:an album of pressed ferns: ruled out position(s) 1
9. [order] from clue 3 book:a water-stained atlas: ruled out position(s) 4
10. [order] from clue 3 bookmark:a pressed violet: ruled out position(s) 1,2,3,4
11. [order] from clue 4 bookmark:a recipe for quince jelly: ruled out position(s) 4,5
12. [order] from clue 2 bookmark:a postcard from Hull: ruled out position(s) 1,3,4,5
13. [order] from clue 1 bookmark:a tram ticket: ruled out position(s) 1
14. [order] from clue 1 book:a water-stained atlas: ruled out position(s) 3
15. [bijection] bookmark:a recipe for quince jelly: ruled out position(s) 2
16. [bijection] bookmark:a tram ticket: ruled out position(s) 2
17. [bijection] bookmark:a pawn ticket: ruled out position(s) 2,5
18. [bijection] bookmark:a pawn ticket: ruled out position(s) 1,3
19. [order] from clue 6 book:a book of sea shanties: ruled out position(s) 3
20. [bijection] book:an album of pressed ferns: ruled out position(s) 4
21. [bijection] bookmark:a recipe for quince jelly: ruled out position(s) 3

---

<sub>seed `2026172646707` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
