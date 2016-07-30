from __future__ import print_function
import os
from random import choice
import sys


from moves import Rock, Paper, Scissors


def convert_move(move):
    if move == 'r':
        return Rock()
    elif move == 'p':
        return Paper()
    elif move == 's':
        return Scissors()


class Game:
    def __init__(self, player, rounds=3):
        self.rounds = rounds
        self.player = player
        self.score = [0, 0]

    def summary(self, title):
        print("\n{}".format(title))
        print("-"*len(title))
        print("{}: {}".format(self.player, self.score[0]))
        print("Computer: {}\n".format(self.score[1]))

    def get_move(self, move=None):
        move = move or input("[R]ock, [P]aper, [S]cissors? ").lower()
        if move == 'q':
            print("Bye!")
            sys.exit()
        elif move not in list('rps'):
            return self.get_choice()
        return convert_move(move)

    def game_round(self):
        player_move = self.get_move()
        computer_move = convert_move(choice(list('rps')))
        if player_move > computer_move:
            self.score[0] += 1
            print("\nYou won that round, {}!".format(self.player))
        elif computer_move > player_move:
            self.score[1] += 1
            print("\nYou lost that round, {}!".format(self.player))
        else:
            print("\nYou tied!")
        self.summary("Current score")

    def game_over(self):
        if self.score[0] > self.score[1]:
            print("{} wins!".format(self.player))
        else:
            print("{} loses!".format(self.player))
        self.summary("Final score")

    def get_choice(self):
        pass


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    game = Game(player=input("What's your name? "))

    while 3 not in game.score:
        game.game_round()
    else:
        game.game_over()
