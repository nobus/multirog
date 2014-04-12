import os
import sys
import unittest

path = os.getcwd()
sys.path.append(path)


from location import Location


class LocationTest(unittest.TestCase):
    def setUp(self):
        self.loc = Location()

    def test_get(self):
        l = self.loc.get()
        self.assertTrue(l)

    def test_get_yx(self):
        x = y = self.loc.size - 1
        a = self.loc.get(y=y, x=x)
        self.assertIsNotNone(a)

    def test_search_free_position(self):
        x, y = self.loc.search_free_position()
        p = self.loc.get(y=y, x=x)
        assert p == 0

if __name__ == '__main__':
    unittest.main()
