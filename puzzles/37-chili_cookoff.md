# The Firehouse Chili Cook-Off

**Difficulty** 5/7 (hard) &nbsp;&nbsp; **Grid** 4 x 5 &nbsp;&nbsp; **Clues** 12 &nbsp;&nbsp; **id** `8f3fab3099e7`

## Introduction

The volunteer fire department holds a chili cook-off every fall, and the judging has never once ended quietly.
Five cooks are involved. Determine each cook's placing, secret and topping.
- **Cook**: Verna, Bobbi Jo, Gracie Mapp, Hollis and Luis Ortega.
- **Placing** (listed from better to worse): first, second, third, fourth and fifth.
- **Secret**: a square of dark chocolate, fire-roasted corn, root beer, a splash of cider vinegar and nothing but salt.
- **Topping**: oyster crackers, scallions, crushed corn chips, shredded cheddar and sour cream.
Every cook has a different placing, secret and topping, so within each category every item is used exactly once.

## Clues

1. Gracie Mapp and fifth are exactly one place apart in placing order, in one direction or the other. The cook who tops it with oyster crackers is better than fifth in placing order.
2. The cook who swears by a splash of cider vinegar is worse than second in placing order. Luis Ortega does not place second.
3. Bobbi Jo and fourth are exactly one place apart in placing order, in one direction or the other.
4. Second and the cook who tops it with shredded cheddar both sit at odd-numbered places or both at even-numbered places.
5. The cook who swears by a square of dark chocolate and fourth are exactly one place apart in placing order, in one direction or the other.
6. Third falls somewhere between the cook who swears by fire-roasted corn and the cook who swears by root beer in placing order.
7. The cook who tops it with oyster crackers is worse than first in placing order.
8. At least one of the following holds, and possibly more than one: (a) Verna and the cook who tops it with scallions are exactly one place apart in placing order, in one direction or the other. (b) Hollis is better than the cook who tops it with oyster crackers in placing order.
9. Luis Ortega is better than the cook who tops it with scallions in placing order.
10. Bobbi Jo falls somewhere between the cook who tops it with crushed corn chips and the cook who tops it with oyster crackers in placing order.
11. Bobbi Jo does not swear by a square of dark chocolate.
12. The cook who swears by root beer and the cook who tops it with scallions are exactly three places apart in placing order.

## Solving chart

*Placing vs Cook*

| | Verna | Bobbi Jo | Gracie Mapp | Hollis | Luis Ortega |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Secret*

| | a square of dark chocolate | fire-roasted corn | root beer | a splash of cider vinegar | nothing but salt |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Placing vs Topping*

| | oyster crackers | scallions | crushed corn chips | shredded cheddar | sour cream |
|---|---|---|---|---|---|
| **first** | | | | | |
| **second** | | | | | |
| **third** | | | | | |
| **fourth** | | | | | |
| **fifth** | | | | | |

*Cook vs Secret*

| | a square of dark chocolate | fire-roasted corn | root beer | a splash of cider vinegar | nothing but salt |
|---|---|---|---|---|---|
| **Verna** | | | | | |
| **Bobbi Jo** | | | | | |
| **Gracie Mapp** | | | | | |
| **Hollis** | | | | | |
| **Luis Ortega** | | | | | |

*Cook vs Topping*

| | oyster crackers | scallions | crushed corn chips | shredded cheddar | sour cream |
|---|---|---|---|---|---|
| **Verna** | | | | | |
| **Bobbi Jo** | | | | | |
| **Gracie Mapp** | | | | | |
| **Hollis** | | | | | |
| **Luis Ortega** | | | | | |

*Secret vs Topping*

| | oyster crackers | scallions | crushed corn chips | shredded cheddar | sour cream |
|---|---|---|---|---|---|
| **a square of dark chocolate** | | | | | |
| **fire-roasted corn** | | | | | |
| **root beer** | | | | | |
| **a splash of cider vinegar** | | | | | |
| **nothing but salt** | | | | | |

