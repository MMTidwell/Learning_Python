# NOTES FOUND ONLINE!
# https://gist.github.com/anonymous/91865cb266659c2c3f24#file-gistfile1-py-L67

# BUILD IMPORTS FOR GAME
from random import randint


# VARIABLES FOR GAME
intro = 'The Gothons of Planet Parcal #25 have invaded your ship and destroyed your entire crew. You are the last \n' \
        'surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it\n' \
        'in the bridge, and blow the ship up after getting into and escape pod.\n\n' \
        'You\'re running down the central corridor to the Weapons when a Gothon jumps out, red scaly skin, \n' \
        'dark grimy teeth, and evil clown costume flowing around his hate filled body. He\'s blocking the door to \n' \
        'the Armory and about to pull a weapon to blast you.\n'
shoot = '\nQuick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and\n' \
        'moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. \n' \
        'This completely ruins his brand new costume his mother bought him, which makes him fly into a rage and \n' \
        'blast you repeatedly in the face until your dead. Then he eats you.\n'
dodge = '\nLike a world class boxer you dodge, weave, slip and slide right as the Gothon\'s blaster cranks a\n' \
        'laser past your head. In the middle of your artful dodge your foot slips and you band you head on the\n' \
        'metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and\n' \
        'eats you.\n'
joke = '\nLucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: \n' \
       '\nLbhe zbgure vf sng, jura fru fvgf nebaq gur ubhfr, fur fvgr nebhaq gur ubhgfr. \n\nThe Gothon stops, \n' \
       'tries not to laugh, then busts out laughing and can\'t move. While he\'s laughing you run up and shoot\n' \
       'him square in the head putting him down, then jump through the Weapon Armory door.\n'
armor = '\nYou do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be\n' \
        'hiding. It\'s dead quiet, too quiet. You stand up and run to the far side of the room and find the \n' \
        'neurton bomb in its container. There\'s a keypad lock on the box and you need the code to get the bomb \n' \
        'out. If you get the code wrong 10 times then teh lock closes forever and you can\'t get the bomb. The \n' \
        'code is 3 digits.\n'
secret = '\nYou have entered the override key! The container clicks open and the seal breaks, letting gas out.\n' \
         'You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right\n' \
         'spot.\n'
unlock = '\nThe container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run\n' \
         'as fast as you can to the bridge where you must place it in the right spot.\n'
locked = '\nThe container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run\n' \
         'as fast as you can to the bridge where you must place it in the right spot.\n'
bridge = '\nYou burst onto the Bridge with the neutron destruct bomb under you arm and surprise 5 Gothons who are\n' \
         'trying to take control of the ship. Each of them has an even uglier clown costume than the last. They \n' \
         'haven\'t pulled their weapons out yet, as they see the active bomb under your arm and don\'t want to set \n' \
         'it off.\n'
throw = "\nIn a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop \n" \
        "it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically \n" \
        "try to disarm the bomb. You die knowing they will probably blow up when it goes off.\n"
place = "\nYou point you blaster at the bomb under your arm and teh Gothons put their hands up and start to sweat.\n" \
        "You inch backward to the door, open it and then carefully place the bomb on the floor, pointing your \n" \
        "blaster at it. You then jump back through the door, push the close button and blast the \n" \
        "lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this \n" \
        "tin can.\n"
pod = '\nYou rush through the ship desperately trying to make it to the escape pod before the whole ship \n' \
      'explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. \n' \
      'You get to the chamber with the escape pods, and now need to pick one and to take. There\'s 5 pods, ' \
      'which one do you take?\n'

# Scene is the base class for the game as it is kind of like blue-prints or structure for the game. Other classes will
#  draw from it to give it an enter(self) method.
class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"


