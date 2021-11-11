import json
import random
import Tools


class Class:
    armor = 0
    damage = []
    life = 0
    special = []

    def __init__(self, armor, damage, life, special, name):
        self.armor = armor
        self.damage = damage
        self.life = life
        self.special = special
        self.name = name

    def FromJson(data):
        armor = data["armor"]
        damage = data["damage"]
        life = data["life"]
        special = data["special"]

        return Class(armor, damage, life, special)

    def Hit(self, target, orcIndex, numberAdv):
        if Tools.RollDice(1, 20) > target.armor:
            damage = Tools.RollDice(self.damage[0], self.damage[1])
            target.life -= damage

            if (target.life <= 0):
                if (self.name == "Orc"):
                    print(str(self.name) + " " + str((orcIndex + 1) - numberAdv) + " killed the " + str(target.name) + " with " + str(damage) + " damage")
                else:
                    print(str(self.name) + " killed " + str(target.name) + " " + str(orcIndex) + " with " + str(damage) + " damage")

            else:
                if (self.name == "Orc"):
                    print(str(self.name) + " " + str((orcIndex + 1) - numberAdv) + " dealt " + str(damage) + " damage to " + str(target.name))
                else:
                    print(str(self.name) + " dealt " + str(damage) + " damage to " + str(target.name) + " " + str(orcIndex))

                if (target.name == "Orc"):
                    print(str(target.name) + " " + str(orcIndex) + " has now " + str(target.life) + " HP")
                else:
                    print(str(target.name) + " has now " + str(target.life) + " HP")

        else:
            if (self.name == "Orc"):
                print(str(self.name) + " " + str((orcIndex + 1) - numberAdv) + " missed his attack")
            else:
                print(str(self.name) + " missed his attack")

    def IsAlive(self):
        return self.life > 0


class Warrior(Class):
    def __init__(self, armor, damage, life, special, name):
        super().__init__(armor, damage, life, special, name)

    def __str__(self):
        return "WARRIOR: " + str(self.life) + " HP / Armor: " + str(self.armor)  + " / Damage: " + str(self.damage) + " / Second Win: " + str(self.special)

class Rogue(Class):
    def __init__(self, armor, damage, life, special, name):
        super().__init__(armor, damage, life, special, name)

    def __str__(self):
        return "ROGUE: " + str(self.life) + " HP / Armor: " + str(self.armor)  + " / Damage: " + str(self.damage) + " / Sneak: " + str(self.special)

class Mage(Class):
    def __init__(self, armor, damage, life, special, name):
        super().__init__(armor, damage, life, special, name)

    def __str__(self):
        return "MAGE: " + str(self.life) + " HP / Armor: " + str(self.armor)  + " / Damage: " + str(self.damage) + " / FireBall: " + str(self.special)

class GroupAdventurer:
    group = []
    
    def __init__(self, number):
        self.number = number

        with open('bdd.json') as json_file:
            data = json.load(json_file)
            input = data['Warrior']
            w = Warrior(input['armor'], input['damage'], input['life'], input['special'], "Warrior")
            self.group.append(w)
            input = data['Mage']
            r = Rogue(input['armor'], input['damage'], input['life'], input['special'], "Rogue")
            self.group.append(r)
            m = Mage(input['armor'], input['damage'], input['life'], input['special'], "Mage")
            self.group.append(m)
            input = data['Rogue']
            
            print("Here is our group of " + str(self.number) + " mighty adventurers!")
            for i in range(len(self.group)):
                print(self.group[i])

    def FromJson(self, data):
        for c in data:
            self.group.append(Class.FromJson(data[c]))

    def Initiative(self, index):
        initiative = {}

        for i in range(index, len(self.group)):
            initiative[i] = random.randint(1, 20)
        
        return initiative

    def Alive(self):
        deadCount = 0
        for i in range(len(self.group)):
            if (self.group[i].IsAlive() == False):
                deadCount += 1
        if (deadCount >= self.number):
            return False

        return True


class Orc(Class):
    def __init__(self, armor, damage, life, special, name):
        super().__init__(armor, damage, life, special, name)

    def __str__(self):
        return "ORC: " + str(self.life) + " HP / Armor: " + str(self.armor)  + " / Damage: " + str(self.damage)

class Horde:
    enemies = []

    def __init__(self, number):
        self.number = number

        with open('bdd.json') as json_file:
            data = json.load(json_file)
            input = data['Orc']
            for i in range(self.number):
                self.enemies.append(Orc(input['armor'], input['damage'], input['life'], input['special'], "Orc"))

        print("\nThe Horde is composed of " + str(number) + " powerful Orcs\n" + str(self.enemies[0]) + "\n")
                
    def Initiative(self, index):
        initiative = {}

        for i in range(index, index + len(self.enemies)):
            initiative[i] = random.randint(1, 20)
        
        return initiative

    def Alive(self):
        deadCount = 0
        for i in range(len(self.enemies)):
            if (self.enemies[i].IsAlive() == False):
                print(str(self.enemies[i].name) + " is dead")
                deadCount += 1
        if (deadCount >= len(self.enemies)):
            return False

        return True