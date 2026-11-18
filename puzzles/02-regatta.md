# The Mudflat Regatta

*The Mudflat Regatta is rowed over a course that is only a course at high tide, which is where most of the trouble starts.*

**Difficulty** 1/7 (gentle) &nbsp;&nbsp; **Grid** 3 x 4 &nbsp;&nbsp; **Clues** 5 &nbsp;&nbsp; **id** `2ac653cf75bc`

## Introduction

There are 4 entries. Each has exactly one placing and one item from every other category below, and within each category every item belongs to a different entry.
- **Placing** (listed in order): first, second, third and fourth.
- **Crew**: the Brickworks crew, the Customs crew, the Creamery crew and the Tannery crew.
- **Colours**: mustard and black, navy with a white band, lilac and bronze and pink and cream.
The places above are listed in order, from first to fourth.

## Clues

1. The Tannery crew goes with third. Navy with a white band goes with the Tannery crew.
2. Lilac and bronze goes with the Customs crew.
3. Mustard and black's placing is better than fourth.
4. The Brickworks crew does not go with second.
5. The Customs crew's placing is better than mustard and black's placing.

## Solving chart

*Placing vs Crew*

| | the Brickworks crew | the Customs crew | the Creamery crew | the Tannery crew |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Placing vs Colours*

| | mustard and black | navy with a white band | lilac and bronze | pink and cream |
|---|---|---|---|---|
| **first** | | | | |
| **second** | | | | |
| **third** | | | | |
| **fourth** | | | | |

*Crew vs Colours*

| | mustard and black | navy with a white band | lilac and bronze | pink and cream |
|---|---|---|---|---|
| **the Brickworks crew** | | | | |
| **the Customs crew** | | | | |
| **the Creamery crew** | | | | |
| **the Tannery crew** | | | | |

## Solution

| Placing | Crew | Colours |
|---|---|---|
| first | the Customs crew | lilac and bronze |
| second | the Creamery crew | mustard and black |
| third | the Tannery crew | navy with a white band |
| fourth | the Brickworks crew | pink and cream |

## How it falls out

1. [direct] from clue 6 crew:the Tannery crew: ruled out position(s) 1,2,4
2. [direct] from clue 5 colours:navy with a white band: ruled out position(s) 1,2,4
3. [direct] from clue 2 crew:the Brickworks crew: ruled out position(s) 2
4. [bijection] colours:mustard and black: ruled out position(s) 3
5. [bijection] colours:lilac and bronze: ruled out position(s) 3
6. [bijection] colours:pink and cream: ruled out position(s) 3
7. [bijection] crew:the Brickworks crew: ruled out position(s) 3
8. [bijection] crew:the Customs crew: ruled out position(s) 3
9. [bijection] crew:the Creamery crew: ruled out position(s) 3
10. [order] from clue 3 crew:the Customs crew: ruled out position(s) 4
11. [order] from clue 3 colours:mustard and black: ruled out position(s) 1
12. [order] from clue 1 colours:mustard and black: ruled out position(s) 4
13. [order] from clue 3 crew:the Customs crew: ruled out position(s) 2
14. [direct] from clue 4 colours:lilac and bronze: ruled out position(s) 2,4
15. [bijection] colours:pink and cream: ruled out position(s) 1,2
16. [bijection] crew:the Brickworks crew: ruled out position(s) 1
17. [bijection] crew:the Creamery crew: ruled out position(s) 1
18. [bijection] crew:the Creamery crew: ruled out position(s) 4

---

<sub>seed `2026172591274` &middot; score 3.97 &middot; atoms 6 &middot; positives 3 &middot; solved by order</sub>
