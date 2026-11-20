# The Walling Match at Gunnerside

**Difficulty** 2/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `dab3fe3a0ef4`

## Introduction

A measured length of fallen wall each, and a whole morning in which to rebuild it to the satisfaction of a judge who will push on every cope.
Five wallers are involved. Determine each waller's finishing time and feature.
- **Waller**: Tam Ridley, Jenny Fawcett, Ossian Baird, Ewart Beck and Mab Teasdale.
- **Finishing time** (listed from earlier to later): 8am, 9am, 10am, 11am and noon.
- **Feature built**: a stile, a cripple hole, a wall head, a water smoot and a plain run of copes.
Every waller has a different finishing time and feature, so within each category every item is used exactly once.

## Clues

1. The waller who builds in a water smoot finishes at 8am.
2. Ewart Beck finishes at 9am.
3. Ossian Baird builds in a stile.
4. The waller who builds in a plain run of copes and 9am are exactly one hour apart in finishing time order, in one direction or the other.
5. 10am falls somewhere between the waller who builds in a wall head and the waller who builds in a water smoot in finishing time order.
6. Jenny Fawcett is earlier than 10am in finishing time order.
7. The waller who builds in a stile is earlier than Mab Teasdale in finishing time order.

## Solving chart

*Finishing time vs Waller*

| | Tam Ridley | Jenny Fawcett | Ossian Baird | Ewart Beck | Mab Teasdale |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Finishing time vs Feature built*

| | a stile | a cripple hole | a wall head | a water smoot | a plain run of copes |
|---|---|---|---|---|---|
| **8am** | | | | | |
| **9am** | | | | | |
| **10am** | | | | | |
| **11am** | | | | | |
| **noon** | | | | | |

*Waller vs Feature built*

| | a stile | a cripple hole | a wall head | a water smoot | a plain run of copes |
|---|---|---|---|---|---|
| **Tam Ridley** | | | | | |
| **Jenny Fawcett** | | | | | |
| **Ossian Baird** | | | | | |
| **Ewart Beck** | | | | | |
| **Mab Teasdale** | | | | | |

## Solution

| Finishing time | Waller | Feature built |
|---|---|---|
| 8am | Jenny Fawcett | a water smoot |
| 9am | Ewart Beck | a cripple hole |
| 10am | Tam Ridley | a plain run of copes |
| 11am | Ossian Baird | a stile |
| noon | Mab Teasdale | a wall head |

## How it falls out

1. [direct] from clue 4 waller:Ewart Beck: ruled out position(s) 1,3,4,5
2. [direct] from clue 1 feature:a water smoot: ruled out position(s) 2,3,4,5
3. [bijection] feature:a stile: ruled out position(s) 1
4. [bijection] feature:a cripple hole: ruled out position(s) 1
5. [bijection] feature:a wall head: ruled out position(s) 1
6. [bijection] feature:a plain run of copes: ruled out position(s) 1
7. [bijection] waller:Tam Ridley: ruled out position(s) 2
8. [bijection] waller:Jenny Fawcett: ruled out position(s) 2
9. [bijection] waller:Ossian Baird: ruled out position(s) 2
10. [bijection] waller:Mab Teasdale: ruled out position(s) 2
11. [direct] from clue 3 feature:a stile: ruled out position(s) 2
12. [direct] from clue 3 waller:Ossian Baird: ruled out position(s) 1
13. [order] from clue 7 feature:a plain run of copes: ruled out position(s) 2,4,5
14. [order] from clue 6 waller:Jenny Fawcett: ruled out position(s) 3,4,5
15. [order] from clue 5 feature:a stile: ruled out position(s) 5
16. [order] from clue 5 waller:Mab Teasdale: ruled out position(s) 1,3
17. [order] from clue 2 feature:a wall head: ruled out position(s) 2,3
18. [direct] from clue 3 waller:Ossian Baird: ruled out position(s) 5
19. [bijection] feature:a stile: ruled out position(s) 3
20. [bijection] feature:a cripple hole: ruled out position(s) 3
21. [bijection] feature:a cripple hole: ruled out position(s) 4,5
22. [bijection] waller:Tam Ridley: ruled out position(s) 1
23. [order] from clue 5 waller:Mab Teasdale: ruled out position(s) 4
24. [direct] from clue 3 waller:Ossian Baird: ruled out position(s) 3
25. [bijection] feature:a wall head: ruled out position(s) 4
26. [bijection] waller:Tam Ridley: ruled out position(s) 4,5

---

<sub>seed `2026172894227` &middot; score 4.38 &middot; atoms 7 &middot; positives 3 &middot; solved by order</sub>
