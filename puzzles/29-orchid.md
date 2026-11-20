# The Orchid House Reckoning

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `87cac5acc3ac`

## Introduction

The orchid house at Fenn Park is shared by its growers, each convinced the others are overwatering.
Five growers are involved. Determine each grower's harvest month, orchid and pest.
- **Grower**: Rowena, Ambrose, Sigismund, Nkiruka and Columbine.
- **Harvest month** (listed from earlier to later): January, February, March, April and May.
- **Orchid**: a ghost orchid, a moth orchid, a jewel orchid, a dancing lady and a slipper orchid.
- **Pest**: thrips, a persistent slug, fungus gnats, scale insects and red spider mite.
Every grower has a different harvest month, orchid and pest, so within each category every item is used exactly once.

## Clues

1. The grower who grows a slipper orchid and April are exactly one month apart in harvest month order, in one direction or the other.
2. Ambrose and January are exactly three months apart in harvest month order.
3. The grower who is troubled by thrips is exactly one month earlier than February, with no harvest month in between.
4. The grower who grows a moth orchid falls somewhere between the grower who is troubled by fungus gnats and the grower who is troubled by red spider mite in harvest month order.
5. The grower who grows a slipper orchid is exactly one month earlier than the grower who is troubled by a persistent slug, with no harvest month in between.
6. The grower who grows a moth orchid is exactly one month earlier than Columbine, with no harvest month in between.
7. Sigismund falls somewhere between the grower who grows a jewel orchid and the grower who grows a slipper orchid in harvest month order.
8. Sigismund and the grower who grows a dancing lady are exactly three months apart in harvest month order.
9. Nkiruka falls somewhere between the grower who is troubled by a persistent slug and the grower who is troubled by red spider mite in harvest month order.

## Solving chart

*Harvest month vs Grower*

| | Rowena | Ambrose | Sigismund | Nkiruka | Columbine |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Harvest month vs Orchid*

| | a ghost orchid | a moth orchid | a jewel orchid | a dancing lady | a slipper orchid |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Harvest month vs Pest*

| | thrips | a persistent slug | fungus gnats | scale insects | red spider mite |
|---|---|---|---|---|---|
| **January** | | | | | |
| **February** | | | | | |
| **March** | | | | | |
| **April** | | | | | |
| **May** | | | | | |

*Grower vs Orchid*

| | a ghost orchid | a moth orchid | a jewel orchid | a dancing lady | a slipper orchid |
|---|---|---|---|---|---|
| **Rowena** | | | | | |
| **Ambrose** | | | | | |
| **Sigismund** | | | | | |
| **Nkiruka** | | | | | |
| **Columbine** | | | | | |

*Grower vs Pest*

| | thrips | a persistent slug | fungus gnats | scale insects | red spider mite |
|---|---|---|---|---|---|
| **Rowena** | | | | | |
| **Ambrose** | | | | | |
| **Sigismund** | | | | | |
| **Nkiruka** | | | | | |
| **Columbine** | | | | | |

*Orchid vs Pest*

| | thrips | a persistent slug | fungus gnats | scale insects | red spider mite |
|---|---|---|---|---|---|
| **a ghost orchid** | | | | | |
| **a moth orchid** | | | | | |
| **a jewel orchid** | | | | | |
| **a dancing lady** | | | | | |
| **a slipper orchid** | | | | | |

## Solution

| Harvest month | Grower | Orchid | Pest |
|---|---|---|---|
| January | Rowena | a jewel orchid | thrips |
| February | Sigismund | a ghost orchid | red spider mite |
| March | Nkiruka | a slipper orchid | scale insects |
| April | Ambrose | a moth orchid | a persistent slug |
| May | Columbine | a dancing lady | fungus gnats |

## How it falls out

1. [order] from clue 9 grower:Sigismund: ruled out position(s) 3
2. [order] from clue 9 orchid:a dancing lady: ruled out position(s) 3
3. [order] from clue 8 orchid:a slipper orchid: ruled out position(s) 5
4. [order] from clue 8 pest:a persistent slug: ruled out position(s) 1
5. [order] from clue 7 pest:thrips: ruled out position(s) 2,3,4,5
6. [order] from clue 6 orchid:a moth orchid: ruled out position(s) 1,5
7. [order] from clue 5 grower:Sigismund: ruled out position(s) 1,5
8. [order] from clue 5 orchid:a jewel orchid: ruled out position(s) 2
9. [order] from clue 9 orchid:a dancing lady: ruled out position(s) 2,4
10. [order] from clue 4 grower:Ambrose: ruled out position(s) 1,2,3,5
11. [order] from clue 3 orchid:a slipper orchid: ruled out position(s) 1,2,4
12. [order] from clue 8 pest:a persistent slug: ruled out position(s) 2,3,5
13. [order] from clue 5 orchid:a jewel orchid: ruled out position(s) 3,4
14. [order] from clue 2 grower:Columbine: ruled out position(s) 1,2
15. [order] from clue 1 grower:Nkiruka: ruled out position(s) 1,4,5
16. [order] from clue 1 pest:red spider mite: ruled out position(s) 3,4,5
17. [order] from clue 6 pest:fungus gnats: ruled out position(s) 1,2
18. [bijection] grower:Rowena: ruled out position(s) 4
19. [bijection] grower:Sigismund: ruled out position(s) 4
20. [bijection] grower:Columbine: ruled out position(s) 4
21. [bijection] grower:Rowena: ruled out position(s) 2,3,5
22. [bijection] orchid:a ghost orchid: ruled out position(s) 3
23. [bijection] orchid:a moth orchid: ruled out position(s) 3
24. [bijection] pest:fungus gnats: ruled out position(s) 4
25. [bijection] pest:scale insects: ruled out position(s) 1,4
26. [bijection] pest:red spider mite: ruled out position(s) 1
27. [order] from clue 1 grower:Nkiruka: ruled out position(s) 2
28. [order] from clue 6 orchid:a moth orchid: ruled out position(s) 2
29. [order] from clue 6 pest:fungus gnats: ruled out position(s) 3
30. [order] from clue 2 grower:Columbine: ruled out position(s) 3
31. [order] from clue 9 orchid:a dancing lady: ruled out position(s) 1
32. [order] from clue 5 orchid:a jewel orchid: ruled out position(s) 5
33. [bijection] orchid:a ghost orchid: ruled out position(s) 1,4,5
34. [bijection] pest:scale insects: ruled out position(s) 2,5

---

<sub>seed `2026173005093` &middot; score 5.675 &middot; atoms 9 &middot; positives 0 &middot; solved by order</sub>
