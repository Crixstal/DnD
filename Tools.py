import random


def RollDice(number, value):
    res = 0
    for i in range(number):
        res += random.randint(1, value)
    return res
