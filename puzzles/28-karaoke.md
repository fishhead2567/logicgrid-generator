# Tuesday Night at the Dented Bell

*The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; talent is not.*

**Difficulty** 3/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 6 &nbsp;&nbsp; **id** `c70b56ef8e4b`

## Introduction

There are 5 turns. Each has exactly one slot and one item from every other category below, and within each category every item belongs to a different turn.
- **Running order** (listed in order): slot one, slot two, slot three, slot four and slot five.
- **Singer**: Annalise, Vikram, Caitriona, Deshawn and Bogdan.
- **Song**: a rap performed entirely from memory, a sea shanty, a power ballad, a novelty country number and an eight-minute prog epic.
- **Reception**: a singalong, the landlord cutting the power, scattered applause, one heckler and a request for an encore nobody wanted.
The slots above are listed in order, from slot one to slot five.

## Clues

1. Slot three does not go with a power ballad, but deshawn goes with a power ballad.
2. One heckler goes with a rap performed entirely from memory.
3. Vikram and a novelty country number are exactly two slots apart in slot order. Slot two falls somewhere between Vikram and an eight-minute prog epic in slot order. The landlord cutting the power and slot two are next to each other in slot order, in one order or the other.
4. Scattered applause does not go with Caitriona. Scattered applause's slot is immediately earlier than a novelty country number's slot, with no slot in between. Slot one and a novelty country number are next to each other in slot order, in one order or the other.
5. Bogdan and slot five are exactly three slots apart in slot order.
6. A request for an encore nobody wanted's slot is earlier than slot five.

## Solving chart

*Running order vs Singer*

| | Annalise | Vikram | Caitriona | Deshawn | Bogdan |
|---|---|---|---|---|---|
| **slot one** | | | | | |
| **slot two** | | | | | |
| **slot three** | | | | | |
| **slot four** | | | | | |
| **slot five** | | | | | |

*Running order vs Song*

| | a rap performed entirely from memory | a sea shanty | a power ballad | a novelty country number | an eight-minute prog epic |
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

| | a rap performed entirely from memory | a sea shanty | a power ballad | a novelty country number | an eight-minute prog epic |
|---|---|---|---|---|---|
| **Annalise** | | | | | |
| **Vikram** | | | | | |
| **Caitriona** | | | | | |
| **Deshawn** | | | | | |
| **Bogdan** | | | | | |

*Singer vs Reception*

| | a singalong | the landlord cutting the power | scattered applause | one heckler | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **Annalise** | | | | | |
| **Vikram** | | | | | |
| **Caitriona** | | | | | |
| **Deshawn** | | | | | |
| **Bogdan** | | | | | |

*Song vs Reception*

| | a singalong | the landlord cutting the power | scattered applause | one heckler | a request for an encore nobody wanted |
|---|---|---|---|---|---|
| **a rap performed entirely from memory** | | | | | |
| **a sea shanty** | | | | | |
| **a power ballad** | | | | | |
| **a novelty country number** | | | | | |
| **an eight-minute prog epic** | | | | | |

## Solution

| Running order | Singer | Song | Reception |
|---|---|---|---|
| slot one | Annalise | an eight-minute prog epic | scattered applause |
| slot two | Bogdan | a novelty country number | a request for an encore nobody wanted |
| slot three | Caitriona | a sea shanty | the landlord cutting the power |
| slot four | Vikram | a rap performed entirely from memory | one heckler |
| slot five | Deshawn | a power ballad | a singalong |

## How it falls out

1. [direct] from clue 3 song:a power ballad: ruled out position(s) 3
2. [direct] from clue 10 singer:Deshawn: ruled out position(s) 3
3. [order] from clue 11 reception:scattered applause: ruled out position(s) 5
4. [order] from clue 11 song:a novelty country number: ruled out position(s) 1
5. [order] from clue 7 reception:the landlord cutting the power: ruled out position(s) 2,4,5
6. [order] from clue 6 song:a novelty country number: ruled out position(s) 3,4,5
7. [order] from clue 11 reception:scattered applause: ruled out position(s) 2,3,4
8. [order] from clue 5 singer:Vikram: ruled out position(s) 1,2,3,5
9. [order] from clue 4 song:an eight-minute prog epic: ruled out position(s) 2,3,4,5
10. [order] from clue 2 reception:a request for an encore nobody wanted: ruled out position(s) 5
11. [order] from clue 1 singer:Bogdan: ruled out position(s) 1,3,4,5
12. [direct] from clue 9 singer:Caitriona: ruled out position(s) 1
13. [bijection] reception:a singalong: ruled out position(s) 1
14. [bijection] reception:the landlord cutting the power: ruled out position(s) 1
15. [bijection] reception:one heckler: ruled out position(s) 1
16. [bijection] reception:a request for an encore nobody wanted: ruled out position(s) 1
17. [bijection] singer:Annalise: ruled out position(s) 2,4
18. [bijection] singer:Caitriona: ruled out position(s) 2,4
19. [bijection] singer:Deshawn: ruled out position(s) 2,4
20. [bijection] song:a rap performed entirely from memory: ruled out position(s) 1,2
21. [bijection] song:a sea shanty: ruled out position(s) 1,2
22. [bijection] song:a power ballad: ruled out position(s) 1,2
23. [direct] from clue 10 singer:Deshawn: ruled out position(s) 1
24. [direct] from clue 10 song:a power ballad: ruled out position(s) 4
25. [direct] from clue 8 reception:one heckler: ruled out position(s) 2
26. [bijection] reception:a singalong: ruled out position(s) 3
27. [bijection] reception:one heckler: ruled out position(s) 3
28. [bijection] reception:a request for an encore nobody wanted: ruled out position(s) 3
29. [bijection] singer:Annalise: ruled out position(s) 5
30. [bijection] singer:Caitriona: ruled out position(s) 5
31. [bijection] singer:Annalise: ruled out position(s) 3
32. [bijection] song:a rap performed entirely from memory: ruled out position(s) 5
33. [bijection] song:a sea shanty: ruled out position(s) 5
34. [direct] from clue 8 reception:one heckler: ruled out position(s) 5
35. [direct] from clue 8 song:a rap performed entirely from memory: ruled out position(s) 3
36. [bijection] reception:a singalong: ruled out position(s) 4
37. [bijection] reception:a request for an encore nobody wanted: ruled out position(s) 4
38. [bijection] reception:a singalong: ruled out position(s) 2
39. [bijection] song:a sea shanty: ruled out position(s) 4

---

<sub>seed `2026172797168` &middot; score 5.355 &middot; atoms 11 &middot; positives 2 &middot; solved by order</sub>
