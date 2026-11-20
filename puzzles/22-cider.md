# The Pomace and the Prize

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `7ab7a90bb6a1`

## Introduction

Every maker presses in a different month, and each is privately certain the others have let theirs go to vinegar.
Five makers are involved. Determine each maker's pressing month, apple and fault.
- **Maker**: Araminta, Jethro, Morwenna, Petroc and Haskell.
- **Pressing month** (listed from earlier to later): January, February, March, April and May.
- **Apple**: Somerset Redstreak, Kingston Black, Browns Apple, Yarlington Mill and Foxwhelp.
- **Fault**: ropiness, acetification, sulphur, a stuck ferment and mousiness.
Every maker has a different pressing month, apple and fault, so within each category every item is used exactly once.

## Clues

1. The maker who is accused of a stuck ferment presses in March.
2. The maker who presses Kingston Black does not press in March. Morwenna and March are exactly two months apart in pressing month order.
3. Jethro is exactly one month earlier than March, with no pressing month in between.
4. The maker who presses Kingston Black does not press in January.
5. The maker who presses Yarlington Mill is exactly one month earlier than Petroc, with no pressing month in between.
6. Petroc is exactly one month earlier than the maker who presses Foxwhelp, with no pressing month in between.
7. The maker who is accused of a stuck ferment is exactly one month earlier than the maker who presses Foxwhelp, with no pressing month in between.
8. The maker who is accused of ropiness is exactly one month earlier than the maker who presses Somerset Redstreak, with no pressing month in between.
9. The maker who is accused of mousiness and Haskell are exactly four months apart in pressing month order.
10. The maker who is accused of sulphur and Haskell are exactly one month apart in pressing month order, in one direction or the other.

## Solving chart

*Pressing month vs Maker*

| | Araminta | Jethro | Morwenna | Petroc | Haskell |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Pressing month vs Apple*

| | Somerset Redstreak | Kingston Black | Browns Apple | Yarlington Mill | Foxwhelp |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Pressing month vs Fault*

| | ropiness | acetification | sulphur | a stuck ferment | mousiness |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Maker vs Apple*

| | Somerset Redstreak | Kingston Black | Browns Apple | Yarlington Mill | Foxwhelp |
|---|---|---|---|---|---|
| **Araminta** | | | | | |
| **Jethro** | | | | | |
| **Morwenna** | | | | | |
| **Petroc** | | | | | |
| **Haskell** | | | | | |

*Maker vs Fault*

| | ropiness | acetification | sulphur | a stuck ferment | mousiness |
|---|---|---|---|---|---|
| **Araminta** | | | | | |
| **Jethro** | | | | | |
| **Morwenna** | | | | | |
| **Petroc** | | | | | |
| **Haskell** | | | | | |

*Apple vs Fault*

| | ropiness | acetification | sulphur | a stuck ferment | mousiness |
|---|---|---|---|---|---|
| **Somerset Redstreak** | | | | | |
| **Kingston Black** | | | | | |
| **Browns Apple** | | | | | |
| **Yarlington Mill** | | | | | |
| **Foxwhelp** | | | | | |

## Solution

| Pressing month | Maker | Apple | Fault |
|---|---|---|---|
| January | Morwenna | Browns Apple | mousiness |
| February | Jethro | Yarlington Mill | ropiness |
| March | Petroc | Somerset Redstreak | a stuck ferment |
| April | Araminta | Foxwhelp | sulphur |
| May | Haskell | Kingston Black | acetification |

## How it falls out

1. [direct] from clue 10 fault:a stuck ferment: ruled out position(s) 1,2,4,5
2. [direct] from clue 9 apple:Kingston Black: ruled out position(s) 3
3. [direct] from clue 3 apple:Kingston Black: ruled out position(s) 1
4. [bijection] fault:ropiness: ruled out position(s) 3
5. [bijection] fault:acetification: ruled out position(s) 3
6. [bijection] fault:sulphur: ruled out position(s) 3
7. [bijection] fault:mousiness: ruled out position(s) 3
8. [order] from clue 8 maker:Petroc: ruled out position(s) 5
9. [order] from clue 8 apple:Foxwhelp: ruled out position(s) 1
10. [order] from clue 7 maker:Morwenna: ruled out position(s) 2,3,4
11. [order] from clue 6 apple:Foxwhelp: ruled out position(s) 2,3,5
12. [order] from clue 8 maker:Petroc: ruled out position(s) 1,2,4
13. [order] from clue 5 fault:ropiness: ruled out position(s) 5
14. [order] from clue 5 apple:Somerset Redstreak: ruled out position(s) 1,4
15. [order] from clue 4 fault:mousiness: ruled out position(s) 2,4
16. [order] from clue 4 maker:Haskell: ruled out position(s) 2,3,4
17. [order] from clue 11 fault:sulphur: ruled out position(s) 1,5
18. [order] from clue 2 apple:Yarlington Mill: ruled out position(s) 1,3,4,5
19. [order] from clue 1 maker:Jethro: ruled out position(s) 1,3,4,5
20. [bijection] apple:Somerset Redstreak: ruled out position(s) 2
21. [bijection] apple:Kingston Black: ruled out position(s) 2,4
22. [bijection] apple:Browns Apple: ruled out position(s) 2,4
23. [bijection] apple:Browns Apple: ruled out position(s) 3,5
24. [bijection] maker:Araminta: ruled out position(s) 2,3
25. [bijection] maker:Araminta: ruled out position(s) 1,5
26. [order] from clue 5 fault:ropiness: ruled out position(s) 1
27. [bijection] apple:Somerset Redstreak: ruled out position(s) 5
28. [order] from clue 5 fault:ropiness: ruled out position(s) 4
29. [bijection] fault:acetification: ruled out position(s) 2
30. [bijection] fault:sulphur: ruled out position(s) 2
31. [order] from clue 11 maker:Haskell: ruled out position(s) 1
32. [order] from clue 4 fault:mousiness: ruled out position(s) 5
33. [bijection] fault:acetification: ruled out position(s) 1,4
34. [bijection] maker:Morwenna: ruled out position(s) 5

---

<sub>seed `2026172949660` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
