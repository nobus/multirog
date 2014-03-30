import random


class Location:
    def __init__(self):
        self.size = 20
        self.generate()

    def generate(self):
        self.loc = []
        for y in xrange(0, self.size):
            a = map(lambda x: 0, xrange(0, self.size))
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
