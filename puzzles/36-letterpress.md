# The Jobbing Shop on Dyer's Row

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 13 &nbsp;&nbsp; **id** `1adeff24d4e5`

## Introduction

A jobbing print shop where every job has its quoted price, and one hell-box filling up faster than anybody will admit to.
Five compositors are involved. Determine each compositor's quoted price, typeface and mishap.
- **Compositor**: Harriet Lisle, Cecil Braddock, Ned Ashby, Winifred Oakes and Josiah Peake.
- **Quoted price** (listed from cheaper to dearer): $3, $5, $7, $9 and $11.
- **Typeface**: Perpetua, Bodoni, Plantin, Baskerville and Caslon.
- **Mishap**: a slurred impression, an inverted sort, a clean run, a cracked chase and a loose quoin.
Every compositor has a different quoted price, typeface and mishap, so within each category every item is used exactly once.

## Clues

1. The compositor who sets in Perpetua owns up to a cracked chase.
2. At least one of the following holds, and possibly more than one: (a) Ned Ashby quotes $3. (b) Josiah Peake does not quote $9.
3. The compositor who sets in Baskerville and $9 are exactly one price step apart in quoted price order, in one direction or the other.
4. $9 falls somewhere between the compositor who owns up to a clean run and the compositor who owns up to an inverted sort in quoted price order.
5. $7 falls somewhere between the compositor who owns up to a loose quoin and the compositor who owns up to a slurred impression in quoted price order.
6. Winifred Oakes and $7 are exactly one price step apart in quoted price order, in one direction or the other.
7. The compositor who sets in Plantin is dearer than $5 in quoted price order.
8. The compositor who owns up to a loose quoin is dearer than $5 in quoted price order.
9. The following two do NOT both hold; either one alone may hold, and so may neither: (a) Josiah Peake is cheaper than the compositor who sets in Baskerville in quoted price order. (b) Harriet Lisle does not set in Baskerville.
10. Ned Ashby does not own up to a slurred impression.
11. The compositor who owns up to a clean run falls somewhere between Cecil Braddock and the compositor who sets in Perpetua in quoted price order.
12. Cecil Braddock and the compositor who sets in Bodoni are exactly one price step apart in quoted price order, in one direction or the other.
13. Josiah Peake and the compositor who owns up to an inverted sort are exactly one price step apart in quoted price order, in one direction or the other.

## Solving chart

*Quoted price vs Compositor*

| | Harriet Lisle | Cecil Braddock | Ned Ashby | Winifred Oakes | Josiah Peake |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Quoted price vs Typeface*

| | Perpetua | Bodoni | Plantin | Baskerville | Caslon |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Quoted price vs Mishap*

| | a slurred impression | an inverted sort | a clean run | a cracked chase | a loose quoin |
|---|---|---|---|---|---|
| **$3** | | | | | |
| **$5** | | | | | |
| **$7** | | | | | |
| **$9** | | | | | |
| **$11** | | | | | |

*Compositor vs Typeface*

| | Perpetua | Bodoni | Plantin | Baskerville | Caslon |
|---|---|---|---|---|---|
| **Harriet Lisle** | | | | | |
| **Cecil Braddock** | | | | | |
| **Ned Ashby** | | | | | |
| **Winifred Oakes** | | | | | |
| **Josiah Peake** | | | | | |

*Compositor vs Mishap*

| | a slurred impression | an inverted sort | a clean run | a cracked chase | a loose quoin |
|---|---|---|---|---|---|
| **Harriet Lisle** | | | | | |
| **Cecil Braddock** | | | | | |
| **Ned Ashby** | | | | | |
| **Winifred Oakes** | | | | | |
| **Josiah Peake** | | | | | |

*Typeface vs Mishap*

| | a slurred impression | an inverted sort | a clean run | a cracked chase | a loose quoin |
|---|---|---|---|---|---|
| **Perpetua** | | | | | |
| **Bodoni** | | | | | |
| **Plantin** | | | | | |
| **Baskerville** | | | | | |
| **Caslon** | | | | | |

