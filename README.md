# Dice Game
## First Task: Compare Two Dices

Implement a function that tests two dices and computes two values: the first value is the number of times the first dice wins, the second value is the number of times the second dice wins. A dice wins if its number is greater than the other dice.


## Second Task: Is there a Best Dice?

Check among the three given dices whether there is one dice that is better than the rest.
Implement a function that takes a list of dices and checks whether there is dice (in this list) that is better than all other dices. A dice is better than the other  if it wins more frequently. If there is such a dice, return its index. Otherwise, return -1.


## Third Task: Implement a Strategy

Implement a function that takes a list of dices and returns a strategy. The strategy is a dictionary:
After analyzing the given list of dices and you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the index of the dice you would like to choose.
If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then specify for each dice that your opponent may take, the dice that you would take in return. For each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first.
