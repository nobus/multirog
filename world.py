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
        player = self.players.get(name, None)

        if player:
            loc = player.get_location()
            loc.unregister_player(name)
            del self.players[name]

    def get_player(self, name):
        return self.players.get(name, None)

    def get_location(self, x=None, y=None):
        if x is None:
            x = self.size / 2

        if y is None:
            y = self.size / 2

        if x < self.size and y < self.size:
            return self.locations[x][y]
        else:
            return None

    def get_map_location(self, x=None, y=None):
        location = self.get_location(x, y)
        return location.get()

    def get_players_from_location(self, x=None, y=None):
        ret = []
        location = self.get_location(x, y)
        players = location.get_current_players()

        for name in players:
            player = self.players[name]
            x, y, _ = player.get_position()
            ret.append((name, x, y))

        return ret
