def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for x in dice1:
        for y in dice2:
            if x > y:
                dice1_wins += 1
            elif x < y:
                dice2_wins += 1
    return dice1_wins, dice2_wins


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    wins = [0]*len(dices)
    for x in range(len(dices)):
        for y in range(x + 1, len(dices)):
            a, b = count_wins(dices[x], dices[y])
            if a > b:
                wins[x] += 1
            else:
                wins[y] += 1
    check = True
    elem = wins[0]
    for x in wins:
        if elem != wins[x]:
            check = False

    if check is True:
        return -1
    elif check is False:
        max_int = max(wins)
        max_index = wins.index(max_int)
        if max_index != 0:
            for x in range(0, wins[max_index]):
                if wins[max_index] == wins[x]:
                    check = True
        for x in range(max_index + 1, len(wins)):
            if wins[max_index] == wins[x]:
                check = True
        if check is True:
            return -1
        else:
            return max_index


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True

    if find_the_best_dice(dices) != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = find_the_best_dice(dices)
    else:
        strategy["choose_first"] = False
        for x in range(len(dices)):
            for y in range(len(dices)):
                dice1_win, dice2_win = count_wins(dices[x], dices[y])
                if dice1_win < dice2_win:
                    break
            strategy[x] = y

    print(strategy)


compute_strategy(dices)
