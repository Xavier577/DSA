from linear_search import linear_search
import unittest


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 1), 0, "Should be 0")
        self.assertEqual(linear_search(arr, 2), 1, "Should be 1")
        self.assertEqual(linear_search(arr, 3), 2, "Should be 2")
        self.assertEqual(linear_search(arr, 4), 3, "Should be 3")
        self.assertEqual(linear_search(arr, 5), 4, "Should be 4")
        self.assertEqual(linear_search(arr, 6), -1, "Should be -1")


if __name__ == "__main__":
    unittest.main()
