


                                        #	>>> Variables and Strings <<<
# Variables- what the string is referred to as (a name, on the left side of string)
# Strings- a string of letters, numbers, and/or words on the right side of a variable, they are surrounded by " or '.
variable_name = "This is a string." 
variable_name1 = "This is a string. %s" 
variable_name2 = "This is a string. %r" 




                                        #	>>> Printing <<<
# Printing- is giving an outcome when the code is run.
print "String"
print 'String'

# Printing multi lines per statement
print ("Multiple\n"
       "lines\n"
       "on \n"
       "print statement.\n")  # Notice that when we put the """ on its own line it leaves a blank line

# Printing multi prints on the same line
print "Prints on",
print 'same line, and I don\'t need to add additional spaces!'

# Print string by calling variable name
print variable_name

# Print "String", variable_name, "String" (do NOT need spaces before last ", it will do it on its own)
print "What is a string?", variable_name, "Oh now I see."

# Print variable with line formatting
print variable_name1 % "makes since"
print variable_name2 % "makes since"




                                        #	>>> Basic Operators <<<
# MATH AND BOOLEAN
    # TRUTH TABLES ON PAGE 93-94!!!
    # PEMDAS Method
        # float- the remainder after division
        # + 	Plus
        # - 	Minus
        # / 	Divide
        # .0 	Divide actual (with remainder)
        # * 	Multiply
        # ** 	Squared
        # % 	Remainder after divide
        # //    Backslash
        # += 	Adding
        # -= 	Subtraction
        # /=    Divide
        # //=   Floor Division
        # *=    Multiply
        # **=   Squared

    # BOOLEAN
        # and       Only True if both are True
        # or        True unless both are False
        # not       opposite of True or False
        # not(or)   Only True if both are False
        # not(and)  Only False when both are True
        # is        Equality, same as '=='
        # !=	    Not equal to
        # ==	    Equal to
        # < 	    Less Than
        # >= 	    Greater than or equal to
        # <= 	    Less than or equal to
        # <>        Not equal to

# CONVERSION AND MEANING
    # THESE ARE ALL USED WITH THE % BEFORE THE LETTER
    # IF YOU ARE USING MORE THAN 1 IN A STRING THEN THEY WILL BE SHOWN (VARIABLE, VARIABLE, VARIABLE)
    # %d	Signed integer decimal.
    # %i	Signed integer decimal.
    # o		Unsigned octal.	(1)
    # u		Unsigned decimal.
    # x		Unsigned hexadecimal (lowercase).
    # X		Unsigned hexadecimal (uppercase).
    # e		Floating point exponential format (lowercase).
    # E		Floating point exponential format (uppercase).
    # f		Floating point decimal format.
    # F		Floating point decimal format.
    # g		Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
    # G		Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
    # c		Single character (accepts integer or single character string).
    # %r	String (converts any python object using repr()).	(converts raw data)
    # %s	String (converts any python object using str()).
    # %		No argument is converted, results in a "%" character in the result.
    # {}    Used when doing .format() at the end (this is much more simple than %conversion)

# FORMATTING 
    # .format()		            inserts variable inside {} when in string.
    # .round()		            rounds floating number
    # .float()                  turns number into a float
    # int()			            turns string into integer (whole number, even when '.' is used)
    # len()			            length of variable inside the ()
    # = open()		            opens file  **EX 15**
    # .close()		            closes file  **EX 16**
    # .read()		            prints file (can not edit)  **EX 15**
    # .readline 	            prints out first line
    # .readlines	            prints out all lines
    # .truncate() 	            file size  **EX 16**
    # .write() 		            writes to file  **EX 16**
    # .seek()		            finds area in file (index #)
    # del                       deletes item for you
    # .isdigit()                checks to see if input is a integer
    # .upper()                  turns all letters into uppercase
    # .lower()                  turns all letters into lowercase
    # break                     used to get out of loops, even when true
    # continue                  forces loop to continue within even if false
    # .isalpha                  checks to ensure letters exist
    # for __ in enumerate(__):  gives back the step and value you are at in the loop
    # **kwargs                  unpacks dicts
    # *step                     unpacks tuples and list

