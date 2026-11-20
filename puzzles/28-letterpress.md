# The Jobbing Shop on Dyer's Row

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `cd2ec448a3eb`

## Introduction

A jobbing print shop where every job has its quoted price, and one hell-box filling up faster than anybody will admit to.
Five compositors are involved. Determine each compositor's quoted price, typeface and job.
- **Compositor**: Alfred Nunn, Winifred Oakes, Harriet Lisle, Verity Stallard and Ned Ashby.
- **Quoted price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Typeface**: Bodoni, Perpetua, Gill Sans, Caslon and Garamond.
- **Job**: a seed catalogue, a parish newsletter, a regatta programme, a wedding order of service and an auction bill.
Every compositor has a different quoted price, typeface and job, so within each category every item is used exactly once.

## Clues

1. The compositor who sets in Gill Sans and $5 are exactly one price step apart in quoted price order, in one direction or the other.
2. $9 is exactly one price step cheaper than the compositor who is setting a wedding order of service, with no quoted price in between.
3. Harriet Lisle does not quote $11.
4. Winifred Oakes is exactly one price step cheaper than $7, with no quoted price in between.
5. The compositor who sets in Caslon and $9 are exactly one price step apart in quoted price order, in one direction or the other.
6. Ned Ashby falls somewhere between the compositor who sets in Caslon and the compositor who sets in Perpetua in quoted price order.
7. The compositor who is setting a parish newsletter falls somewhere between the compositor who sets in Garamond and the compositor who sets in Gill Sans in quoted price order.
8. Verity Stallard is exactly one price step cheaper than the compositor who sets in Bodoni, with no quoted price in between.
9. The compositor who is setting a seed catalogue is exactly one price step cheaper than Ned Ashby, with no quoted price in between.
10. The compositor who sets in Caslon is not setting a wedding order of service.
11. The compositor who sets in Caslon and the compositor who is setting an auction bill are exactly one price step apart in quoted price order, in one direction or the other.

## Solving chart

*Quoted price vs Compositor*

| | Alfred Nunn | Winifred Oakes | Harriet Lisle | Verity Stallard | Ned Ashby |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Quoted price vs Typeface*

| | Bodoni | Perpetua | Gill Sans | Caslon | Garamond |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Quoted price vs Job*

| | a seed catalogue | a parish newsletter | a regatta programme | a wedding order of service | an auction bill |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Compositor vs Typeface*

| | Bodoni | Perpetua | Gill Sans | Caslon | Garamond |
|---|---|---|---|---|---|
| **Alfred Nunn** | | | | | |
| **Winifred Oakes** | | | | | |
| **Harriet Lisle** | | | | | |
| **Verity Stallard** | | | | | |
| **Ned Ashby** | | | | | |

*Compositor vs Job*

| | a seed catalogue | a parish newsletter | a regatta programme | a wedding order of service | an auction bill |
|---|---|---|---|---|---|
| **Alfred Nunn** | | | | | |
| **Winifred Oakes** | | | | | |
| **Harriet Lisle** | | | | | |
| **Verity Stallard** | | | | | |
| **Ned Ashby** | | | | | |

*Typeface vs Job*

| | a seed catalogue | a parish newsletter | a regatta programme | a wedding order of service | an auction bill |
|---|---|---|---|---|---|
| **Bodoni** | | | | | |
| **Perpetua** | | | | | |
| **Gill Sans** | | | | | |
| **Caslon** | | | | | |
| **Garamond** | | | | | |

## Solution

| Quoted price | Compositor | Typeface | Job |
|---|---|---|---|
| $3 | Verity Stallard | Gill Sans | a regatta programme |
| $5 | Winifred Oakes | Bodoni | a parish newsletter |
| $7 | Harriet Lisle | Caslon | a seed catalogue |
| $9 | Ned Ashby | Garamond | an auction bill |
| $11 | Alfred Nunn | Perpetua | a wedding order of service |

## How it falls out

1. [direct] from clue 5 compositor:Harriet Lisle: ruled out position(s) 5
2. [order] from clue 11 compositor:Ned Ashby: ruled out position(s) 1,5
3. [order] from clue 9 job:a wedding order of service: ruled out position(s) 1,2,3,4
4. [order] from clue 8 face:Gill Sans: ruled out position(s) 2,4,5
5. [order] from clue 7 job:a parish newsletter: ruled out position(s) 1,5
6. [order] from clue 7 face:Garamond: ruled out position(s) 2
7. [order] from clue 6 compositor:Verity Stallard: ruled out position(s) 5
8. [order] from clue 6 face:Bodoni: ruled out position(s) 1
9. [order] from clue 3 face:Caslon: ruled out position(s) 1,2,4
10. [order] from clue 11 face:Perpetua: ruled out position(s) 4
11. [order] from clue 4 job:an auction bill: ruled out position(s) 1,3,5
12. [order] from clue 2 compositor:Winifred Oakes: ruled out position(s) 1,3,4,5
13. [order] from clue 1 job:a seed catalogue: ruled out position(s) 4,5
14. [direct] from clue 10 face:Caslon: ruled out position(s) 5
15. [order] from clue 11 compositor:Ned Ashby: ruled out position(s) 3
16. [order] from clue 11 face:Perpetua: ruled out position(s) 2,3
17. [order] from clue 1 job:a seed catalogue: ruled out position(s) 2
18. [bijection] compositor:Alfred Nunn: ruled out position(s) 2
19. [bijection] compositor:Harriet Lisle: ruled out position(s) 2
20. [bijection] compositor:Verity Stallard: ruled out position(s) 2
21. [bijection] compositor:Ned Ashby: ruled out position(s) 2
22. [bijection] compositor:Alfred Nunn: ruled out position(s) 1,3,4
23. [bijection] face:Bodoni: ruled out position(s) 3
24. [bijection] face:Gill Sans: ruled out position(s) 3
25. [bijection] face:Garamond: ruled out position(s) 3
26. [bijection] face:Bodoni: ruled out position(s) 4,5
27. [bijection] job:a regatta programme: ruled out position(s) 5
28. [order] from clue 7 face:Garamond: ruled out position(s) 1
29. [order] from clue 11 face:Perpetua: ruled out position(s) 1
30. [order] from clue 1 job:a seed catalogue: ruled out position(s) 1
31. [order] from clue 6 compositor:Verity Stallard: ruled out position(s) 3,4
32. [bijection] compositor:Harriet Lisle: ruled out position(s) 1,4
33. [bijection] face:Garamond: ruled out position(s) 5
34. [bijection] job:a parish newsletter: ruled out position(s) 3
35. [bijection] job:a regatta programme: ruled out position(s) 3
36. [bijection] job:a regatta programme: ruled out position(s) 2,4
37. [order] from clue 7 job:a parish newsletter: ruled out position(s) 4
38. [bijection] job:an auction bill: ruled out position(s) 2

---

<sub>seed `2026172997174` &middot; score 5.675 &middot; atoms 11 &middot; positives 0 &middot; solved by order</sub>
