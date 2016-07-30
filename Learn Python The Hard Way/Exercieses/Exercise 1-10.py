 										#	>>> EXERCISE 1 <<<
 										# 	PRINT STATEMENTS
print "EXERCISE 1 PRINT STATEMENTS"
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun"
print 'Yay! Typing'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

# STUDY DRILL
print "Another line.\n\n"




 										#	>>> EXERCISE 2 <<<
 										#	COMMENT LINES
print "EXERCISE 2 COMMENT LINES"
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this." # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This wont run."

print "This # will run. \n\n"

# STUDY DRILL
# Study drill was double checking you work and seeing if there were any bugs
# In line 24  you will notice that the # is in a string, this prints normally with the # included.
# Reading code backwards will help you catch errors and not just see "code". 




										#	>>> EXERCISE 3 <<<
										#	MATH AND FLOATS
print "EXERCISE 3 MATH AND FLOATS"
# prints string
print "I will now count my chickens:"

# pints strings followed by total 
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

# prints string
print "Now I will count the eggs:"

# prints total
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# prints string with numbers
print "Is it true that 3 + 2 < 5 - 7?"

# prints total
print 3 + 2 < 5 - 7

# prints strings followed by total
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

# prints string
print "Oh, that's why it's False."

# prints string
print "How about some more."

# prints strings followed by total
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2, '\n'

# STUDY DRILL
# Floating points are when you add '.0' at the end of a number to get the most accurate answer. 
print "I will now count my chickens:"
print "Hens", 25 + 30 / 6.0
print "Roosters", 100 - 25.0 * 3 % 4.0
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6.0
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7.0
print "What is 3 + 2?", 3 + 2.0
print "What is 5 - 7?", 5 - 7.0
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > -2.0
print "Is it greater or equal?", 5 >= -2.0
print "Is it less or equal?", 5 <= -2.0
print "This is a floating number with '/':", 5 / 2.0 # Notice that the / gives exact number. 
print "This is a floating number with '%':", 5 % 2.0, '\n\n' # Notice that the % drops the remainder. 




 										#	>>> EXERCISE 4 <<<
 										#	VARIABLES AND NAMES
print "EXERCISE 4 VARIABLES AND NAMES"
# Variable- a name for something so you can recall it later rather than writing the same code again 
# Variables 
# 100 cars
cars = 100
# space for 4
space_in_a_car = 4.0
# 30 drivers
drivers = 30
# 90 customers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capasicty = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Print lines with strings, calling variables, followed by strings
# This might have been faster if we used the .format() method. 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capasicty, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car.\n\n"

# STUDY DRILL
# Goes over floating numbers, variables, and = vs. ==.




 										#	>>> EXERCISE 5 <<<
 								#	VARIABLES AND PRINTING AND STRINGS
print "EXERCISE 5 VARIABLES AND PRINTING AND STRINGS"
name = "Mittsy M. Tidwell"
age = 31
height = 63 # inches
weight = 136 # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print "Let's talk about %s." % name # uses %s because it is converting object into a string
print "She's %d inches tall." % height # uses %d because it is an integer 
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "Shes got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth # if you use %d it will throw an 
	# error if you use %r it will read 'White' vs White. % can not be alone in character due to error. 

# Uses %d because you are replacing with integers 
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight), '\n\n'

# STUDY DRILL
# Change variable names 
print """CONVERSON AND MEANING
d	Signed integer decimal.	
i	Signed integer decimal.	
o	Unsigned octal.	(1)
u	Unsigned decimal.	
x	Unsigned hexadecimal (lowercase).	
X	Unsigned hexadecimal (uppercase).	
e	Floating point exponential format (lowercase).	
E	Floating point exponential format (uppercase).	
f	Floating point decimal format.	
F	Floating point decimal format.	
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.	
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.	
c	Single character (accepts integer or single character string).	
r	String (converts any python object using repr()).	
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result. \n\n"""




 										#	>>> EXERCISE 6 <<<
 										# 	STRINGS AND TEXT
print "EXERCISE 6 - STRINGS AND TEXT"
# String- a bit of text you want to display. If you would like multiple formats in your string, you
	# must put them inside a () and separated by ,. 
# Variables and strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing specific strings by calling their variables
print x
print y

# Printing strings and formatting where another string will go by calling the variable
print "I said: %r." % x
print "I also said: '%s'." % y

# Variables and strings
hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

# Print strings by calling variables
print joke_evaluation % hilarious

# Variables and strings
w = "This is the left side of..."
e = "a string with the right side."

# Printing 2 strings by calling the variable
print w + e + '\n\n'

# STUDY DRILL
# 4 places a string is inside another string- lines 185, 185, 192, 193, 200 (calls line 197)
# There are 5
# Adding 2 strings together keeps them separate but prints them together, kinda like adding




 										#	>>> EXERCISE 7 <<<
 										#	MORE PRINTING
print "EXERCISE 7 MORE PRINTING"
print "Mary had a littel lamb."
print "It's fleece was white as %s." % 'snow' # noitce that 'snow' is not a variable in this line, 
												# but a string.
print "And everywhere that Mary went."
print "." * 10 # what did that do? => it prints 10 *'s. 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12 + '\n\n'
# when the comma is there it allows both prints on the same line, without it prints on 2 lines.

# STUDY DRILL
# check for mistakes and write them down on sperate paper




 										#	>>> EXERCISE 8 <<<
 										#	PRINTING, PRINTING
print "EXERCISE 8 PRINTING, PRINTING."
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
) + '\n\n'




 										#	>>> EXERCISE 9 <<<
 									#	PRINTING, PRINTING, PRINTING
print "EXERCISE 9 PRINTING, PRINTING, PRINTING." 	
# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"		

print "Here are the days: ", days # Original line from book.
print "Here are the months: %r" % months  # Notice how the \n are printed in, that is due to the %r,
		# if we had done %s, the \n would not have printed and each one would be on its own line. 

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
even 4 lines if we want, or 5 or 6.
"""					




 										#	>>> EXERCISE 10 <<<
 										# 	WHAT WAS THAT?
print "EXERCISE 10 WHAT WAS THAT"
tabby_cat = "\tI'm tabbed in."
persain_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persain_cat
print backslash_cat
print fat_cat