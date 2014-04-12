from location import Location
from player import Player


class World:
    def __init__(self, size=3):
        self.size = size
        self.generate()

        self.start_location = self.locations[self.size / 2][self.size / 2]
        self.players = {}

    def generate(self):
        self.locations = []

        for y in xrange(0, self.size):
            a = map(lambda x: Location(), xrange(0, self.size))
            self.locations.append(a)

    def add_player(self, name):
        self.players[name] = Player(name, self.start_location)

    def del_player(self, name):
        if name in self.players:
            del self.players[name]

    def get_player(self, name):
        return self.players.get(name, None)
