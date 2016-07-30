                                            #	>>> EXERCISE 38 <<<
                                            #   DOING THINGS TO LIST
print "\nEXERCISE 38 DOING THINGS TO LIST"
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# Splits 'ten_things' string into a variable, then renames it
# SPLIT(' ', TEN_THINGS) => split ten_things with ' ' between them
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # New variable with '.pop()' function, this will pull the last element from 'more_stuff'
    # POP(MORE_STUFF) => pops last off more_stuff
    next_one = more_stuff.pop()
    # Prints string, and says what was pulled from 'more_stuff'
    print "Adding ", next_one
    # Adds what was pulled off of more_stuff and adds it to the 'stuff' list
    # APPEND(STUFF, NEXT_ONE) => append stuff on next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
# POP(STUFF) => pops off the end of stuff
print stuff.pop()
# JOIN(' ', STUFF) => joins things with ' ' between them in stuff
print " ".join(stuff)
# JOIN('#', STUFF[3:5] => joins things with '#' between them in stuff
print "#".join(stuff[3:5])
print "\n"

                                            #	>>> EXERCISE 39 <<<
                                    #   DICTIONARIES, OH LOVELY DICTIONARIES
print "EXERCISE 39 DICTIONARIES, OH LOVELY DICTIONARIES"
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = dict(CA='San Francisco', MI='Detroit', FL='Jacksonville')

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states["Florida"]

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get("Texas", None)

if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('STX', 'Does not exist')
print "The city form the state 'TX' is: %s\n\n" % city

                                        #	>>> EXERCISE 40 <<<
                                    #   MODULES, CLASSES, AND OBJECTS
print 'EXERCISE 40 MODULES, CLASSES, AND OBJECTS'
# Modules can be called and used when imported. In order to import, the imported file must be saved in the same folder.
# Play around with this using import mystuff.
# Class is like an module, and dict. It is a named collection of attributes or package. However it is different from
# modules and dict. Kind of like a mini stamp or a mold
"""
import mystuff

# dict style
dict = {'apples': 'variable'}
print dict['apples']

# module style
mystuff.apple()
print mystuff.tangerine

# class style
thing = mystuff.MyStuff()
thing.apple()
print thing.tangerine
"""


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def chain(self):
        for line in self.lyrics:
            print line


