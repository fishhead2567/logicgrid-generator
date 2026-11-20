# Preserves, and the Preservation of Grudges

**Difficulty** 2/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `5e04d153fe0b`

## Introduction

The preserves tent is the most competitive building at the show, and the only one with a locked door.
Four entrants are involved. Determine each entrant's price and preserve.
- **Entrant**: Harriet, Emeka, Ottilie and Bernadette.
- **Price** (listed from cheaper to dearer): $3, $5, $7 and $9.
- **Preserve**: medlar jam; green walnut pickle; sloe and apple butter; and quince jelly.
Every entrant has a different price and preserve, so within each category every item is used exactly once.

## Clues

1. The entrant who enters sloe and apple butter charges $9.
2. The entrant who enters quince jelly charges $5.
3. The entrant who enters green walnut pickle is exactly one price step cheaper than $5, with no price in between.
4. $3 is exactly one price step cheaper than Emeka, with no price in between.
5. The entrant who enters quince jelly is cheaper than Ottilie in price order.
6. Harriet and the entrant who enters sloe and apple butter are exactly one price step apart in price order, in one direction or the other.

## Solving chart

*Price vs Entrant*

| | Harriet | Emeka | Ottilie | Bernadette |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Price vs Preserve*

| | medlar jam | green walnut pickle | sloe and apple butter | quince jelly |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Entrant vs Preserve*

| | medlar jam | green walnut pickle | sloe and apple butter | quince jelly |
|---|---|---|---|---|
| **Harriet** | | | | |
| **Emeka** | | | | |
| **Ottilie** | | | | |
| **Bernadette** | | | | |

## Solution

| Price | Entrant | Preserve |
|---|---|---|
| $3 | Bernadette | green walnut pickle |
| $5 | Emeka | quince jelly |
| $7 | Harriet | medlar jam |
| $9 | Ottilie | sloe and apple butter |

## How it falls out

1. [direct] from clue 4 preserve:quince jelly: ruled out position(s) 1,3,4
2. [direct] from clue 1 preserve:sloe and apple butter: ruled out position(s) 1,2,3
3. [bijection] preserve:medlar jam: ruled out position(s) 2,4
4. [bijection] preserve:green walnut pickle: ruled out position(s) 2,4
5. [order] from clue 6 entrant:Harriet: ruled out position(s) 1,2,4
6. [order] from clue 5 entrant:Emeka: ruled out position(s) 1,3,4
7. [order] from clue 3 preserve:green walnut pickle: ruled out position(s) 3
8. [order] from clue 2 entrant:Ottilie: ruled out position(s) 1,2
9. [bijection] entrant:Ottilie: ruled out position(s) 3
10. [bijection] entrant:Bernadette: ruled out position(s) 2,3
11. [bijection] entrant:Bernadette: ruled out position(s) 4
12. [bijection] preserve:medlar jam: ruled out position(s) 1

---

<sub>seed `2026172807118` &middot; score 4.27 &middot; atoms 6 &middot; positives 2 &middot; solved by order</sub>
