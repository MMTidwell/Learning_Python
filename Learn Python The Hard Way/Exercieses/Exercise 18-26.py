                                    # >>> EXERCISE 18 <<<
                                # 	NAMES, VARIABLES, CODE, FUNCTIONS
print "EXERCISE 18 NAMES, VARIABLES, CODE, FUNCTIONS"
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no arguments
def print_none():
    print "I got nothin'.\n\n"

print_two("Mitt", "Tidwell")
print_two_again("Mitt", "Tidwell")
print_one("First!")
print_none()

# STUDY DRILL
# make a list functions and a check list for calling function.




                                        #	>>> EXERCISE 19 <<<
                                        #   FUNCTIONS AND VARIABLES
print "EXERCISE 19 FUNCTIONS AND VARIABLES"
# defines a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# calls on function to print and run values inside () as the arguments
print "We can just give the fucntion numbers directly:"
cheese_and_crackers(20, 30)

# creates new variables outside of the function
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crakcers = 50

# calls on function and runs variables for the values of the arguments
cheese_and_crackers(amount_of_cheese, amount_of_crakcers)

# calls on function and does math for the values of the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# calls function and runs variables and numbers for the values of the arguments
print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crakcers + 1000)
print ''
# STUDY DRILL
# explain in english, read backwards, crate my own function and run 10x




                                        #	>>> EXERCISE 20 <<<
                                        #   FUNCTIONS AND FILES
print "EXERCISE 20 FUNCTIONS AND FILES"
print "this will run better alone with 'test.txt' as the argument and taken out of the string. \n\n"
"""
from sys import argv

script, input_file = argv

# defines "print_all" function (reads file)
def print_all(f):
    print f.read()

# defines "rewind" function (looks for called index)
def rewind(f):
    f.seek(0)

# defines "print_a_line" function (prints line number and prints line)
def print_a_line(line_count, f):
    print line_count, f.readline()

# variable used to open file, called for arguments in functions and when printing
current_file = open(input_file)

print "First let's print the wholefile:\n"
# prints "print_all" functions (prints the whole file)
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# prints the "rewind function (tells where to go)
rewind(current_file)

print "Let's print three lines:"
# goes to "print_a_line" function, prints line_count(aka current_line) and what is on the line.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)"""
# STUDY DRILL
# write in english, change to += (this did not work and kept throwing an error), check arguments




                                        #	>>> EXERCISE 21 <<<
                                #   FUNCTIONS CAN RETURN SOMETHING
print "EXERCISE 21 FUNCTIONS CAN RETURN SOMETHING"
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDE %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Helight: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# a puzzle for extra credit
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?\n\n"




                                        #	>>> EXERCISE 24 <<<
                                    #   MORE PRACTICE WITH FUNCTIONS
print "EXERCISE 24 MORE PRACTICE WITH FUNCTIONS"
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# beans is the same as jelly_beans just with a new name, it will hold the return value of jelly_beans
beans, jars, crates = secret_formula(start_point)
# print pulls from 182
print "With a starting point of: %d" % start_point
# print pulls from 183, then 176, then 182
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10
print "We can also do that this way:"
# print pulls from 176, then 189, then 182
print "We'd have %d beans, %d jars, and %d crates.\n\n" % secret_formula(start_point)




                                        #	>>> EXERCISE 25 <<<
                                #   EVEN MORE PRACTICE WITH FUNCTIONS
print "EXERCISE 25 EVEN MORE PRACTICE WITH FUNCTIONS\n This will need to be done in the shell for it to run.\n\n"
def break_words25(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words25(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word25(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word25(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence25(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last25(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted25(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)




                                        #	>>> EXERCISE 26 <<<
                                                #   TEST
print "EXERCISE 26 TEST!!"
print "**Please note that this is the corrected copy of the test.**"
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates. \n\n" % secret_formula(start_point)


sentence = "All good things come to those who wait."

words = break_words(sentence)
print words
sorted_words = sort_words(words)
print sorted_words

print_first_word(words)
print_last_word(words)
print words
print_first_word(sorted_words)
print_last_word(sorted_words)
print sorted_words
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
