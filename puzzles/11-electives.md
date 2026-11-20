# Elective Sign-Up at Ridgeline High

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `12ace8926ec0`

## Introduction

A gym full of sign-up tables, a line out the door, and a counselor who gave up on alphabetical order an hour ago.
Five students are involved. Determine each student's birthday month and elective.
- **Student**: Darnell, Linnea, Omar, Mateo and Trey.
- **Birthday month** (listed from earlier to later): January, February, March, April and May.
- **Elective**: Spanish, digital art, robotics, wood shop and theater tech.
Every student has a different birthday month and elective, so within each category every item is used exactly once.

## Clues

1. The student who signs up for Spanish was not born in February. Trey is exactly one month earlier than February, with no birthday month in between.
2. Mateo is exactly one month earlier than April, with no birthday month in between. Omar was not born in April.
3. The student who signs up for Spanish and Mateo are exactly one month apart in birthday month order, in one direction or the other.
4. The student who signs up for robotics is earlier than Omar in birthday month order. Omar is earlier than the student who signs up for wood shop in birthday month order.
5. The student who signs up for digital art is exactly one month earlier than Linnea, with no birthday month in between.

## Solving chart

*Birthday month vs Student*

| | Darnell | Linnea | Omar | Mateo | Trey |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Birthday month vs Elective*

| | Spanish | digital art | robotics | wood shop | theater tech |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Student vs Elective*

| | Spanish | digital art | robotics | wood shop | theater tech |
|---|---|---|---|---|---|
| **Darnell** | | | | | |
| **Linnea** | | | | | |
| **Omar** | | | | | |
| **Mateo** | | | | | |
| **Trey** | | | | | |

## Solution

| Birthday month | Student | Elective |
|---|---|---|
| January | Trey | robotics |
| February | Omar | theater tech |
| March | Mateo | digital art |
| April | Linnea | Spanish |
| May | Darnell | wood shop |

## How it falls out

1. [direct] from clue 6 elective:Spanish: ruled out position(s) 2
2. [direct] from clue 5 student:Omar: ruled out position(s) 4
3. [order] from clue 8 student:Mateo: ruled out position(s) 1,2,4,5
4. [order] from clue 7 student:Omar: ruled out position(s) 5
5. [order] from clue 7 elective:wood shop: ruled out position(s) 1
6. [order] from clue 4 elective:Spanish: ruled out position(s) 1,3,5
7. [order] from clue 3 elective:digital art: ruled out position(s) 5
8. [order] from clue 3 student:Linnea: ruled out position(s) 1
9. [order] from clue 2 elective:robotics: ruled out position(s) 3,4,5
10. [order] from clue 2 student:Omar: ruled out position(s) 1
11. [order] from clue 7 elective:wood shop: ruled out position(s) 2
12. [order] from clue 1 student:Trey: ruled out position(s) 2,3,4,5
13. [bijection] elective:digital art: ruled out position(s) 4
14. [bijection] elective:wood shop: ruled out position(s) 4
15. [bijection] elective:theater tech: ruled out position(s) 4
16. [bijection] student:Darnell: ruled out position(s) 1,3
17. [bijection] student:Linnea: ruled out position(s) 3
18. [bijection] student:Omar: ruled out position(s) 3
19. [order] from clue 2 elective:robotics: ruled out position(s) 2
20. [order] from clue 3 elective:digital art: ruled out position(s) 2
21. [order] from clue 3 student:Linnea: ruled out position(s) 5
22. [bijection] elective:digital art: ruled out position(s) 1
23. [bijection] elective:theater tech: ruled out position(s) 1
24. [bijection] elective:theater tech: ruled out position(s) 3,5
25. [bijection] student:Darnell: ruled out position(s) 2
26. [bijection] student:Linnea: ruled out position(s) 2
27. [bijection] student:Darnell: ruled out position(s) 4
28. [bijection] elective:wood shop: ruled out position(s) 3

---

<sub>seed `2026172962554` &middot; score 5.1 &middot; atoms 8 &middot; positives 0 &middot; solved by order</sub>
