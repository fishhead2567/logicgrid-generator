# The Foragers of Thorn Bottom

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `22721a8c30f2`

## Introduction

The Thorn Bottom foraging club keeps meticulous records, chiefly so that blame can be apportioned later.
Five foragers are involved. Determine each forager's day, find and wood.
- **Forager**: Ramiro, Annika, Tobias, Guinevere and Eilish.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Find**: a cauliflower fungus, a penny bun, a horn of plenty, a chicken of the woods and a parasol mushroom.
- **Wood**: Hangman's Copse, Dovecote Wood, the Old Deer Park, Nettlebed and Scrag End.
Every forager has a different day, find and wood, so within each category every item is used exactly once.

## Clues

1. At least one of the following holds, and possibly more than one: (a) Tobias forages on Thursday. (b) Tobias does not forage on Wednesday.
2. The forager who searches Scrag End and Monday are exactly one day apart in day order, in one direction or the other.
3. The forager who finds a parasol mushroom and Thursday are exactly two days apart in day order.
4. The forager who searches Hangman's Copse falls somewhere between the forager who finds a cauliflower fungus and Eilish in day order.
5. At least one of the following holds, and possibly more than one: (a) The forager who finds a cauliflower fungus is earlier than the forager who searches Dovecote Wood in day order. (b) The forager who finds a cauliflower fungus searches Nettlebed.
6. Guinevere and the forager who searches Scrag End are exactly two days apart in day order.
7. The forager who searches Hangman's Copse is earlier than the forager who finds a penny bun in day order.
8. The forager who finds a horn of plenty is exactly one day earlier than the forager who searches the Old Deer Park, with no day in between.
9. Annika and the forager who searches Nettlebed are exactly three days apart in day order.

## Solving chart

*Day vs Forager*

| | Ramiro | Annika | Tobias | Guinevere | Eilish |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Find*

| | a cauliflower fungus | a penny bun | a horn of plenty | a chicken of the woods | a parasol mushroom |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Wood*

| | Hangman's Copse | Dovecote Wood | the Old Deer Park | Nettlebed | Scrag End |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Forager vs Find*

| | a cauliflower fungus | a penny bun | a horn of plenty | a chicken of the woods | a parasol mushroom |
|---|---|---|---|---|---|
| **Ramiro** | | | | | |
| **Annika** | | | | | |
| **Tobias** | | | | | |
| **Guinevere** | | | | | |
| **Eilish** | | | | | |

*Forager vs Wood*

| | Hangman's Copse | Dovecote Wood | the Old Deer Park | Nettlebed | Scrag End |
|---|---|---|---|---|---|
| **Ramiro** | | | | | |
| **Annika** | | | | | |
| **Tobias** | | | | | |
| **Guinevere** | | | | | |
| **Eilish** | | | | | |

*Find vs Wood*

| | Hangman's Copse | Dovecote Wood | the Old Deer Park | Nettlebed | Scrag End |
|---|---|---|---|---|---|
| **a cauliflower fungus** | | | | | |
| **a penny bun** | | | | | |
| **a horn of plenty** | | | | | |
| **a chicken of the woods** | | | | | |
| **a parasol mushroom** | | | | | |

## Solution

| Day | Forager | Find | Wood |
|---|---|---|---|
| Monday | Eilish | a chicken of the woods | Dovecote Wood |
| Tuesday | Annika | a parasol mushroom | Scrag End |
| Wednesday | Ramiro | a horn of plenty | Hangman's Copse |
| Thursday | Guinevere | a penny bun | the Old Deer Park |
| Friday | Tobias | a cauliflower fungus | Nettlebed |

## How it falls out

1. [order] from clue 9 wood:Hangman's Copse: ruled out position(s) 1,5
2. [order] from clue 8 find:a parasol mushroom: ruled out position(s) 1,3,4,5
3. [order] from clue 6 wood:Scrag End: ruled out position(s) 1,3,4,5
4. [order] from clue 7 forager:Guinevere: ruled out position(s) 1,2,3,5
5. [order] from clue 3 find:a penny bun: ruled out position(s) 1,2
6. [order] from clue 2 forager:Annika: ruled out position(s) 3
7. [order] from clue 2 wood:Nettlebed: ruled out position(s) 3
8. [order] from clue 1 find:a horn of plenty: ruled out position(s) 5
9. [order] from clue 1 wood:the Old Deer Park: ruled out position(s) 1
10. [bijection] find:a cauliflower fungus: ruled out position(s) 2
11. [bijection] find:a horn of plenty: ruled out position(s) 2
12. [bijection] find:a chicken of the woods: ruled out position(s) 2
13. [bijection] forager:Ramiro: ruled out position(s) 4
14. [bijection] forager:Annika: ruled out position(s) 4
15. [bijection] forager:Tobias: ruled out position(s) 4
16. [bijection] forager:Eilish: ruled out position(s) 4
17. [bijection] wood:Hangman's Copse: ruled out position(s) 2
18. [bijection] wood:Dovecote Wood: ruled out position(s) 2
19. [bijection] wood:the Old Deer Park: ruled out position(s) 2
20. [bijection] wood:Nettlebed: ruled out position(s) 2
21. [order] from clue 3 find:a penny bun: ruled out position(s) 3
22. [order] from clue 2 forager:Annika: ruled out position(s) 5
23. [order] from clue 2 wood:Nettlebed: ruled out position(s) 1
24. [order] from clue 1 find:a horn of plenty: ruled out position(s) 1
25. [order] from clue 1 wood:the Old Deer Park: ruled out position(s) 3
26. [bijection] wood:Dovecote Wood: ruled out position(s) 3,4,5
27. [bijection] wood:Hangman's Copse: ruled out position(s) 4
28. [order] from clue 9 find:a cauliflower fungus: ruled out position(s) 3
29. [order] from clue 9 forager:Eilish: ruled out position(s) 3
30. [disjunction] from clue 5 forager:Tobias: ruled out position(s) 3
31. [disjunction] from clue 4 find:a cauliflower fungus: ruled out position(s) 1
32. [order] from clue 9 forager:Eilish: ruled out position(s) 5
33. [bijection] find:a chicken of the woods: ruled out position(s) 3,4,5
34. [bijection] forager:Ramiro: ruled out position(s) 1,2,5
35. [bijection] find:a horn of plenty: ruled out position(s) 4
36. [bijection] forager:Tobias: ruled out position(s) 1,2
37. [order] from clue 1 wood:the Old Deer Park: ruled out position(s) 5
38. [bijection] wood:Nettlebed: ruled out position(s) 4
39. [disjunction] from clue 4 find:a cauliflower fungus: ruled out position(s) 4
40. [order] from clue 2 forager:Annika: ruled out position(s) 1
_... and 2 further steps._

---

<sub>seed `2026173076364` &middot; score 9.5355 &middot; atoms 9 &middot; positives 0 &middot; solved by disjunction</sub>
