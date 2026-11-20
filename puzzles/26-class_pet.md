# The Room 12 Class Pet Vote

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 12 &nbsp;&nbsp; **id** `429532d01139`

## Introduction

Mr. Ocampo said the class could pick one pet. Nobody warned him that would mean campaign posters.
Five kids are involved. Determine each kid's vote count, pet and habitat.
- **Kid**: Dashiell, Kwame, Sanjay, Tilly and Josefina.
- **Vote count** (listed from lower to higher): 4 votes, 6 votes, 8 votes, 10 votes and 12 votes.
- **Pet**: a dwarf hamster, a pair of fancy rats, a box turtle, a leopard gecko and a bearded dragon.
- **Habitat**: a glass terrarium, a wire cage, a tall aviary, a wooden hutch and a felt-lined shoebox.
Every kid has a different vote count, pet and habitat, so within each category every item is used exactly once.

## Clues

1. The kid who keeps it in a tall aviary wins 8 votes.
2. Tilly wins 4 votes.
3. Josefina does not win 10 votes. The kid who nominates a dwarf hamster and 10 votes are exactly one vote step apart in vote count order, in one direction or the other.
4. The kid who keeps it in a glass terrarium is exactly one vote step lower than 12 votes, with no vote count in between.
5. The kid who nominates a leopard gecko is higher than 6 votes in vote count order.
6. The kid who keeps it in a wire cage does not win 4 votes.
7. Sanjay and 10 votes are exactly one vote step apart in vote count order, in one direction or the other.
8. The kid who nominates a bearded dragon falls somewhere between Josefina and Tilly in vote count order.
9. The kid who keeps it in a wooden hutch and Dashiell are exactly one vote step apart in vote count order, in one direction or the other.
10. The kid who nominates a pair of fancy rats falls somewhere between the kid who keeps it in a wire cage and the kid who keeps it in a wooden hutch in vote count order.
11. The kid who nominates a leopard gecko falls somewhere between the kid who keeps it in a felt-lined shoebox and Sanjay in vote count order.
12. The kid who keeps it in a felt-lined shoebox and the kid who nominates a leopard gecko are exactly one vote step apart in vote count order, in one direction or the other.

## Solving chart

*Vote count vs Kid*

| | Dashiell | Kwame | Sanjay | Tilly | Josefina |
|---|---|---|---|---|---|
| **4 votes** | | | | | |
| **6 votes** | | | | | |
| **8 votes** | | | | | |
| **10 votes** | | | | | |
| **12 votes** | | | | | |

*Vote count vs Pet*

| | a dwarf hamster | a pair of fancy rats | a box turtle | a leopard gecko | a bearded dragon |
|---|---|---|---|---|---|
| **4 votes** | | | | | |
| **6 votes** | | | | | |
| **8 votes** | | | | | |
| **10 votes** | | | | | |
| **12 votes** | | | | | |

*Vote count vs Habitat*

| | a glass terrarium | a wire cage | a tall aviary | a wooden hutch | a felt-lined shoebox |
|---|---|---|---|---|---|
| **4 votes** | | | | | |
| **6 votes** | | | | | |
| **8 votes** | | | | | |
| **10 votes** | | | | | |
| **12 votes** | | | | | |

*Kid vs Pet*

| | a dwarf hamster | a pair of fancy rats | a box turtle | a leopard gecko | a bearded dragon |
|---|---|---|---|---|---|
| **Dashiell** | | | | | |
| **Kwame** | | | | | |
| **Sanjay** | | | | | |
| **Tilly** | | | | | |
| **Josefina** | | | | | |

*Kid vs Habitat*

| | a glass terrarium | a wire cage | a tall aviary | a wooden hutch | a felt-lined shoebox |
|---|---|---|---|---|---|
| **Dashiell** | | | | | |
| **Kwame** | | | | | |
| **Sanjay** | | | | | |
| **Tilly** | | | | | |
| **Josefina** | | | | | |

*Pet vs Habitat*