## Solution

| Placing | Cook | Secret | Topping |
|---|---|---|---|
| first | Luis Ortega | nothing but salt | crushed corn chips |
| second | Hollis | root beer | shredded cheddar |
| third | Bobbi Jo | a splash of cider vinegar | sour cream |
| fourth | Gracie Mapp | fire-roasted corn | oyster crackers |
| fifth | Verna | a square of dark chocolate | scallions |

## How it falls out

1. [direct] from clue 7 cook:Luis Ortega: ruled out position(s) 2
2. [order] from clue 13 topping:oyster crackers: ruled out position(s) 1
3. [order] from clue 12 secret:fire-roasted corn: ruled out position(s) 3
4. [order] from clue 12 secret:root beer: ruled out position(s) 3
5. [order] from clue 11 cook:Bobbi Jo: ruled out position(s) 1,2,4
6. [order] from clue 10 secret:a square of dark chocolate: ruled out position(s) 1,2,4
7. [order] from clue 9 topping:scallions: ruled out position(s) 3
8. [order] from clue 6 topping:oyster crackers: ruled out position(s) 5
9. [order] from clue 5 cook:Bobbi Jo: ruled out position(s) 5
10. [order] from clue 5 topping:crushed corn chips: ruled out position(s) 3
11. [order] from clue 5 topping:oyster crackers: ruled out position(s) 3
12. [order] from clue 4 cook:Luis Ortega: ruled out position(s) 5
13. [order] from clue 4 topping:scallions: ruled out position(s) 1
14. [order] from clue 9 secret:root beer: ruled out position(s) 4
15. [order] from clue 3 topping:shredded cheddar: ruled out position(s) 1,3,5
16. [order] from clue 2 cook:Gracie Mapp: ruled out position(s) 1,2,3,5
17. [order] from clue 1 secret:a splash of cider vinegar: ruled out position(s) 1,2
18. [direct] from clue 14 secret:a square of dark chocolate: ruled out position(s) 3
19. [bijection] cook:Verna: ruled out position(s) 3,4
20. [bijection] cook:Hollis: ruled out position(s) 3,4
21. [bijection] cook:Luis Ortega: ruled out position(s) 3,4
22. [bijection] secret:fire-roasted corn: ruled out position(s) 5
23. [bijection] secret:root beer: ruled out position(s) 5
24. [bijection] secret:a splash of cider vinegar: ruled out position(s) 5
25. [bijection] secret:nothing but salt: ruled out position(s) 5
26. [bijection] topping:sour cream: ruled out position(s) 1,2,4,5
27. [order] from clue 9 topping:scallions: ruled out position(s) 2
28. [order] from clue 12 secret:fire-roasted corn: ruled out position(s) 1,2
29. [bijection] cook:Verna: ruled out position(s) 1
30. [bijection] cook:Hollis: ruled out position(s) 1
31. [bijection] secret:a splash of cider vinegar: ruled out position(s) 4
32. [bijection] secret:nothing but salt: ruled out position(s) 4
33. [bijection] topping:crushed corn chips: ruled out position(s) 2,4,5
34. [order] from clue 5 topping:oyster crackers: ruled out position(s) 2
35. [bijection] secret:nothing but salt: ruled out position(s) 3
36. [bijection] topping:scallions: ruled out position(s) 4
37. [bijection] topping:shredded cheddar: ruled out position(s) 4
38. [order] from clue 9 secret:root beer: ruled out position(s) 1
39. [bijection] secret:nothing but salt: ruled out position(s) 2
40. [disjunction] from clue 8 cook:Verna: ruled out position(s) 2
_... and 1 further steps._

---

<sub>seed `2026173168448` &middot; score 9.1244 &middot; atoms 14 &middot; positives 0 &middot; solved by disjunction</sub>
