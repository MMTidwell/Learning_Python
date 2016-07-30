### ORIGINAL DO NOT CHANGE IN ANY WAY!! ###


print "Welcome to my quiz!"
quiz_type = raw_input("Which quiz would you like to take? Easy, Medium, Hard?")

# BASIC VARIABLES
GJ = "Good job, keep it up!\n ------------\n"
TA = "Try again\n ------------\n"

# PYTHON VOCABULARY QUESTIONS
# EASY
python_vocabulary_q1 = ('__1__s are sequences of characters that are enclosed in quotes. We can \n'
                        '    enclose them with single or double quotes and assign them to variables. Placing two or more __1__s \n'
                        '    together using the + symbol. It will not have a space between the two __1__s. Adding numbers into \n'
                        '    __1__s is not possible and you will get an error. This is called __2__. When you are __3__ing strings you will want to start the first letter out \n'
                        '    with 0 and work your way up. The spaces between words and ends of sentences will need to be counted \n'
                        '    as well. Selecting a __4__ of a string starting from the first expression, then stopping at \n'
                        '    the last expression. This would look like:<string> [<expression>:<expression>]. Please note that you \n'
                        '    do not have to have a number at the end of the :, but if you do not it will pull the rest of the \n'
                        '    string. You can also do [:] and this will pull the whole string.')

# MEDIUM!
python_vocabulary_q3 = """__1__s take __2__ and return an __3__. __1__s are bits of code 
    that you can call repetitively, and use over and over. __1__s can be defined once and used as 
    many times as needed. There can be any number of __2__, but it has to have the number of __2__ 
    the __1__ expects. When we do not have enough __2__ in the parameters then it will give an error 
    message. __2__ are what you put into a __1__ to tell them what to do and how it is done. __3__ 
    is the return and the result of the __1__."""
python_vocabulary_q4 = """A __4__ Scope refers to a variable that you can make inside the function 
    and will be used, but does not exist outside of the function. A __5__ Scope is when a variable will 
    be available at all times. It is best to avoid using global variable because it is easier to make 
    mistakes with these."""

# HARD!
python_vocabulary_q5 = """__1__ statements are used when controlling when a function is used and how it 
    is used. They are controlled by the __2__ results. If __2__ results are True then the function 
    will continue like normal. If __2__ results are False then it will stop and move to the __3__ 
    statements. __4__ statements are used inside of the __1__ statements, they are used when comparing two or 
    more similar test values."""
python_vocabulary_q6 = """__5__ Statements are used when you are wanting to create a loop for a 
    function, this loop will be used until it returns a false statement. After the false statement it 
    will then move to the next line of code. Loops are a very important concept of computer programming, 
    that allow us to run blocks of code as many times as we wish without having repetition"""
python_vocabulary_q7 = """__6__ are similar to how strings are sequences of characters, __6__s are 
    sequences of anything! We can have __6__s of numbers, __6__s of characters, even __6__s inside of 
    __6__s! And we can mix up the contents too so we can have __6__s containing many diferent things. One 
    of the advantages of having data with structure (like in a __6__) is that you can take advantage of 
    that structure! __7__ is modifying the existing object, so we can change the value of a __6__ 
    after we have created it. Once a __6__ had been modified then we then we have to worry about other 
    variables that might refer to the same object. This can only be done in __6__s."""

# EASY!
if quiz_type == "Easy" or quiz_type == "easy" or quiz_type == "e":
    print "LETS GET STARTED!\n"

    # PYTHON V QUESTION 1 (EASY)
    while True:
        print python_vocabulary_q1
        easy1 = raw_input("Fill in the blank for 1: ")
        if easy1 == "String" or easy1 == "string":
            print "\n" + python_vocabulary_q1.replace("__1__", "string")
            print GJ
            break
        else:
            print TA

    while True:
        easy1_1 = raw_input("Fill in the blank for 2: ")
        if easy1_1 == "Concatenation" or easy1_1 == "concatenation":
            print "\n" + python_vocabulary_q1.replace("__2__", "concatenation").replace("__1__", "string")
            print GJ
            break
        else:
            print TA

    while True:
        easy2 = raw_input("Fill in the blank for 3: ")
        if easy2 == "Index" or easy2 == "index":
            print "\n" + python_vocabulary_q1.replace("__3__", "index")
            print GJ
            break
        else:
            print TA

    while True:
        easy1_2 = raw_input("Fill in the blank for 4: ")
        if easy1_2 == "subsequence" or easy1_2 == "Subsequence" or easy1_2 == "sub-sequence" or easy1_2 == "Sub-sequence":
            print "\n" + python_vocabulary_q1.replace("__4__", "subsequence").replace("__3__", "index")
            print GJ
            break
        else:
            print TA

    print "YOU COMPLETED WIMPY MODE...CAN YOU KEEP GOING?"

