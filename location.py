import random


class Location:
    def __init__(self, size=20, tree_perc=15):
        self.size = size
        self.tree_perc = tree_perc
        self.generate()

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
