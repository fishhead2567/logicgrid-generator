# Elective Sign-Up at Ridgeline High

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `4055e06411f5`

## Introduction

A gym full of sign-up tables, a line out the door, and a counselor who gave up on alphabetical order an hour ago.
Four students are involved. Determine each student's birthday month, elective and middle school.
- **Student**: Trey, Shoshana, Mateo and Linnea.
- **Birthday month** (listed from earlier to later): January, February, March and April.
- **Elective**: yearbook, Spanish, robotics and digital art.
- **Middle school**: Eastbrook Middle, Watermill Middle, Las Palmas Middle and Pinecrest Middle.
Every student has a different birthday month, elective and middle school, so within each category every item is used exactly once.

## Clues

1. The student who comes from Eastbrook Middle was born in March. Shoshana does not come from Eastbrook Middle.
2. Mateo is earlier than the student who signs up for digital art in birthday month order. Mateo falls somewhere between April and January in birthday month order.
3. February falls somewhere between the student who comes from Las Palmas Middle and Trey in birthday month order.
4. March is exactly one month earlier than the student who signs up for Spanish, with no birthday month in between.
5. The student who signs up for yearbook was not born in January.
6. The student who signs up for digital art and Linnea are exactly one month apart in birthday month order, in one direction or the other.
7. The student who comes from Pinecrest Middle is earlier than the student who signs up for Spanish in birthday month order.

## Solving chart

*Birthday month vs Student*

| | Trey | Shoshana | Mateo | Linnea |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Birthday month vs Elective*

| | yearbook | Spanish | robotics | digital art |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Birthday month vs Middle school*

| | Eastbrook Middle | Watermill Middle | Las Palmas Middle | Pinecrest Middle |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Student vs Elective*

| | yearbook | Spanish | robotics | digital art |
|---|---|---|---|---|
| **Trey** | | | | |
| **Shoshana** | | | | |
| **Mateo** | | | | |
| **Linnea** | | | | |

*Student vs Middle school*

| | Eastbrook Middle | Watermill Middle | Las Palmas Middle | Pinecrest Middle |
|---|---|---|---|---|
| **Trey** | | | | |
| **Shoshana** | | | | |
| **Mateo** | | | | |
| **Linnea** | | | | |

*Elective vs Middle school*

| | Eastbrook Middle | Watermill Middle | Las Palmas Middle | Pinecrest Middle |
|---|---|---|---|---|
| **yearbook** | | | | |
| **Spanish** | | | | |
| **robotics** | | | | |
| **digital art** | | | | |

## Solution

| Birthday month | Student | Elective | Middle school |
|---|---|---|---|
| January | Shoshana | robotics | Las Palmas Middle |
| February | Mateo | yearbook | Pinecrest Middle |
| March | Trey | digital art | Eastbrook Middle |
| April | Linnea | Spanish | Watermill Middle |

## How it falls out

1. [direct] from clue 9 elective:yearbook: ruled out position(s) 1
2. [direct] from clue 5 school:Eastbrook Middle: ruled out position(s) 1,2,4
3. [direct] from clue 3 student:Shoshana: ruled out position(s) 3
4. [bijection] school:Watermill Middle: ruled out position(s) 3
5. [bijection] school:Las Palmas Middle: ruled out position(s) 3
6. [bijection] school:Pinecrest Middle: ruled out position(s) 3
7. [order] from clue 8 school:Pinecrest Middle: ruled out position(s) 4
8. [order] from clue 8 elective:Spanish: ruled out position(s) 1
9. [order] from clue 7 student:Mateo: ruled out position(s) 4
10. [order] from clue 7 elective:digital art: ruled out position(s) 1
11. [order] from clue 6 student:Mateo: ruled out position(s) 1
12. [order] from clue 7 elective:digital art: ruled out position(s) 2
13. [order] from clue 4 elective:Spanish: ruled out position(s) 2,3
14. [order] from clue 2 school:Las Palmas Middle: ruled out position(s) 2
15. [order] from clue 2 student:Trey: ruled out position(s) 2
16. [order] from clue 1 student:Linnea: ruled out position(s) 1
17. [bijection] elective:yearbook: ruled out position(s) 4
18. [bijection] elective:robotics: ruled out position(s) 4
19. [bijection] elective:digital art: ruled out position(s) 4
20. [bijection] elective:robotics: ruled out position(s) 2,3
21. [order] from clue 7 student:Mateo: ruled out position(s) 3
22. [order] from clue 1 student:Linnea: ruled out position(s) 3
23. [bijection] elective:yearbook: ruled out position(s) 3
24. [bijection] student:Shoshana: ruled out position(s) 2
25. [bijection] student:Linnea: ruled out position(s) 2
26. [bijection] student:Trey: ruled out position(s) 1,4
27. [order] from clue 2 school:Las Palmas Middle: ruled out position(s) 4
28. [bijection] school:Watermill Middle: ruled out position(s) 1
29. [bijection] school:Pinecrest Middle: ruled out position(s) 1
30. [bijection] school:Watermill Middle: ruled out position(s) 2
31. [bijection] student:Shoshana: ruled out position(s) 4

---

<sub>seed `2026172902146` &middot; score 5.13 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
