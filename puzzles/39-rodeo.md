# The Cutbank County Rodeo

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 13 &nbsp;&nbsp; **id** `083e2f657f70`

## Introduction

Entry fees paid in cash at the gate, and a scoreboard that nobody trusts.
Five riders are involved. Determine each rider's entry fee, event, animal and outcome.
- **Rider**: Travis Mundy, Dalton Reese, Cody Vance, Marla Hobbs and Buck Jessup.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6, $8 and $10.
- **Event**: tie-down roping, bareback, barrel racing, team roping and bull riding.
- **Stock drawn**: Tumbleweed, Widowmaker, Little Sister, Brimstone and Sunday Sermon.
- **Outcome**: a broken barrier, a no-score, a blown stirrup, a slap of the free hand and a clean ride.
Every rider has a different entry fee, event, animal and outcome, so within each category every item is used exactly once.

## Clues

1. The rider who enters bareback pays $10. The rider who finishes with a no-score falls somewhere between $10 and the rider who draws Sunday Sermon in entry fee order.
2. Dalton Reese and $6 are exactly one fee step apart in entry fee order, in one direction or the other. Travis Mundy is exactly one fee step cheaper than $6, with no entry fee in between.
3. The rider who enters team roping is cheaper than $4 in entry fee order.
4. At least one of the following holds, and possibly more than one: (a) $6 is exactly one fee step cheaper than the rider who enters tie-down roping, with no entry fee in between. (b) Cody Vance enters tie-down roping.
5. At least one of the following holds, and possibly more than one: (a) The rider who finishes with a no-score is dearer than $6 in entry fee order. (b) The rider who finishes with a slap of the free hand is cheaper than the rider who draws Little Sister in entry fee order.
6. At least one of the following holds, and possibly more than one: (a) The rider who finishes with a no-score is dearer than $6 in entry fee order. (b) The rider who finishes with a slap of the free hand pays $6.
7. Dalton Reese does not finish with a no-score.
8. The rider who finishes with a broken barrier is cheaper than the rider who draws Widowmaker in entry fee order.
9. Cody Vance and the rider who draws Tumbleweed are exactly one fee step apart in entry fee order, in one direction or the other.
10. The rider who draws Tumbleweed falls somewhere between the rider who finishes with a blown stirrup and the rider who finishes with a clean ride in entry fee order.
11. The rider who finishes with a slap of the free hand falls somewhere between Cody Vance and Marla Hobbs in entry fee order.
12. The rider who enters bull riding and the rider who draws Brimstone are exactly one fee step apart in entry fee order, in one direction or the other.
13. The rider who enters team roping is cheaper than the rider who finishes with a blown stirrup in entry fee order.

## Solving chart

*Entry fee vs Rider*

| | Travis Mundy | Dalton Reese | Cody Vance | Marla Hobbs | Buck Jessup |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Event*

| | tie-down roping | bareback | barrel racing | team roping | bull riding |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Stock drawn*

| | Tumbleweed | Widowmaker | Little Sister | Brimstone | Sunday Sermon |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Outcome*

| | a broken barrier | a no-score | a blown stirrup | a slap of the free hand | a clean ride |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Rider vs Event*

| | tie-down roping | bareback | barrel racing | team roping | bull riding |
|---|---|---|---|---|---|
| **Travis Mundy** | | | | | |
| **Dalton Reese** | | | | | |
| **Cody Vance** | | | | | |
| **Marla Hobbs** | | | | | |
| **Buck Jessup** | | | | | |

*Rider vs Stock drawn*

| | Tumbleweed | Widowmaker | Little Sister | Brimstone | Sunday Sermon |
|---|---|---|---|---|---|
| **Travis Mundy** | | | | | |
| **Dalton Reese** | | | | | |
| **Cody Vance** | | | | | |
| **Marla Hobbs** | | | | | |
| **Buck Jessup** | | | | | |

*Rider vs Outcome*

| | a broken barrier | a no-score | a blown stirrup | a slap of the free hand | a clean ride |
|---|---|---|---|---|---|
| **Travis Mundy** | | | | | |
| **Dalton Reese** | | | | | |
| **Cody Vance** | | | | | |
| **Marla Hobbs** | | | | | |
| **Buck Jessup** | | | | | |

*Event vs Stock drawn*

| | Tumbleweed | Widowmaker | Little Sister | Brimstone | Sunday Sermon |
|---|---|---|---|---|---|
| **tie-down roping** | | | | | |
| **bareback** | | | | | |
| **barrel racing** | | | | | |
| **team roping** | | | | | |
| **bull riding** | | | | | |

