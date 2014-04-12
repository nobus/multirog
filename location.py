import random


class Location:
    def __init__(self, size=32, tree_perc=15):
        self.size = size
        self.tree_perc = tree_perc
        self.generate()

        self.free_position = self.search_free_position()

        self.current_players = []

    def get_tree(self):
        x = random.randint(0, 99)
        if x <= self.tree_perc:
            return 1
        else:
            return 0

    def generate(self):
        self.loc = []
        for y in xrange(0, self.size):
            a = map(lambda x: self.get_tree(), xrange(0, self.size))
            self.loc.append(a)

    def get(self, y=None, x=None):
        if x and y:
            try:
                return self.loc[y][x]
            except Exception, e:
                print e
                return None
        else:
            return self.loc

    def search_free_position(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            if self.loc[x][y] == 0:
                return x, y

    def get_free_position(self):
        return self.free_position

    def register_player(self, name):
        if name not in self.current_players:
            self.current_players.append(name)

    def unregister_player(self, name):
        if name in self.current_players:
            self.current_players.remove(name)

    def get_current_players(self):
        return self.current_players
