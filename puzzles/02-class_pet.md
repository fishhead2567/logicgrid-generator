# The Room 12 Class Pet Vote

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `557fcdaf3241`

## Introduction

Mr. Ocampo said the class could pick one pet. Nobody warned him that would mean campaign posters.
Four kids are involved. Determine each kid's vote count and name.
- **Kid**: Sanjay, Kwame, Dashiell and Ezra.
- **Vote count** (listed from lower to higher): 4 votes, 6 votes, 8 votes and 10 votes.
- **Name**: Noodle, Taco, Rocket and Sir Pickles.
Every kid has a different vote count and name, so within each category every item is used exactly once.

## Clues

1. Kwame wins 6 votes.
2. Ezra wins 8 votes.
3. The kid who calls it Sir Pickles wins 8 votes.
4. The kid who calls it Noodle and 6 votes are exactly one vote step apart in vote count order, in one direction or the other.
5. The kid who calls it Taco is lower than Sanjay in vote count order.

## Solving chart

*Vote count vs Kid*

| | Sanjay | Kwame | Dashiell | Ezra |
|---|---|---|---|---|
| **4 votes** | | | | |
| **6 votes** | | | | |
| **8 votes** | | | | |
| **10 votes** | | | | |

*Vote count vs Name*

| | Noodle | Taco | Rocket | Sir Pickles |
|---|---|---|---|---|
| **4 votes** | | | | |
| **6 votes** | | | | |
| **8 votes** | | | | |
| **10 votes** | | | | |

*Kid vs Name*

| | Noodle | Taco | Rocket | Sir Pickles |
|---|---|---|---|---|
| **Sanjay** | | | | |
| **Kwame** | | | | |
| **Dashiell** | | | | |
| **Ezra** | | | | |

## Solution

| Vote count | Kid | Name |
|---|---|---|
| 4 votes | Dashiell | Noodle |
| 6 votes | Kwame | Taco |
| 8 votes | Ezra | Sir Pickles |
| 10 votes | Sanjay | Rocket |

## How it falls out

1. [direct] from clue 5 petname:Sir Pickles: ruled out position(s) 1,2,4
2. [direct] from clue 4 kid:Ezra: ruled out position(s) 1,2,4
3. [direct] from clue 1 kid:Kwame: ruled out position(s) 1,3,4
4. [bijection] kid:Sanjay: ruled out position(s) 2,3
5. [bijection] kid:Dashiell: ruled out position(s) 2,3
6. [bijection] petname:Noodle: ruled out position(s) 3
7. [bijection] petname:Taco: ruled out position(s) 3
8. [bijection] petname:Rocket: ruled out position(s) 3
9. [order] from clue 3 petname:Taco: ruled out position(s) 4
10. [order] from clue 3 kid:Sanjay: ruled out position(s) 1
11. [order] from clue 2 petname:Noodle: ruled out position(s) 2,4
12. [bijection] kid:Dashiell: ruled out position(s) 4
13. [bijection] petname:Taco: ruled out position(s) 1
14. [bijection] petname:Rocket: ruled out position(s) 1
15. [bijection] petname:Rocket: ruled out position(s) 2

---

<sub>seed `2026172891283` &middot; score 3.97 &middot; atoms 5 &middot; positives 3 &middot; solved by order</sub>
