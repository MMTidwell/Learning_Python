import random
from combat_class import Combat

# Parent class for all of the monsters
class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1

    # Determines HP and XP with each monster randomly
    def __init__(self):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)

    def __str__(self):
        return "{}, HP: {}, XP: {}".format(self.__class__.__name__,
                                           self.hit_points,
                                           self.experience)


class Sloth(Monster):
    name = 'Sloth'
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1


class Blob(Monster):
    name = 'Blob'
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1


class Cyclops(Monster):
    name = 'Cyclops'
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1


class Fairy(Monster):
    name = 'Fairy'
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1


class Beetle(Monster):
    """ MAIN BOSS """
    name = 'Beetle'
    min_hit_points = 2
    max_hit_points = 3
    min_experience = 2
    max_experience = 3
