# DRAW FLOW CHART
# FIND KEY CONCEPTS
# CREATE CLASS HIERARCHY AND OBJECT MAP
# CODE THE CLASSES AND TEST
# RINSE AND REPEAT

# KEY CONCEPTS
#   Death- Where the player dies
#   Dungeon- Start of game, has gnome with guessing game to pass
#   Empty- find shovel, gnome fight, and dig out tunnel
#   Vines- find swarm of gnomes, bomb in pocket, runs to golden door
#   Golden- find door, answer 3 quiz
#   Treasure- treasure opens and coins flow out

# CLASS HIERARCHY
#   Maze (how to get from one point to the next)
#   Game (find what is needed to run game)
#   Room (rooms that we may enter)
#       enter()
#       Death- list of funny ways to die
#       Dungeon- scene 1
#       Empty- scene 2
#       Vines- scene 3
#       Golden- scene 4
#       Treasure- scene 5

# Tells you where you are in the game and where to go next
from random import randint


class Room(object):
    def enter(self):
        pass


# Runs the game
class Game(object):
    # Assigns activity and attributes
    def __init__(self, room_maze):
        self.room_maze = room_maze

    # Actually runs the game through
    def play(self):
        current_room = self.room_maze.opening_room()

        while True and current_room is not None:
            print '-' * 20
            next_room_name = current_room.enter
            current_room = self.room_maze.next_room(next_room_name)


class Death(Room):
    died = [
        'My mom can play better than you!',
        'Is it really that hard?!',
        'This is too simple to fail, but you managed to do that.'
    ]

    def enter(self):
        print Death.died[randint(0, len(self.died) - 1)]


class Dungeon(Room):
    def enter(self):
        print "You awake in a strange room with no idea how you have gotten there. The room is stale and dirty\n" \
              "with cob webs and you begin to shutter, thinking that they must be near. Soon you hear a small \n" \
              "giggle from behind you. Quick to the sound you jump and almost land on a little clay gnome. You \n" \
              "bend to pick the cute guy up and notice that he is covered in blood and caring an axe. The little\n" \
              "gnome says to you:\n\nI will let you go if you can guess what number I am thinking of. I'll give \n" \
              "you a hint, it is between 1 and 10. You have 3 guesses, choose wisely.\n "

        guess = raw_input('> ')
        guesses = 1
        numb = randint(1, 10)

        while int(guess) != numb and guesses < 3:
            if int(guess) == 33:
                print "\nHow ever did you know that?! You have used your mindtrickery...WITCH!!!! \n" \
                      "Quickly you run and find the door that was not there before, you open it and leave.\n"
                return 'empty'
            else:
                print 'Try again!'
                guesses += 1
                guess = raw_input('> ')

        if int(guess) == numb:
            print "\You my go through the door over there, but be weary of what lies ahead. For it is much worse then I."
            return 'empty'
        else:
            print "\nThe gnome starts to laugh again and starts flying around the room. You get dizzy and fall\n" \
                  "down the rabbit hole you go and die.\n"
            return 'death'


class Empty(Room):
    def enter(self):
        print "You have come to an empty room, everything is white. So white that you have to blink several times\n" \
              "before you can see anything. Finally your eyes adjust to the light and you find a shovel against \n" \
              "the wall. You have a choice to make, return to the gnome or dig a tunnel hoping to find\n" \
              "a way out of this mess.\n"

        answer = raw_input("\nChoose: gnome or dig: ")

        if answer == 'gnome':
            print "\nThe gnome is gone when you return, you decide to turn back to the empty room but the door \n" \
                  "is gone. You starve to death...\n"
            return 'death'
        elif answer == 'dig':
            print "\nYou have dug all night but you have chosen correctly and found a way outside where there is \n" \
                  "natural light, sound, and trees with fruit. You have been starving since you arrived at this \n" \
                  "place and have yet to eat. So you take rest only to hear a snake speak to you.\n"
            return 'Treasure'
        else:
            print "Did you read what you wrote?\n"
            return 'empty'


class Treasure(Room):
    def enter(self):
        print "\nAfter a long conversation with the snake you fall asleep. A hours later you awake to the snake \n" \
              "wrapping around you. You look around and find that the gnome has caught up to you and still\n" \
              "carrying the axe. You beg with the gnome for help but get nothing. As the snake is getting\n" \
              "tighter, you are loosing all your strength. Now you must do everything you can to survive.\n"

        answer = input("You grab the: gnome or stick ")

        if answer == "stick":
            print "\nWhile reaching for the stick the snake sees you and bites your head ofF!\n"
            return 'death'
        if answer == "gnome":
            print "\nYou grabbed the gnome in just enough time to stab the snake in the head with the gnomes\n" \
                  "hat. They both scream but you have beaten them both, and are now free. Soon you come to a door,\n" \
                  "thankfully it is unlocked and you find a helicopter to get you home.\n"
            return 'finished'


class Maze(object):
    rooms = {
        'dungeon': Dungeon(),
        'death': Death(),
        'empty': Empty(),
        'treasure': Treasure()
    }

    # Tells you where to start
    def __init__(self, starter_room):
        self.starter_room = starter_room

    # Tells you where to go next
    def next_room(self, room_name):
        return Maze.rooms.get(room_name)

    # Redefines next_room
    def opening_room(self):
        return self.next_room(self.starter_room)


a_map = Maze('dungeon')
a_game = Game(a_map)
a_game.play()
