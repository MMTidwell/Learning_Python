from nose.tools import *
from game import Room

def test_room():
    castle = Room('castle', 'This is the end of the game and you are celebrating saving the princess')
    assert_equal(castle.name, 'castle')
    assert_equal(castle.paths, {})

def test_map():
    grocery = Room('grocery', 'Beginning of game. You are getting groceries and get a call from the king to save the '
                              'princess. From her you can go to the roof or the front door.')
    roof = Room('roof', 'You reach a monster and have to fight, goes to center of town')
    front = Room('front_door', 'You reach a monster and have to fight, goes to center of town')
    center = Room('center', 'You have reached another monster and have to fight, goes to garage')
    garage = Room('garage', 'You have reached another monster and have to fight, goes to the gate')
    gate = Room('gate', 'You have reached the main boss. you must kill him in order to save her and return her home')
    castle = Room('castle', 'You have reached the end of the game and win the heart of the princess.')

    grocery.add_paths({'roof': roof, 'front': front})
    roof.add_paths({'center': center})
    front.add_paths({'center': center})
    center.add_paths({'garage': garage})
    garage.add_paths({'gate': gate})
    gate.add_paths({'castle': castle})

