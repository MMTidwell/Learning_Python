from __future__ import print_function
import random
import logging

# logging makes it to where the player does not see behind the scene
logging.info("You wont see this!")
# This one prints...idk why
logging.warn("OH NO")
# if you want to print to a file and not the player
# basicConfig- filename= tells what file to log into, level= tells the logger what level to look at
#   Critical, Error, Warning, Info, Debug, Notset
logging.basicConfig(filename='game.log', level=logging.DEBUG)
# logging message
logging.debug("Debug message goes here.")
logging.warning("Warning messages goes here.")


player = {'location': None, 'path': []}
# Coded map/grid for game
cells = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
    # monster
    # door
    # start
    monster = random.choice(cells)
    door = random.choice(cells)
    start = random.choice(cells)

    # if monster, door, or start at teh same do it again
    if monster == door or monster == start or door == start:
        monster, door, start = get_locations()

    return monster, door, start


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # player == x and y
    # If player y == 0, remove LEFT
    # If player x == 0, remove UP
    # If player y == 2, remove RIGHT
    # If player x == 2, remove DOWN
    if player in [(0, 0), (1, 0), (2, 0)]:
        moves.remove('LEFT')
    if player in [(0, 0), (0, 1), (0, 2)]:
        moves.remove('UP')
    if player in [(0, 2), (1, 2), (2, 2)]:
        moves.remove('RIGHT')
    if player in [(2, 0), (2, 1), (2, 2)]:
        moves.remove('DOWN')
    return moves


def move_player(player, move):
    # Get player current location
    # If move is left, y - 1
    # If move is right, y + 1
    # If move is up, x - 1
    # If move is down, x + 1
    # Player == x and y
    x, y = player['location']
    player['path'].append((x, y))
    if move == 'LEFT':
        player['location'] = x, y - 1
    elif move == 'UP':
        player['location'] = x - 1, y
    elif move == "RIGHT":
        player['location'] = x, y + 1
    elif move == "DOWN":
        player['location'] = x + 1, y
    return player


def draw_map():
    print (" _ _ _")
    tile = '|{}'
    for idx, cell in enumerate(cells):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player['location']:
                print (tile.format('X'), end='')
            elif cell in player['path']:
                print (tile.format('.'), end='')
            else:
                print (tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            elif cell in player['path']:
                print(tile.format('.|'), end='')
            else:
                print(tile.format('_|'))


monster, door, player['location'] = get_locations()
logging.info('monster: {}; door: {}; player: {}'.format(monster, door, player['location']))


while True:
    moves = get_moves(player['location'])
    print("Welcome to the dungeon")
    print("You are currently in room {}".format(player['location']))
    draw_map()
    print("You can move {}".format(moves))
    print("Enter QUIT to quit.")

    move = input("> ").upper()

    if move == 'QUIT':
        break
        # If it is a good move change player position
        # If a bad move do nothing
        # if the player position is the door, they win
        # if the player position is the monster, they loose
        # Otherwise continue
    if move in moves:
        player = move_player(player, move)
    else:
        print ("Walls are hard stop walking into them.\n")
        continue

    if player == door:
        print ("You escaped!\n")
        break
    elif player == monster:
        print ("You were eaten by the monster!\n")
        break
