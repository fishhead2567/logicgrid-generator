# The Orchid House Reckoning

*The orchid house at Fenn Park is shared by its growers, each convinced the others are overwatering.*

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `0b8b0b5bb0ee`

## Introduction

There are 4 entries. Each has exactly one month and one item from every other category below, and within each category every item belongs to a different entry.
- **Month** (listed in order): January, February, March and April.
- **Grower**: Ambrose, Leocadia, Rowena and Taavi.
- **Pest**: a persistent slug, fungus gnats, thrips and red spider mite.
The months above are listed in order, from January to April.

## Clues

1. Leocadia goes with April, but leocadia does not go with red spider mite.
2. January goes with thrips.
3. Ambrose goes with a persistent slug.
4. April and a persistent slug are next to each other in month order, in one order or the other.
5. Taavi does not go with February.

## Solving chart

*Month vs Grower*

| | Ambrose | Leocadia | Rowena | Taavi |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Month vs Pest*

| | a persistent slug | fungus gnats | thrips | red spider mite |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Grower vs Pest*

| | a persistent slug | fungus gnats | thrips | red spider mite |
|---|---|---|---|---|
| **Ambrose** | | | | |
| **Leocadia** | | | | |
| **Rowena** | | | | |
| **Taavi** | | | | |

## Solution

| Month | Grower | Pest |
|---|---|---|
| January | Taavi | thrips |
| February | Rowena | red spider mite |
| March | Ambrose | a persistent slug |
| April | Leocadia | fungus gnats |

## How it falls out

1. [direct] from clue 5 pest:thrips: ruled out position(s) 2,3,4
2. [direct] from clue 4 grower:Leocadia: ruled out position(s) 1,2,3
3. [direct] from clue 3 grower:Taavi: ruled out position(s) 2
4. [direct] from clue 1 pest:red spider mite: ruled out position(s) 4
5. [bijection] grower:Ambrose: ruled out position(s) 4
6. [bijection] grower:Rowena: ruled out position(s) 4
7. [bijection] grower:Taavi: ruled out position(s) 4
8. [bijection] pest:a persistent slug: ruled out position(s) 1
9. [bijection] pest:fungus gnats: ruled out position(s) 1
10. [bijection] pest:red spider mite: ruled out position(s) 1
11. [direct] from clue 6 grower:Ambrose: ruled out position(s) 1
12. [direct] from clue 6 pest:a persistent slug: ruled out position(s) 4
13. [bijection] pest:fungus gnats: ruled out position(s) 2,3
14. [order] from clue 2 pest:a persistent slug: ruled out position(s) 2
15. [direct] from clue 6 grower:Ambrose: ruled out position(s) 2
16. [bijection] grower:Rowena: ruled out position(s) 3
17. [bijection] grower:Taavi: ruled out position(s) 3
18. [bijection] grower:Rowena: ruled out position(s) 1
19. [bijection] pest:red spider mite: ruled out position(s) 3

---

<sub>seed `2026172583355` &middot; score 3.97 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
