# The Pomace and the Prize

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `adaa7e609ef1`

## Introduction

Six makers press in six different months and each is privately certain the others have let theirs go to vinegar.
Four makers are involved. Determine each maker's pressing month, vessel and fault.
- **Maker**: Silas Vane, Bryony, Jethro and Araminta.
- **Pressing month** (listed from earlier to later): January, February, March and April.
- **Vessel**: a sherry butt, a rum cask, a stainless tank and an oak hogshead.
- **Fault**: a stuck ferment, sulphur, nothing detectable and acetification.
Every maker has a different pressing month, vessel and fault, so within each category every item is used exactly once.

## Clues

1. The maker who is accused of acetification presses in January.
2. Bryony presses in April.
3. Araminta is accused of nothing detectable. Araminta is exactly one month earlier than the maker who ferments in an oak hogshead, with no pressing month in between.
4. The maker who ferments in a rum cask is later than March in pressing month order.
5. The maker who ferments in a stainless tank is exactly one month earlier than the maker who is accused of a stuck ferment, with no pressing month in between.
6. Jethro is exactly one month earlier than the maker who ferments in a rum cask, with no pressing month in between.

## Solving chart

*Pressing month vs Maker*

| | Silas Vane | Bryony | Jethro | Araminta |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Pressing month vs Vessel*

| | a sherry butt | a rum cask | a stainless tank | an oak hogshead |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Pressing month vs Fault*

| | a stuck ferment | sulphur | nothing detectable | acetification |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Maker vs Vessel*

| | a sherry butt | a rum cask | a stainless tank | an oak hogshead |
|---|---|---|---|---|
| **Silas Vane** | | | | |
| **Bryony** | | | | |
| **Jethro** | | | | |
| **Araminta** | | | | |

*Maker vs Fault*

| | a stuck ferment | sulphur | nothing detectable | acetification |
|---|---|---|---|---|
| **Silas Vane** | | | | |
| **Bryony** | | | | |
| **Jethro** | | | | |
| **Araminta** | | | | |

*Vessel vs Fault*

| | a stuck ferment | sulphur | nothing detectable | acetification |
|---|---|---|---|---|
| **a sherry butt** | | | | |
| **a rum cask** | | | | |
| **a stainless tank** | | | | |
| **an oak hogshead** | | | | |

## Solution

| Pressing month | Maker | Vessel | Fault |
|---|---|---|---|
| January | Silas Vane | a sherry butt | acetification |
| February | Araminta | a stainless tank | nothing detectable |
| March | Jethro | an oak hogshead | a stuck ferment |
| April | Bryony | a rum cask | sulphur |

## How it falls out

1. [direct] from clue 3 maker:Bryony: ruled out position(s) 1,2,3
2. [direct] from clue 1 fault:acetification: ruled out position(s) 2,3,4
3. [bijection] fault:a stuck ferment: ruled out position(s) 1
4. [bijection] fault:sulphur: ruled out position(s) 1
5. [bijection] fault:nothing detectable: ruled out position(s) 1
6. [bijection] maker:Silas Vane: ruled out position(s) 4
7. [bijection] maker:Jethro: ruled out position(s) 4
8. [bijection] maker:Araminta: ruled out position(s) 4
9. [direct] from clue 4 fault:nothing detectable: ruled out position(s) 4
10. [direct] from clue 4 maker:Araminta: ruled out position(s) 1
11. [order] from clue 7 vessel:a rum cask: ruled out position(s) 1
12. [order] from clue 6 vessel:a stainless tank: ruled out position(s) 4
13. [order] from clue 5 vessel:an oak hogshead: ruled out position(s) 1,2
14. [order] from clue 2 vessel:a rum cask: ruled out position(s) 2,3
15. [order] from clue 7 maker:Jethro: ruled out position(s) 1,2
16. [bijection] maker:Silas Vane: ruled out position(s) 3
17. [bijection] maker:Araminta: ruled out position(s) 3
18. [bijection] maker:Silas Vane: ruled out position(s) 2
19. [bijection] vessel:a sherry butt: ruled out position(s) 4
20. [bijection] vessel:an oak hogshead: ruled out position(s) 4
21. [direct] from clue 4 fault:nothing detectable: ruled out position(s) 3
22. [bijection] fault:a stuck ferment: ruled out position(s) 2
23. [bijection] fault:sulphur: ruled out position(s) 2
24. [bijection] vessel:a sherry butt: ruled out position(s) 3
25. [bijection] vessel:a stainless tank: ruled out position(s) 3
26. [order] from clue 6 vessel:a stainless tank: ruled out position(s) 1
27. [order] from clue 6 fault:a stuck ferment: ruled out position(s) 4
28. [bijection] fault:sulphur: ruled out position(s) 3
29. [bijection] vessel:a sherry butt: ruled out position(s) 2

---

<sub>seed `2026172778386` &middot; score 4.73 &middot; atoms 7 &middot; positives 3 &middot; solved by order</sub>
