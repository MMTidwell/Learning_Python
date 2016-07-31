# Rules for if statement
#   if statements must have an else
#   if else is not intended for use, you must use a die statement (died("blah"))
#   never nest more than 2 deep, 2nd if must use another function
#   treat if statements like paragraphs (put blank lines before and after each)
#   keep boolean simple, if they get complicated turn them into variables that can be called on

# Rules for loops
#   only use a while loop if loop needs to be endless
#   use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop

# Tips for debugging
#   don't use a debugger
#   use print to help debug
#   check code often

# Study drill
#   list
#   functions
#   modules
#   draw out map
#   try coding


from sys import exit
import random

# LISTS
y_n = ['Y', 'or', 'N']
doors = [1, 2, 3]

# VARIABLES
print "\nWelcome to the dungeon!\nBut first we must ask what is your name?"
name = raw_input("> ")

ready = "Are you ready to play"
open_door = "You reach out and open the door.\nWhat lies ahead is unbelievable."
vines = "What am I?"  # THIS WILL TURN INTO A LIST IN VINES()
door_num = "1, 2, or 3."
correct = "You are correct you can now pass."
wrong = "You have guessed {} times."

empty = """\nYou have now entered an almost empty room. The only thing in here seems to be the little gnome
made of clay. You reach out to pick the little guy up and suddenly he springs to life. He begins to
speak. "Why hello {}, I have been waiting for you. In order for you to pass you will need to
answer this question. What is the solution? 8.9 < 9\"""".format(name)
snake = """\nYou have crawled thorough the tunnel and have come to a forest. You begin to look around and find
a snake. You find comfort in the snake being there and begin to talk to it. Then, it talks back!! "Hello {}
you have made it to the forest. There is a door over there hidden with vines. I will give you the key to it if you
can answer my question. How many doors were there when you woke?\"""".format(name)

bright = """\nYou have come to a very bright room, so bright that you can not see. You hear a voice saying:
'Hello {}, it seems that the light is too bright for your eyes. I will turn them down if you can answer my
question. How do you write 573 divided by 2 with the remainder showing?'""".format(name)
blue = """\nYou see a blue door and open it, there is a pink flamingo flying around. Suddenly the flamingo fly's
right by you and picks you up. 'Well hello there {}! I will fly you to the wale over there if you can tell me
how to turn a string into a integer.'""".format(name)
sea = """\n'You have made it very far {}. Your last test is to guess what number I am thinking of. It will be between 1
and 10.'""".format(name)

dark = """\nYou have come to a dark room. Something fly's by your ear and you can see that it is holding light.
It's a fairy!! 'Well if it is'nt for {}! I would love to show you the large door over there, but I must ask you
what is the name for the result of True or False answers?!'""".format(name)
large = """\nYou have come to the large door, and open it. Just on the other side is a massive dog that is chained to
the ground. He does not look pleased at all. 'What are you doing here?! GO AWAY!' You plead with him, finally he
caves. 'How do you check if an input is a number in python?'"""
gold = """\nYou have now come upon a golden door, its locked. Bummer! So you look around and see on a stone a clue.
It says 'Say aloud what %r, %s, and %d are.'"""


def welcome():
    print "Well, hello {}.\n".format(name)
    play()


def join(a):
    print ' '.join(a)


def play():
    print ready
    join(y_n)
    info = raw_input("> ")

    if info == y_n[0]:
        print "Let's get started then.\n"
        starting_point()
    elif info == y_n[2]:
        print "Your loss, not mine.\n"
        exit(0)
    else:
        print "Learn to read and type.\n"
        play()


def starting_point():
    print "You awaken from a deep sleep in a room with 3 doors. \nWhich do you choose?"
    print door_num
    info = int(raw_input("> "))
    print open_door

    if info == doors[0]:
        empty_room()
    elif info == doors[1]:
        bright_room()
    elif info == doors[2]:
        dark_room()
    else:
        print "Type in a number.\n"
        starting_point()


def game_int():
    guess = 0
    guesses = []

    while len(guesses) < 3:
        ans = int(raw_input('> '))
        if ans == 9:
            print correct
            tunnel()
        elif ans == len(doors):
            print correct
            vine()
        else:
            guess += 1
            guesses.append(ans)
            print wrong.format(len(guesses))
    else:
        print "You slip and fall to your death!"
        exit(0)


def game_str():
    guess = 0
    guesses = []

    while len(guesses) < 3:
        ans = raw_input('> ')
        if ans == 'boolean':
            print correct
            large_door()
        elif ans == "573 / 2.0":
            print correct
            blue_door()
        elif ans == "int()":
            print correct
            wale()
        elif ans == ".isdigit()":
            print correct
            gold_door()
        elif ans == "a list":
            print correct
            gold_room()
        elif ans == "conversion":
            print correct
            gold_room()
        else:
            guess += 1
            guesses.append(ans)
            print wrong.format(len(guesses))
    else:
        print "You slip and brake your ankle, you die!"
        exit(0)


def wale():
    secret_number = random.randint(1, 10)
    guesses = []
    print sea

    while len(guesses) < 5:
        guess = int(raw_input("> "))
        if guess == secret_number:
            print "The wale screams..."
            for i in doors:
                print i
                i += 1
            print "Blastoff!!\nYou go flying through the air and finally reach land."
            gold_room()
        elif guess > secret_number:
            print "You guessed too high."
        else:
            print "You guessed too low."
        guesses.append(guess)
    else:
        print "You have guessed too many times, the wale is not pleased and digests you."
        exit(0)


def empty_room():
    print empty
    game_int()


def bright_room():
    print bright
    game_str()


def dark_room():
    print dark
    game_str()


def tunnel():
    print snake
    game_int()


def blue_door():
    print blue
    game_str()


def large_door():
    print large
    game_str()


def vine():
    print "The key seems to fit, but will not turn. There seems to be something carved in the door. It says:"
    print vines.split(' ')
    game_str()


def gold_door():
    print gold
    game_str()


def gold_room():
    print "\nYou have come to the room filled with gold, it is all yours!!"
    exit(0)


welcome()
