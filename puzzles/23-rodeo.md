# The Cutbank County Rodeo

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `44547aba2a58`

## Introduction

Entry fees paid in cash at the gate, and a scoreboard that nobody trusts.
Five riders are involved. Determine each rider's entry fee, animal and outcome.
- **Rider**: Travis Mundy, Buck Jessup, Cody Vance, Dalton Reese and Earlene Tate.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6, $8 and $10.
- **Stock drawn**: Little Sister, Tumbleweed, Brimstone, Sunday Sermon and Widowmaker.
- **Outcome**: a no-score, a slap of the free hand, a re-ride, a broken barrier and a blown stirrup.
Every rider has a different entry fee, animal and outcome, so within each category every item is used exactly once.

## Clues

1. Earlene Tate draws Tumbleweed.
2. Travis Mundy is cheaper than the rider who draws Brimstone in entry fee order. The rider who finishes with a no-score does not draw Brimstone. Travis Mundy draws Widowmaker.
3. The rider who draws Sunday Sermon does not pay $2.
4. $2 is exactly one fee step cheaper than the rider who finishes with a broken barrier, with no entry fee in between.
5. Dalton Reese is exactly one fee step cheaper than $6, with no entry fee in between.
6. The rider who finishes with a re-ride is exactly one fee step cheaper than Travis Mundy, with no entry fee in between.
7. The rider who finishes with a slap of the free hand and the rider who draws Brimstone are exactly one fee step apart in entry fee order, in one direction or the other.
8. Cody Vance is cheaper than the rider who finishes with a broken barrier in entry fee order.

## Solving chart

*Entry fee vs Rider*

| | Travis Mundy | Buck Jessup | Cody Vance | Dalton Reese | Earlene Tate |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Stock drawn*

| | Little Sister | Tumbleweed | Brimstone | Sunday Sermon | Widowmaker |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Outcome*

| | a no-score | a slap of the free hand | a re-ride | a broken barrier | a blown stirrup |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Rider vs Stock drawn*

| | Little Sister | Tumbleweed | Brimstone | Sunday Sermon | Widowmaker |
|---|---|---|---|---|---|
| **Travis Mundy** | | | | | |
| **Buck Jessup** | | | | | |
| **Cody Vance** | | | | | |
| **Dalton Reese** | | | | | |
| **Earlene Tate** | | | | | |

*Rider vs Outcome*

| | a no-score | a slap of the free hand | a re-ride | a broken barrier | a blown stirrup |
|---|---|---|---|---|---|
| **Travis Mundy** | | | | | |
| **Buck Jessup** | | | | | |
| **Cody Vance** | | | | | |
| **Dalton Reese** | | | | | |
| **Earlene Tate** | | | | | |

*Stock drawn vs Outcome*

| | a no-score | a slap of the free hand | a re-ride | a broken barrier | a blown stirrup |
|---|---|---|---|---|---|
| **Little Sister** | | | | | |
| **Tumbleweed** | | | | | |
| **Brimstone** | | | | | |
| **Sunday Sermon** | | | | | |
| **Widowmaker** | | | | | |

## Solution

| Entry fee | Rider | Stock drawn | Outcome |
|---|---|---|---|
| $2 | Cody Vance | Little Sister | a no-score |
| $4 | Dalton Reese | Sunday Sermon | a broken barrier |
| $6 | Earlene Tate | Tumbleweed | a re-ride |
| $8 | Travis Mundy | Widowmaker | a slap of the free hand |
| $10 | Buck Jessup | Brimstone | a blown stirrup |

## How it falls out

1. [direct] from clue 7 stock:Sunday Sermon: ruled out position(s) 1
2. [order] from clue 9 outcome:a re-ride: ruled out position(s) 5
3. [order] from clue 9 rider:Travis Mundy: ruled out position(s) 1
4. [order] from clue 6 rider:Dalton Reese: ruled out position(s) 1,3,4,5
5. [order] from clue 5 outcome:a broken barrier: ruled out position(s) 1,3,4,5
6. [order] from clue 4 rider:Cody Vance: ruled out position(s) 2,3,4,5
7. [order] from clue 2 rider:Travis Mundy: ruled out position(s) 5
8. [order] from clue 2 stock:Brimstone: ruled out position(s) 1,2
9. [order] from clue 10 outcome:a slap of the free hand: ruled out position(s) 1
10. [order] from clue 9 outcome:a re-ride: ruled out position(s) 4
11. [direct] from clue 3 stock:Widowmaker: ruled out position(s) 1,5
12. [bijection] outcome:a no-score: ruled out position(s) 2
13. [bijection] outcome:a slap of the free hand: ruled out position(s) 2
14. [bijection] outcome:a re-ride: ruled out position(s) 2
15. [bijection] outcome:a blown stirrup: ruled out position(s) 2
16. [bijection] rider:Travis Mundy: ruled out position(s) 2
17. [bijection] rider:Buck Jessup: ruled out position(s) 1,2
18. [bijection] rider:Earlene Tate: ruled out position(s) 1,2
19. [direct] from clue 8 stock:Tumbleweed: ruled out position(s) 1,2
20. [direct] from clue 3 stock:Widowmaker: ruled out position(s) 2
21. [order] from clue 2 stock:Brimstone: ruled out position(s) 3
22. [order] from clue 9 outcome:a re-ride: ruled out position(s) 1
23. [order] from clue 9 rider:Travis Mundy: ruled out position(s) 3
24. [direct] from clue 3 stock:Widowmaker: ruled out position(s) 3
25. [order] from clue 2 stock:Brimstone: ruled out position(s) 4
26. [order] from clue 10 outcome:a slap of the free hand: ruled out position(s) 3,5
27. [direct] from clue 1 outcome:a no-score: ruled out position(s) 5
28. [bijection] outcome:a no-score: ruled out position(s) 3,4
29. [bijection] outcome:a blown stirrup: ruled out position(s) 3,4
30. [bijection] outcome:a blown stirrup: ruled out position(s) 1
31. [bijection] rider:Buck Jessup: ruled out position(s) 4
32. [bijection] rider:Earlene Tate: ruled out position(s) 4
33. [bijection] stock:Little Sister: ruled out position(s) 4,5
34. [bijection] stock:Tumbleweed: ruled out position(s) 4,5
35. [bijection] stock:Sunday Sermon: ruled out position(s) 4,5
36. [bijection] stock:Little Sister: ruled out position(s) 2,3
37. [direct] from clue 8 rider:Earlene Tate: ruled out position(s) 5
38. [bijection] rider:Buck Jessup: ruled out position(s) 3
39. [bijection] stock:Sunday Sermon: ruled out position(s) 3

---

<sub>seed `2026173057582` &middot; score 5.355 &middot; atoms 10 &middot; positives 2 &middot; solved by order</sub>
