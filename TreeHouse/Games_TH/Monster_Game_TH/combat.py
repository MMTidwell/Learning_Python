import random

# parent class for character.py and monster.py files
class Combat:
    dodge_limit = 6
    attack_limit = 6

    # makes it possible to dodge monster based on random number
    # Retruns false if hit and true if missed
    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    # makes it possible to attack monster based on random number
    # returns true if hit and false if missed
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4
