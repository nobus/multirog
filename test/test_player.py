import os
import sys

path = os.getcwd()
sys.path.append(path)

from player import Player
from location import Location


def test_move():
    loc = Location(1, 1, 3)
    player = Player("nobus", loc)

    loc_x, loc_y, x, y = player.move("down")
    assert loc_x == -1

    x, y, d = player.get_position()
    assert d == "down"
