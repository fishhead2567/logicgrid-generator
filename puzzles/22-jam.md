# Preserves, and the Preservation of Grudges

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `b0adf92f3b32`

## Introduction

The preserves tent is the most competitive building at the show, and the only one with a locked door.
Five entrants are involved. Determine each entrant's price, preserve, jar and ingredient.
- **Entrant**: Bernadette, Emeka, Ottilie, Drusilla and Rafferty.
- **Price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Preserve**: quince jelly; rosehip syrup; hot pepper jelly; damson cheese; and sloe and apple butter.
- **Jar**: a tall french jar, a squat kilner, a sealed crock, a recycled honey jar and a hexagonal jar.
- **Secret ingredient**: star anise, a bay leaf, a splash of gin, a spoon of treacle and black pepper.
Every entrant has a different price, preserve, jar and ingredient, so within each category every item is used exactly once.

## Clues

1. The entrant who uses a tall french jar charges $9.
2. The entrant who enters rosehip syrup falls somewhere between $11 and the entrant who adds black pepper in price order.
3. Emeka is dearer than $7 in price order. Emeka does not enter sloe and apple butter.
4. The entrant who adds star anise does not charge $11. The entrant who enters hot pepper jelly does not add star anise.
5. The entrant who uses a squat kilner falls somewhere between Bernadette and Drusilla in price order.
6. The entrant who enters hot pepper jelly is exactly one price step cheaper than the entrant who adds black pepper, with no price in between.
7. The entrant who uses a hexagonal jar is exactly one price step cheaper than Ottilie, with no price in between.
8. The entrant who enters rosehip syrup falls somewhere between the entrant who uses a sealed crock and the entrant who adds a spoon of treacle in price order.
9. The entrant who uses a sealed crock is cheaper than the entrant who adds a bay leaf in price order.
10. Drusilla is exactly one price step cheaper than the entrant who uses a hexagonal jar, with no price in between.
11. The entrant who adds a spoon of treacle is cheaper than the entrant who enters sloe and apple butter in price order. The entrant who enters quince jelly does not add a spoon of treacle.

## Solving chart

*Price vs Entrant*

| | Bernadette | Emeka | Ottilie | Drusilla | Rafferty |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Preserve*

| | quince jelly | rosehip syrup | hot pepper jelly | damson cheese | sloe and apple butter |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Jar*

| | a tall french jar | a squat kilner | a sealed crock | a recycled honey jar | a hexagonal jar |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Secret ingredient*

| | star anise | a bay leaf | a splash of gin | a spoon of treacle | black pepper |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Entrant vs Preserve*

| | quince jelly | rosehip syrup | hot pepper jelly | damson cheese | sloe and apple butter |
|---|---|---|---|---|---|
| **Bernadette** | | | | | |
| **Emeka** | | | | | |
| **Ottilie** | | | | | |
| **Drusilla** | | | | | |
| **Rafferty** | | | | | |

*Entrant vs Jar*

| | a tall french jar | a squat kilner | a sealed crock | a recycled honey jar | a hexagonal jar |
|---|---|---|---|---|---|
| **Bernadette** | | | | | |
| **Emeka** | | | | | |
| **Ottilie** | | | | | |
| **Drusilla** | | | | | |
| **Rafferty** | | | | | |

*Entrant vs Secret ingredient*

| | star anise | a bay leaf | a splash of gin | a spoon of treacle | black pepper |
|---|---|---|---|---|---|
| **Bernadette** | | | | | |
| **Emeka** | | | | | |
| **Ottilie** | | | | | |
| **Drusilla** | | | | | |
| **Rafferty** | | | | | |

*Preserve vs Jar*

| | a tall french jar | a squat kilner | a sealed crock | a recycled honey jar | a hexagonal jar |
|---|---|---|---|---|---|
| **quince jelly** | | | | | |
| **rosehip syrup** | | | | | |
| **hot pepper jelly** | | | | | |
| **damson cheese** | | | | | |
| **sloe and apple butter** | | | | | |

*Preserve vs Secret ingredient*

| | star anise | a bay leaf | a splash of gin | a spoon of treacle | black pepper |
|---|---|---|---|---|---|
| **quince jelly** | | | | | |
| **rosehip syrup** | | | | | |
| **hot pepper jelly** | | | | | |
| **damson cheese** | | | | | |
| **sloe and apple butter** | | | | | |

