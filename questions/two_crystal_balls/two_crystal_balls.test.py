import unittest
from two_crystal_balls import two_crystal_balls


class TestTwoCrystalBallsSolutions(unittest.TestCase):
    def test_lvl(self):
        floor_lvl = [False, False, False, False, False, True, True, True, True, True]

        self.assertEqual(two_crystal_balls(floor_lvl), 5, "should break at index 5")


if __name__ == "__main__":
    unittest.main()
