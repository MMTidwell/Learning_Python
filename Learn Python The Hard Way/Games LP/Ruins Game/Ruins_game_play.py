from room_class import Grocery, FrontDoor, Roof, Death, Fight, CenterTown, Garage, HeadOut, LastFight, Castle
from monster_class import Sloth, Blob, Cyclops, Fairy, Beetle


class RunGame(object):
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()

        while True and current_room is not None:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)


class ClassToClass(object):
    rooms = {
        'fight': Fight(),
        'death': Death(),
        'grocery': Grocery(),
        'roof': Roof(),
        'front_door': FrontDoor(),
        'center_town': CenterTown(),
        'garage': Garage(),
        'head_out': HeadOut(),
        'last_fight': LastFight(),
        'castle': Castle(),
        'sloth': Sloth(),
        'blob': Blob(),
        'cyclops': Cyclops(),
        'fairy': Fairy(),
        'beetle': Beetle()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    @staticmethod
    def next_room(room_name):
        return ClassToClass.rooms.get(room_name)

    def opening_room(self):
        return self.next_room(self.start_room)


start = ClassToClass('grocery')
game = RunGame(start)
game.play()