| | a glass terrarium | a wire cage | a tall aviary | a wooden hutch | a felt-lined shoebox |
|---|---|---|---|---|---|
| **a dwarf hamster** | | | | | |
| **a pair of fancy rats** | | | | | |
| **a box turtle** | | | | | |
| **a leopard gecko** | | | | | |
| **a bearded dragon** | | | | | |

## Solution

| Vote count | Kid | Pet | Habitat |
|---|---|---|---|
| 4 votes | Tilly | a box turtle | a wooden hutch |
| 6 votes | Dashiell | a bearded dragon | a felt-lined shoebox |
| 8 votes | Josefina | a leopard gecko | a tall aviary |
| 10 votes | Kwame | a pair of fancy rats | a glass terrarium |
| 12 votes | Sanjay | a dwarf hamster | a wire cage |

## How it falls out

1. [direct] from clue 13 habitat:a wire cage: ruled out position(s) 1
2. [direct] from clue 10 kid:Josefina: ruled out position(s) 4
3. [direct] from clue 6 habitat:a tall aviary: ruled out position(s) 1,2,4,5
4. [direct] from clue 4 kid:Tilly: ruled out position(s) 2,3,4,5
5. [bijection] habitat:a glass terrarium: ruled out position(s) 3
6. [bijection] habitat:a wire cage: ruled out position(s) 3
7. [bijection] habitat:a wooden hutch: ruled out position(s) 3
8. [bijection] habitat:a felt-lined shoebox: ruled out position(s) 3
9. [bijection] kid:Dashiell: ruled out position(s) 1
10. [bijection] kid:Kwame: ruled out position(s) 1
11. [bijection] kid:Sanjay: ruled out position(s) 1
12. [bijection] kid:Josefina: ruled out position(s) 1
13. [order] from clue 11 habitat:a glass terrarium: ruled out position(s) 1,2,5
14. [order] from clue 9 pet:a dwarf hamster: ruled out position(s) 1,2,4
15. [order] from clue 7 pet:a bearded dragon: ruled out position(s) 1,5
16. [order] from clue 7 kid:Josefina: ruled out position(s) 2
17. [order] from clue 5 kid:Sanjay: ruled out position(s) 2,4
18. [order] from clue 3 pet:a pair of fancy rats: ruled out position(s) 1,5
19. [order] from clue 2 pet:a leopard gecko: ruled out position(s) 1,2
20. [order] from clue 8 habitat:a felt-lined shoebox: ruled out position(s) 1
21. [order] from clue 1 pet:a leopard gecko: ruled out position(s) 5
22. [order] from clue 1 habitat:a felt-lined shoebox: ruled out position(s) 4
23. [bijection] habitat:a wire cage: ruled out position(s) 4
24. [bijection] habitat:a wooden hutch: ruled out position(s) 4
25. [bijection] habitat:a wooden hutch: ruled out position(s) 2,5
26. [bijection] pet:a box turtle: ruled out position(s) 2,3,4,5
27. [order] from clue 12 kid:Dashiell: ruled out position(s) 3,4,5
28. [order] from clue 3 habitat:a wire cage: ruled out position(s) 2
29. [bijection] habitat:a felt-lined shoebox: ruled out position(s) 5
30. [bijection] kid:Kwame: ruled out position(s) 2
31. [bijection] kid:Kwame: ruled out position(s) 3,5
32. [bijection] pet:a dwarf hamster: ruled out position(s) 3
33. [order] from clue 8 pet:a leopard gecko: ruled out position(s) 4
34. [order] from clue 1 kid:Sanjay: ruled out position(s) 3
35. [bijection] kid:Josefina: ruled out position(s) 5
36. [bijection] pet:a pair of fancy rats: ruled out position(s) 3
37. [bijection] pet:a bearded dragon: ruled out position(s) 3
38. [order] from clue 7 pet:a bearded dragon: ruled out position(s) 4
39. [bijection] pet:a pair of fancy rats: ruled out position(s) 2

---

<sub>seed `2026172981336` &middot; score 5.355 &middot; atoms 13 &middot; positives 2 &middot; solved by order</sub>