# Engine => is a class
class Engine(object):
    # __init__ => will be invoked when the class is instantiated (when we start to build)
    # scene_map => is an instance (object), and instances are the house (building blocks)
    # We can change scene_map for different situations and they will not effect the other. ex. one house my be blue
    #   while the other is green but structurally they are the same since they are from the same class.
    # self => parameter will be passes as a reference to the instance that is being created. When self is being
    #   called it will only change that instance the one time and not the others created before or after it.
    # def __init__ line => logs, reports, and assigns activity and assign as an attribute
    def __init__(self, scene_map):
        # scene_map is stored as an attribute
        self.scene_map = scene_map

    def play(self):
        # Calls the 'opening_scene' method on the Map instance will return a reference to the first Scene in the
        #   instance's 'scenes' and  'dict'
        current_scene = self.scene_map.opening_scene()

        # While true loop => will run until called by 'enter' or 'next_scene' throw an exception.
        while True and current_scene is not None:
            print "\n--------"
            # When scene instance is referenced by 'current_scene' will have its 'enter' method invoked, which returns
            #   a 'str' with the name of the next scene it will go to.
            next_scene_name = current_scene.enter()
            # Calls on 'map.next_scene' method and pass the scene name from the above call to 'enter'. This returns a
            #   'scene' object.
            current_scene = self.scene_map.next_scene(next_scene_name)


# Inherits from Scene class. Since Scene calls for a enter() method, it must be used here as well
class Death(Scene):
    # quips belongs to Death class
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."]

    # enter(self) is used due to parent class calling for it
    def enter(self):
        # Can use 'print random.choice(self.quips)
        # Picks random index of quips
        print Death.quips[randint(0, len(self.quips) - 1)]


class CentralCorridor(Scene):
    def enter(self):
        print intro

        action = raw_input('Actions: shoot, dodge!, tell a joke.\n> ')

        if action == 'shoot':
            print shoot
            # key of map.scene, allowing the scene to be looked up as necessary
            return 'death'

        elif action == 'dodge!':
            print dodge
            return 'death'

        elif action == 'tell a joke':
            print joke
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!\n"
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print armor

        # Could write 'code = str(randint(100-999)
        code = '%d%d%d' % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 1

        while int(guess) != code and guesses < 10:
            if int(guess) == 333:
                print secret
                return 'the_bridge'
            else:
                print "BZZZZDDDD!\n"
                guesses += 1
                guess = raw_input("[keypad]> ")

        if int(guess) == code:
            print unlock
            return 'the_bridge'
        else:
            print locked
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print bridge

        action = raw_input("Actions: throw the bomb or slowly place the bomb ")

        if action == 'throw the bomb':
            print throw
            return 'death'

        elif action == 'slowly place the bomb':
            print place
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!\n"
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print pod

        good_pod = randint(1, 5)
        guess = raw_input('[pod #]> ')
        guesses = 1

        if int(guess) == 3:
            print '\nYou jump into pod %s and hit the eject button. The pod easily slides out into space heading to\n' \
                  'the planet below. As it flies into the planet, you look back and see your ship implode then \n' \
                  'explode like a bright star, taking out the Gothon ship at the same time. You won!\n' % guess
            return None

        while guesses == 1:
            if int(guess) != good_pod:
                print '\nYou jump into pod %s and hit the eject button. The pod escapes out into the void of space,\n' \
                      'then implodes as the hull ruptures, crashing your body into jam jelly.\n' % guess
                return 'death'
            else:
                print '\nYou jump into pod %s and hit the eject button. The pod easily slides out into space \n' \
                      'heading to the planet below. As it flies into the planet, you look back and see your ship \n' \
                      'implode then explode like a bright star, taking out the Gothon ship at the same time. You\n' \
                      'won!\n' % guess
                return None


class Map(object):
    scenes = {
        'laser_weapon_armory': LaserWeaponArmory(),
        'central_corridor': CentralCorridor(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
    }

    # Only used to tell what scene will be played first
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Looks up the scene object that is associated with the name passed as an argument
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    # Made to make things read better
    def opening_scene(self):
        return self.next_scene(self.start_scene)

# Create a map object, pass a name for the scene as an argument. The Map.__init__ method will be invoked with a
#   reference to the object being created and the string will be stored as an attribute of the instance to be used by
#   the opening_scene method
# If 'central_corridor' is changed to another scene name in scenes dict then it will start the game at the point.
a_map = Map('central_corridor')
# Instantiate the Engine.__init__ to call and pass a reference to the instance that called the method ('a_game'),
# and the 'Map' to be used. Have to define in order to take 'a-map' to Engine class
a_game = Engine(a_map)
# Uses the white true loop in Engine and runs the game
a_game.play()
