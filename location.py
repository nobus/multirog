import random


class Location:
    def __init__(self):
        self.size = 20
        self.generate()

    def generate(self):
        self.loc = []
        for y in xrange(0, self.size):
            self.loc.append([])
            for x in xrange(0, self.size):
                self.loc[y].append(0)

    def get(self, y=None, x=None):
        if x and y:
            return self.log[y][x]
        else:
            return self.loc
