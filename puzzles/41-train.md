# The Loft Layout Dispute

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `9a786ef7d7be`

## Introduction

The members of the model railway society share one loft layout and a deep well of resentment.
Five modellers are involved. Determine each modeller's shelf, scenery and grievance.
- **Modeller**: Rosamond, Esperanza, Hendrik, Gilbert and Abiodun.
- **Shelf** (listed from lower to higher): the bottom shelf, the second shelf, the third shelf, the fourth shelf and the fifth shelf.
- **Scenery**: a working level crossing, a sheet of static grass, a flocked cutting, a river of resin and a coal staithe.
- **Grievance**: the timetable, the wiring, somebody else's couplings, a missing screwdriver and the lighting.
Every modeller has a different shelf, scenery and grievance, so within each category every item is used exactly once.

## Clues

1. Esperanza complains about somebody else's couplings.
2. The modeller who builds a coal staithe and the fourth shelf are exactly one shelf apart in shelf order, in one direction or the other.
3. The modeller who complains about the timetable and the fifth shelf are exactly one shelf apart in shelf order, in one direction or the other.
4. The fourth shelf falls somewhere between the modeller who builds a river of resin and the modeller who builds a sheet of static grass in shelf order.
5. Abiodun is exactly one shelf lower than the third shelf, with no shelf in between.
6. At least one of the following holds, and possibly more than one: (a) The modeller who builds a river of resin stores on the bottom shelf. (b) One of Gilbert and the modeller who builds a coal staithe sits at an odd-numbered shelf and the other at an even-numbered shelf.
7. Rosamond does not build a working level crossing. One of Abiodun and the modeller who builds a working level crossing sits at an odd-numbered shelf and the other at an even-numbered shelf.
8. The modeller who complains about a missing screwdriver does not build a sheet of static grass.
9. The modeller who complains about somebody else's couplings is lower than the modeller who builds a sheet of static grass in shelf order.
10. The modeller who complains about the wiring is exactly one shelf lower than Abiodun, with no shelf in between.

## Solving chart

*Shelf vs Modeller*

| | Rosamond | Esperanza | Hendrik | Gilbert | Abiodun |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Scenery*

| | a working level crossing | a sheet of static grass | a flocked cutting | a river of resin | a coal staithe |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Shelf vs Grievance*

| | the timetable | the wiring | somebody else's couplings | a missing screwdriver | the lighting |
|---|---|---|---|---|---|
| **the bottom shelf** | | | | | |
| **the second shelf** | | | | | |
| **the third shelf** | | | | | |
| **the fourth shelf** | | | | | |
| **the fifth shelf** | | | | | |

*Modeller vs Scenery*

| | a working level crossing | a sheet of static grass | a flocked cutting | a river of resin | a coal staithe |
|---|---|---|---|---|---|
| **Rosamond** | | | | | |
| **Esperanza** | | | | | |
| **Hendrik** | | | | | |
| **Gilbert** | | | | | |
| **Abiodun** | | | | | |

*Modeller vs Grievance*

| | the timetable | the wiring | somebody else's couplings | a missing screwdriver | the lighting |
|---|---|---|---|---|---|
| **Rosamond** | | | | | |
| **Esperanza** | | | | | |
| **Hendrik** | | | | | |
| **Gilbert** | | | | | |
| **Abiodun** | | | | | |

*Scenery vs Grievance*

| | the timetable | the wiring | somebody else's couplings | a missing screwdriver | the lighting |
|---|---|---|---|---|---|
| **a working level crossing** | | | | | |
| **a sheet of static grass** | | | | | |
| **a flocked cutting** | | | | | |
| **a river of resin** | | | | | |
| **a coal staithe** | | | | | |

## Solution

| Shelf | Modeller | Scenery | Grievance |
|---|---|---|---|
| the bottom shelf | Hendrik | a working level crossing | the wiring |
| the second shelf | Abiodun | a river of resin | a missing screwdriver |
| the third shelf | Esperanza | a coal staithe | somebody else's couplings |
| the fourth shelf | Gilbert | a flocked cutting | the timetable |
| the fifth shelf | Rosamond | a sheet of static grass | the lighting |

## How it falls out

1. [order] from clue 9 grievance:the wiring: ruled out position(s) 5
2. [order] from clue 9 modeller:Abiodun: ruled out position(s) 1
3. [order] from clue 7 scenery:a river of resin: ruled out position(s) 4
4. [order] from clue 7 scenery:a sheet of static grass: ruled out position(s) 4
5. [order] from clue 5 scenery:a coal staithe: ruled out position(s) 1,2,4
6. [order] from clue 4 grievance:the timetable: ruled out position(s) 1,2,3,5
7. [order] from clue 3 grievance:somebody else's couplings: ruled out position(s) 5
8. [order] from clue 3 scenery:a sheet of static grass: ruled out position(s) 1
9. [order] from clue 2 modeller:Abiodun: ruled out position(s) 3,4,5
10. [order] from clue 9 grievance:the wiring: ruled out position(s) 2,3,4
11. [order] from clue 6 scenery:a working level crossing: ruled out position(s) 2,4
12. [direct] from clue 1 modeller:Esperanza: ruled out position(s) 5
13. [bijection] grievance:somebody else's couplings: ruled out position(s) 1,4
14. [bijection] grievance:a missing screwdriver: ruled out position(s) 1,4
15. [bijection] grievance:the lighting: ruled out position(s) 1,4
16. [bijection] modeller:Rosamond: ruled out position(s) 2
17. [bijection] modeller:Esperanza: ruled out position(s) 2
18. [bijection] modeller:Hendrik: ruled out position(s) 2
19. [bijection] modeller:Gilbert: ruled out position(s) 2
20. [bijection] scenery:a flocked cutting: ruled out position(s) 1,2,3,5
21. [order] from clue 3 scenery:a sheet of static grass: ruled out position(s) 2
22. [direct] from clue 1 grievance:somebody else's couplings: ruled out position(s) 2
23. [direct] from clue 1 modeller:Esperanza: ruled out position(s) 1,4
24. [order] from clue 3 scenery:a sheet of static grass: ruled out position(s) 3
25. [direct] from clue 11 grievance:a missing screwdriver: ruled out position(s) 5
26. [order] from clue 7 scenery:a river of resin: ruled out position(s) 5
27. [bijection] grievance:a missing screwdriver: ruled out position(s) 3
28. [bijection] grievance:the lighting: ruled out position(s) 3
29. [bijection] grievance:the lighting: ruled out position(s) 2
30. [bijection] modeller:Rosamond: ruled out position(s) 3
31. [bijection] modeller:Hendrik: ruled out position(s) 3
32. [bijection] modeller:Gilbert: ruled out position(s) 3
33. [bijection] scenery:a working level crossing: ruled out position(s) 5
34. [bijection] scenery:a coal staithe: ruled out position(s) 5
35. [bijection] scenery:a river of resin: ruled out position(s) 1,3
36. [bijection] scenery:a working level crossing: ruled out position(s) 3
37. [direct] from clue 10 modeller:Rosamond: ruled out position(s) 1
38. [disjunction] from clue 8 modeller:Gilbert: ruled out position(s) 1,5
39. [bijection] modeller:Rosamond: ruled out position(s) 4
40. [bijection] modeller:Hendrik: ruled out position(s) 4
_... and 1 further steps._

---

<sub>seed `2026173004844` &middot; score 8.5792 &middot; atoms 11 &middot; positives 1 &middot; solved by disjunction</sub>
