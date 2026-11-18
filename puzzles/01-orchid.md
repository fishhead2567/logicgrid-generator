# The Orchid House Reckoning

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `21916313eb18`

## Introduction

The orchid house at Fenn Park is shared by its growers, each convinced the others are overwatering.
Four growers are involved. Determine each grower's harvest month and potting mix.
- **Grower**: Ambrose, Columbine, Leocadia and Rowena.
- **Harvest month** (listed from earlier to later): January, February, March and April.
- **Potting mix**: tree fern fibre; coconut husk; perlite and charcoal; and lava rock.
Every grower has a different harvest month and potting mix, so within each category every item is used exactly once.

## Clues

1. Columbine harvests in April. Columbine does not pot in lava rock.
2. The grower who pots in perlite and charcoal harvests in January.
3. Ambrose pots in tree fern fibre.
4. The grower who pots in tree fern fibre and April are exactly one month apart in harvest month order, in one direction or the other.
5. Rowena does not harvest in February.

## Solving chart

*Harvest month vs Grower*

| | Ambrose | Columbine | Leocadia | Rowena |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Harvest month vs Potting mix*

| | tree fern fibre | coconut husk | perlite and charcoal | lava rock |
|---|---|---|---|---|
| **January** | | | | |
| **February** | | | | |
| **March** | | | | |
| **April** | | | | |

*Grower vs Potting mix*

| | tree fern fibre | coconut husk | perlite and charcoal | lava rock |
|---|---|---|---|---|
| **Ambrose** | | | | |
| **Columbine** | | | | |
| **Leocadia** | | | | |
| **Rowena** | | | | |

## Solution

| Harvest month | Grower | Potting mix |
|---|---|---|
| January | Rowena | perlite and charcoal |
| February | Leocadia | lava rock |
| March | Ambrose | tree fern fibre |
| April | Columbine | coconut husk |

## How it falls out

1. [direct] from clue 5 mix:perlite and charcoal: ruled out position(s) 2,3,4
2. [direct] from clue 4 grower:Columbine: ruled out position(s) 1,2,3
3. [direct] from clue 3 grower:Rowena: ruled out position(s) 2
4. [direct] from clue 1 mix:lava rock: ruled out position(s) 4
5. [bijection] grower:Ambrose: ruled out position(s) 4
6. [bijection] grower:Leocadia: ruled out position(s) 4
7. [bijection] grower:Rowena: ruled out position(s) 4
8. [bijection] mix:tree fern fibre: ruled out position(s) 1
9. [bijection] mix:coconut husk: ruled out position(s) 1
10. [bijection] mix:lava rock: ruled out position(s) 1
11. [direct] from clue 6 grower:Ambrose: ruled out position(s) 1
12. [direct] from clue 6 mix:tree fern fibre: ruled out position(s) 4
13. [bijection] mix:coconut husk: ruled out position(s) 2,3
14. [order] from clue 2 mix:tree fern fibre: ruled out position(s) 2
15. [direct] from clue 6 grower:Ambrose: ruled out position(s) 2
16. [bijection] grower:Leocadia: ruled out position(s) 3
17. [bijection] grower:Rowena: ruled out position(s) 3
18. [bijection] grower:Leocadia: ruled out position(s) 1
19. [bijection] mix:lava rock: ruled out position(s) 3

---

<sub>seed `2026172583355` &middot; score 3.97 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
