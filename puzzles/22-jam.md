# Preserves, and the Preservation of Grudges

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `f794a760cdbb`

## Introduction

The preserves tent is the most competitive building at the show, and the only one with a locked door.
Five entrants are involved. Determine each entrant's price, preserve and ingredient.
- **Entrant**: Stanislaw, Rafferty, Harriet, Drusilla and Bernadette.
- **Price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Preserve**: green walnut pickle; rosehip syrup; medlar jam; sloe and apple butter; and quince jelly.
- **Secret ingredient**: nothing whatsoever, orange zest, star anise, black pepper and a splash of gin.
Every entrant has a different price, preserve and ingredient, so within each category every item is used exactly once.

## Clues

1. The entrant who adds a splash of gin charges $3.
2. The entrant who enters rosehip syrup does not charge $5. Stanislaw is exactly one price step cheaper than $5, with no price in between.
3. The entrant who adds nothing whatsoever is exactly one price step cheaper than $11, with no price in between.
4. Drusilla falls somewhere between the entrant who enters sloe and apple butter and $3 in price order.
5. Harriet and the entrant who adds orange zest are exactly one price step apart in price order, in one direction or the other.
6. Rafferty is exactly one price step cheaper than the entrant who enters medlar jam, with no price in between.
7. The entrant who enters medlar jam is exactly one price step cheaper than the entrant who adds orange zest, with no price in between.
8. The entrant who enters quince jelly falls somewhere between Drusilla and Harriet in price order.
9. The entrant who enters quince jelly and the entrant who adds star anise are exactly one price step apart in price order, in one direction or the other.

## Solving chart

*Price vs Entrant*

| | Stanislaw | Rafferty | Harriet | Drusilla | Bernadette |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Preserve*

| | green walnut pickle | rosehip syrup | medlar jam | sloe and apple butter | quince jelly |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Secret ingredient*

| | nothing whatsoever | orange zest | star anise | black pepper | a splash of gin |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Entrant vs Preserve*

| | green walnut pickle | rosehip syrup | medlar jam | sloe and apple butter | quince jelly |
|---|---|---|---|---|---|
| **Stanislaw** | | | | | |
| **Rafferty** | | | | | |
| **Harriet** | | | | | |
| **Drusilla** | | | | | |
| **Bernadette** | | | | | |

*Entrant vs Secret ingredient*

| | nothing whatsoever | orange zest | star anise | black pepper | a splash of gin |
|---|---|---|---|---|---|
| **Stanislaw** | | | | | |
| **Rafferty** | | | | | |
| **Harriet** | | | | | |
| **Drusilla** | | | | | |
| **Bernadette** | | | | | |

*Preserve vs Secret ingredient*

| | nothing whatsoever | orange zest | star anise | black pepper | a splash of gin |
|---|---|---|---|---|---|
| **green walnut pickle** | | | | | |
| **rosehip syrup** | | | | | |
| **medlar jam** | | | | | |
| **sloe and apple butter** | | | | | |
| **quince jelly** | | | | | |

## Solution

| Price | Entrant | Preserve | Secret ingredient |
|---|---|---|---|
| $3 | Stanislaw | rosehip syrup | a splash of gin |
| $5 | Drusilla | green walnut pickle | star anise |
| $7 | Rafferty | quince jelly | black pepper |
| $9 | Harriet | medlar jam | nothing whatsoever |
| $11 | Bernadette | sloe and apple butter | orange zest |

## How it falls out

1. [direct] from clue 8 preserve:rosehip syrup: ruled out position(s) 2
2. [direct] from clue 4 secret:a splash of gin: ruled out position(s) 2,3,4,5
3. [bijection] secret:nothing whatsoever: ruled out position(s) 1
4. [bijection] secret:orange zest: ruled out position(s) 1
5. [bijection] secret:star anise: ruled out position(s) 1
6. [bijection] secret:black pepper: ruled out position(s) 1
7. [order] from clue 9 entrant:Stanislaw: ruled out position(s) 2,3,4,5
8. [order] from clue 7 entrant:Drusilla: ruled out position(s) 1,5
9. [order] from clue 7 preserve:sloe and apple butter: ruled out position(s) 1,2
10. [order] from clue 6 preserve:medlar jam: ruled out position(s) 5
11. [order] from clue 3 preserve:quince jelly: ruled out position(s) 1,5
12. [order] from clue 3 entrant:Harriet: ruled out position(s) 3
13. [order] from clue 2 entrant:Rafferty: ruled out position(s) 4,5
14. [order] from clue 2 preserve:medlar jam: ruled out position(s) 1
15. [order] from clue 6 secret:orange zest: ruled out position(s) 2
16. [order] from clue 5 entrant:Harriet: ruled out position(s) 1
17. [order] from clue 3 preserve:quince jelly: ruled out position(s) 2
18. [order] from clue 1 secret:nothing whatsoever: ruled out position(s) 2,3,5
19. [bijection] entrant:Rafferty: ruled out position(s) 1
20. [bijection] entrant:Bernadette: ruled out position(s) 1
21. [bijection] secret:orange zest: ruled out position(s) 4
22. [bijection] secret:star anise: ruled out position(s) 4
23. [bijection] secret:black pepper: ruled out position(s) 4
24. [order] from clue 6 preserve:medlar jam: ruled out position(s) 3
25. [order] from clue 5 entrant:Harriet: ruled out position(s) 5
26. [order] from clue 3 preserve:quince jelly: ruled out position(s) 4
27. [order] from clue 3 entrant:Drusilla: ruled out position(s) 3
28. [order] from clue 10 secret:star anise: ruled out position(s) 3,5
29. [order] from clue 2 entrant:Rafferty: ruled out position(s) 2
30. [order] from clue 2 preserve:medlar jam: ruled out position(s) 2
31. [order] from clue 6 secret:orange zest: ruled out position(s) 3
32. [order] from clue 5 entrant:Harriet: ruled out position(s) 2
33. [order] from clue 3 entrant:Drusilla: ruled out position(s) 4
34. [bijection] entrant:Bernadette: ruled out position(s) 2,3,4
35. [bijection] preserve:green walnut pickle: ruled out position(s) 3,4
36. [bijection] preserve:rosehip syrup: ruled out position(s) 3,4
37. [bijection] preserve:sloe and apple butter: ruled out position(s) 3,4
38. [bijection] preserve:green walnut pickle: ruled out position(s) 1,5
39. [bijection] secret:black pepper: ruled out position(s) 2,5
40. [bijection] preserve:rosehip syrup: ruled out position(s) 5

---

<sub>seed `2026172749654` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
