# Elective Sign-Up at Ridgeline High

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 4 x 4 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `93058c19cdc8`

## Introduction

A gym full of sign-up tables, a line out the door, and a counselor who gave up on alphabetical order an hour ago.
Four students are involved. Determine each student's birthday month, middle school and ambition.
- **Student**: Mateo, Darnell, Trey and Linnea.
- **Birthday month** (listed from earlier to later): January, February, March and April.
- **Middle school**: Eastbrook Middle, Watermill Middle, North Terrace Middle and Dutch Hollow Middle.
- **Ambition**: a storm chaser, an architect, a game designer and a pastry chef.
Every student has a different birthday month, middle school and ambition, so within each category every item is used exactly once.

## Clues

1. The student who comes from Dutch Hollow Middle was born in March.
2. Mateo was born in April.
3. The student who wants to be a pastry chef was not born in January.
4. The student who comes from Eastbrook Middle and January are exactly one month apart in birthday month order, in one direction or the other.
5. The student who wants to be a storm chaser is exactly one month earlier than the student who comes from Dutch Hollow Middle, with no birthday month in between.
6. Trey falls somewhere between the student who wants to be a pastry chef and the student who wants to be an architect in birthday month order.
7. The student who comes from Watermill Middle and Darnell are exactly one month apart in birthday month order, in one direction or the other.
8. The student who wants to be a game designer is earlier than the student who comes from Watermill Middle in birthday month order.

## Solving chart

*Birthday month vs Student*

| | Mateo | Darnell | Trey | Linnea |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Birthday month vs Middle school*

| | Eastbrook Middle | Watermill Middle | North Terrace Middle | Dutch Hollow Middle |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Birthday month vs Ambition*

| | a storm chaser | an architect | a game designer | a pastry chef |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Student vs Middle school*

| | Eastbrook Middle | Watermill Middle | North Terrace Middle | Dutch Hollow Middle |
|---|---|---|---|---|
| **Mateo** | | | | |
| **Darnell** | | | | |
| **Trey** | | | | |
| **Linnea** | | | | |

*Student vs Ambition*

| | a storm chaser | an architect | a game designer | a pastry chef |
|---|---|---|---|---|
| **Mateo** | | | | |
| **Darnell** | | | | |
| **Trey** | | | | |
| **Linnea** | | | | |

*Middle school vs Ambition*

| | a storm chaser | an architect | a game designer | a pastry chef |
|---|---|---|---|---|
| **Eastbrook Middle** | | | | |
| **Watermill Middle** | | | | |
| **North Terrace Middle** | | | | |
| **Dutch Hollow Middle** | | | | |

## Solution

| Birthday month | Student | Middle school | Ambition |
|---|---|---|---|
| January | Linnea | North Terrace Middle | an architect |
| February | Trey | Eastbrook Middle | a storm chaser |
| March | Darnell | Dutch Hollow Middle | a game designer |
| April | Mateo | Watermill Middle | a pastry chef |

## How it falls out

1. [direct] from clue 8 student:Mateo: ruled out position(s) 1,2,3
2. [direct] from clue 5 ambition:a pastry chef: ruled out position(s) 1
3. [direct] from clue 2 school:Dutch Hollow Middle: ruled out position(s) 1,2,4
4. [bijection] school:Eastbrook Middle: ruled out position(s) 3
5. [bijection] school:Watermill Middle: ruled out position(s) 3
6. [bijection] school:North Terrace Middle: ruled out position(s) 3
7. [bijection] student:Darnell: ruled out position(s) 4
8. [bijection] student:Trey: ruled out position(s) 4
9. [bijection] student:Linnea: ruled out position(s) 4
10. [order] from clue 7 ambition:a storm chaser: ruled out position(s) 1,3,4
11. [order] from clue 4 school:Eastbrook Middle: ruled out position(s) 1,4
12. [order] from clue 3 student:Trey: ruled out position(s) 1
13. [order] from clue 3 ambition:an architect: ruled out position(s) 3
14. [order] from clue 1 ambition:a game designer: ruled out position(s) 4
15. [order] from clue 1 school:Watermill Middle: ruled out position(s) 1
16. [order] from clue 6 student:Darnell: ruled out position(s) 2
17. [bijection] ambition:an architect: ruled out position(s) 2
18. [bijection] ambition:a game designer: ruled out position(s) 2
19. [bijection] ambition:a pastry chef: ruled out position(s) 2
20. [bijection] school:Watermill Middle: ruled out position(s) 2
21. [bijection] school:North Terrace Middle: ruled out position(s) 2
22. [bijection] school:North Terrace Middle: ruled out position(s) 4
23. [order] from clue 6 student:Darnell: ruled out position(s) 1
24. [order] from clue 3 ambition:an architect: ruled out position(s) 4
25. [bijection] ambition:a game designer: ruled out position(s) 1
26. [bijection] ambition:a pastry chef: ruled out position(s) 3
27. [bijection] student:Trey: ruled out position(s) 3
28. [bijection] student:Linnea: ruled out position(s) 3
29. [bijection] student:Linnea: ruled out position(s) 2

---

<sub>seed `2026172794224` &middot; score 4.93 &middot; atoms 8 &middot; positives 2 &middot; solved by order</sub>
