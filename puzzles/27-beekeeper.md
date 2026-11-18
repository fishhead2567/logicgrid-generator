# The Honey Show Scandal

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `610c7b4ed97e`

## Introduction

The annual honey show has been judged, and at least two people are writing letters about it.
Five beekeepers are involved. Determine each beekeeper's entry fee, hive and note.
- **Beekeeper**: Breda, Ezekiel, Antonina, Fausto and Priya.
- **Entry fee** (listed from cheaper to dearer): $2, $4, $6, $8 and $10.
- **Hive type**: a long deep hive, a Langstroth hive, a skep, a WBC hive and a Warre hive.
- **Judge's note**: an unlabelled lid, a trace of wax, crystallised early, a cloudy jar and an overbearing aroma.
Every beekeeper has a different entry fee, hive and note, so within each category every item is used exactly once.

## Clues

1. The beekeeper who keeps a Warre hive is cheaper than the beekeeper who has a jar noted as crystallised early in entry fee order. The beekeeper who keeps a Warre hive pays $4.
2. Breda falls somewhere between $2 and $8 in entry fee order.
3. Antonina is exactly one fee step cheaper than $10, with no entry fee in between.
4. The beekeeper who has a jar noted as an overbearing aroma and $10 are exactly one fee step apart in entry fee order, in one direction or the other.
5. Fausto is exactly one fee step cheaper than $6, with no entry fee in between.
6. The beekeeper who keeps a Langstroth hive falls somewhere between $10 and Ezekiel in entry fee order.
7. The beekeeper who has a jar noted as crystallised early is cheaper than the beekeeper who keeps a skep in entry fee order.
8. The beekeeper who has a jar noted as a trace of wax is exactly one fee step cheaper than the beekeeper who keeps a WBC hive, with no entry fee in between.
9. The beekeeper who keeps a skep does not have a jar noted as an unlabelled lid.

## Solving chart

*Entry fee vs Beekeeper*

| | Breda | Ezekiel | Antonina | Fausto | Priya |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Hive type*

| | a long deep hive | a Langstroth hive | a skep | a WBC hive | a Warre hive |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Entry fee vs Judge's note*

| | an unlabelled lid | a trace of wax | crystallised early | a cloudy jar | an overbearing aroma |
|---|---|---|---|---|---|
| **$2** | | | | | |
| **$4** | | | | | |
| **$6** | | | | | |
| **$8** | | | | | |
| **$10** | | | | | |

*Beekeeper vs Hive type*

| | a long deep hive | a Langstroth hive | a skep | a WBC hive | a Warre hive |
|---|---|---|---|---|---|
| **Breda** | | | | | |
| **Ezekiel** | | | | | |
| **Antonina** | | | | | |
| **Fausto** | | | | | |
| **Priya** | | | | | |

*Beekeeper vs Judge's note*

| | an unlabelled lid | a trace of wax | crystallised early | a cloudy jar | an overbearing aroma |
|---|---|---|---|---|---|
| **Breda** | | | | | |
| **Ezekiel** | | | | | |
| **Antonina** | | | | | |
| **Fausto** | | | | | |
| **Priya** | | | | | |

*Hive type vs Judge's note*

| | an unlabelled lid | a trace of wax | crystallised early | a cloudy jar | an overbearing aroma |
|---|---|---|---|---|---|
| **a long deep hive** | | | | | |
| **a Langstroth hive** | | | | | |
| **a skep** | | | | | |
| **a WBC hive** | | | | | |
| **a Warre hive** | | | | | |

## Solution

| Entry fee | Beekeeper | Hive type | Judge's note |
|---|---|---|---|
| $2 | Ezekiel | a long deep hive | an unlabelled lid |
| $4 | Fausto | a Warre hive | a trace of wax |
| $6 | Breda | a WBC hive | crystallised early |
| $8 | Antonina | a Langstroth hive | an overbearing aroma |
| $10 | Priya | a skep | a cloudy jar |

## How it falls out

1. [direct] from clue 3 hive:a Warre hive: ruled out position(s) 1,3,4,5
2. [bijection] hive:a long deep hive: ruled out position(s) 2
3. [bijection] hive:a Langstroth hive: ruled out position(s) 2
4. [bijection] hive:a skep: ruled out position(s) 2
5. [bijection] hive:a WBC hive: ruled out position(s) 2
6. [order] from clue 10 keeper:Fausto: ruled out position(s) 1,3,4,5
7. [order] from clue 8 hive:a Langstroth hive: ruled out position(s) 1,5
8. [order] from clue 8 keeper:Ezekiel: ruled out position(s) 4,5
9. [order] from clue 7 verdict:an overbearing aroma: ruled out position(s) 1,2,3,5
10. [order] from clue 6 keeper:Breda: ruled out position(s) 1,4,5
11. [order] from clue 5 verdict:a trace of wax: ruled out position(s) 1,5
12. [order] from clue 5 hive:a WBC hive: ruled out position(s) 1
13. [order] from clue 4 verdict:crystallised early: ruled out position(s) 5
14. [order] from clue 4 hive:a skep: ruled out position(s) 1
15. [order] from clue 2 keeper:Antonina: ruled out position(s) 1,2,3,5
16. [order] from clue 1 verdict:crystallised early: ruled out position(s) 1,2
17. [order] from clue 4 hive:a skep: ruled out position(s) 3
18. [bijection] hive:a long deep hive: ruled out position(s) 3,4,5
19. [bijection] keeper:Breda: ruled out position(s) 2
20. [bijection] keeper:Ezekiel: ruled out position(s) 2
21. [bijection] keeper:Priya: ruled out position(s) 2,4
22. [bijection] keeper:Priya: ruled out position(s) 1,3
23. [bijection] verdict:an unlabelled lid: ruled out position(s) 4
24. [bijection] verdict:a trace of wax: ruled out position(s) 4
25. [bijection] verdict:crystallised early: ruled out position(s) 4
26. [bijection] verdict:a cloudy jar: ruled out position(s) 4
27. [order] from clue 5 hive:a WBC hive: ruled out position(s) 5
28. [bijection] hive:a skep: ruled out position(s) 4
29. [bijection] keeper:Ezekiel: ruled out position(s) 3
30. [bijection] verdict:an unlabelled lid: ruled out position(s) 3
31. [bijection] verdict:a trace of wax: ruled out position(s) 3
32. [bijection] verdict:a cloudy jar: ruled out position(s) 3
33. [order] from clue 5 hive:a WBC hive: ruled out position(s) 4
34. [direct] from clue 9 verdict:an unlabelled lid: ruled out position(s) 5
35. [bijection] hive:a Langstroth hive: ruled out position(s) 3
36. [bijection] verdict:an unlabelled lid: ruled out position(s) 2
37. [bijection] verdict:a cloudy jar: ruled out position(s) 2
38. [bijection] verdict:a cloudy jar: ruled out position(s) 1

---

<sub>seed `2026172789249` &middot; score 5.515 &middot; atoms 10 &middot; positives 1 &middot; solved by order</sub>
