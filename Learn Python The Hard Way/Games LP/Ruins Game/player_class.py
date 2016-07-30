import random
from combat_class import Combat

# Sets up player for entire game
class Player(Combat):
    # attack_limit and hit_points are set to 10, so the player is stronger
    attack_limit = 10
    experience = 0
    hit_points = 10

    # over rides the attack method in combat_class
    def attack(self):
        num = random.randint(1, self.attack_limit)
        # num += higher chance of stronger hit
        if self.weapon == "knife":
            num += 1
        elif self.weapon == 'saw blade':
            num += 2
        return num > 4

    def get_weapon(self):
        weapon_choice = raw_input("Choose your weapon: [K]nife, [P]lastic sword, [S]aw blade? ").lower()
        if weapon_choice == 'k':
            return 'knife'
        elif weapon_choice == 'p':
            return 'plastic sword'
        elif weapon_choice == 's':
            return 'saw blade'
        else:
            return self.get_weapon()

    def __init__(self):
        self.name = raw_input("Name your player: ").title()
        self.weapon = self.get_weapon()
        self.hit_points = self.hit_points

    def __str__(self):
        return "\n{}, HP: {}, XP: {}".format(self.name, self.hit_points, self.experience)

    def rest(self):
        # player rest and builds HP back up, can not go above stated amount
        if self.hit_points < 15:
            self.hit_points += 1

    def level_up(self):
        # if monster died then, player gets its XP
        return self.experience >= 5
