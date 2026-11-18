# Tuesday Night at the Dented Bell

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 8 &nbsp;&nbsp; **id** `3461a7266d47`

## Introduction

The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; talent is not.
Five singers are involved. Determine each singer's slot, song and reception.
- **Singer**: Deshawn, Annalise, Vikram, Bogdan and Pernilla.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Song**: a maudlin folk song, a disco standard, an eight-minute prog epic, a sea shanty and a power ballad.
- **Reception**: a standing ovation, the landlord cutting the power, polite silence, a request for an encore nobody wanted and one heckler.
Every singer has a different slot, song and reception, so within each category every item is used exactly once.

## Clues

1. Bogdan gets polite silence. The singer who performs an eight-minute prog epic is earlier than the singer who gets polite silence in slot order.
2. Slot four falls somewhere between the singer who gets a request for an encore nobody wanted and the singer who performs a disco standard in slot order.
3. The singer who performs a power ballad falls somewhere between the singer who gets a request for an encore nobody wanted and slot two in slot order.
4. Slot two falls somewhere between the singer who gets one heckler and Annalise in slot order.
5. The singer who performs a sea shanty does not sing in slot five.
6. The singer who gets a standing ovation and Pernilla are exactly two slots apart in slot order.
7. Vikram is earlier than the singer who performs an eight-minute prog epic in slot order.
8. Annalise falls somewhere between the singer who gets one heckler and the singer who performs a sea shanty in slot order.

## Solving chart

*Running order vs Singer*

| | Deshawn | Annalise | Vikram | Bogdan | Pernilla |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Song*

| | a maudlin folk song | a disco standard | an eight-minute prog epic | a sea shanty | a power ballad |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Reception*

| | a standing ovation | the landlord cutting the power | polite silence | a request for an encore nobody wanted | one heckler |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Singer vs Song*

| | a maudlin folk song | a disco standard | an eight-minute prog epic | a sea shanty | a power ballad |
|---|---|---|---|---|---|
| **Deshawn** | | | | | |
| **Annalise** | | | | | |
| **Vikram** | | | | | |
| **Bogdan** | | | | | |
| **Pernilla** | | | | | |

*Singer vs Reception*

| | a standing ovation | the landlord cutting the power | polite silence | a request for an encore nobody wanted | one heckler |
|---|---|---|---|---|---|
| **Deshawn** | | | | | |
| **Annalise** | | | | | |
| **Vikram** | | | | | |
| **Bogdan** | | | | | |
| **Pernilla** | | | | | |

*Song vs Reception*

| | a standing ovation | the landlord cutting the power | polite silence | a request for an encore nobody wanted | one heckler |
|---|---|---|---|---|---|
| **a maudlin folk song** | | | | | |
| **a disco standard** | | | | | |
| **an eight-minute prog epic** | | | | | |
| **a sea shanty** | | | | | |
| **a power ballad** | | | | | |

## Solution

| Running order | Singer | Song | Reception |
|---|---|---|---|
| slot one | Vikram | a disco standard | one heckler |
| slot two | Deshawn | an eight-minute prog epic | the landlord cutting the power |
| slot three | Annalise | a power ballad | a standing ovation |
| slot four | Bogdan | a sea shanty | polite silence |
| slot five | Pernilla | a maudlin folk song | a request for an encore nobody wanted |

## How it falls out

1. [direct] from clue 1 song:a sea shanty: ruled out position(s) 5
2. [order] from clue 9 reception:a request for an encore nobody wanted: ruled out position(s) 4
3. [order] from clue 9 song:a disco standard: ruled out position(s) 4
4. [order] from clue 8 song:a power ballad: ruled out position(s) 1,2,5
5. [order] from clue 8 reception:a request for an encore nobody wanted: ruled out position(s) 1,2,3
6. [order] from clue 9 song:a disco standard: ruled out position(s) 5
7. [order] from clue 5 song:an eight-minute prog epic: ruled out position(s) 5
8. [order] from clue 5 reception:polite silence: ruled out position(s) 1
9. [order] from clue 4 singer:Annalise: ruled out position(s) 1,5
10. [order] from clue 3 singer:Vikram: ruled out position(s) 4,5
11. [order] from clue 3 song:an eight-minute prog epic: ruled out position(s) 1
12. [order] from clue 5 reception:polite silence: ruled out position(s) 2
13. [order] from clue 2 reception:one heckler: ruled out position(s) 2,3,4,5
14. [order] from clue 2 singer:Annalise: ruled out position(s) 2
15. [order] from clue 4 singer:Annalise: ruled out position(s) 4
16. [order] from clue 4 song:a sea shanty: ruled out position(s) 1,2,3
17. [direct] from clue 6 singer:Bogdan: ruled out position(s) 1,2
18. [bijection] reception:a standing ovation: ruled out position(s) 1,5
19. [bijection] reception:the landlord cutting the power: ruled out position(s) 1,5
20. [bijection] reception:polite silence: ruled out position(s) 5
21. [bijection] singer:Deshawn: ruled out position(s) 3
22. [bijection] singer:Vikram: ruled out position(s) 3
23. [bijection] singer:Bogdan: ruled out position(s) 3
24. [bijection] singer:Pernilla: ruled out position(s) 3
25. [bijection] song:a maudlin folk song: ruled out position(s) 4
26. [bijection] song:an eight-minute prog epic: ruled out position(s) 4
27. [bijection] song:a power ballad: ruled out position(s) 4
28. [bijection] song:a maudlin folk song: ruled out position(s) 1,2,3
29. [direct] from clue 6 reception:polite silence: ruled out position(s) 3
30. [direct] from clue 6 singer:Bogdan: ruled out position(s) 5
31. [bijection] reception:a standing ovation: ruled out position(s) 4
32. [bijection] reception:the landlord cutting the power: ruled out position(s) 4
33. [bijection] singer:Deshawn: ruled out position(s) 4
34. [bijection] singer:Pernilla: ruled out position(s) 4
35. [bijection] song:a disco standard: ruled out position(s) 3
36. [bijection] song:an eight-minute prog epic: ruled out position(s) 3
37. [bijection] song:a disco standard: ruled out position(s) 2
38. [order] from clue 3 singer:Vikram: ruled out position(s) 2
39. [order] from clue 7 reception:a standing ovation: ruled out position(s) 2
40. [order] from clue 7 singer:Pernilla: ruled out position(s) 2
_... and 4 further steps._

---

<sub>seed `2026172757573` &middot; score 5.515 &middot; atoms 9 &middot; positives 1 &middot; solved by order</sub>
