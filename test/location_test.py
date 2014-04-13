import os
import sys
import unittest

path = os.getcwd()
sys.path.append(path)


from location import Location


class LocationTest(unittest.TestCase):
    def setUp(self):
        self.loc = Location(0, 0, 3)

    def test_get(self):
        l = self.loc.get()
        self.assertTrue(l)

    def test_get_yx(self):
        x = y = self.loc.size - 1
        a = self.loc.get(y=y, x=x)
        self.assertIsNotNone(a)

    def test_search_free_position(self):
        x, y = self.loc.search_free_position()
        p = self.loc.get(x=x, y=y)
        assert p == 0

    def test_registred_players(self):
        self.loc.register_player("nobus")
        self.loc.register_player("bobus")

        p = self.loc.get_current_players()
        assert len(p) == 2

        self.loc.unregister_player("popus")
        p = self.loc.get_current_players()
        assert len(p) == 2

        self.loc.unregister_player("bobus")
        p = self.loc.get_current_players()
        assert len(p) == 1


def test_next_location():
    loc = Location(1, 1, 3)

    loc_x, loc_y, x, y = loc.next_location("up", 10, -1)
    assert loc_y == 0
    assert loc_x == 1

    loc_x, loc_y, x, y = loc.next_location("down", 10, loc.size + 1)
    assert loc_y == 2
    assert loc_x == 1

    loc_x, loc_y, x, y = loc.next_location("left", -1, 10)
    assert loc_x == 0
    assert loc_y == 1

    loc_x, loc_y, x, y = loc.next_location("right", loc.size + 1, 10)
    assert loc_x == 2
    assert loc_y == 1


def test_next_location2():
    loc = Location(0, 0, 3)

    loc_x, loc_y, x, y = loc.next_location("up", 10, -1)
    assert loc_y == 2
    assert loc_x == 0

    loc_x, loc_y, x, y = loc.next_location("left", -1, 10)
    assert loc_x == 2
    assert loc_y == 0


def test_next_location3():
    loc = Location(2, 2, 3)

    loc_x, loc_y, x, y = loc.next_location("down", 10, loc.size + 1)
    assert loc_y == 0
    assert loc_x == 2

    loc_x, loc_y, x, y = loc.next_location("right", loc.size + 1, 10)
    assert loc_x == 0
    assert loc_y == 2


if __name__ == '__main__':
    unittest.main()
