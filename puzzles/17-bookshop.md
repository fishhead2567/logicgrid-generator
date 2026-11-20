# Mrs Pell's Impossible Shelves

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `e29ceb1e5111`

## Introduction

Mrs Pell's secondhand bookshop shelves by a system she alone understands, and she has gone to Margate for a fortnight.
Five volumes are involved. Determine each volume's shelf and price.
- **Volume**: a guide to fungi, a treatise on clocks, a book of sea shanties, a water-stained atlas and a Latin primer.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Pencilled price**: half a crown; seven and six; four shillings; ninepence; and a guinea.
Every volume has a different shelf and price, so within each category every item is used exactly once.

## Clues

1. A guide to fungi and the fifth shelf are exactly one shelf apart in shelf order, in one direction or the other. A water-stained atlas sits on the fifth shelf.
2. The volume that is priced at four shillings is exactly one shelf lower than the third shelf, with no shelf in between.
3. A Latin primer is lower than the second shelf in shelf order.
4. A guide to fungi is exactly one shelf lower than the volume that is priced at seven and six, with no shelf in between.
5. The volume that is priced at a guinea is exactly one shelf lower than a book of sea shanties, with no shelf in between.
6. A book of sea shanties is exactly one shelf lower than the volume that is priced at ninepence, with no shelf in between.

## Solving chart

*Shelf vs Volume*

| | a guide to fungi | a treatise on clocks | a book of sea shanties | a water-stained atlas | a Latin primer |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Pencilled price*

| | half a crown | seven and six | four shillings | ninepence | a guinea |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Volume vs Pencilled price*

| | half a crown | seven and six | four shillings | ninepence | a guinea |
|---|---|---|---|---|---|
| **a guide to fungi** | | | | | |
| **a treatise on clocks** | | | | | |
| **a book of sea shanties** | | | | | |
| **a water-stained atlas** | | | | | |
| **a Latin primer** | | | | | |

## Solution

| Shelf | Volume | Pencilled price |
|---|---|---|
| the bottom shelf | a Latin primer | a guinea |
| the second shelf | a book of sea shanties | four shillings |
| the third shelf | a treatise on clocks | ninepence |
| the fourth shelf | a guide to fungi | half a crown |
| the fifth shelf | a water-stained atlas | seven and six |

## How it falls out

1. [direct] from clue 3 book:a water-stained atlas: ruled out position(s) 1,2,3,4
2. [bijection] book:a guide to fungi: ruled out position(s) 5
3. [bijection] book:a treatise on clocks: ruled out position(s) 5
4. [bijection] book:a book of sea shanties: ruled out position(s) 5
5. [bijection] book:a Latin primer: ruled out position(s) 5
6. [order] from clue 7 book:a Latin primer: ruled out position(s) 2,3,4
7. [order] from clue 6 price_tag:ninepence: ruled out position(s) 1
8. [order] from clue 5 price_tag:four shillings: ruled out position(s) 1,3,4,5
9. [order] from clue 4 price_tag:a guinea: ruled out position(s) 4,5
10. [order] from clue 4 book:a book of sea shanties: ruled out position(s) 1
11. [order] from clue 6 price_tag:ninepence: ruled out position(s) 2
12. [order] from clue 2 book:a guide to fungi: ruled out position(s) 1,2,3
13. [order] from clue 1 price_tag:seven and six: ruled out position(s) 1,2,3,4
14. [bijection] book:a treatise on clocks: ruled out position(s) 1,4
15. [bijection] book:a book of sea shanties: ruled out position(s) 4
16. [bijection] price_tag:half a crown: ruled out position(s) 2,5
17. [bijection] price_tag:ninepence: ruled out position(s) 5
18. [bijection] price_tag:a guinea: ruled out position(s) 2
19. [order] from clue 4 price_tag:a guinea: ruled out position(s) 3
20. [order] from clue 4 book:a book of sea shanties: ruled out position(s) 3
21. [order] from clue 6 price_tag:ninepence: ruled out position(s) 4
22. [bijection] book:a treatise on clocks: ruled out position(s) 2
23. [bijection] price_tag:half a crown: ruled out position(s) 1,3

---

<sub>seed `2026173010068` &middot; score 4.86 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
