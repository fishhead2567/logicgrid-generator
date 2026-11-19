# The Room 12 Class Pet Vote

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `975ae76073d7`

## Introduction

Mr. Ocampo said the class could pick one pet. Nobody warned him that would mean campaign posters.
Five kids are involved. Determine each kid's vote count, pet and name.
- **Kid**: Marisol, Ezra, Josefina, Kwame and Dashiell.
- **Vote count** (listed from lower to higher): 4 votes, 6 votes, 8 votes, 10 votes and 12 votes.
- **Pet**: a leopard gecko, a hermit crab, a box turtle, a pair of fancy rats and a bearded dragon.
- **Name**: Biscuit, Rocket, Taco, Zuzu and Sir Pickles.
Every kid has a different vote count, pet and name, so within each category every item is used exactly once.

## Clues

1. The kid who nominates a hermit crab calls it Biscuit.
2. The kid who nominates a leopard gecko falls somewhere between 12 votes and 8 votes in vote count order.
3. The kid who nominates a pair of fancy rats falls somewhere between the kid who calls it Rocket and 12 votes in vote count order.
4. Dashiell is exactly one vote step lower than 10 votes, with no vote count in between.
5. The kid who calls it Sir Pickles falls somewhere between Marisol and 10 votes in vote count order.
6. Kwame falls somewhere between the kid who calls it Rocket and the kid who calls it Sir Pickles in vote count order.
7. Ezra and the kid who calls it Sir Pickles are exactly one vote step apart in vote count order, in one direction or the other.
8. The kid who calls it Taco falls somewhere between Dashiell and the kid who nominates a bearded dragon in vote count order.
9. The kid who nominates a pair of fancy rats falls somewhere between Kwame and the kid who calls it Biscuit in vote count order.

## Solving chart

*Vote count vs Kid*

| | Marisol | Ezra | Josefina | Kwame | Dashiell |
|---|---|---|---|---|---|
| **4 votes** | | | | | |
| **6 votes** | | | | | |
| **8 votes** | | | | | |
| **10 votes** | | | | | |
| **12 votes** | | | | | |

*Vote count vs Pet*

| | a leopard gecko | a hermit crab | a box turtle | a pair of fancy rats | a bearded dragon |
|---|---|---|---|---|---|
| **4 votes** | | | | | |
| **6 votes** | | | | | |
| **8 votes** | | | | | |
| **10 votes** | | | | | |
| **12 votes** | | | | | |

*Vote count vs Name*

| | Biscuit | Rocket | Taco | Zuzu | Sir Pickles |
|---|---|---|---|---|---|
| **4 votes** | | | | | |
| **6 votes** | | | | | |
| **8 votes** | | | | | |
| **10 votes** | | | | | |
| **12 votes** | | | | | |

*Kid vs Pet*

| | a leopard gecko | a hermit crab | a box turtle | a pair of fancy rats | a bearded dragon |
|---|---|---|---|---|---|
| **Marisol** | | | | | |
| **Ezra** | | | | | |
| **Josefina** | | | | | |
| **Kwame** | | | | | |
| **Dashiell** | | | | | |

*Kid vs Name*

| | Biscuit | Rocket | Taco | Zuzu | Sir Pickles |
|---|---|---|---|---|---|
| **Marisol** | | | | | |
| **Ezra** | | | | | |
| **Josefina** | | | | | |
| **Kwame** | | | | | |
| **Dashiell** | | | | | |

*Pet vs Name*

| | Biscuit | Rocket | Taco | Zuzu | Sir Pickles |
|---|---|---|---|---|---|
| **a leopard gecko** | | | | | |
| **a hermit crab** | | | | | |
| **a box turtle** | | | | | |
| **a pair of fancy rats** | | | | | |
| **a bearded dragon** | | | | | |

## Solution

| Vote count | Kid | Pet | Name |
|---|---|---|---|
| 4 votes | Marisol | a bearded dragon | Rocket |
| 6 votes | Kwame | a box turtle | Taco |
| 8 votes | Dashiell | a pair of fancy rats | Sir Pickles |
| 10 votes | Ezra | a leopard gecko | Zuzu |
| 12 votes | Josefina | a hermit crab | Biscuit |

## How it falls out

1. [order] from clue 9 petname:Taco: ruled out position(s) 1,5
2. [order] from clue 8 petname:Sir Pickles: ruled out position(s) 1,4,5
3. [order] from clue 8 kid:Marisol: ruled out position(s) 3,4,5
4. [order] from clue 7 pet:a pair of fancy rats: ruled out position(s) 1,5
5. [order] from clue 7 petname:Rocket: ruled out position(s) 4,5
6. [order] from clue 6 kid:Kwame: ruled out position(s) 1,3,4,5
7. [order] from clue 6 petname:Rocket: ruled out position(s) 2,3
8. [order] from clue 6 petname:Sir Pickles: ruled out position(s) 2
9. [order] from clue 5 pet:a pair of fancy rats: ruled out position(s) 2
10. [order] from clue 5 petname:Biscuit: ruled out position(s) 1,2,3
11. [order] from clue 4 kid:Dashiell: ruled out position(s) 1,2,4,5
12. [order] from clue 9 petname:Taco: ruled out position(s) 3
13. [order] from clue 9 pet:a bearded dragon: ruled out position(s) 2,3,4
14. [order] from clue 3 pet:a leopard gecko: ruled out position(s) 1,2,3,5
15. [order] from clue 2 kid:Ezra: ruled out position(s) 1,3,5
16. [direct] from clue 1 pet:a hermit crab: ruled out position(s) 1,2,3
17. [bijection] kid:Marisol: ruled out position(s) 2
18. [bijection] kid:Ezra: ruled out position(s) 2
19. [bijection] kid:Josefina: ruled out position(s) 2,3
20. [bijection] kid:Josefina: ruled out position(s) 1,4
21. [bijection] pet:a hermit crab: ruled out position(s) 4
22. [bijection] pet:a box turtle: ruled out position(s) 4
23. [bijection] pet:a pair of fancy rats: ruled out position(s) 4
24. [bijection] pet:a box turtle: ruled out position(s) 1,3,5
25. [bijection] petname:Zuzu: ruled out position(s) 1,3
26. [direct] from clue 1 petname:Biscuit: ruled out position(s) 4
27. [bijection] pet:a bearded dragon: ruled out position(s) 5
28. [bijection] petname:Zuzu: ruled out position(s) 5
29. [order] from clue 9 petname:Taco: ruled out position(s) 4
30. [bijection] petname:Zuzu: ruled out position(s) 2

---

<sub>seed `2026172841738` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
