# Christmas Morning on Lark Street

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `0b9bf4b7efb5`

## Introduction

A pile of wish lists, and one set of parents trying very hard to remember who asked for what.
Five kids are involved. Determine each kid's age, pajamas and snack.
- **Kid**: Margo, Deshawn, Frankie, Rosalind and Yuki.
- **Age** (listed from younger to older): 8 years old, 9 years old, 10 years old, 11 years old and 12 years old.
- **Pajamas**: purple fleece pajamas, blue star pajamas, reindeer pajamas, snowflake pajamas and red flannel pajamas.
- **Snack**: a slice of fruitcake, peanut butter crackers, carrot sticks, oatmeal cookies and gingerbread.
Every kid has a different age, pajamas and snack, so within each category every item is used exactly once.

## Clues

1. The kid who wears snowflake pajamas is younger than 9 years old in age order. The kid who leaves out gingerbread is 9 years old.
2. The kid who wears red flannel pajamas falls somewhere between 12 years old and 9 years old in age order.
3. 10 years old falls somewhere between Margo and Yuki in age order. The kid who leaves out a slice of fruitcake is younger than Margo in age order. Yuki does not wear red flannel pajamas.
4. 9 years old falls somewhere between Frankie and the kid who wears purple fleece pajamas in age order.
5. The kid who wears blue star pajamas and the kid who leaves out gingerbread are exactly one year apart in age order, in one direction or the other.
6. The kid who leaves out peanut butter crackers falls somewhere between Frankie and Yuki in age order.
7. Deshawn falls somewhere between the kid who leaves out gingerbread and the kid who leaves out oatmeal cookies in age order.
8. The kid who wears blue star pajamas and the kid who leaves out oatmeal cookies are exactly one year apart in age order, in one direction or the other.

## Solving chart

*Age vs Kid*

| | Margo | Deshawn | Frankie | Rosalind | Yuki |
|---|---|---|---|---|---|
| **8 years old** | | | | | |
| **9 years old** | | | | | |
| **10 years old** | | | | | |
| **11 years old** | | | | | |
| **12 years old** | | | | | |

*Age vs Pajamas*

| | purple fleece pajamas | blue star pajamas | reindeer pajamas | snowflake pajamas | red flannel pajamas |
|---|---|---|---|---|---|
| **8 years old** | | | | | |
| **9 years old** | | | | | |
| **10 years old** | | | | | |
| **11 years old** | | | | | |
| **12 years old** | | | | | |

*Age vs Snack*

| | a slice of fruitcake | peanut butter crackers | carrot sticks | oatmeal cookies | gingerbread |
|---|---|---|---|---|---|
| **8 years old** | | | | | |
| **9 years old** | | | | | |
| **10 years old** | | | | | |
| **11 years old** | | | | | |
| **12 years old** | | | | | |

*Kid vs Pajamas*

| | purple fleece pajamas | blue star pajamas | reindeer pajamas | snowflake pajamas | red flannel pajamas |
|---|---|---|---|---|---|
| **Margo** | | | | | |
| **Deshawn** | | | | | |
| **Frankie** | | | | | |
| **Rosalind** | | | | | |
| **Yuki** | | | | | |

*Kid vs Snack*

| | a slice of fruitcake | peanut butter crackers | carrot sticks | oatmeal cookies | gingerbread |
|---|---|---|---|---|---|
| **Margo** | | | | | |
| **Deshawn** | | | | | |
| **Frankie** | | | | | |
| **Rosalind** | | | | | |
| **Yuki** | | | | | |

*Pajamas vs Snack*

| | a slice of fruitcake | peanut butter crackers | carrot sticks | oatmeal cookies | gingerbread |
|---|---|---|---|---|---|
| **purple fleece pajamas** | | | | | |
| **blue star pajamas** | | | | | |
| **reindeer pajamas** | | | | | |
| **snowflake pajamas** | | | | | |
| **red flannel pajamas** | | | | | |

## Solution

| Age | Kid | Pajamas | Snack |
|---|---|---|---|
| 8 years old | Frankie | snowflake pajamas | a slice of fruitcake |
| 9 years old | Margo | reindeer pajamas | gingerbread |
| 10 years old | Deshawn | blue star pajamas | peanut butter crackers |
| 11 years old | Rosalind | red flannel pajamas | oatmeal cookies |
| 12 years old | Yuki | purple fleece pajamas | carrot sticks |

## How it falls out

1. [direct] from clue 4 snack:gingerbread: ruled out position(s) 1,3,4,5
2. [bijection] snack:a slice of fruitcake: ruled out position(s) 2
3. [bijection] snack:peanut butter crackers: ruled out position(s) 2
4. [bijection] snack:carrot sticks: ruled out position(s) 2
5. [bijection] snack:oatmeal cookies: ruled out position(s) 2
6. [order] from clue 11 snack:peanut butter crackers: ruled out position(s) 1,5
7. [order] from clue 10 pajamas:blue star pajamas: ruled out position(s) 1
8. [order] from clue 9 pajamas:snowflake pajamas: ruled out position(s) 2,3,4,5
9. [order] from clue 8 kid:Margo: ruled out position(s) 3
10. [order] from clue 8 kid:Yuki: ruled out position(s) 3
11. [order] from clue 7 snack:a slice of fruitcake: ruled out position(s) 5
12. [order] from clue 7 kid:Margo: ruled out position(s) 1
13. [order] from clue 5 pajamas:red flannel pajamas: ruled out position(s) 1,2,5
14. [order] from clue 3 kid:Deshawn: ruled out position(s) 1,2,5
15. [order] from clue 3 snack:oatmeal cookies: ruled out position(s) 1,3
16. [order] from clue 10 pajamas:blue star pajamas: ruled out position(s) 2
17. [order] from clue 2 pajamas:blue star pajamas: ruled out position(s) 4,5
18. [order] from clue 10 snack:oatmeal cookies: ruled out position(s) 5
19. [order] from clue 3 kid:Deshawn: ruled out position(s) 4
20. [order] from clue 1 kid:Frankie: ruled out position(s) 2
21. [order] from clue 1 pajamas:purple fleece pajamas: ruled out position(s) 2
22. [bijection] kid:Frankie: ruled out position(s) 3
23. [bijection] kid:Rosalind: ruled out position(s) 3
24. [bijection] pajamas:purple fleece pajamas: ruled out position(s) 1,3
25. [bijection] pajamas:reindeer pajamas: ruled out position(s) 1,3
26. [bijection] pajamas:red flannel pajamas: ruled out position(s) 3
27. [bijection] pajamas:reindeer pajamas: ruled out position(s) 4,5
28. [bijection] snack:a slice of fruitcake: ruled out position(s) 4
29. [bijection] snack:peanut butter crackers: ruled out position(s) 4
30. [bijection] snack:carrot sticks: ruled out position(s) 4
31. [bijection] snack:carrot sticks: ruled out position(s) 1,3
32. [direct] from clue 6 kid:Yuki: ruled out position(s) 4
33. [order] from clue 1 kid:Frankie: ruled out position(s) 4,5
34. [order] from clue 11 kid:Yuki: ruled out position(s) 1,2
35. [order] from clue 8 kid:Margo: ruled out position(s) 4,5
36. [order] from clue 7 snack:a slice of fruitcake: ruled out position(s) 3
37. [bijection] kid:Rosalind: ruled out position(s) 1,2,5
38. [bijection] pajamas:purple fleece pajamas: ruled out position(s) 4

---

<sub>seed `2026173041744` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
