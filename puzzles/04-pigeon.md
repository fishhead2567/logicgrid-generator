# Andy's Swiftest Birds

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `a7db3a10cde0`

## Introduction

Andy races pigeons, and each bird is bred for a different combination of stubbornness and speed.
Four pigeons are involved. Determine each pigeon's distance and breed.
- **Pigeon**: Alabaster, Nutmeg, Hieronymus and Cadwallader.
- **Distance** (listed from shorter to longer): 200 miles, 300 miles, 400 miles and 500 miles.
- **Breed**: a Delbar, a Janssen, a Stichelbaut and a Sion.
Every pigeon has a different distance and breed, so within each category every item is used exactly once.

## Clues

1. The pigeon that descends from a Sion and 200 miles are exactly one hundred miles apart in distance order, in one direction or the other. Cadwallader flies 200 miles.
2. The pigeon that descends from a Delbar flies 200 miles.
3. The pigeon that descends from a Stichelbaut flies 400 miles.
4. Alabaster descends from a Sion.
5. Nutmeg does not fly 500 miles.

## Solving chart

*Distance vs Pigeon*

| | Alabaster | Nutmeg | Hieronymus | Cadwallader |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Distance vs Breed*

| | a Delbar | a Janssen | a Stichelbaut | a Sion |
|---|---|---|---|---|
| **200 miles** | | | | |
| **300 miles** | | | | |
| **400 miles** | | | | |
| **500 miles** | | | | |

*Pigeon vs Breed*

| | a Delbar | a Janssen | a Stichelbaut | a Sion |
|---|---|---|---|---|
| **Alabaster** | | | | |
| **Nutmeg** | | | | |
| **Hieronymus** | | | | |
| **Cadwallader** | | | | |

## Solution

| Distance | Pigeon | Breed |
|---|---|---|
| 200 miles | Cadwallader | a Delbar |
| 300 miles | Alabaster | a Sion |
| 400 miles | Nutmeg | a Stichelbaut |
| 500 miles | Hieronymus | a Janssen |

## How it falls out

1. [direct] from clue 6 breed:a Stichelbaut: ruled out position(s) 1,2,4
2. [direct] from clue 4 breed:a Delbar: ruled out position(s) 2,3,4
3. [direct] from clue 2 bird:Nutmeg: ruled out position(s) 4
4. [direct] from clue 1 bird:Cadwallader: ruled out position(s) 2,3,4
5. [bijection] bird:Alabaster: ruled out position(s) 1
6. [bijection] bird:Nutmeg: ruled out position(s) 1
7. [bijection] bird:Hieronymus: ruled out position(s) 1
8. [bijection] breed:a Janssen: ruled out position(s) 1,3
9. [bijection] breed:a Sion: ruled out position(s) 1,3
10. [direct] from clue 3 bird:Alabaster: ruled out position(s) 3
11. [order] from clue 5 breed:a Sion: ruled out position(s) 4
12. [direct] from clue 3 bird:Alabaster: ruled out position(s) 4
13. [bijection] bird:Nutmeg: ruled out position(s) 2
14. [bijection] bird:Hieronymus: ruled out position(s) 2
15. [bijection] bird:Hieronymus: ruled out position(s) 3
16. [bijection] breed:a Janssen: ruled out position(s) 2

---

<sub>seed `2026172607112` &middot; score 3.67 &middot; atoms 6 &middot; positives 4 &middot; solved by order</sub>
