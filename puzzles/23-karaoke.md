# Tuesday Night at the Dented Bell

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 9 &nbsp;&nbsp; **id** `3461a7266d47`

## Introduction

The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; talent is not.
Five singers are involved. Determine each singer's slot, song and reception.
- **Singer**: Deshawn, Annalise, Vikram, Bogdan and Pernilla.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Song**: a maudlin folk song, a disco standard, an eight-minute prog epic, a sea shanty and a power ballad.
- **Reception**: a standing ovation, the landlord cutting the power, polite silence, a request for an encore nobody wanted and one heckler.
Every singer has a different slot, song and reception, so within each category every item is used exactly once.

## Clues

1. Slot two is exactly one slot earlier than the singer who performs a power ballad, with no slot in between. The singer who gets a standing ovation does not sing in slot two.
2. Slot four falls somewhere between Pernilla and the singer who performs an eight-minute prog epic in slot order.
3. Annalise does not sing in slot one.
4. Deshawn is later than slot one in slot order.
5. The singer who gets polite silence and slot five are exactly one slot apart in slot order, in one direction or the other.
6. The singer who gets the landlord cutting the power falls somewhere between slot one and the singer who performs a sea shanty in slot order.
7. Deshawn is earlier than the singer who performs a power ballad in slot order.
8. The singer who gets a request for an encore nobody wanted and the singer who performs an eight-minute prog epic are exactly three slots apart in slot order.
9. The singer who gets one heckler and Bogdan are exactly three slots apart in slot order. Bogdan is earlier than the singer who performs a maudlin folk song in slot order.

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

1. [direct] from clue 9 singer:Annalise: ruled out position(s) 1
2. [direct] from clue 1 reception:a standing ovation: ruled out position(s) 2
3. [order] from clue 11 reception:a request for an encore nobody wanted: ruled out position(s) 3
4. [order] from clue 11 song:an eight-minute prog epic: ruled out position(s) 3
5. [order] from clue 10 reception:the landlord cutting the power: ruled out position(s) 1,5
6. [order] from clue 10 song:a sea shanty: ruled out position(s) 1,2
7. [order] from clue 8 song:a power ballad: ruled out position(s) 1,2,4,5
8. [order] from clue 7 singer:Bogdan: ruled out position(s) 5
9. [order] from clue 7 song:a maudlin folk song: ruled out position(s) 1
10. [order] from clue 6 singer:Deshawn: ruled out position(s) 1
11. [order] from clue 5 reception:one heckler: ruled out position(s) 2,3
12. [order] from clue 5 singer:Bogdan: ruled out position(s) 3
13. [order] from clue 4 reception:polite silence: ruled out position(s) 1,2,3,5
14. [order] from clue 3 singer:Deshawn: ruled out position(s) 3,4,5
15. [order] from clue 2 singer:Pernilla: ruled out position(s) 4
16. [order] from clue 2 song:an eight-minute prog epic: ruled out position(s) 4
17. [order] from clue 11 reception:a request for an encore nobody wanted: ruled out position(s) 1
18. [bijection] reception:a standing ovation: ruled out position(s) 4
19. [bijection] reception:the landlord cutting the power: ruled out position(s) 4
20. [bijection] reception:a request for an encore nobody wanted: ruled out position(s) 4
21. [bijection] reception:one heckler: ruled out position(s) 4
22. [bijection] singer:Annalise: ruled out position(s) 2
23. [bijection] singer:Vikram: ruled out position(s) 2
24. [bijection] singer:Bogdan: ruled out position(s) 2
25. [bijection] singer:Pernilla: ruled out position(s) 2
26. [bijection] song:a maudlin folk song: ruled out position(s) 3
27. [bijection] song:a disco standard: ruled out position(s) 3
28. [bijection] song:a sea shanty: ruled out position(s) 3
29. [order] from clue 5 reception:one heckler: ruled out position(s) 5
30. [order] from clue 5 singer:Bogdan: ruled out position(s) 1
31. [order] from clue 7 song:a maudlin folk song: ruled out position(s) 2,4
32. [order] from clue 11 song:an eight-minute prog epic: ruled out position(s) 1
33. [bijection] reception:a standing ovation: ruled out position(s) 1
34. [bijection] singer:Annalise: ruled out position(s) 4
35. [bijection] singer:Vikram: ruled out position(s) 4
36. [bijection] song:a disco standard: ruled out position(s) 5
37. [bijection] song:an eight-minute prog epic: ruled out position(s) 5
38. [bijection] song:a sea shanty: ruled out position(s) 5
39. [bijection] song:a disco standard: ruled out position(s) 2,4
40. [order] from clue 11 reception:a request for an encore nobody wanted: ruled out position(s) 2
_... and 6 further steps._

---

<sub>seed `2026172757573` &middot; score 5.675 &middot; atoms 11 &middot; positives 0 &middot; solved by order</sub>
