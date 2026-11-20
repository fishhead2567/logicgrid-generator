# The Quarter-Peal at St Botolph's

**Difficulty** 4/7 (moderate) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 11 &nbsp;&nbsp; **id** `2da77c3fe4bf`

## Introduction

The Tuesday practice, and a tower captain keeping a ledger of everyone's mistakes.
Five ringers are involved. Determine each ringer's round, method and bell.
- **Ringer**: Fenwick, Lavinia, Ambrose, Osbert and Prudence.
- **Round** (listed from earlier to later): round one, round two, round three, round four and round five.
- **Method**: Plain Bob Major, Grandsire Triples, Kent Treble Bob, Grandsire Doubles and Plain Bob Minor.
- **Bell**: the sharp second, the third, the fifth, the tenor and the second.
Every ringer has a different round, method and bell, so within each category every item is used exactly once.

## Clues

1. Prudence calls Grandsire Triples.
2. The ringer who takes the third and round four are exactly one round apart in round order, in one direction or the other.
3. Fenwick is later than round four in round order.
4. The ringer who calls Grandsire Triples does not ring in round four.
5. The ringer who takes the fifth is exactly one round earlier than round two, with no round in between.
6. Osbert is earlier than the ringer who takes the second in round order.
7. The ringer who calls Kent Treble Bob and Lavinia both sit at odd-numbered rounds or both at even-numbered rounds.
8. The ringer who takes the second falls somewhere between the ringer who calls Grandsire Triples and the ringer who calls Plain Bob Minor in round order.
9. The ringer who takes the third and the ringer who calls Grandsire Triples are exactly one round apart in round order, in one direction or the other.
10. The ringer who takes the sharp second falls somewhere between the ringer who calls Kent Treble Bob and the ringer who calls Plain Bob Minor in round order.
11. The ringer who calls Plain Bob Major and Lavinia are exactly one round apart in round order, in one direction or the other.

## Solving chart

*Round vs Ringer*

| | Fenwick | Lavinia | Ambrose | Osbert | Prudence |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Round vs Method*

| | Plain Bob Major | Grandsire Triples | Kent Treble Bob | Grandsire Doubles | Plain Bob Minor |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Round vs Bell*

| | the sharp second | the third | the fifth | the tenor | the second |
|---|---|---|---|---|---|
| **round one** | | | | | |
| **round two** | | | | | |
| **round three** | | | | | |
| **round four** | | | | | |
| **round five** | | | | | |

*Ringer vs Method*

| | Plain Bob Major | Grandsire Triples | Kent Treble Bob | Grandsire Doubles | Plain Bob Minor |
|---|---|---|---|---|---|
| **Fenwick** | | | | | |
| **Lavinia** | | | | | |
| **Ambrose** | | | | | |
| **Osbert** | | | | | |
| **Prudence** | | | | | |

*Ringer vs Bell*

| | the sharp second | the third | the fifth | the tenor | the second |
|---|---|---|---|---|---|
| **Fenwick** | | | | | |
| **Lavinia** | | | | | |
| **Ambrose** | | | | | |
| **Osbert** | | | | | |
| **Prudence** | | | | | |

*Method vs Bell*

| | the sharp second | the third | the fifth | the tenor | the second |
|---|---|---|---|---|---|
| **Plain Bob Major** | | | | | |
| **Grandsire Triples** | | | | | |
| **Kent Treble Bob** | | | | | |
| **Grandsire Doubles** | | | | | |
| **Plain Bob Minor** | | | | | |

## Solution

| Round | Ringer | Method | Bell |
|---|---|---|---|
| round one | Osbert | Kent Treble Bob | the fifth |
| round two | Prudence | Grandsire Triples | the sharp second |
| round three | Lavinia | Grandsire Doubles | the third |
| round four | Ambrose | Plain Bob Major | the second |
| round five | Fenwick | Plain Bob Minor | the tenor |

## How it falls out

1. [direct] from clue 3 method:Grandsire Triples: ruled out position(s) 4
2. [direct] from clue 7 ringer:Prudence: ruled out position(s) 4
3. [order] from clue 10 bell:the second: ruled out position(s) 1,5
4. [order] from clue 9 bell:the sharp second: ruled out position(s) 1,5
5. [order] from clue 8 bell:the fifth: ruled out position(s) 2,3,4,5
6. [order] from clue 6 ringer:Osbert: ruled out position(s) 4,5
7. [order] from clue 5 ringer:Fenwick: ruled out position(s) 1,2,3,4
8. [order] from clue 4 bell:the third: ruled out position(s) 1,2,4
9. [order] from clue 1 bell:the third: ruled out position(s) 5
10. [order] from clue 1 method:Grandsire Triples: ruled out position(s) 1,3,5
11. [order] from clue 10 bell:the second: ruled out position(s) 2
12. [order] from clue 10 method:Plain Bob Minor: ruled out position(s) 1,2,3
13. [order] from clue 9 method:Kent Treble Bob: ruled out position(s) 4,5
14. [direct] from clue 7 ringer:Prudence: ruled out position(s) 1,3,5
15. [bijection] bell:the sharp second: ruled out position(s) 3
16. [bijection] bell:the tenor: ruled out position(s) 1,3
17. [bijection] bell:the second: ruled out position(s) 3
18. [bijection] bell:the tenor: ruled out position(s) 2,4
19. [bijection] method:Plain Bob Major: ruled out position(s) 2
20. [bijection] method:Kent Treble Bob: ruled out position(s) 2
21. [bijection] method:Grandsire Doubles: ruled out position(s) 2
22. [bijection] ringer:Lavinia: ruled out position(s) 2,5
23. [bijection] ringer:Ambrose: ruled out position(s) 2,5
24. [bijection] ringer:Osbert: ruled out position(s) 2
25. [order] from clue 11 ringer:Lavinia: ruled out position(s) 4
26. [order] from clue 2 method:Plain Bob Major: ruled out position(s) 1,3,5
27. [order] from clue 2 ringer:Lavinia: ruled out position(s) 1
28. [order] from clue 10 method:Plain Bob Minor: ruled out position(s) 4
29. [bijection] bell:the sharp second: ruled out position(s) 4
30. [bijection] method:Grandsire Doubles: ruled out position(s) 4,5
31. [bijection] ringer:Ambrose: ruled out position(s) 3
32. [bijection] ringer:Osbert: ruled out position(s) 3
33. [bijection] ringer:Ambrose: ruled out position(s) 1
34. [order] from clue 9 method:Kent Treble Bob: ruled out position(s) 3
35. [bijection] method:Grandsire Doubles: ruled out position(s) 1

---

<sub>seed `2026173089258` &middot; score 5.515 &middot; atoms 11 &middot; positives 1 &middot; solved by order</sub>
