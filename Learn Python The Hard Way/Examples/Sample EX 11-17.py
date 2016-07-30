print "EXERCISE 11 ASKING QUESTIONS"
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much to you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (
	age, height, weight)



print "EXERCISE 12 PROMPTING PEOPLE"
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)




print "EXERCISE 13 PARAMETERS, UNPACKING, VARIABLES"
from sys import argv

script, first, second, third = argv # => argv is the argument variable

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third




print "EXERCISE 14 PROMTING AND PASSING"
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
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)




print "EXERCISE 15 READING FILES"
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




print "EXERCISE 16 READING AND WRITING FILES"
# calls sys to import argument variables
from sys import argv

# these are the arguments that will be called on when opening the file in powerShell
script, filename = argv

# prints strings and argv 
print """ 
We're going to erase %r." 
If you don't want that, hit CLTR-C (^C).
If you do want that, hit RETURN.
"""  % filename

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





print "EXERCISE 17 MORE FILES"
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
