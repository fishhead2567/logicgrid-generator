# The Cutbank County Rodeo

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `8beb98920a3f`

## Introduction

Six riders, six entry fees paid in cash at the gate, and a scoreboard that nobody trusts.
Five riders are involved. Determine each rider's entry fee, animal and outcome.
- **Rider**: Cody Vance, Buck Jessup, Dalton Reese, Roselle Kerr and Earlene Tate.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6, $8 and $10.
- **Stock drawn**: Brimstone, Half Past Three, Copper Penny, Little Sister and Tumbleweed.
- **Outcome**: a slap of the free hand, a broken barrier, a re-ride, a disqualification and a clean ride.
Every rider has a different entry fee, animal and outcome, so within each category every item is used exactly once.

## Clues

1. The rider who finishes with a slap of the free hand is cheaper than Earlene Tate in entry fee order. Earlene Tate draws Copper Penny.
2. The rider who draws Half Past Three and $4 are exactly one fee step apart in entry fee order, in one direction or the other.
3. $4 falls somewhere between Dalton Reese and the rider who draws Brimstone in entry fee order. The rider who draws Tumbleweed is cheaper than Dalton Reese in entry fee order.
4. The rider who finishes with a broken barrier is exactly one fee step cheaper than $8, with no entry fee in between.
5. Earlene Tate is cheaper than the rider who finishes with a clean ride in entry fee order.
6. Roselle Kerr is cheaper than the rider who draws Copper Penny in entry fee order.
7. The rider who finishes with a disqualification falls somewhere between the rider who draws Half Past Three and the rider who draws Little Sister in entry fee order.
8. The rider who finishes with a disqualification does not draw Copper Penny. Cody Vance does not finish with a disqualification.

## Solving chart

*Entry fee vs Rider*

| | Cody Vance | Buck Jessup | Dalton Reese | Roselle Kerr | Earlene Tate |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Stock drawn*

| | Brimstone | Half Past Three | Copper Penny | Little Sister | Tumbleweed |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Outcome*

| | a slap of the free hand | a broken barrier | a re-ride | a disqualification | a clean ride |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Rider vs Stock drawn*

| | Brimstone | Half Past Three | Copper Penny | Little Sister | Tumbleweed |
|---|---|---|---|---|---|
| **Cody Vance** | | | | | |
| **Buck Jessup** | | | | | |
| **Dalton Reese** | | | | | |
| **Roselle Kerr** | | | | | |
| **Earlene Tate** | | | | | |

*Rider vs Outcome*

| | a slap of the free hand | a broken barrier | a re-ride | a disqualification | a clean ride |
|---|---|---|---|---|---|
| **Cody Vance** | | | | | |
| **Buck Jessup** | | | | | |
| **Dalton Reese** | | | | | |
| **Roselle Kerr** | | | | | |
| **Earlene Tate** | | | | | |

*Stock drawn vs Outcome*

| | a slap of the free hand | a broken barrier | a re-ride | a disqualification | a clean ride |
|---|---|---|---|---|---|
| **Brimstone** | | | | | |
| **Half Past Three** | | | | | |
| **Copper Penny** | | | | | |
| **Little Sister** | | | | | |
| **Tumbleweed** | | | | | |

## Solution

| Entry fee | Rider | Stock drawn | Outcome |
|---|---|---|---|
| $2 | Roselle Kerr | Brimstone | a slap of the free hand |
| $4 | Earlene Tate | Copper Penny | a re-ride |
| $6 | Cody Vance | Half Past Three | a broken barrier |
| $8 | Buck Jessup | Tumbleweed | a disqualification |
| $10 | Dalton Reese | Little Sister | a clean ride |

## How it falls out

1. [order] from clue 11 rider:Dalton Reese: ruled out position(s) 2
2. [order] from clue 11 stock:Brimstone: ruled out position(s) 2
3. [order] from clue 7 stock:Half Past Three: ruled out position(s) 2,4,5
4. [order] from clue 6 stock:Tumbleweed: ruled out position(s) 5
5. [order] from clue 6 rider:Dalton Reese: ruled out position(s) 1
6. [order] from clue 11 stock:Brimstone: ruled out position(s) 3,4,5
7. [order] from clue 5 outcome:a slap of the free hand: ruled out position(s) 5
8. [order] from clue 5 rider:Earlene Tate: ruled out position(s) 1
9. [order] from clue 4 outcome:a disqualification: ruled out position(s) 1,5
10. [order] from clue 4 stock:Little Sister: ruled out position(s) 2
11. [order] from clue 3 rider:Earlene Tate: ruled out position(s) 5
12. [order] from clue 3 outcome:a clean ride: ruled out position(s) 1,2
13. [order] from clue 5 outcome:a slap of the free hand: ruled out position(s) 4
14. [order] from clue 2 outcome:a broken barrier: ruled out position(s) 1,2,4,5
15. [order] from clue 1 rider:Roselle Kerr: ruled out position(s) 5
16. [order] from clue 1 stock:Copper Penny: ruled out position(s) 1
17. [direct] from clue 8 stock:Copper Penny: ruled out position(s) 5
18. [order] from clue 1 rider:Roselle Kerr: ruled out position(s) 4
19. [bijection] outcome:a slap of the free hand: ruled out position(s) 3
20. [bijection] outcome:a re-ride: ruled out position(s) 3
21. [bijection] outcome:a disqualification: ruled out position(s) 3
22. [bijection] outcome:a clean ride: ruled out position(s) 3
23. [bijection] stock:Half Past Three: ruled out position(s) 1
24. [bijection] stock:Little Sister: ruled out position(s) 1
25. [bijection] stock:Tumbleweed: ruled out position(s) 1
26. [bijection] stock:Little Sister: ruled out position(s) 3,4
27. [order] from clue 4 outcome:a disqualification: ruled out position(s) 2
28. [direct] from clue 10 rider:Cody Vance: ruled out position(s) 4
29. [direct] from clue 9 stock:Copper Penny: ruled out position(s) 4
30. [direct] from clue 8 rider:Earlene Tate: ruled out position(s) 4
31. [order] from clue 1 rider:Roselle Kerr: ruled out position(s) 3
32. [bijection] outcome:a re-ride: ruled out position(s) 4
33. [bijection] outcome:a clean ride: ruled out position(s) 4
34. [bijection] stock:Copper Penny: ruled out position(s) 3
35. [bijection] stock:Tumbleweed: ruled out position(s) 3
36. [bijection] stock:Tumbleweed: ruled out position(s) 2
37. [order] from clue 6 rider:Dalton Reese: ruled out position(s) 3,4
38. [direct] from clue 8 rider:Earlene Tate: ruled out position(s) 3
39. [order] from clue 5 outcome:a slap of the free hand: ruled out position(s) 2
40. [order] from clue 1 rider:Roselle Kerr: ruled out position(s) 2
_... and 4 further steps._

---

<sub>seed `2026172913009` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
