# Tuesday Night at the Dented Bell

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 12 &nbsp;&nbsp; **id** `436ea20afeef`

## Introduction

The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; talent is not.
Five singers are involved. Determine each singer's slot, song and reception.
- **Singer**: Vikram, Annalise, Mercy, Caitriona and Deshawn.
- **Running order** (listed from earlier to later): slot one, slot two, slot three, slot four and slot five.
- **Song**: a power ballad, a rap performed entirely from memory, a sea shanty, a novelty country number and an eight-minute prog epic.
- **Reception**: a singalong, the landlord cutting the power, scattered applause, one heckler and a request for an encore nobody wanted.
Every singer has a different slot, song and reception, so within each category every item is used exactly once.

## Clues

1. Deshawn sings in slot two.
2. The singer who gets scattered applause and slot four are exactly three slots apart in slot order.
3. The singer who performs an eight-minute prog epic and slot two are exactly one slot apart in slot order, in one direction or the other.
4. The singer who performs a rap performed entirely from memory and slot five are exactly two slots apart in slot order.
5. The singer who performs a power ballad falls somewhere between the singer who gets a singalong and slot two in slot order.
6. Slot four is exactly one slot earlier than Caitriona, with no slot in between.
7. One of the singer who gets scattered applause and Annalise sits at an odd-numbered slot and the other at an even-numbered slot.
8. Deshawn falls somewhere between the singer who performs a sea shanty and the singer who performs an eight-minute prog epic in slot order.
9. The singer who gets a request for an encore nobody wanted does not perform a rap performed entirely from memory.
10. The singer who gets one heckler and the singer who performs a rap performed entirely from memory are exactly one slot apart in slot order, in one direction or the other.
11. Vikram does not perform a rap performed entirely from memory.
12. Deshawn is earlier than the singer who gets one heckler in slot order.

## Solving chart

*Running order vs Singer*

| | Vikram | Annalise | Mercy | Caitriona | Deshawn |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Song*

| | a power ballad | a rap performed entirely from memory | a sea shanty | a novelty country number | an eight-minute prog epic |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Reception*

| | a singalong | the landlord cutting the power | scattered applause | one heckler | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Singer vs Song*

| | a power ballad | a rap performed entirely from memory | a sea shanty | a novelty country number | an eight-minute prog epic |
|---|---|---|---|---|---|
| **Vikram** | | | | | |
| **Annalise** | | | | | |
| **Mercy** | | | | | |
| **Caitriona** | | | | | |
| **Deshawn** | | | | | |

*Singer vs Reception*

| | a singalong | the landlord cutting the power | scattered applause | one heckler | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **Vikram** | | | | | |
| **Annalise** | | | | | |
| **Mercy** | | | | | |
| **Caitriona** | | | | | |
| **Deshawn** | | | | | |

*Song vs Reception*

| | a singalong | the landlord cutting the power | scattered applause | one heckler | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **a power ballad** | | | | | |
| **a rap performed entirely from memory** | | | | | |
| **a sea shanty** | | | | | |
| **a novelty country number** | | | | | |
| **an eight-minute prog epic** | | | | | |

## Solution

| Running order | Singer | Song | Reception |
|---|---|---|---|
| slot one | Vikram | an eight-minute prog epic | scattered applause |
| slot two | Deshawn | a novelty country number | a request for an encore nobody wanted |
| slot three | Mercy | a rap performed entirely from memory | the landlord cutting the power |
| slot four | Annalise | a power ballad | one heckler |
| slot five | Caitriona | a sea shanty | a singalong |

## How it falls out

1. [direct] from clue 6 singer:Deshawn: ruled out position(s) 1,3,4,5
2. [bijection] singer:Vikram: ruled out position(s) 2
3. [bijection] singer:Annalise: ruled out position(s) 2
4. [bijection] singer:Mercy: ruled out position(s) 2
5. [bijection] singer:Caitriona: ruled out position(s) 2
6. [order] from clue 11 singer:Caitriona: ruled out position(s) 1,3,4
7. [order] from clue 10 reception:scattered applause: ruled out position(s) 2,3,4,5
8. [order] from clue 9 song:a power ballad: ruled out position(s) 1,2,5
9. [order] from clue 9 reception:a singalong: ruled out position(s) 1,2,3
10. [order] from clue 8 reception:one heckler: ruled out position(s) 1,2
11. [order] from clue 12 song:a rap performed entirely from memory: ruled out position(s) 1
12. [order] from clue 7 singer:Annalise: ruled out position(s) 1,3,5
13. [order] from clue 5 song:a rap performed entirely from memory: ruled out position(s) 2,4,5
14. [order] from clue 12 reception:one heckler: ruled out position(s) 3,5
15. [order] from clue 2 song:an eight-minute prog epic: ruled out position(s) 2,4,5
16. [order] from clue 1 song:a sea shanty: ruled out position(s) 2
17. [direct] from clue 4 singer:Vikram: ruled out position(s) 3
18. [direct] from clue 3 reception:a request for an encore nobody wanted: ruled out position(s) 3
19. [bijection] reception:a singalong: ruled out position(s) 4
20. [bijection] reception:the landlord cutting the power: ruled out position(s) 1,4
21. [bijection] reception:a request for an encore nobody wanted: ruled out position(s) 1,4
22. [bijection] reception:the landlord cutting the power: ruled out position(s) 2,5
23. [bijection] singer:Vikram: ruled out position(s) 4,5
24. [bijection] singer:Mercy: ruled out position(s) 4,5
25. [bijection] singer:Mercy: ruled out position(s) 1
26. [bijection] song:a power ballad: ruled out position(s) 3
27. [bijection] song:a sea shanty: ruled out position(s) 3
28. [bijection] song:a novelty country number: ruled out position(s) 3
29. [bijection] song:an eight-minute prog epic: ruled out position(s) 3
30. [bijection] song:a novelty country number: ruled out position(s) 1,4,5
31. [order] from clue 1 song:a sea shanty: ruled out position(s) 1
32. [bijection] reception:a request for an encore nobody wanted: ruled out position(s) 5
33. [bijection] song:a sea shanty: ruled out position(s) 4

---

<sub>seed `2026172797168` &middot; score 5.515 &middot; atoms 12 &middot; positives 1 &middot; solved by order</sub>
