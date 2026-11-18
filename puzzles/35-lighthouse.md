# The Saltmarsh Light Rotation

*The lighthouses along the Saltmarsh coast share a single relief keeper roster, and the logbooks have become a scholarly mess.*

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 5 x 5 &nbsp;&nbsp; **Clues** 7 &nbsp;&nbsp; **id** `83588c00d8df`

## Introduction

There are 5 shifts. Each has exactly one day and one item from every other category below, and within each category every item belongs to a different shift.
- **Day** (listed in order): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Keeper**: Barnaby, Clementine, Hollis, Lucian and Saoirse.
- **Lighthouse**: Thimble Reef, Gannet Rock, Siren Shoal, Pelter Head and Blackwater Bar.
- **Logged chore**: splicing the hoist rope, repainting the gallery, regrinding the lens, rebedding the storm glass and overhauling the foghorn.
- **Weather noted**: a flat calm, sea fog, hail, sleet and a gale.
The days above are listed in order, from Monday to Friday.

## Clues

1. Monday goes with Siren Shoal.
2. Repainting the gallery and sea fog are exactly four days apart in day order. Splicing the hoist rope falls somewhere between Wednesday and sea fog in day order.
3. At least one of the following holds, and possibly more than one: (a) Tuesday is earlier than regrinding the lens' day. (b) Repainting the gallery goes with Pelter Head.
4. Tuesday, Saoirse and sleet are three different shifts. A gale falls somewhere between regrinding the lens and Saoirse in day order. Regrinding the lens and Pelter Head both sit at odd-numbered days or both at even-numbered days.
5. Lucian, Siren Shoal and hail are three different shifts. Barnaby, Thimble Reef and hail are three different shifts. Overhauling the foghorn falls somewhere between Lucian and Pelter Head in day order.
6. Blackwater Bar's day is immediately earlier than Clementine's day, with no day in between.
7. Thimble Reef's day is immediately earlier than splicing the hoist rope's day, with no day in between.

## Solving chart

*Day vs Keeper*

| | Barnaby | Clementine | Hollis | Lucian | Saoirse |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Lighthouse*

| | Thimble Reef | Gannet Rock | Siren Shoal | Pelter Head | Blackwater Bar |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Logged chore*

| | splicing the hoist rope | repainting the gallery | regrinding the lens | rebedding the storm glass | overhauling the foghorn |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Weather noted*

| | a flat calm | sea fog | hail | sleet | a gale |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Keeper vs Lighthouse*

| | Thimble Reef | Gannet Rock | Siren Shoal | Pelter Head | Blackwater Bar |
|---|---|---|---|---|---|
| **Barnaby** | | | | | |
| **Clementine** | | | | | |
| **Hollis** | | | | | |
| **Lucian** | | | | | |
| **Saoirse** | | | | | |

*Keeper vs Logged chore*

| | splicing the hoist rope | repainting the gallery | regrinding the lens | rebedding the storm glass | overhauling the foghorn |
|---|---|---|---|---|---|
| **Barnaby** | | | | | |
| **Clementine** | | | | | |
| **Hollis** | | | | | |
| **Lucian** | | | | | |
| **Saoirse** | | | | | |

*Keeper vs Weather noted*

| | a flat calm | sea fog | hail | sleet | a gale |
|---|---|---|---|---|---|
| **Barnaby** | | | | | |
| **Clementine** | | | | | |
| **Hollis** | | | | | |
| **Lucian** | | | | | |
| **Saoirse** | | | | | |

*Lighthouse vs Logged chore*

| | splicing the hoist rope | repainting the gallery | regrinding the lens | rebedding the storm glass | overhauling the foghorn |
|---|---|---|---|---|---|
| **Thimble Reef** | | | | | |
| **Gannet Rock** | | | | | |
| **Siren Shoal** | | | | | |
| **Pelter Head** | | | | | |
| **Blackwater Bar** | | | | | |

*Lighthouse vs Weather noted*

| | a flat calm | sea fog | hail | sleet | a gale |
|---|---|---|---|---|---|
| **Thimble Reef** | | | | | |
| **Gannet Rock** | | | | | |
| **Siren Shoal** | | | | | |
| **Pelter Head** | | | | | |
| **Blackwater Bar** | | | | | |

*Logged chore vs Weather noted*

