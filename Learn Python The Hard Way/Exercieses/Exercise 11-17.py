 										#	>>> EXERCISE 11 <<<
 										# 	ASKING QUESTIONS
print "EXERCISE 11 ASKING QUESTIONS"
print "I am turning this exercise into a string so it will not run the error.\n"

"""
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much to you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (
	age, height, weight)
""" 									




 										#	>>> EXERCISE 12 <<<
 										# 	PROMPTING PEOPLE
print "EXERCISE 12 PROMPTING PEOPLE"
print "I am turning this exercise into a string so it will not run the error.\n"
"""
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
"""




 										#	>>> EXERCISE 13 <<<
 										# 	PARAMETERS, UNPACKING, VARIABLES
print "EXERCISE 13 PARAMETERS, UNPACKING, VARIABLES"
print """this needs to be done in windows powershell in order to work. you will also,
	need to call file like this... "python sample 11-.py first 2nd 3rd" in order for it to not error.
	you can change the 3 words after "sample 11-.py" into what you would like. just note that you 
	will want to use 3 words since it calls for 4 variables in the code. the firs variable is the
	name of the file. however you can do as many as you would like. \n\n"""

"""
from sys import argv

script, first, second, third = argv # => argv is the argument variable

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
"""
# STUDY DRILLS
# Using both raw_input and import argv together, it asked a question for the user, user answered and
	# answer was printed out on following line.
# The arguments that are passes in the command line before the script is run are strings.




 										#	>>> EXERCISE 14 <<<
 										# 	PROMTING AND PASSING
print "EXERCISE 14 PROMTING AND PASSING"
print """this needs to be done in windows powershell in order to work. you will also,
	need to call file like this... "python sample 11-.py mittsy" in order for it to not error.
	this file will ask the user questions and then relay the answers they put in at the end.\n\n"""

"""
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
"""Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" """% (likes, lives, computer)
"""
# STUDY DRILLS
# Play with Zonk and Adventure (Saved under "tester.py")
# Change prompt variable, add another argument




 										#	>>> EXERCISE 15 <<<
 										# 	READING FILES
print "EXERCISE 15 READING FILES"
print """this needs to be done in windows powershell in order to work. you will also,
	need to call file like this... "python sample 11-.py ex15_sample.txt". this example opens
	any kind of file so you can view it in powershell. \n\n"""

"""
# calls on sys and imports argument variables
from sys import argv

# these are the arguments that will be called on when opening the file in powerShell
script, filename = argv

# tells powerShell what file to open (hint it is the file you call when opening this)
txt = open(filename)

# prints string and fills in %r with filename, then prints the file
print "Here's your file %r:" % filename
print txt.read()

# prints string and prompts input from user
print "Type the filename again:"
file_again = raw_input("> ")

# new variable opening file again
txt_again = open(file_again)

# prints file
print txt_again.read()
"""
# STUDY DRILL
# write comments explaining code
# code can be adjusted to print either the file or ask what file is being printed. but the 
	# sys import and argv must be there to call the file.




 										#	>>> EXERCISE 16 <<<
 										# 	READING AND WRITING FILES
print "EXERCISE 16 READING AND WRITING FILES"
print """this needs to be done in windows powershell in order to work. you will also,
	need to call file like this... "python sample 11-.py test.txt". this will allow you to open 
	a file, delete file, and wrtie new lines in it. \n\n"""

"""
# calls sys to import argument variables
from sys import argv

# these are the arguments that will be called on when opening the file in powerShell
script, filename = argv

# prints strings and argv 
print """ """
We're going to erase %r." 
If you don't want that, hit CLTR-C (^C).
If you do want that, hit RETURN.
""" """ % filename

# calls for user input
raw_input("? ")

# prints string and calls file to open
print "Opening the file..."
target = open(filename, 'w')

# prints string and deletes file that was called
print "Truncating the file. Goodbye!"
target.truncate() 

# prints string
print "Now I'm going to ask you for three lines."

# calls for user input to write lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = line1 + "\n" + line2 + "\n" + line3

# prints string
print "I'm going to write these to the file."

# prints strings into file that was called and deleted
target.write(line4)

# prints string and then closes the file
print "And finally, we close it."
target.close()
"""
# STUDY DRILL
# write comments explaining code
# created a new variable "line4" so it could add all the lines together with '\n' so there is
	# less repetitions. 
# 'w' is passed in when opening the file so python knows that it will be editing the file. With 
	# this you do not really need the 'target.truncate()' function as it will be editing it. 
# create code similar to ex 15 
"""
from sys import argv

script, filename = argv

read_file = open(filename)

print filename
print read_file.read()

read_file.close()"""




 										#	>>> EXERCISE 17 <<<
 										# 	MORE FILES
print "EXERCISE 17 MORE FILES"
print """this needs to be done in windows powershell in order to work. you will also,
	need to call file like this... "python sample 11-..py test.txt new_file.txt". this will copy one 
	file to another. \n\n"""
"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these 2 in one line too, how? => indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CRTL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."
"""
# STUDY DRILL
# cat, shorten to 1 line, .close(). .close() is used to keep things clean
