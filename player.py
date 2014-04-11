

class Player(object):
    def __init__(self, name, x, y, loc_size):
        self.name = name
        self.x = x
        self.y = y
        self.loc_size = loc_size

    def get_position(self):
        return (self.x, self.y)

    def _move(f):
        def m(self):
            f(self)
            return self.get_position()

        return m

    @_move
    def move_up(self):
        if self.y > 0:
            self.y -= 1

    @_move
    def move_down(self):
        if self.y < self.loc_size:
            self.y += 1

    @_move
    def move_left(self):
        if self.x > 0:
            self.x -= 1

    @_move
    def move_right(self):
        if self.x < self.loc_size:
            self.x += 1

    _move = staticmethod(_move)
