# Score categories
# Change the values as you see fit

YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == ONES:
        return dice.count(1)
    
    if category == TWOS:
        return 2 * dice.count(2)

    if category == THREES:
        return 3 * dice.count(3)

    if category == FOURS:
        return 4 * dice.count(4)

    if category == FIVES:
        return 5 * dice.count(5)

    if category == SIXES:
        return 6 * dice.count(6)

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category == CHOICE:
        return sum(dice)

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1,2,3,4,5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2,3,4,5,6] else 0


    if category == FULL_HOUSE:
        if len(set(dice)) == 2:
            num_dice = dice.count(set(dice).pop())
            if num_dice in [2,3]:
                return sum(dice)
        return 0

    if category == FOUR_OF_A_KIND:
        return sum([d * 4 for d in set(dice) if dice.count(d) >= 4]) 
