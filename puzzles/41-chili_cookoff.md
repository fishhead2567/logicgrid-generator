# The Firehouse Chili Cook-Off

**Difficulty** 6/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 12 &nbsp;&nbsp; **id** `7c8c5d7feefe`

## Introduction

The volunteer fire department holds a chili cook-off every fall, and the judging has never once ended quietly.
Five cooks are involved. Determine each cook's placing, chili and topping.
- **Cook**: Bobbi Jo, Sunny Deel, Verna, Gracie Mapp and Luis Ortega.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Chili**: a pumpkin chili, a white chicken chili, a green chile stew, a smoky chipotle chili and a five-bean chili.
- **Topping**: sour cream, crushed corn chips, a fried egg, pickled onions and scallions.
Every cook has a different placing, chili and topping, so within each category every item is used exactly once.

## Clues

1. The following two do NOT both hold; either one alone may hold, and so may neither: (a) Verna is exactly one place better than fourth, with no placing in between. (b) The cook who enters a white chicken chili places third.
2. At least one of the following holds, and possibly more than one: (a) Luis Ortega places third. (b) One of Luis Ortega and second sits at an odd-numbered placing and the other at an even-numbered placing.
3. At least one of the following holds, and possibly more than one: (a) Verna and the cook who tops it with pickled onions are exactly one place apart in placing order, in one direction or the other. (b) Luis Ortega places third.
4. Luis Ortega is better than third in placing order.
5. The cook who enters a five-bean chili and third both sit at odd-numbered places or both at even-numbered places.
6. The cook who tops it with scallions and second are exactly three places apart in placing order.
7. The cook who tops it with pickled onions is exactly one place better than fifth, with no placing in between.
8. The cook who enters a white chicken chili and second are exactly one place apart in placing order, in one direction or the other.
9. The cook who enters a green chile stew falls somewhere between the cook who tops it with scallions and the cook who tops it with sour cream in placing order.
10. The cook who enters a smoky chipotle chili is exactly one place better than Sunny Deel, with no placing in between.
11. The cook who enters a smoky chipotle chili does not top it with a fried egg.
12. Gracie Mapp and the cook who tops it with crushed corn chips are exactly four places apart in placing order.

## Solving chart

*Placing vs Cook*

| | Bobbi Jo | Sunny Deel | Verna | Gracie Mapp | Luis Ortega |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Chili*

| | a pumpkin chili | a white chicken chili | a green chile stew | a smoky chipotle chili | a five-bean chili |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Topping*

| | sour cream | crushed corn chips | a fried egg | pickled onions | scallions |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Cook vs Chili*

| | a pumpkin chili | a white chicken chili | a green chile stew | a smoky chipotle chili | a five-bean chili |
|---|---|---|---|---|---|
| **Bobbi Jo** | | | | | |
| **Sunny Deel** | | | | | |
| **Verna** | | | | | |
| **Gracie Mapp** | | | | | |
| **Luis Ortega** | | | | | |

*Cook vs Topping*

| | sour cream | crushed corn chips | a fried egg | pickled onions | scallions |
|---|---|---|---|---|---|
| **Bobbi Jo** | | | | | |
| **Sunny Deel** | | | | | |
| **Verna** | | | | | |
| **Gracie Mapp** | | | | | |
| **Luis Ortega** | | | | | |

*Chili vs Topping*

| | sour cream | crushed corn chips | a fried egg | pickled onions | scallions |
|---|---|---|---|---|---|
| **a pumpkin chili** | | | | | |
| **a white chicken chili** | | | | | |
| **a green chile stew** | | | | | |
| **a smoky chipotle chili** | | | | | |
| **a five-bean chili** | | | | | |

## Solution

| Placing | Cook | Chili | Topping |
|---|---|---|---|
| first | Luis Ortega | a white chicken chili | crushed corn chips |
| second | Bobbi Jo | a pumpkin chili | a fried egg |
| third | Verna | a smoky chipotle chili | sour cream |
| fourth | Sunny Deel | a green chile stew | pickled onions |
| fifth | Gracie Mapp | a five-bean chili | scallions |

## How it falls out

1. [order] from clue 12 cook:Gracie Mapp: ruled out position(s) 2,3,4
2. [order] from clue 12 topping:crushed corn chips: ruled out position(s) 2,3,4
3. [order] from clue 11 chili:a smoky chipotle chili: ruled out position(s) 5
4. [order] from clue 11 cook:Sunny Deel: ruled out position(s) 1
5. [order] from clue 10 cook:Luis Ortega: ruled out position(s) 3,4,5
6. [order] from clue 9 chili:a white chicken chili: ruled out position(s) 2,4,5
7. [order] from clue 6 chili:a green chile stew: ruled out position(s) 1,5
8. [order] from clue 5 topping:pickled onions: ruled out position(s) 1,2,3,5
9. [order] from clue 3 chili:a five-bean chili: ruled out position(s) 2,4
10. [order] from clue 2 topping:scallions: ruled out position(s) 1,2,3,4
11. [order] from clue 6 topping:sour cream: ruled out position(s) 4,5
12. [bijection] topping:crushed corn chips: ruled out position(s) 5
13. [bijection] topping:a fried egg: ruled out position(s) 4,5
14. [order] from clue 12 cook:Gracie Mapp: ruled out position(s) 1
15. [bijection] cook:Bobbi Jo: ruled out position(s) 5
16. [bijection] cook:Sunny Deel: ruled out position(s) 5
17. [bijection] cook:Verna: ruled out position(s) 5
18. [bijection] topping:sour cream: ruled out position(s) 1
19. [bijection] topping:a fried egg: ruled out position(s) 1
20. [order] from clue 6 chili:a green chile stew: ruled out position(s) 2
21. [order] from clue 11 chili:a smoky chipotle chili: ruled out position(s) 4
22. [disjunction] from clue 8 cook:Verna: ruled out position(s) 1,2,4
23. [disjunction] from clue 7 chili:a white chicken chili: ruled out position(s) 3
24. [disjunction] from clue 4 cook:Luis Ortega: ruled out position(s) 2
25. [bijection] chili:a pumpkin chili: ruled out position(s) 1
26. [bijection] chili:a smoky chipotle chili: ruled out position(s) 1
27. [bijection] chili:a five-bean chili: ruled out position(s) 1
28. [bijection] cook:Bobbi Jo: ruled out position(s) 1,3
29. [bijection] cook:Sunny Deel: ruled out position(s) 3
30. [order] from clue 11 chili:a smoky chipotle chili: ruled out position(s) 2
31. [order] from clue 11 cook:Sunny Deel: ruled out position(s) 2
32. [direct] from clue 1 topping:a fried egg: ruled out position(s) 3
33. [bijection] chili:a pumpkin chili: ruled out position(s) 3
34. [bijection] chili:a green chile stew: ruled out position(s) 3
35. [bijection] chili:a five-bean chili: ruled out position(s) 3
36. [bijection] chili:a pumpkin chili: ruled out position(s) 4,5
37. [bijection] cook:Bobbi Jo: ruled out position(s) 4
38. [bijection] topping:sour cream: ruled out position(s) 2

---

<sub>seed `2026173000118` &middot; score 9.6333 &middot; atoms 12 &middot; positives 0 &middot; solved by disjunction</sub>
