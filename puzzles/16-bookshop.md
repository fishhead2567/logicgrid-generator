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

1. The volume that was bought by Fenella is exactly one shelf lower than the third shelf, with no shelf in between. A guide to fungi sits on the third shelf.
2. The volume that is priced at a guinea sits on the fourth shelf.
3. A water-stained atlas falls somewhere between the volume that is priced at two shillings and the fifth shelf in shelf order.
4. The third shelf is exactly one shelf lower than the volume that was bought by Verity, with no shelf in between.
5. The volume that was bought by Augustus and the volume that is priced at seven and six are exactly one shelf apart in shelf order, in one direction or the other.
6. The volume that is priced at two shillings is lower than an album of pressed ferns in shelf order.
7. A treatise on clocks is exactly one shelf lower than the volume that was bought by Ottoline, with no shelf in between.
8. The volume that was bought by Augustus is not priced at one and six. The volume that is priced at one and six is lower than the volume that was bought by Rodrigo in shelf order.

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

1. [direct] from clue 2 book:a guide to fungi: ruled out position(s) 1,2,4,5
2. [direct] from clue 1 price_tag:a guinea: ruled out position(s) 1,2,3,5
3. [bijection] book:a book of sea shanties: ruled out position(s) 3
4. [bijection] book:an album of pressed ferns: ruled out position(s) 3
5. [bijection] book:a treatise on clocks: ruled out position(s) 3
6. [bijection] book:a water-stained atlas: ruled out position(s) 3
7. [bijection] price_tag:seven and six: ruled out position(s) 4
8. [bijection] price_tag:half a crown: ruled out position(s) 4
9. [bijection] price_tag:one and six: ruled out position(s) 4
10. [bijection] price_tag:two shillings: ruled out position(s) 4
11. [order] from clue 10 buyer:Augustus: ruled out position(s) 5
12. [order] from clue 9 book:a water-stained atlas: ruled out position(s) 1,5
13. [order] from clue 9 price_tag:two shillings: ruled out position(s) 5
14. [order] from clue 8 book:an album of pressed ferns: ruled out position(s) 1
15. [order] from clue 7 price_tag:one and six: ruled out position(s) 5
16. [order] from clue 7 buyer:Rodrigo: ruled out position(s) 1
17. [order] from clue 6 buyer:Fenella: ruled out position(s) 1,3,4,5
18. [order] from clue 5 book:a treatise on clocks: ruled out position(s) 5
19. [order] from clue 5 buyer:Ottoline: ruled out position(s) 1,4
20. [order] from clue 4 buyer:Verity: ruled out position(s) 1,2,3,5
21. [bijection] buyer:Ottoline: ruled out position(s) 2
22. [bijection] buyer:Rodrigo: ruled out position(s) 2,4
23. [bijection] buyer:Augustus: ruled out position(s) 2,4
24. [bijection] buyer:Augustus: ruled out position(s) 3
25. [order] from clue 10 price_tag:seven and six: ruled out position(s) 1,3,5
26. [direct] from clue 3 price_tag:one and six: ruled out position(s) 1
27. [order] from clue 5 book:a treatise on clocks: ruled out position(s) 1
28. [bijection] book:a book of sea shanties: ruled out position(s) 2,4,5
29. [bijection] price_tag:half a crown: ruled out position(s) 2
30. [bijection] price_tag:one and six: ruled out position(s) 2
31. [bijection] price_tag:two shillings: ruled out position(s) 2
32. [bijection] price_tag:half a crown: ruled out position(s) 1,3
33. [order] from clue 7 buyer:Rodrigo: ruled out position(s) 3
34. [bijection] book:an album of pressed ferns: ruled out position(s) 2,4
35. [bijection] buyer:Ottoline: ruled out position(s) 5
36. [bijection] price_tag:two shillings: ruled out position(s) 3
37. [order] from clue 5 book:a treatise on clocks: ruled out position(s) 4
38. [bijection] book:a water-stained atlas: ruled out position(s) 2

---

<sub>seed `2026172702140` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
