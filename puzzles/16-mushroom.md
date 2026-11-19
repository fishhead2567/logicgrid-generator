# The Foragers of Thorn Bottom

**Difficulty** 3/7 (easy) &nbsp;&nbsp; **Grid** 3 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `ac912de06f09`

## Introduction

The Thorn Bottom foraging club keeps meticulous records, chiefly so that blame can be apportioned later.
Five foragers are involved. Determine each forager's day and basket.
- **Forager**: Ramiro, Eilish, Solomon, Annika and Tobias.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Basket**: a canvas satchel, an upturned hat, a string bag, a wicker trug and a tin pail.
Every forager has a different day and basket, so within each category every item is used exactly once.

## Clues

1. Ramiro carries a string bag.
2. Annika carries a wicker trug.
3. Annika is exactly one day earlier than the forager who carries a canvas satchel, with no day in between. The forager who carries a canvas satchel is later than Wednesday in day order.
4. The forager who carries a tin pail is later than Wednesday in day order.
5. Monday is exactly one day earlier than Tobias, with no day in between.
6. Eilish does not forage on Friday.

## Solving chart

*Day vs Forager*

| | Ramiro | Eilish | Solomon | Annika | Tobias |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Basket*

| | a canvas satchel | an upturned hat | a string bag | a wicker trug | a tin pail |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Forager vs Basket*

| | a canvas satchel | an upturned hat | a string bag | a wicker trug | a tin pail |
|---|---|---|---|---|---|
| **Ramiro** | | | | | |
| **Eilish** | | | | | |
| **Solomon** | | | | | |
| **Annika** | | | | | |
| **Tobias** | | | | | |

## Solution

| Day | Forager | Basket |
|---|---|---|
| Monday | Ramiro | a string bag |
| Tuesday | Tobias | an upturned hat |
| Wednesday | Annika | a wicker trug |
| Thursday | Eilish | a canvas satchel |
| Friday | Solomon | a tin pail |

## How it falls out

1. [direct] from clue 2 forager:Eilish: ruled out position(s) 5
2. [order] from clue 7 forager:Tobias: ruled out position(s) 1,3,4,5
3. [order] from clue 6 basket:a canvas satchel: ruled out position(s) 1,2,3
4. [order] from clue 5 basket:a tin pail: ruled out position(s) 1,2,3
5. [order] from clue 3 forager:Annika: ruled out position(s) 1,2,5
6. [direct] from clue 4 basket:a wicker trug: ruled out position(s) 1,2,5
7. [bijection] forager:Ramiro: ruled out position(s) 2
8. [bijection] forager:Eilish: ruled out position(s) 2
9. [bijection] forager:Solomon: ruled out position(s) 2
10. [direct] from clue 1 basket:a string bag: ruled out position(s) 2
11. [bijection] basket:an upturned hat: ruled out position(s) 1,3,4,5
12. [bijection] basket:a string bag: ruled out position(s) 3,4,5
13. [direct] from clue 1 forager:Ramiro: ruled out position(s) 3,4,5
14. [bijection] basket:a wicker trug: ruled out position(s) 4
15. [bijection] forager:Eilish: ruled out position(s) 1
16. [bijection] forager:Solomon: ruled out position(s) 1
17. [bijection] forager:Solomon: ruled out position(s) 3,4
18. [direct] from clue 4 forager:Annika: ruled out position(s) 4
19. [order] from clue 3 basket:a canvas satchel: ruled out position(s) 5
20. [bijection] basket:a tin pail: ruled out position(s) 4
21. [bijection] forager:Eilish: ruled out position(s) 3

---

<sub>seed `2026172802143` &middot; score 4.62 &middot; atoms 7 &middot; positives 2 &middot; solved by order</sub>