# ESCAPE SEQUENCES
    # '\\'		# Backslash
    # '\''		# Single-quote
    # '\"'		# Double-quote
    # '\a' 		# ASC11 bel (BEL)
    # '\b' 		# ASC11 backspace (BS)
    # '\f'		# ASC11 form feed (FF)
    # '\n' 		# ASC11 linefeed (LF) (used like this=> 2 lines. At then of string=> creates 1)
    # \N{name}		# Character named name in Unicode database (Unicode only)
    # \r 			# ASC11 carriage return (CR)
    # \t 			# ASC11 horizontal tab (TAB)
    # \uxxxx 		# Character with 16-bit hex value (Unicode only)
    # \Uxxxxxxxx 	# Character with 32-bit hex value (Unicode only)
    # \v 			# ASC11 vertical tab (VT)
    # \ooo			# Character with octal value oo
    # \xhh			# Character with hex value hh

# LISTS
    # []	            Empty string
    # [0]	            First index in list
    # [-1]	            Last index in list
    # [x]	            Specific index number
    # [x:]	            Everything after x is printed
    # [:x] 	            Everything before x is printed
    # [x:x]	            Everything between 2 specific index numbers
    # [::#]             '::'-list is splitting, '#'-steps splitting
    # [#::#]            First '#'- start, '::' list splitting, second '#'- steps splitting
    # [::-1]            Calls the list backwards
    # [#:#:-1]          First '#'- end number, Second '#'- start number, '-1'- backwards
    # list[#] =         changes the value of the index
    # cmp(list1,list2)  compares elements in both lists
    # len(list)         length of list
    # max(list)         largest value in list (length of word/number)
    # min(list)         smallest value in list (length of word/number)
    # .count()          how many times the () occurs in list
    # .extend()         appends the contest of () to the list
    # .split(' ')       splits string where there is ' '
    # ' '.join()        turns list into a string
    # .append()         adds to the end of the list
    # .remove()         removes from list.
    # .index()          returns the lowest index () occurs
    # .insert()         inserts at that index
    # .pop()            removes and returns last object from list (look this up!)
    # .reverse()        reverses objects in list in place
    # .sort()           sorts smallest to largest
    # .sorted()         sorts list in alpha
    # range(low,high)   checks between x and y, returns everything in-between but does not 'count' the last one

# CLASSES BUILT IN
    # __dict__:                 Dictionary containing the classes namespace
    # __doc__:                  Class documentation string or none, if undefined
    # __name__:                 Class name
    # __module__:               Module name in class is defined. This is "__main__" in interactive mode
    # __bases__:                Empty tuple containing the base classes, in order in the base class list
    # __del__()                 Deletes class
    # __init__(self{,args...])  Constructor with optional arguments
    # __repr__(self)            String representation
    # __str__(self)             Printable string representation
    # __cmp__(self, x)          Object comparison

# DICT
    # del dict['name']      deletes field 'name'
    # dict.clear()          deletes all entries in dict, will return {}
    # del dict              deletes entire dict
    # cmp(dict1, dict2)     compares both dicts
    # len(dict)             total length of dict (number of items)
    # str(dict)             printable string of dict
    # type(dict)            returns dict type
    # dict.copy             returns a shallow copy of dict
    # dict.items()          returns a list of dicts
    # dict.update(dict2)    adds dictionary dict2 key values pairs to dict
    # dict.values()         returns list of dict values

# EXIT SYS
    # exit (0)      Clean exit from program
    # exit (1)      Error in program and program exits due to that

# DATES AND TIME
    # datetime.now()        what today's date and time is down to millisecond
    # datetime.delta()      controls days, hours, min
    # .date()               prints today's date
    # .time()               prints time
    # .combine()            prints date and time together
    # .strftime()           string form time
    # .strptime()           string parsed into time=> makes a datetime from a string

# IMPORT MODULES
    # from random import randint
    # import datetime
    # from __future__ import print_function

