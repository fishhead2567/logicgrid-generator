# Preserves, and the Preservation of Grudges

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `d90682969ed6`

## Introduction

The preserves tent is the most competitive building at the show, and the only one with a locked door.
Five entrants are involved. Determine each entrant's price, preserve and ingredient.
- **Entrant**: Ottilie, Emeka, Harriet, Bernadette and Stanislaw.
- **Price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Preserve**: rosehip syrup; hot pepper jelly; green walnut pickle; quince jelly; and sloe and apple butter.
- **Secret ingredient**: star anise, orange zest, a splash of gin, black pepper and nothing whatsoever.
Every entrant has a different price, preserve and ingredient, so within each category every item is used exactly once.

## Clues

1. The entrant who adds nothing whatsoever and $5 are exactly one price step apart in price order, in one direction or the other. Bernadette charges $5.
2. The entrant who adds star anise charges $3.
3. Stanislaw is exactly one price step cheaper than $9, with no price in between. The entrant who adds black pepper does not charge $9.
4. The entrant who adds a splash of gin is dearer than $5 in price order.
5. The entrant who enters green walnut pickle is cheaper than $11 in price order.
6. Emeka is exactly one price step cheaper than the entrant who enters green walnut pickle, with no price in between.
7. Ottilie is cheaper than the entrant who enters hot pepper jelly in price order.
8. The entrant who enters rosehip syrup and the entrant who adds a splash of gin are exactly one price step apart in price order, in one direction or the other.
9. Bernadette is exactly one price step cheaper than the entrant who enters quince jelly, with no price in between.

## Solving chart

*Price vs Entrant*

| | Ottilie | Emeka | Harriet | Bernadette | Stanislaw |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Preserve*

| | rosehip syrup | hot pepper jelly | green walnut pickle | quince jelly | sloe and apple butter |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Secret ingredient*

| | star anise | orange zest | a splash of gin | black pepper | nothing whatsoever |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Entrant vs Preserve*

| | rosehip syrup | hot pepper jelly | green walnut pickle | quince jelly | sloe and apple butter |
|---|---|---|---|---|---|
| **Ottilie** | | | | | |
| **Emeka** | | | | | |
| **Harriet** | | | | | |
| **Bernadette** | | | | | |
| **Stanislaw** | | | | | |

*Entrant vs Secret ingredient*

| | star anise | orange zest | a splash of gin | black pepper | nothing whatsoever |
|---|---|---|---|---|---|
| **Ottilie** | | | | | |
| **Emeka** | | | | | |
| **Harriet** | | | | | |
| **Bernadette** | | | | | |
| **Stanislaw** | | | | | |

*Preserve vs Secret ingredient*

| | star anise | orange zest | a splash of gin | black pepper | nothing whatsoever |
|---|---|---|---|---|---|
| **rosehip syrup** | | | | | |
| **hot pepper jelly** | | | | | |
| **green walnut pickle** | | | | | |
| **quince jelly** | | | | | |
| **sloe and apple butter** | | | | | |

## Solution

| Price | Entrant | Preserve | Secret ingredient |
|---|---|---|---|
| $3 | Emeka | sloe and apple butter | star anise |
| $5 | Bernadette | green walnut pickle | black pepper |
| $7 | Stanislaw | quince jelly | nothing whatsoever |
| $9 | Ottilie | rosehip syrup | orange zest |
| $11 | Harriet | hot pepper jelly | a splash of gin |

## How it falls out

1. [direct] from clue 4 secret:black pepper: ruled out position(s) 4
2. [direct] from clue 2 entrant:Bernadette: ruled out position(s) 1,3,4,5
3. [direct] from clue 1 secret:star anise: ruled out position(s) 2,3,4,5
4. [bijection] entrant:Ottilie: ruled out position(s) 2
5. [bijection] entrant:Emeka: ruled out position(s) 2
6. [bijection] entrant:Harriet: ruled out position(s) 2
7. [bijection] entrant:Stanislaw: ruled out position(s) 2
8. [bijection] secret:orange zest: ruled out position(s) 1
9. [bijection] secret:a splash of gin: ruled out position(s) 1
10. [bijection] secret:black pepper: ruled out position(s) 1
11. [bijection] secret:nothing whatsoever: ruled out position(s) 1
12. [order] from clue 11 secret:a splash of gin: ruled out position(s) 2
13. [order] from clue 10 preserve:rosehip syrup: ruled out position(s) 1
14. [order] from clue 9 entrant:Ottilie: ruled out position(s) 5
15. [order] from clue 9 preserve:hot pepper jelly: ruled out position(s) 1
16. [order] from clue 8 entrant:Emeka: ruled out position(s) 5
17. [order] from clue 8 preserve:green walnut pickle: ruled out position(s) 1,3
18. [order] from clue 7 preserve:quince jelly: ruled out position(s) 1,2,4,5
19. [order] from clue 6 entrant:Stanislaw: ruled out position(s) 1,4,5
20. [order] from clue 5 secret:nothing whatsoever: ruled out position(s) 2,4,5
21. [order] from clue 3 preserve:green walnut pickle: ruled out position(s) 5
22. [order] from clue 8 entrant:Emeka: ruled out position(s) 4
23. [bijection] entrant:Ottilie: ruled out position(s) 3
24. [bijection] entrant:Emeka: ruled out position(s) 3
25. [bijection] entrant:Harriet: ruled out position(s) 3
26. [bijection] entrant:Harriet: ruled out position(s) 1,4
27. [bijection] preserve:rosehip syrup: ruled out position(s) 3
28. [bijection] preserve:hot pepper jelly: ruled out position(s) 3
29. [bijection] preserve:sloe and apple butter: ruled out position(s) 3
30. [bijection] preserve:sloe and apple butter: ruled out position(s) 2,4,5
31. [bijection] secret:orange zest: ruled out position(s) 3
32. [bijection] secret:a splash of gin: ruled out position(s) 3
33. [bijection] secret:black pepper: ruled out position(s) 3
34. [order] from clue 10 preserve:rosehip syrup: ruled out position(s) 2
35. [order] from clue 8 preserve:green walnut pickle: ruled out position(s) 4
36. [bijection] entrant:Ottilie: ruled out position(s) 1
37. [bijection] preserve:hot pepper jelly: ruled out position(s) 2
38. [order] from clue 9 preserve:hot pepper jelly: ruled out position(s) 4
39. [bijection] preserve:rosehip syrup: ruled out position(s) 5
40. [order] from clue 10 secret:a splash of gin: ruled out position(s) 4
_... and 3 further steps._

---

<sub>seed `2026172805087` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
