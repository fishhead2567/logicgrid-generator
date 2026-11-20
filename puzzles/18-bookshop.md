# Mrs Pell's Impossible Shelves

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `04a148ea315a`

## Introduction

Mrs Pell's secondhand bookshop shelves by a system she alone understands, and she has gone to Margate for a fortnight.
Four volumes are involved. Determine each volume's shelf, keepsake and price.
- **Volume**: an album of pressed ferns, a book of sea shanties, a Latin primer and a water-stained atlas.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf and the fourth shelf.
- **Found inside**: a pawn ticket, a tram ticket, a recipe for quince jelly and a pressed violet.
- **Pencilled price**: a guinea; four shillings; two shillings; and seven and six.
Every volume has a different shelf, keepsake and price, so within each category every item is used exactly once.

## Clues

1. A book of sea shanties falls somewhere between the bottom shelf and the fourth shelf in shelf order. The volume that is priced at a guinea sits on the bottom shelf.
2. A water-stained atlas sits on the third shelf.
3. The second shelf falls somewhere between the volume that is priced at a guinea and the volume that is priced at four shillings in shelf order.
4. The volume that contains a recipe for quince jelly is higher than the bottom shelf in shelf order.
5. The volume that is priced at two shillings is exactly one shelf lower than the fourth shelf, with no shelf in between.
6. A Latin primer is not priced at four shillings.
7. A book of sea shanties is lower than the volume that contains a pawn ticket in shelf order.
8. The volume that contains a pressed violet and the volume that is priced at four shillings are exactly one shelf apart in shelf order, in one direction or the other.

## Solving chart

*Shelf vs Volume*

| | an album of pressed ferns | a book of sea shanties | a Latin primer | a water-stained atlas |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Found inside*

| | a pawn ticket | a tram ticket | a recipe for quince jelly | a pressed violet |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Shelf vs Pencilled price*

| | a guinea | four shillings | two shillings | seven and six |
|---|---|---|---|---|
| **the bottom shelf** | | | | |
| **the second shelf** | | | | |
| **the third shelf** | | | | |
| **the fourth shelf** | | | | |

*Volume vs Found inside*

| | a pawn ticket | a tram ticket | a recipe for quince jelly | a pressed violet |
|---|---|---|---|---|
| **an album of pressed ferns** | | | | |
| **a book of sea shanties** | | | | |
| **a Latin primer** | | | | |
| **a water-stained atlas** | | | | |

*Volume vs Pencilled price*

| | a guinea | four shillings | two shillings | seven and six |
|---|---|---|---|---|
| **an album of pressed ferns** | | | | |
| **a book of sea shanties** | | | | |
| **a Latin primer** | | | | |
| **a water-stained atlas** | | | | |

*Found inside vs Pencilled price*

| | a guinea | four shillings | two shillings | seven and six |
|---|---|---|---|---|
| **a pawn ticket** | | | | |
| **a tram ticket** | | | | |
| **a recipe for quince jelly** | | | | |
| **a pressed violet** | | | | |

## Solution

| Shelf | Volume | Found inside | Pencilled price |
|---|---|---|---|
| the bottom shelf | a Latin primer | a tram ticket | a guinea |
| the second shelf | a book of sea shanties | a recipe for quince jelly | seven and six |
| the third shelf | a water-stained atlas | a pressed violet | two shillings |
| the fourth shelf | an album of pressed ferns | a pawn ticket | four shillings |

## How it falls out

1. [direct] from clue 2 book:a water-stained atlas: ruled out position(s) 1,2,4
2. [direct] from clue 1 price_tag:a guinea: ruled out position(s) 2,3,4
3. [bijection] book:an album of pressed ferns: ruled out position(s) 3
4. [bijection] book:a book of sea shanties: ruled out position(s) 3
5. [bijection] book:a Latin primer: ruled out position(s) 3
6. [bijection] price_tag:four shillings: ruled out position(s) 1
7. [bijection] price_tag:two shillings: ruled out position(s) 1
8. [bijection] price_tag:seven and six: ruled out position(s) 1
9. [order] from clue 9 price_tag:four shillings: ruled out position(s) 2
10. [order] from clue 8 bookmark:a recipe for quince jelly: ruled out position(s) 1
11. [order] from clue 7 book:a book of sea shanties: ruled out position(s) 1,4
12. [order] from clue 6 bookmark:a pressed violet: ruled out position(s) 1
13. [order] from clue 5 price_tag:two shillings: ruled out position(s) 2,4
14. [order] from clue 3 bookmark:a pawn ticket: ruled out position(s) 1,2
15. [bijection] book:an album of pressed ferns: ruled out position(s) 2
16. [bijection] book:a Latin primer: ruled out position(s) 2
17. [bijection] bookmark:a tram ticket: ruled out position(s) 2,3,4
18. [bijection] price_tag:four shillings: ruled out position(s) 3
19. [bijection] price_tag:seven and six: ruled out position(s) 3
20. [bijection] price_tag:seven and six: ruled out position(s) 4
21. [order] from clue 6 bookmark:a pressed violet: ruled out position(s) 2,4
22. [direct] from clue 4 book:a Latin primer: ruled out position(s) 4
23. [bijection] book:an album of pressed ferns: ruled out position(s) 1
24. [bijection] bookmark:a pawn ticket: ruled out position(s) 3
25. [bijection] bookmark:a recipe for quince jelly: ruled out position(s) 3
26. [bijection] bookmark:a recipe for quince jelly: ruled out position(s) 4

---

<sub>seed `2026172917984` &middot; score 4.93 &middot; atoms 9 &middot; positives 2 &middot; solved by order</sub>
