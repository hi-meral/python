import random


class Dice():
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        t1 = (x, y)
        return t1


dice1 = Dice()

print(dice1.roll())
