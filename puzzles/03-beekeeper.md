# The Honey Show Scandal

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `11b1bffd9c2a`

## Introduction

The annual honey show has been judged, and at least two people are writing letters about it.
Four beekeepers are involved. Determine each beekeeper's entry fee and honey.
- **Beekeeper**: Fausto, Mungo, Priya and Ezekiel.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6 and $8.
- **Honey**: lime blossom honey, chestnut honey, borage honey and clover honey.
Every beekeeper has a different entry fee and honey, so within each category every item is used exactly once.

## Clues

1. Priya enters borage honey. The beekeeper who enters borage honey pays $6.
2. Fausto enters chestnut honey.
3. Mungo is dearer than $4 in entry fee order.
4. Ezekiel does not pay $2.
5. The beekeeper who enters lime blossom honey does not pay $8.

## Solving chart

*Entry fee vs Beekeeper*

| | Fausto | Mungo | Priya | Ezekiel |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Entry fee vs Honey*

| | lime blossom honey | chestnut honey | borage honey | clover honey |
|---|---|---|---|---|
| **$2** | | | | |
| **$4** | | | | |
| **$6** | | | | |
| **$8** | | | | |

*Beekeeper vs Honey*

| | lime blossom honey | chestnut honey | borage honey | clover honey |
|---|---|---|---|---|
| **Fausto** | | | | |
| **Mungo** | | | | |
| **Priya** | | | | |
| **Ezekiel** | | | | |

## Solution

| Entry fee | Beekeeper | Honey |
|---|---|---|
| $2 | Fausto | chestnut honey |
| $4 | Ezekiel | lime blossom honey |
| $6 | Priya | borage honey |
| $8 | Mungo | clover honey |

## How it falls out

1. [direct] from clue 5 honey:borage honey: ruled out position(s) 1,2,4
2. [direct] from clue 3 keeper:Ezekiel: ruled out position(s) 1
3. [direct] from clue 2 keeper:Priya: ruled out position(s) 1,2,4
4. [direct] from clue 1 honey:lime blossom honey: ruled out position(s) 4
5. [bijection] honey:lime blossom honey: ruled out position(s) 3
6. [bijection] honey:chestnut honey: ruled out position(s) 3
7. [bijection] honey:clover honey: ruled out position(s) 3
8. [bijection] keeper:Fausto: ruled out position(s) 3
9. [bijection] keeper:Mungo: ruled out position(s) 3
10. [bijection] keeper:Ezekiel: ruled out position(s) 3
11. [order] from clue 4 keeper:Mungo: ruled out position(s) 1,2
12. [bijection] keeper:Fausto: ruled out position(s) 4
13. [bijection] keeper:Ezekiel: ruled out position(s) 4
14. [bijection] keeper:Fausto: ruled out position(s) 2
15. [direct] from clue 6 honey:chestnut honey: ruled out position(s) 2,4
16. [bijection] honey:lime blossom honey: ruled out position(s) 1
17. [bijection] honey:clover honey: ruled out position(s) 1
18. [bijection] honey:clover honey: ruled out position(s) 2

---

<sub>seed `2026172699196` &middot; score 3.97 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
