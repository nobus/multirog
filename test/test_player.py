import os
import sys

path = os.getcwd()
sys.path.append(path)

from player import Player
from location import Location


def test_move_decorator():
    l = Location()
    p = Player("nobus", l)
    assert type(p.move_left()) == tuple