*Jar vs Secret ingredient*

| | star anise | a bay leaf | a splash of gin | a spoon of treacle | black pepper |
|---|---|---|---|---|---|
| **a tall french jar** | | | | | |
| **a squat kilner** | | | | | |
| **a sealed crock** | | | | | |
| **a recycled honey jar** | | | | | |
| **a hexagonal jar** | | | | | |

## Solution

| Price | Entrant | Preserve | Jar | Secret ingredient |
|---|---|---|---|---|
| $3 | Drusilla | hot pepper jelly | a sealed crock | a splash of gin |
| $5 | Rafferty | quince jelly | a hexagonal jar | black pepper |
| $7 | Ottilie | rosehip syrup | a squat kilner | star anise |
| $9 | Emeka | damson cheese | a tall french jar | a spoon of treacle |
| $11 | Bernadette | sloe and apple butter | a recycled honey jar | a bay leaf |

## How it falls out

1. [direct] from clue 13 secret:star anise: ruled out position(s) 5
2. [direct] from clue 3 jar:a tall french jar: ruled out position(s) 1,2,3,5
3. [bijection] jar:a squat kilner: ruled out position(s) 4
4. [bijection] jar:a sealed crock: ruled out position(s) 4
5. [bijection] jar:a recycled honey jar: ruled out position(s) 4
6. [bijection] jar:a hexagonal jar: ruled out position(s) 4
7. [order] from clue 14 entrant:Drusilla: ruled out position(s) 3,5
8. [order] from clue 14 jar:a hexagonal jar: ruled out position(s) 1
9. [order] from clue 12 preserve:rosehip syrup: ruled out position(s) 1,5
10. [order] from clue 10 secret:a spoon of treacle: ruled out position(s) 5
11. [order] from clue 10 preserve:sloe and apple butter: ruled out position(s) 1
12. [order] from clue 9 jar:a hexagonal jar: ruled out position(s) 5
13. [order] from clue 9 entrant:Ottilie: ruled out position(s) 1,2,5
14. [order] from clue 14 entrant:Drusilla: ruled out position(s) 4
15. [order] from clue 8 jar:a sealed crock: ruled out position(s) 5
16. [order] from clue 8 secret:a bay leaf: ruled out position(s) 1
17. [order] from clue 12 preserve:rosehip syrup: ruled out position(s) 4
18. [order] from clue 12 secret:a spoon of treacle: ruled out position(s) 2
19. [order] from clue 7 secret:black pepper: ruled out position(s) 3,4,5
20. [order] from clue 5 jar:a squat kilner: ruled out position(s) 1,5
21. [order] from clue 5 entrant:Bernadette: ruled out position(s) 1,2
22. [order] from clue 4 entrant:Emeka: ruled out position(s) 1,2,3
23. [order] from clue 2 preserve:hot pepper jelly: ruled out position(s) 2,3,4,5
24. [order] from clue 2 secret:black pepper: ruled out position(s) 1
25. [order] from clue 7 preserve:rosehip syrup: ruled out position(s) 2
26. [order] from clue 12 jar:a sealed crock: ruled out position(s) 3
27. [order] from clue 12 secret:a spoon of treacle: ruled out position(s) 1,3
28. [order] from clue 10 preserve:sloe and apple butter: ruled out position(s) 2,3,4
29. [direct] from clue 11 entrant:Emeka: ruled out position(s) 5
30. [direct] from clue 6 preserve:quince jelly: ruled out position(s) 4
31. [direct] from clue 1 secret:star anise: ruled out position(s) 1
32. [bijection] entrant:Bernadette: ruled out position(s) 4
33. [bijection] entrant:Ottilie: ruled out position(s) 4
34. [bijection] entrant:Rafferty: ruled out position(s) 4
35. [bijection] jar:a recycled honey jar: ruled out position(s) 1,2,3
36. [bijection] preserve:quince jelly: ruled out position(s) 1,3,5
37. [bijection] preserve:damson cheese: ruled out position(s) 1,3,5
38. [bijection] preserve:damson cheese: ruled out position(s) 2
39. [bijection] secret:star anise: ruled out position(s) 2,4
40. [bijection] secret:a bay leaf: ruled out position(s) 2,4
_... and 10 further steps._

---

<sub>seed `2026172749654` &middot; score 6.13 &middot; atoms 14 &middot; positives 1 &middot; solved by order</sub>
