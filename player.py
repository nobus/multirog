

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.direction = "down"

        self.location = location
        self.location.register_player(self.name)
        self.x, self.y = self.location.search_free_position()

    def get_location(self):
        return self.location

    def get_position(self):
        return (self.x, self.y, self.get_direction())

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def set_location(self, location):
        self.location = location

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == self.get_direction():

            if direction == "up":
                new_y = self.y - 1
                new_x = self.x
            elif direction == "down":
                new_y = self.y + 1
                new_x = self.x
            elif direction == "left":
                new_y = self.y
                new_x = self.x - 1
            elif direction == "right":
                new_y = self.y
                new_x = self.x + 1

            next_loc_x, next_loc_y, nx, ny = self.location.next_location(direction, new_x, new_y)

            if next_loc_x is None and next_loc_y is None:
                if self.location.get_path(new_x, new_y):
                    self.set_position(new_x, new_y)
            else:
                return next_loc_x, next_loc_y, nx, ny
        else:
            self.set_direction(direction)

        return -1, -1, 0, 0
