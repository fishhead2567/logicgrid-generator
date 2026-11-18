# Mrs Pell's Impossible Shelves

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `e2543b96baa8`

## Introduction

Mrs Pell's secondhand bookshop shelves by a system she alone understands, and she has gone to Margate for a fortnight.
Five volumes are involved. Determine each volume's shelf, keepsake and price.
- **Volume**: a water-stained atlas, a book of sea shanties, an album of pressed ferns, a beekeeping manual and a guide to fungi.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Found inside**: a lock of hair, a laundry list, a postcard from Hull, a recipe for quince jelly and a pressed violet.
- **Pencilled price**: half a crown; seven and six; two shillings; a guinea; and one and six.
Every volume has a different shelf, keepsake and price, so within each category every item is used exactly once.

## Clues

1. The volume that contains a pressed violet is higher than the second shelf in shelf order. An album of pressed ferns and the second shelf are exactly three shelves apart in shelf order.
2. The volume that contains a recipe for quince jelly is not priced at half a crown. The volume that contains a recipe for quince jelly does not sit on the second shelf.
3. The volume that is priced at seven and six and the second shelf are exactly one shelf apart in shelf order, in one direction or the other.
4. The second shelf falls somewhere between the volume that contains a postcard from Hull and the volume that is priced at one and six in shelf order.
5. The volume that contains a postcard from Hull is not priced at half a crown. A water-stained atlas does not contain a postcard from Hull.
6. The volume that is priced at one and six is exactly one shelf lower than a guide to fungi, with no shelf in between.
7. The volume that is priced at half a crown is lower than an album of pressed ferns in shelf order.
8. The volume that is priced at a guinea falls somewhere between the volume that contains a lock of hair and the volume that contains a postcard from Hull in shelf order.
9. A beekeeping manual and the volume that is priced at one and six both sit at odd-numbered shelves or both at even-numbered shelves.
10. The volume that is priced at a guinea is exactly one shelf lower than a water-stained atlas, with no shelf in between. A book of sea shanties is not priced at a guinea.

## Solving chart

*Shelf vs Volume*

| | a water-stained atlas | a book of sea shanties | an album of pressed ferns | a beekeeping manual | a guide to fungi |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Found inside*

| | a lock of hair | a laundry list | a postcard from Hull | a recipe for quince jelly | a pressed violet |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Pencilled price*

| | half a crown | seven and six | two shillings | a guinea | one and six |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Volume vs Found inside*

| | a lock of hair | a laundry list | a postcard from Hull | a recipe for quince jelly | a pressed violet |
|---|---|---|---|---|---|
| **a water-stained atlas** | | | | | |
| **a book of sea shanties** | | | | | |
| **an album of pressed ferns** | | | | | |
| **a beekeeping manual** | | | | | |
| **a guide to fungi** | | | | | |

*Volume vs Pencilled price*

| | half a crown | seven and six | two shillings | a guinea | one and six |
|---|---|---|---|---|---|
| **a water-stained atlas** | | | | | |
| **a book of sea shanties** | | | | | |
| **an album of pressed ferns** | | | | | |
| **a beekeeping manual** | | | | | |
| **a guide to fungi** | | | | | |

*Found inside vs Pencilled price*

| | half a crown | seven and six | two shillings | a guinea | one and six |
|---|---|---|---|---|---|
| **a lock of hair** | | | | | |
| **a laundry list** | | | | | |
| **a postcard from Hull** | | | | | |
| **a recipe for quince jelly** | | | | | |
| **a pressed violet** | | | | | |

## Solution

| Shelf | Volume | Found inside | Pencilled price |
|---|---|---|---|
| the bottom shelf | a beekeeping manual | a lock of hair | one and six |
| the second shelf | a guide to fungi | a laundry list | a guinea |
| the third shelf | a water-stained atlas | a recipe for quince jelly | seven and six |
| the fourth shelf | a book of sea shanties | a pressed violet | half a crown |
| the fifth shelf | an album of pressed ferns | a postcard from Hull | two shillings |

## How it falls out

1. [direct] from clue 4 bookmark:a recipe for quince jelly: ruled out position(s) 2
2. [order] from clue 14 price_tag:seven and six: ruled out position(s) 2,4,5
3. [order] from clue 13 price_tag:one and six: ruled out position(s) 5
4. [order] from clue 13 book:a guide to fungi: ruled out position(s) 1
5. [order] from clue 12 price_tag:a guinea: ruled out position(s) 1,5
6. [order] from clue 10 price_tag:half a crown: ruled out position(s) 5
7. [order] from clue 10 book:an album of pressed ferns: ruled out position(s) 1
8. [order] from clue 9 bookmark:a pressed violet: ruled out position(s) 1,2
9. [order] from clue 7 book:an album of pressed ferns: ruled out position(s) 2,3,4
10. [order] from clue 2 book:a water-stained atlas: ruled out position(s) 1,2
11. [order] from clue 1 bookmark:a postcard from Hull: ruled out position(s) 2
12. [order] from clue 1 price_tag:one and six: ruled out position(s) 2
13. [order] from clue 13 book:a guide to fungi: ruled out position(s) 3
14. [bijection] book:a water-stained atlas: ruled out position(s) 5
15. [bijection] book:a book of sea shanties: ruled out position(s) 5
16. [bijection] book:a beekeeping manual: ruled out position(s) 5
17. [bijection] book:a guide to fungi: ruled out position(s) 5
18. [bijection] price_tag:two shillings: ruled out position(s) 1,2,3,4
19. [order] from clue 13 price_tag:one and six: ruled out position(s) 4
20. [order] from clue 8 book:a beekeeping manual: ruled out position(s) 2,4
21. [order] from clue 2 price_tag:a guinea: ruled out position(s) 4
22. [bijection] price_tag:half a crown: ruled out position(s) 1,2,3
23. [direct] from clue 6 bookmark:a postcard from Hull: ruled out position(s) 4
24. [direct] from clue 3 bookmark:a recipe for quince jelly: ruled out position(s) 4
25. [bijection] price_tag:a guinea: ruled out position(s) 3
26. [order] from clue 12 bookmark:a lock of hair: ruled out position(s) 2
27. [direct] from clue 11 book:a book of sea shanties: ruled out position(s) 2
28. [order] from clue 2 book:a water-stained atlas: ruled out position(s) 4
29. [direct] from clue 5 bookmark:a postcard from Hull: ruled out position(s) 3
30. [bijection] book:a book of sea shanties: ruled out position(s) 3
31. [bijection] book:a beekeeping manual: ruled out position(s) 3
32. [bijection] book:a guide to fungi: ruled out position(s) 4
33. [bijection] bookmark:a laundry list: ruled out position(s) 1,3,4,5
34. [order] from clue 13 price_tag:one and six: ruled out position(s) 3
35. [order] from clue 1 bookmark:a postcard from Hull: ruled out position(s) 1
36. [order] from clue 12 bookmark:a lock of hair: ruled out position(s) 3,4,5
37. [bijection] book:a book of sea shanties: ruled out position(s) 1
38. [bijection] bookmark:a recipe for quince jelly: ruled out position(s) 1,5
39. [bijection] bookmark:a pressed violet: ruled out position(s) 5
40. [bijection] bookmark:a pressed violet: ruled out position(s) 3
_... and 1 further steps._

---

<sub>seed `2026172789249` &middot; score 5.675 &middot; atoms 14 &middot; positives 0 &middot; solved by order</sub>
