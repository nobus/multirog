import random


class Location:
    def __init__(self, loc_x, loc_y, world_size, size=32, tree_perc=15):
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.world_size = world_size

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

    def get(self, x=None, y=None):
        if x is not None and y is not None:
            try:
                return self.loc[x][y]
            except Exception, e:
                print e
                return None
        else:
            return self.loc

    def get_position_in_world(self):
        return self.loc_x, self.loc_y

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

    def location_up(self, x, y):
        if self.loc_y == 0:
            loc_y = self.world_size - 1
        else:
            loc_y = self.loc_y - 1

        return self.loc_x, loc_y, x, self.size - 1

    def location_down(self, x, y):
        if self.loc_y == self.world_size - 1:
            loc_y = 0
        else:
            loc_y = self.loc_y + 1

        return self.loc_x, loc_y, x, 0

    def location_left(self, x, y):
        if self.loc_x == 0:
            loc_x = self.world_size - 1
        else:
            loc_x = self.loc_x - 1

        return loc_x, self.loc_y, self.size - 1, y

    def location_right(self, x, y):
        if self.loc_x == self.world_size - 1:
            loc_x = 0
        else:
            loc_x = self.loc_x + 1

        return loc_x, self.loc_y, 0, y

    def next_location(self, direction, x, y):
        if direction == "up" and y < 0:
            return self.location_up(x, y)
        elif direction == "down" and y >= self.size:
            return self.location_down(x, y)
        elif direction == "left" and x < 0:
            return self.location_left(x, y)
        elif direction == "right" and x >= self.size:
            return self.location_right(x, y)
        else:
            return None, None, 0, 0

    def get_path(self, x, y):
        try:
            if self.loc[x][y] == 0:
                return True
            else:
                return False
        except:
            return False
