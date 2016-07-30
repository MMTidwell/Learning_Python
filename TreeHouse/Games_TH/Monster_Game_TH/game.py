# Import the classes that you will need for game
from charcter import Character
from monster import Dragon
from monster import Troll
from monster import Goblin
import sys


# crate a class to play the game
class Game(object):
    # setting up who's turn it is and determine if the game is over by who is dead
    def setup(self):
        # triggers the name and weapon
        self.player = Character()
        # picks monster
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon(),
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            # retrieves next monster form list in class game under self.monsters list
            # .pop(0) removes first item in list not the last
            # Will throw and exception if it is the last monster, try block is needed
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        # check to see if the monster attacks
        # if so tell the player
        # check to see if the player wants to dodge,
        # if so see if the dodge is successful
        # if it is, move on
        # If its not, remove one player hit_point
        # if the monster is not attacking tell that ot the player too
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))
            if raw_input("Would you like to dodge? y or n? ").lower() == 'y':
                if self.player.dodge():
                    print("You dodged the attack!")
                else:
                    print("You got hit anyways.")
                    self.player.hit_points -= 1
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.hit_points -= 1
        else:
            print("{} is not attacking this turn.".format(self.monster))

    def player_turn(self):
        # let player attack, rest, or quit
        # if they attack
        # see if the attack is successful
        # if successful see if monster dodges
        # if not dodged subtract the right num of hit_points from the mosnter
        # if not a good attack, tell the player
        # if they rest
        # call the player.rest() method
        # if they quit, exit the game
        # if they pick anything else, re-run this method
        player_choice = raw_input("Would you like to [A]tack, [R]est, [Q]uit? ").lower()
        if player_choice == 'a':
            print("You're attacking {}!".format(self.monster))

            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged you're attack.".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You hit {} with your {}.".format(self.monster, self.player.weapon))
            else:
                print("You missed")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        # if monster has no more hit_points
        # up the players experience
        # print message
        # get a new monster
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("You killed {}".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
        while self.player.hit_points and (self.monster or self.monsters):
            print("\n" + '=' 20)
            print(self.player)
            self.monster_turn()
            print("\n" + '=' * 20)
            self.player_turn()
            self.cleanup()
            print("\n" + '=' * 20)

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You loose!")
        sys.exit()

print Game()
