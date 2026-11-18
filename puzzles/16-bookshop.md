# Mrs Pell's Impossible Shelves

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `d7bd206c23b6`

## Introduction

Mrs Pell's secondhand bookshop shelves by a system she alone understands, and she has gone to Margate for a fortnight.
Five volumes are involved. Determine each volume's shelf, buyer and price.
- **Volume**: a book of sea shanties, a guide to fungi, an album of pressed ferns, a treatise on clocks and a water-stained atlas.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Buyer**: Fenella, Verity, Ottoline, Rodrigo and Augustus.
- **Pencilled price**: seven and six; half a crown; one and six; two shillings; and a guinea.
Every volume has a different shelf, buyer and price, so within each category every item is used exactly once.

## Clues

1. The volume that was bought by Fenella is exactly one shelf lower than the third shelf, with no shelf in between. A treatise on clocks was bought by Fenella.
2. A guide to fungi was bought by Ottoline.
3. A water-stained atlas falls somewhere between the volume that is priced at two shillings and the fifth shelf in shelf order. A water-stained atlas is not priced at half a crown.
4. The volume that was bought by Fenella falls somewhere between a book of sea shanties and the fourth shelf in shelf order.
5. The third shelf is exactly one shelf lower than the volume that was bought by Verity, with no shelf in between.
6. The volume that is priced at one and six is exactly one shelf lower than the fourth shelf, with no shelf in between.
7. The volume that was bought by Augustus and the volume that is priced at seven and six are exactly one shelf apart in shelf order, in one direction or the other.
8. The volume that is priced at one and six is lower than the volume that was bought by Rodrigo in shelf order.

## Solving chart

*Shelf vs Volume*

| | a book of sea shanties | a guide to fungi | an album of pressed ferns | a treatise on clocks | a water-stained atlas |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Buyer*

| | Fenella | Verity | Ottoline | Rodrigo | Augustus |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Pencilled price*

| | seven and six | half a crown | one and six | two shillings | a guinea |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Volume vs Buyer*

| | Fenella | Verity | Ottoline | Rodrigo | Augustus |
|---|---|---|---|---|---|
| **a book of sea shanties** | | | | | |
| **a guide to fungi** | | | | | |
| **an album of pressed ferns** | | | | | |
| **a treatise on clocks** | | | | | |
| **a water-stained atlas** | | | | | |

*Volume vs Pencilled price*

| | seven and six | half a crown | one and six | two shillings | a guinea |
|---|---|---|---|---|---|
| **a book of sea shanties** | | | | | |
| **a guide to fungi** | | | | | |
| **an album of pressed ferns** | | | | | |
| **a treatise on clocks** | | | | | |
| **a water-stained atlas** | | | | | |

*Buyer vs Pencilled price*

| | seven and six | half a crown | one and six | two shillings | a guinea |
|---|---|---|---|---|---|
| **Fenella** | | | | | |
| **Verity** | | | | | |
| **Ottoline** | | | | | |
| **Rodrigo** | | | | | |
| **Augustus** | | | | | |

## Solution

| Shelf | Volume | Buyer | Pencilled price |
|---|---|---|---|
| the bottom shelf | a book of sea shanties | Augustus | two shillings |
| the second shelf | a treatise on clocks | Fenella | seven and six |
| the third shelf | a guide to fungi | Ottoline | one and six |
| the fourth shelf | a water-stained atlas | Verity | a guinea |
| the fifth shelf | an album of pressed ferns | Rodrigo | half a crown |

## How it falls out

1. [order] from clue 9 book:a water-stained atlas: ruled out position(s) 1,5
2. [order] from clue 9 price_tag:two shillings: ruled out position(s) 4,5
3. [order] from clue 8 buyer:Fenella: ruled out position(s) 1,4,5
4. [order] from clue 8 book:a book of sea shanties: ruled out position(s) 3,4,5
5. [order] from clue 7 price_tag:one and six: ruled out position(s) 5
6. [order] from clue 7 buyer:Rodrigo: ruled out position(s) 1
7. [order] from clue 6 buyer:Fenella: ruled out position(s) 3
8. [order] from clue 8 book:a book of sea shanties: ruled out position(s) 2
9. [order] from clue 5 price_tag:one and six: ruled out position(s) 1,2,4
10. [order] from clue 7 buyer:Rodrigo: ruled out position(s) 2,3
11. [order] from clue 4 buyer:Verity: ruled out position(s) 1,2,3,5
12. [direct] from clue 1 book:a treatise on clocks: ruled out position(s) 1,3,4,5
13. [bijection] book:a guide to fungi: ruled out position(s) 1,2
14. [bijection] book:an album of pressed ferns: ruled out position(s) 1,2
15. [bijection] book:a water-stained atlas: ruled out position(s) 2
16. [bijection] buyer:Ottoline: ruled out position(s) 2,4
17. [bijection] buyer:Rodrigo: ruled out position(s) 4
18. [bijection] buyer:Augustus: ruled out position(s) 2,4
19. [bijection] price_tag:seven and six: ruled out position(s) 3
20. [bijection] price_tag:half a crown: ruled out position(s) 3
21. [bijection] price_tag:two shillings: ruled out position(s) 3
22. [bijection] price_tag:a guinea: ruled out position(s) 3
23. [order] from clue 10 price_tag:seven and six: ruled out position(s) 1,5
24. [direct] from clue 2 book:a guide to fungi: ruled out position(s) 4
25. [direct] from clue 2 buyer:Ottoline: ruled out position(s) 1
26. [bijection] buyer:Ottoline: ruled out position(s) 5
27. [bijection] buyer:Augustus: ruled out position(s) 5
28. [bijection] buyer:Augustus: ruled out position(s) 3
29. [order] from clue 10 price_tag:seven and six: ruled out position(s) 4
30. [direct] from clue 2 book:a guide to fungi: ruled out position(s) 5
31. [bijection] book:an album of pressed ferns: ruled out position(s) 3
32. [bijection] book:a water-stained atlas: ruled out position(s) 3
33. [bijection] book:an album of pressed ferns: ruled out position(s) 4
34. [bijection] price_tag:half a crown: ruled out position(s) 2
35. [bijection] price_tag:two shillings: ruled out position(s) 2
36. [bijection] price_tag:a guinea: ruled out position(s) 2
37. [direct] from clue 3 price_tag:half a crown: ruled out position(s) 4
38. [bijection] price_tag:half a crown: ruled out position(s) 1
39. [bijection] price_tag:a guinea: ruled out position(s) 1
40. [bijection] price_tag:a guinea: ruled out position(s) 5

---

<sub>seed `2026172702140` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