*Event vs Outcome*

| | a broken barrier | a no-score | a blown stirrup | a slap of the free hand | a clean ride |
|---|---|---|---|---|---|
| **tie-down roping** | | | | | |
| **bareback** | | | | | |
| **barrel racing** | | | | | |
| **team roping** | | | | | |
| **bull riding** | | | | | |

*Stock drawn vs Outcome*

| | a broken barrier | a no-score | a blown stirrup | a slap of the free hand | a clean ride |
|---|---|---|---|---|---|
| **Tumbleweed** | | | | | |
| **Widowmaker** | | | | | |
| **Little Sister** | | | | | |
| **Brimstone** | | | | | |
| **Sunday Sermon** | | | | | |

## Solution

| Entry fee | Rider | Event | Stock drawn | Outcome |
|---|---|---|---|---|
| $2 | Cody Vance | team roping | Sunday Sermon | a clean ride |
| $4 | Travis Mundy | bull riding | Tumbleweed | a no-score |
| $6 | Buck Jessup | barrel racing | Brimstone | a slap of the free hand |
| $8 | Dalton Reese | tie-down roping | Little Sister | a broken barrier |
| $10 | Marla Hobbs | bareback | Widowmaker | a blown stirrup |

## How it falls out

1. [direct] from clue 11 event:bareback: ruled out position(s) 1,2,3,4
2. [bijection] event:tie-down roping: ruled out position(s) 5
3. [bijection] event:barrel racing: ruled out position(s) 5
4. [bijection] event:team roping: ruled out position(s) 5
5. [bijection] event:bull riding: ruled out position(s) 5
6. [order] from clue 9 outcome:a blown stirrup: ruled out position(s) 1
7. [order] from clue 8 stock:Tumbleweed: ruled out position(s) 1,5
8. [order] from clue 7 outcome:a broken barrier: ruled out position(s) 5
9. [order] from clue 7 stock:Widowmaker: ruled out position(s) 1
10. [order] from clue 5 rider:Dalton Reese: ruled out position(s) 1,3,5
11. [order] from clue 4 outcome:a slap of the free hand: ruled out position(s) 1,5
12. [order] from clue 3 event:team roping: ruled out position(s) 2,3,4
13. [order] from clue 2 rider:Travis Mundy: ruled out position(s) 1,3,4,5
14. [order] from clue 1 outcome:a no-score: ruled out position(s) 1,5
15. [order] from clue 1 stock:Sunday Sermon: ruled out position(s) 4,5
16. [bijection] event:tie-down roping: ruled out position(s) 1
17. [bijection] event:barrel racing: ruled out position(s) 1
18. [bijection] event:bull riding: ruled out position(s) 1
19. [bijection] rider:Dalton Reese: ruled out position(s) 2
20. [bijection] rider:Cody Vance: ruled out position(s) 2
21. [bijection] rider:Marla Hobbs: ruled out position(s) 2
22. [bijection] rider:Buck Jessup: ruled out position(s) 2
23. [direct] from clue 15 outcome:a no-score: ruled out position(s) 4
24. [order] from clue 1 stock:Sunday Sermon: ruled out position(s) 3
25. [bijection] rider:Cody Vance: ruled out position(s) 4
26. [bijection] rider:Marla Hobbs: ruled out position(s) 4
27. [bijection] rider:Buck Jessup: ruled out position(s) 4
28. [order] from clue 10 stock:Tumbleweed: ruled out position(s) 3
29. [order] from clue 8 outcome:a clean ride: ruled out position(s) 4
30. [disjunction] from clue 13 event:tie-down roping: ruled out position(s) 2
31. [disjunction] from clue 12 stock:Little Sister: ruled out position(s) 1,2
32. [disjunction] from clue 6 outcome:a no-score: ruled out position(s) 3
33. [disjunction] from clue 6 outcome:a slap of the free hand: ruled out position(s) 2,4
34. [disjunction] from clue 12 stock:Little Sister: ruled out position(s) 3
35. [order] from clue 4 rider:Cody Vance: ruled out position(s) 3
36. [order] from clue 4 rider:Marla Hobbs: ruled out position(s) 3
37. [disjunction] from clue 13 event:tie-down roping: ruled out position(s) 3
38. [order] from clue 1 stock:Sunday Sermon: ruled out position(s) 2
39. [bijection] event:barrel racing: ruled out position(s) 4
40. [bijection] event:bull riding: ruled out position(s) 4
_... and 17 further steps._

---

<sub>seed `2026173084283` &middot; score 10.62 &middot; atoms 15 &middot; positives 1 &middot; solved by disjunction</sub>