## Solution

| Quoted price | Compositor | Typeface | Mishap |
|---|---|---|---|
| $3 | Ned Ashby | Perpetua | a cracked chase |
| $5 | Winifred Oakes | Caslon | a slurred impression |
| $7 | Harriet Lisle | Baskerville | a clean run |
| $9 | Josiah Peake | Bodoni | a loose quoin |
| $11 | Cecil Braddock | Plantin | an inverted sort |

## How it falls out

1. [order] from clue 11 compositor:Winifred Oakes: ruled out position(s) 1,3,5
2. [order] from clue 10 mishap:a loose quoin: ruled out position(s) 1,2
3. [order] from clue 9 mishap:a clean run: ruled out position(s) 1,5
4. [order] from clue 8 face:Plantin: ruled out position(s) 1,2
5. [order] from clue 7 face:Baskerville: ruled out position(s) 1,2,4
6. [order] from clue 4 mishap:a clean run: ruled out position(s) 4
7. [order] from clue 4 mishap:an inverted sort: ruled out position(s) 1,2,3,4
8. [order] from clue 2 compositor:Josiah Peake: ruled out position(s) 1,2,3,5
9. [order] from clue 1 mishap:a loose quoin: ruled out position(s) 3
10. [order] from clue 1 mishap:a slurred impression: ruled out position(s) 3,4,5
11. [bijection] compositor:Harriet Lisle: ruled out position(s) 4
12. [bijection] compositor:Cecil Braddock: ruled out position(s) 4
13. [bijection] compositor:Ned Ashby: ruled out position(s) 4
14. [bijection] compositor:Winifred Oakes: ruled out position(s) 4
15. [bijection] mishap:a cracked chase: ruled out position(s) 5
16. [bijection] mishap:a loose quoin: ruled out position(s) 5
17. [direct] from clue 12 face:Perpetua: ruled out position(s) 5
18. [order] from clue 13 face:Bodoni: ruled out position(s) 5
19. [bijection] compositor:Harriet Lisle: ruled out position(s) 2
20. [bijection] compositor:Cecil Braddock: ruled out position(s) 2
21. [bijection] compositor:Ned Ashby: ruled out position(s) 2
22. [bijection] mishap:a cracked chase: ruled out position(s) 4
23. [direct] from clue 12 face:Perpetua: ruled out position(s) 4
24. [order] from clue 13 face:Bodoni: ruled out position(s) 1,3
25. [disjunction] from clue 3 compositor:Ned Ashby: ruled out position(s) 3,5
26. [direct] from clue 5 mishap:a slurred impression: ruled out position(s) 1
27. [bijection] compositor:Harriet Lisle: ruled out position(s) 1
28. [bijection] compositor:Cecil Braddock: ruled out position(s) 1
29. [bijection] mishap:a clean run: ruled out position(s) 2
30. [bijection] mishap:a cracked chase: ruled out position(s) 2
31. [bijection] mishap:a cracked chase: ruled out position(s) 3
32. [direct] from clue 12 face:Perpetua: ruled out position(s) 2,3
33. [order] from clue 9 compositor:Cecil Braddock: ruled out position(s) 3
34. [order] from clue 13 face:Bodoni: ruled out position(s) 2
35. [bijection] compositor:Harriet Lisle: ruled out position(s) 5
36. [bijection] face:Plantin: ruled out position(s) 4
37. [bijection] face:Caslon: ruled out position(s) 1,4
38. [bijection] face:Caslon: ruled out position(s) 3,5
39. [disjunction] from clue 6 face:Baskerville: ruled out position(s) 5
40. [bijection] face:Plantin: ruled out position(s) 3

---

<sub>seed `2026173160529` &middot; score 9.1022 &middot; atoms 13 &middot; positives 1 &middot; solved by disjunction</sub>
