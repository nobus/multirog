import os
import sys

path = os.getcwd()
sys.path.append(path)

from world import World


def test_world_generator():
    w = World()
    size = w.size
    l = w.locations[size - 1][size - 1]
    assert l.get()


def test_add_player():
    n = "nobus"
    w = World()
    w.add_player(n)
    assert w.get_player(n) is not None


def test_del_player():
    n = "nobus"
    w = World()
    w.add_player(n)
    w.del_player(n)
    assert w.get_player(n) is None
