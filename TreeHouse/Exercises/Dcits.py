def word_count(arg):
    arg1 = arg.lower().split()
    dicts = {}
    for word in arg1:
        if word in dicts:
            dicts[word] += 1
        else:
            dicts[word] = 1
    print dicts


word_count("I am that I am")
print ''

# Formatting dicts
my_string = "Hi! my name is {name} and i live in {state}."
print my_string.format(state="TX", name="Mitt")
## OR
my_dict = {'name': 'Mitt', 'state': 'Texas'}
print my_string.format(**my_dict)

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(d, s):
    new_list = []
    for word in d:
        new_list.append(s.format(**word))
    return new_list


string_factory(dicts, string)
print ''

# dicts iteration
my_dict.update({'age': 31, 'country': 'USA', 'employer': 'Tim', 'job': 'student'})
for thing in my_dict:
    print thing
for value in my_dict.values():
    print value
print ''

# Teacher stats
teach = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
        'Kenneth Love': ['Python Basics', 'Python Collections'],
        'Mitt': ['list', 'several', 'things', 'longer'],
        'Tim': ['one']
        }
def most_classes(teacher):
    count = []
    classes = 0
    for key in teacher:
        count.append(len(teacher[key]))

    for value in count:
        if value > classes:
            classes = value

    for key in teacher:
        if classes == len(teacher[key]):
            print key

def num_teachers(teacher):
    teachers = 0
    for key in teacher:
        teachers += 1
    print teachers

def stats(teacher):
    num = []
    for name, value in teacher.items():
        new_list = [name, len(value)]
        num.append(new_list)
    print num

def courses(teacher):
    course_list = []
    for value in teacher.values():
        course_list.extend(value)
    return course_list


most_classes(teach)
num_teachers(teach)
stats(teach)
courses(teach)









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