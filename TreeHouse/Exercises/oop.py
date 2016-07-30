# Monster Creating classes
class Monster(object):  # '(object)' does not have to be there in python 3
    # __init__
    def __init__(self, hit_points, weapon, color, sound): # This sets args and asks on creation OVERRIDE METHOD
        self.hit_points = hit_points
        self.weapon = weapon
        self.color = color
        self.sound = sound


    # Monster Class Methods(AKA def)
    def battlecry(self):
        return self.sound.upper()  # 'self' does have to be there


class Monster2(object):
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get('hit_points', 1)
        self.weapon = kwargs.get('weapon', 'sword')
        self.color = kwargs.get('color', 'green')
        self.sound = kwargs.get('sound', 'roar')


    # Monster Class Methods(AKA def)
    def battlecry2(self):
        return self.sound.upper()  # 'self' does have to be there


# creates a copy of Monster
jubjub = Monster(1, 'sword', 'green', 'tweet')

# changes attribute in object
jubjub.hit_points = 5
print jubjub.hit_points
slimey = Monster(5, 'sword', 'blue', 'glug')
print slimey.weapon
print ''


class Store:
    open = 9
    close = 5

    def hours(self):
        return "We're open from {} to {}.".format(self.open, self.close)


# INHERITANCE
import random

colors = ['yellow', 'green', 'blue', 'purple', 'red', 'orange']


class Monster3(object):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self. experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(colors)
        # note that we are not listing weapon or sound

        for key, value in kwargs.items():
            setattr(self, key, value) # object, attribute, value of attribute


    def __str__(self):  # controls what happens when we make a string from an object
        return '{} {}, HP: {}, XP {}'.format(self.color.title(),
                                             self.__class__.__name__,
                                             self.hit_points,
                                             self.experience)


    # Monster Class Methods(AKA def)
    def battlecry2(self):
        return self.sound.upper()  # 'self' does have to be there

jubjub = Monster3()
print 'JUBJUB'
print jubjub.hit_points
print jubjub.color
print ''

jabber = Monster3(color = 'blue', sound = 'whiffling', hit_points = 500, adjective = 'manxsome')
print 'JABBER'
print jabber.color
print jabber.hit_points
print jabber.battlecry2()
print jabber.adjective
print ''

# SUBCLASS
class Goblin(Monster3):  # doing this makes Goblin take all the attributes of Mnster3
    "pass"  # tells python to keep going like nothing happened.
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'

azog = Goblin()
print azog.hit_points
print azog.color
print ''

class Troll(Monster3):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 5
    sound = 'growl'

class Dragon(Monster3):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 18
    sound = 'raaaawwwwrrr'

azog = Goblin()
snaga = Troll()
pete = Dragon()
print pete.hit_points
print snaga.experience
print pete.hit_points
print snaga.battlecry2()
print pete.battlecry2()































