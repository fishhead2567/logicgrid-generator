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

1. Cadwallader flies 200 miles.
2. Alabaster descends from a Sion. Alabaster flies 300 miles.
3. Hieronymus descends from a Janssen.
4. Nutmeg does not fly 500 miles.
5. The pigeon that descends from a Delbar does not fly 400 miles.

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

1. [direct] from clue 6 bird:Nutmeg: ruled out position(s) 4
2. [direct] from clue 4 bird:Cadwallader: ruled out position(s) 2,3,4
3. [direct] from clue 3 breed:a Delbar: ruled out position(s) 3
4. [direct] from clue 1 bird:Alabaster: ruled out position(s) 1,3,4
5. [direct] from clue 2 breed:a Sion: ruled out position(s) 1,3,4
6. [bijection] bird:Nutmeg: ruled out position(s) 1,2
7. [bijection] bird:Hieronymus: ruled out position(s) 1,2
8. [bijection] bird:Hieronymus: ruled out position(s) 3
9. [bijection] breed:a Delbar: ruled out position(s) 2
10. [bijection] breed:a Janssen: ruled out position(s) 2
11. [bijection] breed:a Stichelbaut: ruled out position(s) 2
12. [direct] from clue 5 breed:a Janssen: ruled out position(s) 1,3
13. [bijection] breed:a Delbar: ruled out position(s) 4
14. [bijection] breed:a Stichelbaut: ruled out position(s) 4
15. [bijection] breed:a Stichelbaut: ruled out position(s) 1

---

<sub>seed `2026172607112` &middot; score 2.585 &middot; atoms 6 &middot; positives 4 &middot; solved by bijection</sub>
