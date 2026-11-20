# The Pomace and the Prize

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `390c14c57960`

## Introduction

Every maker presses in a different month, and each is privately certain the others have let theirs go to vinegar.
Five makers are involved. Determine each maker's pressing month and fault.
- **Maker**: Jethro, Araminta, Haskell, Morwenna and Petroc.
- **Pressing month** (listed from earlier to later): January, February, March, April and May.
- **Fault**: a stuck ferment, mousiness, sulphur, acetification and ropiness.
Every maker has a different pressing month and fault, so within each category every item is used exactly once.

## Clues

1. Haskell presses in January.
2. The maker who is accused of mousiness presses in May.
3. The maker who is accused of ropiness is exactly one month earlier than May, with no pressing month in between.
4. The maker who is accused of acetification is exactly one month earlier than February, with no pressing month in between.
5. March is exactly one month earlier than Araminta, with no pressing month in between.
6. Jethro is exactly one month earlier than the maker who is accused of a stuck ferment, with no pressing month in between.
7. The maker who is accused of a stuck ferment is earlier than Petroc in pressing month order.

## Solving chart

*Pressing month vs Maker*

| | Jethro | Araminta | Haskell | Morwenna | Petroc |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Pressing month vs Fault*

| | a stuck ferment | mousiness | sulphur | acetification | ropiness |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Maker vs Fault*

| | a stuck ferment | mousiness | sulphur | acetification | ropiness |
|---|---|---|---|---|---|
| **Jethro** | | | | | |
| **Araminta** | | | | | |
| **Haskell** | | | | | |
| **Morwenna** | | | | | |
| **Petroc** | | | | | |

## Solution

| Pressing month | Maker | Fault |
|---|---|---|
| January | Haskell | acetification |
| February | Jethro | sulphur |
| March | Morwenna | a stuck ferment |
| April | Araminta | ropiness |
| May | Petroc | mousiness |

## How it falls out

1. [direct] from clue 2 maker:Haskell: ruled out position(s) 2,3,4,5
2. [direct] from clue 1 fault:mousiness: ruled out position(s) 1,2,3,4
3. [bijection] fault:a stuck ferment: ruled out position(s) 5
4. [bijection] fault:sulphur: ruled out position(s) 5
5. [bijection] fault:acetification: ruled out position(s) 5
6. [bijection] fault:ropiness: ruled out position(s) 5
7. [bijection] maker:Jethro: ruled out position(s) 1
8. [bijection] maker:Araminta: ruled out position(s) 1
9. [bijection] maker:Morwenna: ruled out position(s) 1
10. [bijection] maker:Petroc: ruled out position(s) 1
11. [order] from clue 7 fault:acetification: ruled out position(s) 2,3,4
12. [order] from clue 6 maker:Araminta: ruled out position(s) 2,3,5
13. [order] from clue 5 maker:Jethro: ruled out position(s) 4,5
14. [order] from clue 5 fault:a stuck ferment: ruled out position(s) 1,2
15. [order] from clue 4 fault:ropiness: ruled out position(s) 1,2,3
16. [order] from clue 3 maker:Petroc: ruled out position(s) 2,3
17. [bijection] fault:a stuck ferment: ruled out position(s) 4
18. [bijection] fault:sulphur: ruled out position(s) 1,4
19. [bijection] fault:sulphur: ruled out position(s) 3
20. [bijection] maker:Morwenna: ruled out position(s) 4
21. [bijection] maker:Petroc: ruled out position(s) 4
22. [order] from clue 5 maker:Jethro: ruled out position(s) 3
23. [bijection] maker:Morwenna: ruled out position(s) 2,5

---

<sub>seed `2026172946716` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
