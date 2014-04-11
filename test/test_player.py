import sys

path = "/Users/nobus/develop/multirog"
sys.path.append(path)

from player import Player


def test_move_decorator():
    p = Player("nobus", 5, 10, 20)
    assert type(p.move_left()) == tuple
