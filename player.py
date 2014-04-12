

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.x, self.y = self.location.search_free_position()
        self.direction = "down"

    def get_position(self):
        return (self.x, self.y, self.get_direction())

    def get_direction(self):
        return self.direction

    def turn_up(self):
        self.direction = "up"

    def turn_down(self):
        self.direction = "down"

    def turn_left(self):
        self.direction = "left"

    def turn_right(self):
        self.direction = "right"

    def _move(f):
        def m(self):
            f(self)
            return self.get_position()

        return m

    @_move
    def move_up(self):
        if self.get_direction() == "up":
            self.y -= 1
        else:
            self.turn_up()

    @_move
    def move_down(self):
        if self.get_direction() == "down":
            self.y += 1
        else:
            self.turn_down()

    @_move
    def move_left(self):
        if self.get_direction() == "left":
            self.x -= 1
        else:
            self.turn_left()

    @_move
    def move_right(self):
        if self.get_direction() == "right":
            self.x += 1
        else:
            self.turn_right()

    _move = staticmethod(_move)
