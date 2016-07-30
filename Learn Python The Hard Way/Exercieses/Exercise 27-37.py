
                                        #	>>> EXERCISE 27 <<<
                                        #   MEMORIZING LOGIC
print "\nEXERCISE 27 MEMORIZING LOGIC \nThere are notes in Operations.py, but refer to book.\n\n"





                                        #	>>> EXERCISE 28 <<<
                                        #   BOOLEAN PRACTICE
print "EXERCISE 28 BOOLEAN PRACTICE"
print True and True
print False and True
print 1 == 1 and 2 == 1
print "test" == "test"
print 1 == 1 or 2 != 1
print True and 1 == 1
print False and 0 != 0
print True or 1 == 1
print "test" == "testing"
print 1 != 0 and 2 == 1
print "test" != "testing"
print "test" == 1
print not (True and False)
print not (1 == 1 and 0 != 1)
print not (10 == 1 or 1000 == 1000)
print not (1 != 10 or 3 == 4)
print not ("testing" == "testing" and "Zed" == "Cool Guy")
print 1 == 1 and not ("testing" == 1 or 1 == 0)
print "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print ""
print ""





                                        #	>>> EXERCISE 29 <<<
                                        #   WHAT IF
print "EXERCISE 29 WHAT IF."
people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs.\n\n"
# STUDY DRILL
# the if statements are comparison statements.
# if statement is true then it will move down like a def, otherwise it will move to the next code
# if you remove "if" then you will have to remove the ":" as well. Then when you run the code,
    # you will get an error message due to print being indented.
# if you change the variable in the beginning it could change the result





                                        #	>>> EXERCISE 30 <<<
                                        #   ELSE AND IF
print "EXERCISE 30 ELSE AND IF. "
# Variables used for the IF statements bellow
people = 30
cars = 40
buses = 15

# Compares the people anc cars variables, then runs them based on boolean results. If it returns True then program
    # will run next section of code, if False then it will run to 'elif' and 'else'.
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

# If there are multiple elif blocks reading True then the program will only run the first block.
if buses < cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
print "\n"





                                        #	>>> EXERCISE 31 <<<
                                        #   MAKING DECISIONS
print "EXERCISE 31 MAKING DECISIONS"
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
print "\n"





                                        #	>>> EXERCISE 32 <<<
                                        #   LOOPS AND LISTS
print "EXERCISE 32 LOOPS AND LISTS"
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is the count %d" % number

# same as about
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
print "\n"





                                        #	>>> EXERCISE 33 <<<
                                        #   WHILE LOOPS
print "EXERCISE 33 WHILE LOOPS"
numbers = []


def while_loop(n, p):
    count = 0

    while i < n:
        print "At the top i is %d" % count
        numbers.append(count)

        count += p
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % count

print while_loop(4, 2)
print "The numbers: "

for num in numbers:
    print num

print "\n"
# STUDY DRILL
# Change while loop into a function that you can call on.
# Add 2 variables, one for comparison, and the other for the increase amount.





                                        #	>>> EXERCISE 34 <<<
                                        #   ACCESSING ELEMENTS OF LISTS
print "EXERCISE 34 ACCESSING ELEMENTS OF LISTS \nWhen reading the program bellow (1,2,3) means cardinal, (first,",
print "second, third) means ordinal."
animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "The animal at 1 is a %s." % animal[1]
print "The third animal is %s." % animal[2]
print "The first animal is %s." % animal[0]
print "The animal at 3 is %s." % animal[3]
print "The fifth animal is %s." % animal[4]
print "The animal at 2 is %s." % animal[2]
print "The sixth animal is %s" % animal[5]
print "The animal at 4 is %s." % animal[4]
print '\n'





                                        #	>>> EXERCISE 35 <<<
                                        #   BRANCHES AND FUNCTIONS
print "EXERCISE 35 BRANCHES AND FUNCTIONS\nThis has been turned into a string.\n\n"
"""from sys import exit

def gold_room():
    global how_much
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man. learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in from of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear loos at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever starts at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you choose?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()"""
# STUDY DRILL
# .isdigit() to see if input is a integer.





                                        #	>>> EXERCISE 36 <<<
                                        #   DESIGNING AND DEBUGGING
print """EXERCISE 36 DESIGNING AND DEBUGGING\nFirst test draft is in examples file, under ex.36.1.test, a longer
version is filed under ex.36.2.test. I then took that test and shortened it as much as possible at this knowledge
point.\n\n"""





                                        #	>>> EXERCISE 37 <<<
                                        #   SYMBOL REVIEW
print """EXERCISE 37 SYMBOL REVIEW\nThere are no notes for this, however at the end of Operations.py file there are some
that still need to be reviewed and studied.\n\n"""


































