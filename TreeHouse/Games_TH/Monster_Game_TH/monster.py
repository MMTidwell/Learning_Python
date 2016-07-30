
import random
# imports Combat() from combat.py (Combat is the parent class)
from combat import Combat

# colors do not change, this is why it is in all caps. this is nor mandatory for python
COLORS = ['yellow', 'blue', 'red', 'green']

# Subclass of Combat in file combat
class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    # initial values of player, sets hit_points, experience, and color all at random
    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    # turns into a string and replaces the values with .format()
    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

    # sound of the monster, returns sound in all caps
    def battlecry(self):
        return self.sound.upper()


# subclass of monster
class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'

# subclass of monster
class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'

# subclass of monster
class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'rwaaaarrrrrr'

