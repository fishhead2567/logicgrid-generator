# The Jobbing Shop on Dyer's Row

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `e60d8235504a`

## Introduction

A jobbing print shop with six compositors, six quoted prices and one hell-box filling up faster than anybody will admit to.
Four compositors are involved. Determine each compositor's quoted price and job.
- **Compositor**: Harriet Lisle, Ned Ashby, Winifred Oakes and Alfred Nunn.
- **Quoted price** (listed from cheaper to dearer): $3, $5, $7 and $9.
- **Job**: a parish newsletter, a regatta programme, an auction bill and a wedding order of service.
Every compositor has a different quoted price and job, so within each category every item is used exactly once.

## Clues

1. The compositor who is setting a regatta programme quotes $7.
2. Winifred Oakes quotes $5.
3. The compositor who is setting an auction bill quotes $9.
4. Harriet Lisle is exactly one price step cheaper than $5, with no quoted price in between.
5. Ned Ashby and the compositor who is setting a parish newsletter are exactly one price step apart in quoted price order, in one direction or the other.

## Solving chart

*Quoted price vs Compositor*

| | Harriet Lisle | Ned Ashby | Winifred Oakes | Alfred Nunn |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Quoted price vs Job*

| | a parish newsletter | a regatta programme | an auction bill | a wedding order of service |
|---|---|---|---|---|
| **$3** | | | | |
| **$5** | | | | |
| **$7** | | | | |
| **$9** | | | | |

*Compositor vs Job*

| | a parish newsletter | a regatta programme | an auction bill | a wedding order of service |
|---|---|---|---|---|
| **Harriet Lisle** | | | | |
| **Ned Ashby** | | | | |
| **Winifred Oakes** | | | | |
| **Alfred Nunn** | | | | |

## Solution

| Quoted price | Compositor | Job |
|---|---|---|
| $3 | Harriet Lisle | a wedding order of service |
| $5 | Winifred Oakes | a parish newsletter |
| $7 | Ned Ashby | a regatta programme |
| $9 | Alfred Nunn | an auction bill |

## How it falls out

1. [direct] from clue 3 job:an auction bill: ruled out position(s) 1,2,3
2. [direct] from clue 2 compositor:Winifred Oakes: ruled out position(s) 1,3,4
3. [direct] from clue 1 job:a regatta programme: ruled out position(s) 1,2,4
4. [bijection] compositor:Harriet Lisle: ruled out position(s) 2
5. [bijection] compositor:Ned Ashby: ruled out position(s) 2
6. [bijection] compositor:Alfred Nunn: ruled out position(s) 2
7. [bijection] job:a parish newsletter: ruled out position(s) 3,4
8. [bijection] job:a wedding order of service: ruled out position(s) 3,4
9. [order] from clue 5 compositor:Harriet Lisle: ruled out position(s) 3,4
10. [order] from clue 4 compositor:Ned Ashby: ruled out position(s) 4
11. [order] from clue 4 job:a parish newsletter: ruled out position(s) 1
12. [bijection] compositor:Ned Ashby: ruled out position(s) 1
13. [bijection] compositor:Alfred Nunn: ruled out position(s) 1
14. [bijection] compositor:Alfred Nunn: ruled out position(s) 3
15. [bijection] job:a wedding order of service: ruled out position(s) 2

---

<sub>seed `2026172722953` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
