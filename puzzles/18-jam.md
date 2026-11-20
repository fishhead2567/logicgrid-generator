# Preserves, and the Preservation of Grudges

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `67d2c52efd4d`

## Introduction

The preserves tent is the most competitive building at the show, and the only one with a locked door.
Five entrants are involved. Determine each entrant's price and jar.
- **Entrant**: Emeka, Drusilla, Stanislaw, Harriet and Ottilie.
- **Price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Jar**: a tall french jar, a jar with a cloth lid, a recycled honey jar, an unlabelled jar and a hexagonal jar.
Every entrant has a different price and jar, so within each category every item is used exactly once.

## Clues

1. Harriet uses a jar with a cloth lid.
2. Stanislaw falls somewhere between $11 and $7 in price order.
3. Ottilie is dearer than $3 in price order.
4. The entrant who uses an unlabelled jar is exactly one price step cheaper than $5, with no price in between.
5. The entrant who uses a tall french jar is exactly one price step cheaper than $11, with no price in between.
6. The entrant who uses a hexagonal jar is cheaper than Emeka in price order.
7. The entrant who uses a tall french jar is exactly one price step cheaper than Harriet, with no price in between.

## Solving chart

*Price vs Entrant*

| | Emeka | Drusilla | Stanislaw | Harriet | Ottilie |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Price vs Jar*

| | a tall french jar | a jar with a cloth lid | a recycled honey jar | an unlabelled jar | a hexagonal jar |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Entrant vs Jar*

| | a tall french jar | a jar with a cloth lid | a recycled honey jar | an unlabelled jar | a hexagonal jar |
|---|---|---|---|---|---|
| **Emeka** | | | | | |
| **Drusilla** | | | | | |
| **Stanislaw** | | | | | |
| **Harriet** | | | | | |
| **Ottilie** | | | | | |

## Solution

| Price | Entrant | Jar |
|---|---|---|
| $3 | Drusilla | an unlabelled jar |
| $5 | Ottilie | a hexagonal jar |
| $7 | Emeka | a recycled honey jar |
| $9 | Stanislaw | a tall french jar |
| $11 | Harriet | a jar with a cloth lid |

## How it falls out

1. [order] from clue 7 entrant:Stanislaw: ruled out position(s) 1,2,3,5
2. [order] from clue 5 jar:a tall french jar: ruled out position(s) 1,2,3,5
3. [order] from clue 4 jar:an unlabelled jar: ruled out position(s) 2,3,4,5
4. [order] from clue 3 jar:a hexagonal jar: ruled out position(s) 5
5. [order] from clue 3 entrant:Emeka: ruled out position(s) 1
6. [order] from clue 2 entrant:Ottilie: ruled out position(s) 1
7. [order] from clue 1 entrant:Harriet: ruled out position(s) 1,2,3,4
8. [direct] from clue 6 jar:a jar with a cloth lid: ruled out position(s) 1,2,3,4
9. [bijection] entrant:Emeka: ruled out position(s) 4,5
10. [bijection] entrant:Drusilla: ruled out position(s) 4,5
11. [bijection] entrant:Ottilie: ruled out position(s) 4,5
12. [bijection] entrant:Drusilla: ruled out position(s) 2,3
13. [bijection] jar:a recycled honey jar: ruled out position(s) 1,4,5
14. [bijection] jar:a hexagonal jar: ruled out position(s) 1,4
15. [order] from clue 3 jar:a hexagonal jar: ruled out position(s) 3
16. [order] from clue 3 entrant:Emeka: ruled out position(s) 2
17. [bijection] entrant:Ottilie: ruled out position(s) 3
18. [bijection] jar:a recycled honey jar: ruled out position(s) 2

---

<sub>seed `2026173017987` &middot; score 4.86 &middot; atoms 7 &middot; positives 1 &middot; solved by order</sub>