# MEDIUM!
if quiz_type == "Medium" or quiz_type == "medium" or quiz_type == "m":
    print "LETS GET GOING!\n"

    # PYTHON V QUESTION 3 (MEDIUM)
    while True:
        print python_vocabulary_q3
        med1 = raw_input("Fill in the blank for 1: ")
        if med1 == "Function" or med1 == "function":
            print "\n" + python_vocabulary_q3.replace("__1__", "function")
            print GJ
            break
        else:
            print TA

    while True:
        med1_1 = raw_input("Fill in the blank for 2: ")
        if med1_1 == "Input" or med1_1 == "input":
            print "\n" + python_vocabulary_q3.replace("__2__", "input").replace("__1__", "function")
            print GJ
            break
        else:
            print TA

    while True:
        med1_2 = raw_input("Fill in the blank for 3: ")
        if med1_2 == "Output" or med1_2 == "output":
            print "\n" + python_vocabulary_q3.replace("__3__", "output").replace("__2__", "input").replace("__1__",
                                                                                                           "function")
            print GJ
            break
        else:
            print TA
        # PYTHON V QUESTION 4 (MEDIUM)
    while True:
        print python_vocabulary_q4
        med2 = raw_input("Fill in the blank for 1: ")
        if med2 == "Local" or med2 == "local":
            print "\n" + python_vocabulary_q4.replace("__4__", "Local")
            print GJ
            break
        else:
            print TA

    while True:
        med2_1 = raw_input("Fill in the blank for 2: ")
        if med2_1 == "Global" or med2_1 == "global":
            print "\n" + python_vocabulary_q4.replace("__5__", "Global").replace("__4__", "Local")
            print GJ
            break
        else:
            print TA
    print "GOOD TRY, NOW LETS GO FOR HARD!"

# HARD!
if quiz_type == "Hard" or quiz_type == "hard" or quiz_type == "h":
    quiz_start = raw_input("ARE YOU READY?! ")
    if quiz_start == "yes" or quiz_start == "Yes":
        print "LETS GET GOING!"

    # PYTHON V QUESTION 5 (HARD)
    while True:
        print python_vocabulary_q5
        hard1 = raw_input("Fill in the blank for 1: ")
        if hard1 == "If" or hard1 == "if":
            print "\n" + python_vocabulary_q5.replace("__1__", "If")
            print GJ
            break
        else:
            print TA

    while True:
        hard1_1 = raw_input("Fill in the blank for 2: ")
        if hard1_1 == "Boolean" or hard1_1 == "boolean":
            print "\n" + python_vocabulary_q5.replace("__1__", "If").replace("__2__", "boolean")
            print GJ
            break
        else:
            print TA

    while True:
        hard1_2 = raw_input("Fill in the blank for 3: ")
        if hard1_2 == "Else" or hard1_2 == "else":
            print "\n" + python_vocabulary_q5.replace("__1__", "If").replace("__2__", "boolean").replace("__3__",
                                                                                                         "else")
            print GJ
            break
        else:
            print TA

    while True:
        hard1_3 = raw_input("Fill in the blank for 4: ")
        if hard1_3 == "Or" or hard1_3 == "or":
            print "\n" + python_vocabulary_q5.replace("__1__", "If").replace("__2__", "boolean").replace("__3__",
                                                                                                         "else").replace(
                "__4__", "Or")
            print GJ
            break
        else:
            print TA
        # PYTHON V QUESTION 6 (HARD)
    while True:
        print python_vocabulary_q6
        hard2 = raw_input("Fill in the blank for 1: ")
        if hard2 == "While" or hard2 == "while":
            print "\n" + python_vocabulary_q6.replace("__5__", "While")
            print GJ
            break
        else:
            print TA
        # PYTHON V QUESTION 7 (HARD)
    while True:
        print python_vocabulary_q7
        hard3 = raw_input("Fill in the blank for 1: ")
        if hard3 == "List" or hard3 == "list":
            print "\n" + python_vocabulary_q7.replace("__6__", "list")
            print GJ
            break
        else:
            print TA

    while True:
        hard3_1 = raw_input("Fill in the blank for 1: ")
        if hard3_1 == "Mutation" or hard3_1 == "mutation":
            print "\n" + python_vocabulary_q7.replace("__6__", "list").replace("__7__", "Mutation")
            print GJ
            break
        else:
            print TA
    print "WOOF THAT WAS FUN!"
