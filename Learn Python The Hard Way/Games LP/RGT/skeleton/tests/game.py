class Room(object):
    """ main class, __init__ is setting up name and description and path in order to call on it later. Path is left
    empty so it can be filled in as the game goes on. """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        """ def go => returns paths and gets the direction or None. """
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        """ def add_paths => updates paths """
        self.paths.update(paths)