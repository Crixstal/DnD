import json
import collections
import random
import Tools
import Class


def main():

    numberOfAdventurer = 3
    groupAdv = Class.GroupAdventurer(numberOfAdventurer)
    horde = Class.Horde(random.randint(4, 6))

    initiativeAdventurer = groupAdv.Initiative(0);
    initiativeHorde = horde.Initiative(groupAdv.number);
    mergeList = {**initiativeAdventurer, **initiativeHorde}
    turnOrder = collections.OrderedDict(sorted(mergeList.items(), key = lambda item: item[1], reverse = True))
    print(turnOrder)

    turn = 1

    while (groupAdv.Alive() and horde.Alive()):
        print("\n\n========== TURN " + str(turn) + " ==========\n" )
        for i in turnOrder:
            if (i >= groupAdv.number):
                if (horde.enemies[i - groupAdv.number].IsAlive() == True):
                    target = random.randint(0, groupAdv.number - 1)

                    if (groupAdv.group[target].IsAlive() == False): ## if adventurer is dead, choose another one
                        if (groupAdv.Alive() == False):
                            break
                        while (groupAdv.group[target].IsAlive() == False):
                            target = random.randint(0, groupAdv.number - 1)

                    horde.enemies[i - groupAdv.number].Hit(groupAdv.group[target], i, groupAdv.number)

            else:
                if (groupAdv.group[i - groupAdv.number].IsAlive() == True):
                    target = random.randint(0, horde.number - 1)

                    if (horde.enemies[target].IsAlive() == False): ## if orc is dead, choose another one
                        if (horde.Alive() == False):
                            break
                        while (horde.enemies[target].IsAlive() == False):
                            target = random.randint(0, horde.number - 1)

                    groupAdv.group[i - groupAdv.number].Hit(horde.enemies[target], target, groupAdv.number)

        turn += 1

    if (groupAdv.Alive() == False):
        print("\n\n========== ALL THE ADVENTURERS ARE DEAD! ==========\n\n")
    else:
        print("\n\n========== THE HORDE IS VANQUISHED! ==========\n\n")


main()
