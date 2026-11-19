# A Bad Week at the Pinhole Observatory

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 10 &nbsp;&nbsp; **id** `95aadb73d784`

## Introduction

The Pinhole Amateur Astronomical Society has one good telescope and a great many strong opinions about who may point it where.
Five astronomers are involved. Determine each astronomer's day, target and mishap.
- **Astronomer**: Cornelius, Niamh, Sunniva, Dmitri and Ptolemy.
- **Day** (listed from earlier to later): Monday, Tuesday, Wednesday, Thursday and Friday.
- **Observed**: a lunar occultation, Saturn's rings, a comet fragment, the Andromeda galaxy and the Crab Nebula.
- **Mishap**: a flat battery, a cracked filter, a dropped lens cap, a dewed-up eyepiece and an unexpected cloud bank.
Every astronomer has a different day, target and mishap, so within each category every item is used exactly once.

## Clues

1. The astronomer who is undone by a dewed-up eyepiece does not study the Andromeda galaxy. The astronomer who studies the Andromeda galaxy observes on Tuesday.
2. The astronomer who is undone by a flat battery is earlier than Tuesday in day order.
3. The astronomer who studies a comet fragment and Tuesday are exactly one day apart in day order, in one direction or the other.
4. Niamh is exactly one day earlier than Tuesday, with no day in between.
5. The astronomer who studies a lunar occultation is later than Thursday in day order.
6. Thursday falls somewhere between the astronomer who is undone by a cracked filter and the astronomer who is undone by a dropped lens cap in day order.
7. Ptolemy and the astronomer who is undone by a dropped lens cap are exactly two days apart in day order.
8. The astronomer who is undone by a dropped lens cap falls somewhere between the astronomer who studies a lunar occultation and the astronomer who studies the Crab Nebula in day order.
9. Cornelius and the astronomer who studies a comet fragment are exactly one day apart in day order, in one direction or the other.
10. Dmitri and the astronomer who is undone by a cracked filter are exactly one day apart in day order, in one direction or the other.

## Solving chart

*Day vs Astronomer*

| | Cornelius | Niamh | Sunniva | Dmitri | Ptolemy |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Observed*

| | a lunar occultation | Saturn's rings | a comet fragment | the Andromeda galaxy | the Crab Nebula |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Day vs Mishap*

| | a flat battery | a cracked filter | a dropped lens cap | a dewed-up eyepiece | an unexpected cloud bank |
|---|---|---|---|---|---|
| **Monday** | | | | | |
| **Tuesday** | | | | | |
| **Wednesday** | | | | | |
| **Thursday** | | | | | |
| **Friday** | | | | | |

*Astronomer vs Observed*

| | a lunar occultation | Saturn's rings | a comet fragment | the Andromeda galaxy | the Crab Nebula |
|---|---|---|---|---|---|
| **Cornelius** | | | | | |
| **Niamh** | | | | | |
| **Sunniva** | | | | | |
| **Dmitri** | | | | | |
| **Ptolemy** | | | | | |

*Astronomer vs Mishap*

| | a flat battery | a cracked filter | a dropped lens cap | a dewed-up eyepiece | an unexpected cloud bank |
|---|---|---|---|---|---|
| **Cornelius** | | | | | |
| **Niamh** | | | | | |
| **Sunniva** | | | | | |
| **Dmitri** | | | | | |
| **Ptolemy** | | | | | |

*Observed vs Mishap*

| | a flat battery | a cracked filter | a dropped lens cap | a dewed-up eyepiece | an unexpected cloud bank |
|---|---|---|---|---|---|
| **a lunar occultation** | | | | | |
| **Saturn's rings** | | | | | |
| **a comet fragment** | | | | | |
| **the Andromeda galaxy** | | | | | |
| **the Crab Nebula** | | | | | |

## Solution

| Day | Astronomer | Observed | Mishap |
|---|---|---|---|
| Monday | Niamh | the Crab Nebula | a flat battery |
| Tuesday | Cornelius | the Andromeda galaxy | an unexpected cloud bank |
| Wednesday | Sunniva | a comet fragment | a dropped lens cap |
| Thursday | Dmitri | Saturn's rings | a dewed-up eyepiece |
| Friday | Ptolemy | a lunar occultation | a cracked filter |

## How it falls out

1. [direct] from clue 3 target:the Andromeda galaxy: ruled out position(s) 1,3,4,5
2. [direct] from clue 7 mishap:a dewed-up eyepiece: ruled out position(s) 2
3. [bijection] target:a lunar occultation: ruled out position(s) 2
4. [bijection] target:Saturn's rings: ruled out position(s) 2
5. [bijection] target:a comet fragment: ruled out position(s) 2
6. [bijection] target:the Crab Nebula: ruled out position(s) 2
7. [order] from clue 11 mishap:a dropped lens cap: ruled out position(s) 1,5
8. [order] from clue 10 target:a comet fragment: ruled out position(s) 4,5
9. [order] from clue 9 mishap:a cracked filter: ruled out position(s) 1,2,3,4
10. [order] from clue 9 mishap:a dropped lens cap: ruled out position(s) 4
11. [order] from clue 8 target:a lunar occultation: ruled out position(s) 1,3,4
12. [order] from clue 11 target:the Crab Nebula: ruled out position(s) 3,4,5
13. [order] from clue 6 astronomer:Dmitri: ruled out position(s) 1,2,3,5
14. [order] from clue 5 astronomer:Niamh: ruled out position(s) 2,3,4,5
15. [order] from clue 4 astronomer:Ptolemy: ruled out position(s) 2,3
16. [order] from clue 2 astronomer:Cornelius: ruled out position(s) 1,3,5
17. [order] from clue 1 mishap:a flat battery: ruled out position(s) 2,3,4,5
18. [bijection] astronomer:Cornelius: ruled out position(s) 4
19. [bijection] astronomer:Sunniva: ruled out position(s) 1,4
20. [bijection] astronomer:Ptolemy: ruled out position(s) 1,4
21. [bijection] astronomer:Sunniva: ruled out position(s) 2,5
22. [bijection] mishap:a dewed-up eyepiece: ruled out position(s) 1,5
23. [bijection] mishap:an unexpected cloud bank: ruled out position(s) 1,5
24. [bijection] target:Saturn's rings: ruled out position(s) 1,5
25. [bijection] target:a comet fragment: ruled out position(s) 1
26. [bijection] target:Saturn's rings: ruled out position(s) 3
27. [order] from clue 4 mishap:a dropped lens cap: ruled out position(s) 2
28. [bijection] mishap:a dewed-up eyepiece: ruled out position(s) 3
29. [bijection] mishap:an unexpected cloud bank: ruled out position(s) 3
30. [bijection] mishap:an unexpected cloud bank: ruled out position(s) 4

---

<sub>seed `2026172889252` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
