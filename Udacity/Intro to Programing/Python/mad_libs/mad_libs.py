# Specs
#   Does the game work the way it is supposed to?
#   Code review
#       Use of Variables with proper names
#       Functions -  no longer than 15 lines each, must have a comment line saying what it is doing
#       Use of Data Types - strings, list
#       Use of Code techniques - if, then, else, while, print, return, for loop
#   Game Review
#       3 or more levels to choose from
#       Fill in the blank prompt
#       When correct, prompt shows the same prompt with the blank filled in, else shows empty blanks again


# ---------------------------------------------------------
#   THERE IS ALSO ANOTHER VERSION: testerWORKING.py
# ---------------------------------------------------------


vocab1 = "__1__s are sequences of characters that are enclosed in quotes. We can enclose them with single or double quotes and assign them to variables. Placing two or more __1__s together using the + symbol. It will not have a space between the two __1__s. Adding numbers into __1__s is not possible, as you will get an error. This is called __2__. When you are indexing __1__s you will want to start the first letter with 0 and begin to count. The spaces between words and ends of sentences will need to be counted as well. Selecting a __4__ of a __1__ starting from the first expression, then stopping at the last. This will look like; <__1__>[ __3__ : __3__ ]. Please note that you do not have to have a number at the end of the :, but if you do not it will pull the rest of the __1__. You can also do [:] and this will pull the whole __1__."
vocabA1 = ["string", "concatenation", "expression", "subsequence"]

vocab2 = "__1__s take __2__ and return an __3__. __1__s are bits of code that you can call repetitively, and use over and over. __1__s can be defined once and used as many times as needed. There can be any number of __2__, but it has to have the number of __2__ the __1__ expects. When we do not have enough __2__ in the parameters then it will give an error message. __2__ are what you put into a __1__ to tell them what to do and how it is done. __3__ is the return and the result of the __1__. A __4__ Scope refers to a variable that you can make inside the __1__ and will be used, but does not exist outside of the __1__. A __5__ Scope is when a variable will be available at all times. It is best to avoid using __5__ variable because it is easier to make mistakes with these."
vocabA2 = ["function", "input", "output", "local", "global"]

vocab3 = "__1__ statements are used when controlling a function and how it is used. They are controlled by the __2__ results. If __2__ results are True then the function will continue like normal. If __2__ results are False then it will stop and move to the __3__ statements. __4__ statements are used inside of the __1__ statements, they are used when comparing two or more similar test values. __5__ Statements are used when you are wanting to create a loop for a function, this loop will be used until it returns a false statement. After the false statement it will then move to the next line of code. Loops are a very important concept of computer programming, that allow us to run blocks of code as many times as we wish without having repetition. __6__ are similar to how strings are sequences of characters, __6__s are sequences of anything! We can have __6__s of numbers, __6__s of characters, even __6__s inside of __6__s! And we can mix up the contents too so we can have __6__s containing many different things. One of the advantages of having data with structure (like in a __6__) is that you can take advantage of that structure! __7__ is modifying the existing object, so we can change the value of a __6__ after we have created it. Once a __6__ had been modified then we then we have to worry about other variables that might refer to the same object. This can only be done in __6__s."
vocabA3 = ["if", "boolean", "else", "or", "while", "list", "mutation"]

blanks = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]
replaced = []

def intro():
    """ Welcomes to the game. """
    start = (raw_input("\nWelcome to my Mad-Libs quiz!\nChoose a Difficulty: Easy, Medium, or Hard.\n> ").lower())
    if start == 'easy' or start == 'e':
        return quiz(vocab1, vocabA1)
    if start == 'medium' or start == 'm':
        return quiz(vocab2, vocabA2)
    if start == 'hard' or start == 'h':
        return quiz(vocab3, vocabA3)
    else:
        return intro()


def quiz(q_type, q_ans):
    """ Prints quiz, then splits it """
    print q_type
    count = 0
    q_type = q_type.split()
#    print q_type

    while count < 3:
        for word in q_ans:
            user_answer = raw_input('Fill in the blank \n{0}: \n'.format(count))
            if user_answer != q_ans[count]:
                print "Try Again"
                continue

            else:
                replaced.append(word)
                new_q = ' '.join(q_type).replace(blanks[count], user_answer)
                count += 1
                print new_q


intro()
