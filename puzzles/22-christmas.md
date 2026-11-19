# Christmas Morning on Lark Street

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `f3ab9d685a55`

## Introduction

A pile of wish lists, and one set of parents trying very hard to remember who asked for what.
Five kids are involved. Determine each kid's age, toy and snack.
- **Kid**: Frankie, Deshawn, Esperanza, Alton and Margo.
- **Age** (listed from younger to older): 8 years old, 9 years old, 10 years old, 11 years old and 12 years old.
- **Toy**: an electric keyboard, a pink skateboard, a robot dog, a bug-collecting kit and a karaoke machine.
- **Snack**: carrot sticks, oatmeal cookies, peanut butter crackers, sugar cookies and gingerbread.
Every kid has a different age, toy and snack, so within each category every item is used exactly once.

## Clues

1. Frankie leaves out peanut butter crackers.
2. The kid who leaves out carrot sticks and 9 years old are exactly one year apart in age order, in one direction or the other.
3. Esperanza and 10 years old are exactly one year apart in age order, in one direction or the other.
4. 10 years old is exactly one year younger than the kid who hopes for a karaoke machine, with no age in between.
5. Margo does not leave out sugar cookies. Margo and 12 years old are exactly one year apart in age order, in one direction or the other.
6. The kid who leaves out oatmeal cookies and 9 years old are exactly one year apart in age order, in one direction or the other.
7. Alton does not hope for a robot dog.
8. The kid who hopes for an electric keyboard is exactly one year younger than the kid who leaves out carrot sticks, with no age in between.
9. The kid who hopes for a pink skateboard is younger than Alton in age order.

## Solving chart

*Age vs Kid*

| | Frankie | Deshawn | Esperanza | Alton | Margo |
|---|---|---|---|---|---|
| **8 years old** | | | | | |
| **9 years old** | | | | | |
| **10 years old** | | | | | |
| **11 years old** | | | | | |
| **12 years old** | | | | | |

*Age vs Toy*

| | an electric keyboard | a pink skateboard | a robot dog | a bug-collecting kit | a karaoke machine |
|---|---|---|---|---|---|
| **8 years old** | | | | | |
| **9 years old** | | | | | |
| **10 years old** | | | | | |
| **11 years old** | | | | | |
| **12 years old** | | | | | |

*Age vs Snack*

| | carrot sticks | oatmeal cookies | peanut butter crackers | sugar cookies | gingerbread |
|---|---|---|---|---|---|
| **8 years old** | | | | | |
| **9 years old** | | | | | |
| **10 years old** | | | | | |
| **11 years old** | | | | | |
| **12 years old** | | | | | |

*Kid vs Toy*

| | an electric keyboard | a pink skateboard | a robot dog | a bug-collecting kit | a karaoke machine |
|---|---|---|---|---|---|
| **Frankie** | | | | | |
| **Deshawn** | | | | | |
| **Esperanza** | | | | | |
| **Alton** | | | | | |
| **Margo** | | | | | |

*Kid vs Snack*

| | carrot sticks | oatmeal cookies | peanut butter crackers | sugar cookies | gingerbread |
|---|---|---|---|---|---|
| **Frankie** | | | | | |
| **Deshawn** | | | | | |
| **Esperanza** | | | | | |
| **Alton** | | | | | |
| **Margo** | | | | | |

*Toy vs Snack*

| | carrot sticks | oatmeal cookies | peanut butter crackers | sugar cookies | gingerbread |
|---|---|---|---|---|---|
| **an electric keyboard** | | | | | |
| **a pink skateboard** | | | | | |
| **a robot dog** | | | | | |
| **a bug-collecting kit** | | | | | |
| **a karaoke machine** | | | | | |

## Solution

| Age | Kid | Toy | Snack |
|---|---|---|---|
| 8 years old | Deshawn | a pink skateboard | oatmeal cookies |
| 9 years old | Esperanza | an electric keyboard | sugar cookies |
| 10 years old | Alton | a bug-collecting kit | carrot sticks |
| 11 years old | Margo | a karaoke machine | gingerbread |
| 12 years old | Frankie | a robot dog | peanut butter crackers |

## How it falls out

1. [order] from clue 10 snack:oatmeal cookies: ruled out position(s) 2,4,5
2. [order] from clue 9 toy:a karaoke machine: ruled out position(s) 1,2,3,5
3. [order] from clue 8 toy:a pink skateboard: ruled out position(s) 5
4. [order] from clue 8 kid:Alton: ruled out position(s) 1
5. [order] from clue 7 kid:Esperanza: ruled out position(s) 1,3,5
6. [order] from clue 4 snack:carrot sticks: ruled out position(s) 2,4,5
7. [order] from clue 3 toy:an electric keyboard: ruled out position(s) 1,3,4,5
8. [order] from clue 3 snack:carrot sticks: ruled out position(s) 1
9. [order] from clue 1 kid:Margo: ruled out position(s) 1,2,3,5
10. [direct] from clue 6 snack:sugar cookies: ruled out position(s) 4
11. [bijection] kid:Frankie: ruled out position(s) 4
12. [bijection] kid:Deshawn: ruled out position(s) 4
13. [bijection] kid:Esperanza: ruled out position(s) 4
14. [bijection] kid:Alton: ruled out position(s) 4
15. [bijection] snack:oatmeal cookies: ruled out position(s) 3
16. [bijection] snack:peanut butter crackers: ruled out position(s) 3
17. [bijection] snack:sugar cookies: ruled out position(s) 3
18. [bijection] snack:gingerbread: ruled out position(s) 3
19. [bijection] toy:a pink skateboard: ruled out position(s) 2,4
20. [bijection] toy:a robot dog: ruled out position(s) 2,4
21. [bijection] toy:a bug-collecting kit: ruled out position(s) 2,4
22. [direct] from clue 2 kid:Frankie: ruled out position(s) 3
23. [direct] from clue 2 snack:peanut butter crackers: ruled out position(s) 4
24. [bijection] kid:Frankie: ruled out position(s) 2
25. [bijection] kid:Deshawn: ruled out position(s) 2
26. [bijection] kid:Alton: ruled out position(s) 2
27. [bijection] snack:peanut butter crackers: ruled out position(s) 1
28. [bijection] snack:sugar cookies: ruled out position(s) 1
29. [bijection] snack:gingerbread: ruled out position(s) 1
30. [bijection] snack:gingerbread: ruled out position(s) 2,5
31. [direct] from clue 2 kid:Frankie: ruled out position(s) 1
32. [direct] from clue 2 snack:peanut butter crackers: ruled out position(s) 2
33. [bijection] kid:Deshawn: ruled out position(s) 5
34. [bijection] kid:Alton: ruled out position(s) 5
35. [bijection] kid:Deshawn: ruled out position(s) 3
36. [bijection] snack:sugar cookies: ruled out position(s) 5
37. [order] from clue 8 toy:a pink skateboard: ruled out position(s) 3
38. [direct] from clue 5 toy:a robot dog: ruled out position(s) 3
39. [bijection] toy:a robot dog: ruled out position(s) 1
40. [bijection] toy:a bug-collecting kit: ruled out position(s) 1
_... and 1 further steps._

---

<sub>seed `2026172849657` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