# ASSERT METHODS FOR TESTING
    # assertAlmostEqual(a, b)	        round(a-b, 7) == 0
    # assertNotAlmostEqual(a, b)	    round(a-b, 7) != 0
    # assertGreater(a, b)	            a > b
    # assertGreaterEqual(a, b)	        a >= b
    # assertLess(a, b)	                a < b
    # assertLessEqual(a, b)	            a <= b
    # assertRegexpMatches(s, r)     	r.search(s)
    # assertNotRegexpMatches(s, r)  	not r.search(s)
    # assertItemsEqual(a, b)	        sorted(a) == sorted(b) and works with unhashable objs
    # assertDictContainsSubset(a, b)	all the key/value pairs in a exist in b

# REGULAR EXPRESSIONS
    # BASICS
        # r             raw string
        # re.match      only checks the beginning of the string
        # re.search     checks the whole txt file

        # \w    any Unicode word or character (upper, and lower case, number and  _.)
        # \W    anything that isn't a Unicode character
        # \s    any whitespace
        # \S    anything that isn't whitespace
        # \d    any number from 0-9
        # \D    anything that isn't a number
        # \b    word boundaries or edges of a word
        # \B    anything that isn't the edge of a word

    # ESCAPES
        # {3}       something that occurs exactly 3 times
        # (,3}      something that occurs 0 - 3 times
        # {3,}      occurs 3 or more times
        # {3,5}     occurs 3 - 5 times
        # ?         occurs 0-1 times
        # *         occurs at least 0 times
        # +         occurs at least once

    # SETS
        # [aple]    apple
        # [a-z]     any lowercase letters from a - z
        # [^2]      anything that is not 2




                                        #	>>> Error Message <<<
# String literal error- string needs to be closed
# Syntax error- something is not correct, look for the carat as it will point it out
# Type error- int not in list. Meaning that there is a number when there should be a string. Fix this with str(i)
# Name error- tried to use a variable or object that does not exist





                                        # 	>>> Function <<<
# FUNCTIONS- name pieces of code the way variable name strings and numbers. They take arguments the way
    # your scripts take argv. With the above they let you make your own "mini-scripts" or "tiny commands".

    # To make a function:
        # def name_of_function(argument):
            # this line unpacks the arguments (same as script does in argv)
            # more arguments
            # print/return statements

    # Function check list:
        # starting function
            # def
            # function name
            # (argument, argument, argument):
            # all lines after def are indented 4 spaces
            # end function with dedenting
        # checking function
            # did your function work when called
            # did you put (value, value, value)

# Variables within the functions can not be used outside of the function without calling on the function.
    # If you are going to need to use a variable for more than one function, then it will need to be above
    # the first function.

# Argument(s)- is what is between the () when defining a function. You can use as many as you wish, but keep
    # it less then 5, you can also choose to not have any arguments at all.
    # *args- tells Python to take all the arguments to the function and then put them in args as a list. It is
        # similar to argv but used in def functions. This is not normally used, but can be useful.

# Calling a function- you do not need to put 'print' in front of in order for it to be used. You can also
    # pass in numbers, and variables for the arguments. If there are arguments when def the function then
    # the same amount of arguments must be used with calling the function to be used. You can also call
    # on other def functions when typed into another def function.

# Return- tells the function to give back something byt DOES NOT print it out, returns vanish, prints print it out




                                        #	>>> IF Statements <<<
# IF statements- creates a branch in the code using boolean. If the boolean results in True then it will run the code
    # under the statement, if False it will move to the next function in the program. If there are multiple elif blocks
    # reading True then the program will only run the first block.** EXERCISE 30**

# Structure of IF statement- the If statement will need to be ended with the ':' (doing the ':' tells Python that
    # you are building a block and everything indented is in that block), and the following lines will
    # need to be indented 4 spaces past 'if' in order to run if True.
    # Elif- if the IF statement returns False, then the program will go to the 'elif' or 'else' parts. In a IF
        # statement you can have as many Elif statements as you need.
    # Else- if the IF and or Elif statement returns False, then the 'else' statement will run.
    if cars > people:
        print "We should take the cars."
    elif cars < people:
        print "We should not take the cars."
    else:
        print "We can't decide."

