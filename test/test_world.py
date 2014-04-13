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


def test_get_default_location():
    w = World()
    l = w.get_location()
    assert l


def test_get_location():
    w = World()
    size = w.size
    l = w.get_location(size - 1, size - 1)
    assert l


def test_get_map_location():
    w = World()
    m = w.get_map_location()
    assert type(m) == list


def test_get_players_from_location():
    w = World()
    w.add_player("nobus")
    w.add_player("bobus")
    w.add_player("popus")

    p = w.get_players_from_location()
    assert len(p) == 3

    w.del_player("bobus")
    p = w.get_players_from_location()
    assert len(p) == 2

    assert len(p[0]) == 3
    name = p[0][0]
    assert name == "nobus" or name == "popus"


def test_move_player():
    w = World()
    w.add_player("nobus")

    w.move_player("nobus", "left")

    p = w.get_player("nobus")
    d = p.get_direction()
    assert d == "left"
