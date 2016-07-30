import random

# imports Combat() from combat.py (Combat is the parent class)
from combat import Combat

# Subclass of Combat in file combat
class Character(Combat):
    attack_limit = 10
    experience = 0
    # starting hit_points, gives the player the rest ability
    base_hit_points = 10

    # player bonus, almost always going to return hit
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    # player determines weapon
    def get_weapon(self):
        weapon_choice = raw_input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow"'
        else:
            return self.get_weapon()

    # initial values of player, with name and weapon
    def __init__(self, **kwargs):
        self.name = raw_input("Name: ")
        self.weapon = self.get_weapon()
        # makes sure that player does not get more hit_points than what they started with
        self.hit_points = self.base_hit_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}, HP: {}, XP: {}".format(self.name,
                                           self.hit_points,
                                           self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def leveled_up(self):
        return self.experience >= 5