# Nested decisions- nested decisions are IF statements inside of another IF statement. These are very powerful
    # as they branch from one to another, to another, to another.... ** EXERCISE 31**




                                        #	>>> List <<<
# Lists- are a groups of words or numbers that are in brackets '[]', separated with a ',', can be as long or short
    # as needed, and can contain list within themselves. When it is a list of words, the words have to have "" around
    # them like in a string. If they are numbers they do not need the "" around them.
    hairs = ["brown", "blond", "red"]

# Lists are mutable (specific items can be changed and reassigned or deleted) in order to create your list. Strings are
    # not list lists anc can not be changed on the inside. A simple change can look like:
    hairs[2] = "short"


# When COUNTING the index number of the list (this is done to help find the location), you will start with 0
    # when counting from the left side. If you are counting from the end of the list then you will start with -1.

# Cardinal- counting numbers, starting with 0 (program)
# Ordinal- counting numbers, starting with 1 (natural way). You can convert ordinal to cardinal by -1.





                                        #	>>> Loop <<<
# break- exits out of while loop even when True
# continue- keeps running the loop even when False

# FOR loops- go through each element until it is finished. Once this happens it will move to the next line.
    for number in number_list:
        # number- a new variable name
        # number_list- variable above

# WHILE loops- go though the same function until it returns False, once this happens it will move to the next line.
    # You need to be careful with these as they can cause endless loops.
        # Rules for while loops:
            # most of the time for loops are better
            # make sure that what you testing will result in a False at some point
            # print out your test variable at the top and bottom of the while loop to see what is going on
    while i < 6:
        # i- called variable
        # 6- comparison





                                        #	>>> DICTIONARIES <<<
# Dict- associates one thing to another no matter what it is. These are held in {}, and separated by ','.
    # They can link to one another in order to pull multiple things from each.  **EXAMPLE 39**
    # Each key is separated by a ':' then the items are separated by ',' and the whole thing is enclosed in {}.
    my_dict = {'name': 'Mitt', 'age': '31'}
        # key- word before ':' (name).
        # value- word after ':' (Mitt).

# Calling items within dictionaries
    my_dict['name']

# Adding to dictionaries
    my_dict['job'] = 'student'
# Rules- you can not use the same 'key' name in the same dict, if this is done it will only pull the last one used.
    # Also you can not use [] in them.





                                        # 	>>> Modules <<<
# From- imports specific parts of the module
# Import- imports database from python library

# Modules are very similar to dicts in the way that things are called, however the syntax is different.
    mystuff.apple()  # calling on module for info (this is a function call)
    print mystuff.tangerine  # calling on module for info (this is a variable call)
    print mystuff['apple']  # calling on the dict

# Raw input- asks the user a question and their response is used in the output
    # Turning an answer (input starts as a string) into a number
    a = int(raw_input())
    # Turning an answer into a float
    b = float(raw_input())

# from sys import argv- fills in lines of code (where called) with what is typed in after calling
    # the file in PowerShell. **Exercise 13** is a great example of how it is done. However please note
    # that this will need to be done in Notepad++ and ran in PowerShell, or used in PyCharm. This is similar
    # to raw_input, but does differ some, it asks for the input before the script is run. While raw_input will run
    # script until you fill in the input then it will continue to print.
    script, first, second, third = argv # => argv is the argument variable

# Import Random- imports numbers or words
    string_name = random.randint(lowest, highest) # calls numbers
    string_name2 = random.choice(list_being_called) # calls words

# from os.path import exists- returns true if the file exist, and false it file does not exist. **EXERCISE 17**
    % exists(to_file)

# import time- allows for given amount of time until it is told to do something
    import time
    time.sleep(0.5)  # This tells the program to run slower at a given time.





                                        #	>>> CLASSES <<<
