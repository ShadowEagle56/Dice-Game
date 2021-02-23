# Find-Best-Dice
First Task: Compare Two Dices

Implement a function that takes two dices as input and computes two values: the first value is the number of times the first dice wins (out of all possible 36 choices), the second value is the number of times the second dice wins. We say that a dice wins if the number on it is greater than the number on the other dice.


Second Task: Is there the Best Dice?

Now, your goal is to check whether among the three given dices there is one that is better than the remaining two dices.

Implement a function that takes a list of dices and checks whether there is dice (in this list) that is better than all other dices. We say that a dice is better than another one, if it wins more frequently (that is, out of all 36 possibilities, it wins in a cases, while the second one wins in b cases, and (a > b). If there is such a dice, return its (0-based) index. Otherwise, return -1.


Third Task: Implement a Strategy

You are now ready to play!

Implement a function that takes a list of dices (possibly more than three) and returns a strategy. The strategy is a dictionary:

If, after analyzing the given list of dices, you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose

If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then, specify, for each dice that your opponent may take, the dice that you would take in return. Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first.