happy_bday = Song(['Happy birthday to you',
                   'I dont want to get sued',
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

not_invited = Song(["All of my hoes is exotic",
                    "None of your hoes is invited",
                    "I don't have to front"])

two_step = Song(["I've been here lookin' dynamite",
                 "Alone against the wall",
                 "Girls like you give it all so cold"])

happy_bday.sing_me_a_song()
print ''
bulls_on_parade.sing_me_a_song()
print ''
not_invited.sing_me_a_song()
print ''
two_step.sing_me_a_song()
print '\n'

                                    #	>>> EXERCISE 41 <<<
                            #   LEARNING TO SPEAK OBJECT ORIENTED
print 'EXERCISE 41 LEARNING TO SPEAK OBJECT ORIENTED\nExercise placed in string due to endless quiz'
"""
class X(Y):
    # Make a class named X that is-a Y.
    # Words- Class, is-a
    # Tells python to make a new kind of thing, that inherits from another

class Z(object):
    def __init__(self,J):
    # Class X has-a __init__ that takes self and J as parameters
    # Words- Class, has-a, self
    # Tells python to make a new kind of thing, something is composed of another, self is a variable

class R(object):
    def M(self, J):
    # Class X has-a function named M that takes self and J parameters
    # Words- Class, has-a, self
    # Tells Python to make a new kind of thing, something is composed of another, self is a variable

foo = X()
    # Set foo to an instance of class x
    # Words- instance, class
    # what you get when  you tell python to create a class, tells python to make new kind of thing

foo.M(J)
    # From foo get the M function, and call it when parameters self, J
    # Words- self
    # variable inside of class that is used for objects

foo.k = Q
    # From foo get the K attribute, and set it to Q
    # Words- attribute
    # A property classes have that are from composition and are usually variables
        # A class can be composed of other classes as parts
"""
"""
import random
from urllib import urlopen
import sys

WORLD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []

PHRASES = {
    'class %%%(%%%):':
        'Make a class named %%% that is-a %%%.',
    'class %%%(object):\n\tdef __init__(self, ***)':
        'class %%% has-a __init__ that takes self and *** parameters.',
    'class %%%(object):\n\tdef ***(self, @@@)':
        'class %%% has-a function named *** that takes self and @@@ parameters.',
    '*** = %%%()':
        'Set *** to an instance of class %%%.',
    '***.***(@@@)':
        'From *** get the *** function, and call it with parameters self, @@@.',
    "***.*** = '***'":
        'From *** get the *** attribute and set it to "***".'
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORLD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace('@@@', word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "Answer: %s\n\n" % answer
except EOFError:
    print "\nBye"
"""
print '\n'

                                    #	>>> EXERCISE 42 <<<
                            #   IS-A, HAS-A, OBJECTS AND CLASSES
print "EXERCISE 42 IS-A, HAS-A, OBJECTS AND CLASSES\nThere is nothing to print.\n\n"


# Animal is-a object (yes, sort of confusing)
class Animal(object):
    pass


# Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        # dog has-a name
        self.name = name


# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):
    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        # not sure
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a fish
class Salmon(Fish):
    pass


# Halibut is-a fish
class Halibut(Fish):
    pass


# Rover is-a Dog
rover = Dog("Rover")

# Satan is-a cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# mary has-a pet
mary.pet = satan

# Frank is-a employee
frank = Employee("Frank", 120000)

# frank has-a pet
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# Course is-a Salmon
course = Salmon()

# harry is-a Halibut()
harry = Halibut()





                                        #	>>> EXERCISE 43 <<<
                            #   BASIC OBJECT-ORIENTED ANALYSIS AND DESIGN
print "EXERCISE 43 BASIC OBJECT-ORIENTED ANALYSIS AND DESIGN"
# Map out problems to code:
    # Build basic flow chart to problem
    # Highlight main areas (key points- mostly nouns and verbs and how they are related)
    # Detail flow chart with class hierarchy
        # build classes with nouns and find the parent class, build def with verbs
        # code the classes and their functions
    # Test run
    # Repeat and refine
print 'Gothons.py goes through each step in building, please see that file. You can also see Gothons2 for detailed ' \
      'notes. There is also another game called dungeon.py\n\n'





                                        #	>>> EXERCISE 44 <<<
                                        #   INHERITANCE VS. COMPOSITION
print "EXERCISE 44 INHERITANCE VS COMPOSITION"
# Parent and Child classes and how they interact:
print "1. Actions on the child IMPLY an action on the parent"
class Parent(object):
    # When a def function is inside of a parent class then all child classes will inherit it. Thus meaning that this
    #   function will be preformed even for child classes. This is very handy for repetitive code you need in many
    #   classes.
    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        pass


class Child(Parent):
    # pass is an empty block, telling Python that there is nothing new to define in it. Instead it will inherit all
    #   its behavior from the Parent class.
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print "\n2. Actions on the child OVERRIDE the action on the parent"
# When you want to have the child to behave differently, you will want to override the function in the
#   child, effectively replacing the functionality. To do this, just define a function with the same name in Child.
class Parent2(object):
    def override(self):
        print "PARENT override()"

class Child2(Parent2):
    # This override function overrides the Parent override function because it is in its new class. "The child does
    #   not have to do exactly as the parent..."
    def override(self):
        print "CHILD override()"

dad = Parent2()
son = Child2()

dad.override()
son.override()

print "\n3. Actions on the child ALTER the action on the parent"
# Overriding where you want to alter the behavior before or after the Parent class's version runs. You first override
#   the function just like in the last example. but then you use a Python built-in function named super to the the
#   parent version to call
class Parent3(object):
    def altered(self):
        print "PARENT altered()"

class Child3(Parent3):
    def altered(self):
        print "CHILD, BEFORE PATENT altered()"
        super(Child3, self).altered()
        print "CHILD, AFTER PATENT altered()"

dad = Parent3()
son = Child3()

dad.altered()
son.altered()
print ''

print "COMPOSITION, use classes and modules"
class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child5(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child5()

son.implicit()
son.override()
son.altered()
print ''
print ''





                                        #	>>> EXERCISE 45 <<<
                                        #   YOU MAKE A GAME
print "EXERCISE 45 YOU MAKE A GMAE\nSAVED AS RUINS GAME ON GIT AND ALSO IN GAMES LP INSIDE LEARN PYTHON...\n\n"





                                        #	>>> EXERCISE 46 <<<
                                        #   PROJECT SKELETON
print "EXERCISE 46 PROJECT SKELETON\nSAVED IN PROJECTS\n\n"





                                        #	>>> EXERCISE 47 <<<
                                        #   AUTOMATED TESTING
print "EXERCISE 47 AUTOMATED TESTING\nSAVED IN EXAMPLES EX47\n\n"





                                        #	>>> EXERCISE 48 <<<
                                        #   ADVANCED USER INPUT
print "EXERCISE 48 ADVANCED USER INPUT\nSAVED IN EXAMPLES EX48"
# OUT GAME LEXICON
#   Direction words: North, South, East, West, Down, Up, Left, Right, Back
#   Verbs: Go, Stop, Kill, Eat
#   Stop Words: The, In, Of, From, At, It
#   Nouns: Door, Bear, Princess, Cabinet
#   Numbers: Any string of 0 through 9 characters

# BREAKING UP A SENTENCE
#   We need a way of breaking up the sentences so we can figure out what they are
#   stuff = raw_input('> ')
#   words = stuff.split()

# LEXICON TUPLES
#   We need to figure out what the words are that we just broke up, this is done with tuples
#   first_word = ('direction', 'north')
#   second_word = ('verb', 'go')
#   sentence = [first_word, second_word]

# SCANNING THE INPUT
#   Takes a string of raw input from a user and return a sentence that's composed of a list of tuples with the (TOKEN,
#       WORD) parings. If a word ist part of the lexicon, then it should still return the WORD but set the TOKEN to
#       an error TOKEN. The error TOKEN will tell the user they messed up.

# EXCEPTIONS AND NUMBERS
#   Deals with valueErrors and what to do with them