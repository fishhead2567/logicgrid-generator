# The Saltmarsh Light Rotation

*The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.*

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `9d9c6807d605`

## Introduction

There are 5 shifts. Each has exactly one day and one item from every other category below, and within each category every item belongs to a different shift.
- **Day** (listed in order): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Keeper**: Lucian, Saoirse, Emmerich, Perpetua and Clementine.
- **Lighthouse**: Gannet Rock, Thimble Reef, Siren Shoal, Mawes Point and Pelter Head.
- **Weather noted**: sea fog, thunder, hail, sleet and a flat calm.
The days above are listed in order, from Monday to Friday.

## Clues

1. Emmerich goes with sea fog.
2. Wednesday, Lucian and sleet are three different shifts.
3. Thursday, Siren Shoal and a flat calm are three different shifts.
4. Thunder falls somewhere between Thursday and Clementine in day order.
5. Hail falls somewhere between Mawes Point and Pelter Head in day order. Saoirse falls somewhere between Wednesday and Pelter Head in day order.
6. Sea fog falls somewhere between Lucian and Gannet Rock in day order.
7. Perpetua and thunder are exactly two days apart in day order.

## Solving chart

*Day vs Keeper*

| | Lucian | Saoirse | Emmerich | Perpetua | Clementine |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Lighthouse*

| | Gannet Rock | Thimble Reef | Siren Shoal | Mawes Point | Pelter Head |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Weather noted*

| | sea fog | thunder | hail | sleet | a flat calm |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Keeper vs Lighthouse*

| | Gannet Rock | Thimble Reef | Siren Shoal | Mawes Point | Pelter Head |
|---|---|---|---|---|---|
| **Lucian** | | | | | |
| **Saoirse** | | | | | |
| **Emmerich** | | | | | |
| **Perpetua** | | | | | |
| **Clementine** | | | | | |

*Keeper vs Weather noted*

| | sea fog | thunder | hail | sleet | a flat calm |
|---|---|---|---|---|---|
| **Lucian** | | | | | |
| **Saoirse** | | | | | |
| **Emmerich** | | | | | |
| **Perpetua** | | | | | |
| **Clementine** | | | | | |

*Lighthouse vs Weather noted*

| | sea fog | thunder | hail | sleet | a flat calm |
|---|---|---|---|---|---|
| **Gannet Rock** | | | | | |
| **Thimble Reef** | | | | | |
| **Siren Shoal** | | | | | |
| **Mawes Point** | | | | | |
| **Pelter Head** | | | | | |

## Solution

| Day | Keeper | Lighthouse | Weather noted |
|---|---|---|---|
| Monday | Clementine | Pelter Head | sleet |
| Tuesday | Saoirse | Gannet Rock | thunder |
| Wednesday | Emmerich | Siren Shoal | sea fog |
| Thursday | Perpetua | Thimble Reef | hail |
| Friday | Lucian | Mawes Point | a flat calm |

## How it falls out

1. [bijection] from clue 7 keeper:Lucian: ruled out position(s) 3
2. [bijection] from clue 7 weather:sleet: ruled out position(s) 3
3. [bijection] from clue 6 light:Siren Shoal: ruled out position(s) 4
4. [bijection] from clue 6 weather:a flat calm: ruled out position(s) 4
5. [order] from clue 8 weather:hail: ruled out position(s) 1,5
6. [order] from clue 5 keeper:Saoirse: ruled out position(s) 1,3,5
7. [order] from clue 5 light:Pelter Head: ruled out position(s) 2,3,4
8. [order] from clue 4 weather:sea fog: ruled out position(s) 1,5
9. [order] from clue 2 weather:thunder: ruled out position(s) 1,4,5
10. [order] from clue 2 keeper:Clementine: ruled out position(s) 3,4,5
11. [order] from clue 3 keeper:Perpetua: ruled out position(s) 2,3
12. [direct] from clue 1 keeper:Emmerich: ruled out position(s) 1,5
13. [bijection] keeper:Emmerich: ruled out position(s) 2,4
14. [direct] from clue 1 weather:sea fog: ruled out position(s) 2,4
15. [order] from clue 4 light:Gannet Rock: ruled out position(s) 3
16. [bijection] weather:thunder: ruled out position(s) 3
17. [bijection] weather:hail: ruled out position(s) 3
18. [bijection] weather:a flat calm: ruled out position(s) 3
19. [order] from clue 3 keeper:Perpetua: ruled out position(s) 1,5
20. [order] from clue 2 keeper:Clementine: ruled out position(s) 2
21. [bijection] keeper:Lucian: ruled out position(s) 1,4
22. [bijection] keeper:Saoirse: ruled out position(s) 4
23. [bijection] keeper:Lucian: ruled out position(s) 2
24. [bijection] weather:hail: ruled out position(s) 2
25. [bijection] weather:sleet: ruled out position(s) 2
26. [bijection] weather:a flat calm: ruled out position(s) 2
27. [order] from clue 8 light:Mawes Point: ruled out position(s) 4
28. [order] from clue 5 light:Pelter Head: ruled out position(s) 5
29. [order] from clue 8 light:Mawes Point: ruled out position(s) 1,2,3
30. [bijection] from clue 7 weather:sleet: ruled out position(s) 5
31. [order] from clue 4 light:Gannet Rock: ruled out position(s) 4,5
32. [bijection] light:Gannet Rock: ruled out position(s) 1
33. [bijection] light:Thimble Reef: ruled out position(s) 1,5
34. [bijection] light:Siren Shoal: ruled out position(s) 1,5
35. [bijection] light:Thimble Reef: ruled out position(s) 2,3
36. [bijection] weather:sleet: ruled out position(s) 4
37. [bijection] weather:a flat calm: ruled out position(s) 1
38. [bijection] light:Siren Shoal: ruled out position(s) 2

---

<sub>seed `2026172813006` &middot; score 5.515 &middot; atoms 8 &middot; positives 1 &middot; solved by order</sub>