# It is best to create classes in a separate file, and import them through the import function.
# Class- is a way to take a grouping of functions and data and place them inside a container so you can access them
    # with the '.' operator. Classes are more commonly used than modules, this is because classes do not interfere
    # with one another. With modules you can only use one per program
    class mystuff(object):
        def __init__(self):
            self.tangerine = "And now a thousand years between"

        def apple(self):
            print "I AM CLASSY APPLES!"





                                        #	>>> OBJECT <<<
# Objects are created when you create a class. When creating an object this is what happens inside python
    # 1. Create object- thing = MyStuff()
    # 2. Python creates an empty object with the functions you specified in the class using def
    # 3. Python looks for __init__ function, if so it will call that function to initialize the newly created
        # empty object.
    # 4. Self is the empty variable python created
    # 5. Python takes new object and assigns it to the thing variable

# **EXERCISE 41** Shows how to call and use classes
    # class
        class X(___):

        class ___(object):
            def __init__(self,___):

        class ___(object):
            def M(self, ___):

    # Calling a class
        ___ = ___()  # Set ___ to an instance of class ___. ***(creates an object)***
        ___.___(___)  # From ___ get the ___ function, and call it when parameters self, ___.
        ___.___ = "___"  # From ___ get the ___ attribute, and set it to "___".




                                    #	>>> TUPLES <<<
# Tuples- ordered non key collections stay the same way they are created, similar to immutable list.
#   What makes a Tuple is not the '()', but the ','.
my_tuple = (1, 2, 3)
print my_tuple
print ''
#   You can access the tuple in the same way you can a list
print my_tuple[1]
print ''
#   You can NOT change the values due to item assignment error, meaning you can NOT delete, pop, or change items.
#   Tuples have a fixed size and memory
# Simultaneous assignment- creating 2 or more tuples and assigning them to one another.
a, b = 1, 2
print a
print b
c = (3, 4)
print c
d, e = c
print d, e
f = d, e
print f
print f == c
del a, b
a = 1
b = 2
a, b = b, a
print b, a
print ''

def my_func():
    return 1, 2, 3

print my_func()
tup = my_func()
print tup
x, y, z = my_func()
print x, y, z
print ''




                                        #	>>> INHERITANCE <<<
# Parent Class- main class, setting attributes and functions for subclasses.
# Child Class- AKA subclass, takes all the info from the parent class and can be changed in order to fit that classes
#   needs. Any instance of  a child class will also take on the parent classes attributes as well.
# Parent and Child classes and how they interact:
#   1. Actions on the child imply an action on the parent
#   2. Actions on the child override the action on the parent
#   3. Actions on the child alter the action on the parent

                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>>  <<<
                                        #	>>> BASIC VOCAB <<<
# CLASS- Tell python to make a new kind of thing
    # INSTANCE- What you get when you tell Python to create a class
        # OBJECT- 2 meanings; the most basic kind of thing, and any instance of something
            # SELF- Inside the functions in a class, self is a variable for the instance/object being accessed
# DEF- How you define a function inside a class
# INHERITANCE- The concept that 1 class can inherit traits from another class (parent to child)
    # IS-A- A phrase to say that something inherits from another
# COMPOSITION- the concept that a class can be composed of other classes as parts (wheels to car)
    # HAS-A- A phrase to say that something is composed of other things or has traits.
    # ATTRIBUTE- A property classes have that are from composition and are usually variables




                                        #	>>> SHOULD GO OVER LATER <<<
# Assert- ensures something is True           
# Class- defines a class             
# Raise- raises an exception when something goes wrong
# Pass- shows an empty block         
# @- at(decorators)
# global- variable outside of block 
# yield- pause here and return later
# exec- runs a line as Python
# finally- exceptions or not finally do this
# lambda- creates a short anonymous function
# None- shows no value
# return- exit function with return value

# try- tries code to see if it will run
    try:
        count = in(input("Give me a number: "))
# except- finds the error that we are looking for. If it finds it, than it will work the block
    except ValueError:
        print ("That's not a number!")
# else- if the block does not fail, this block will run.
    else:
        ("Hi " + count)


                                        # 	>>> Code Source <<<
www.bitbucket.org
www.github.com
www.gitoritous.org
www.launchpad.net
www.sourceforge.net
www.freecode.com