| | a flat calm | sea fog | hail | sleet | a gale |
|---|---|---|---|---|---|
| **splicing the hoist rope** | | | | | |
| **repainting the gallery** | | | | | |
| **regrinding the lens** | | | | | |
| **rebedding the storm glass** | | | | | |
| **overhauling the foghorn** | | | | | |

## Solution

| Day | Keeper | Lighthouse | Logged chore | Weather noted |
|---|---|---|---|---|
| Monday | Saoirse | Siren Shoal | repainting the gallery | a flat calm |
| Tuesday | Lucian | Blackwater Bar | rebedding the storm glass | a gale |
| Wednesday | Clementine | Thimble Reef | overhauling the foghorn | sleet |
| Thursday | Hollis | Gannet Rock | splicing the hoist rope | hail |
| Friday | Barnaby | Pelter Head | regrinding the lens | sea fog |

## How it falls out

1. [direct] from clue 3 light:Siren Shoal: ruled out position(s) 2,3,4,5
2. [bijection] from clue 11 keeper:Saoirse: ruled out position(s) 2
3. [bijection] from clue 11 weather:sleet: ruled out position(s) 2
4. [bijection] from clue 10 keeper:Lucian: ruled out position(s) 1
5. [bijection] from clue 10 weather:hail: ruled out position(s) 1
6. [bijection] light:Thimble Reef: ruled out position(s) 1
7. [bijection] light:Gannet Rock: ruled out position(s) 1
8. [bijection] light:Pelter Head: ruled out position(s) 1
9. [bijection] light:Blackwater Bar: ruled out position(s) 1
10. [order] from clue 9 chore:overhauling the foghorn: ruled out position(s) 1,2,5
11. [order] from clue 6 light:Blackwater Bar: ruled out position(s) 5
12. [order] from clue 6 keeper:Clementine: ruled out position(s) 1,2
13. [order] from clue 5 light:Thimble Reef: ruled out position(s) 5
14. [order] from clue 5 chore:splicing the hoist rope: ruled out position(s) 1,2
15. [order] from clue 4 chore:splicing the hoist rope: ruled out position(s) 3,5
16. [order] from clue 4 weather:sea fog: ruled out position(s) 1,2,3,4
17. [order] from clue 5 light:Thimble Reef: ruled out position(s) 2,4
18. [order] from clue 2 weather:a gale: ruled out position(s) 1,5
19. [order] from clue 1 chore:repainting the gallery: ruled out position(s) 2,3,4,5
20. [bijection] from clue 7 keeper:Barnaby: ruled out position(s) 3
21. [bijection] from clue 7 weather:hail: ruled out position(s) 3
22. [bijection] chore:regrinding the lens: ruled out position(s) 1,4
23. [bijection] chore:rebedding the storm glass: ruled out position(s) 1,4
24. [bijection] chore:overhauling the foghorn: ruled out position(s) 4
25. [bijection] light:Gannet Rock: ruled out position(s) 3
26. [bijection] light:Pelter Head: ruled out position(s) 3
27. [bijection] light:Blackwater Bar: ruled out position(s) 3
28. [bijection] weather:a flat calm: ruled out position(s) 5
29. [bijection] weather:hail: ruled out position(s) 5
30. [bijection] weather:sleet: ruled out position(s) 5
31. [order] from clue 6 keeper:Clementine: ruled out position(s) 4
32. [order] from clue 9 keeper:Lucian: ruled out position(s) 3
33. [bijection] chore:regrinding the lens: ruled out position(s) 3
34. [bijection] chore:rebedding the storm glass: ruled out position(s) 3
35. [disjunction] from clue 8 chore:regrinding the lens: ruled out position(s) 2
36. [order] from clue 12 light:Pelter Head: ruled out position(s) 2,4
37. [order] from clue 9 keeper:Lucian: ruled out position(s) 4,5
38. [order] from clue 2 keeper:Saoirse: ruled out position(s) 4,5
39. [bijection] from clue 10 weather:hail: ruled out position(s) 2
40. [bijection] from clue 7 keeper:Barnaby: ruled out position(s) 4
_... and 17 further steps._

---

<sub>seed `2026172852601` &middot; score 9.1942 &middot; atoms 12 &middot; positives 1 &middot; solved by disjunction</sub>
