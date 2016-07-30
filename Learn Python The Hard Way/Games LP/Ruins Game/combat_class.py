import random

# decides randomly if it will attack/dodge
class Combat(object):
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        # higher number = more dodges
        num = random.randint(1, self.dodge_limit)
        return num > 4

    def attack(self):
        # lower number = more hits
        num = random.randint(1, self.attack_limit)
        return num > 3
