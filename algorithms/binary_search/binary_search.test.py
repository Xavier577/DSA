import unittest
from binary_search import binary_search, recursive_binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(binary_search(arr, 1), 0, "should be 0")
        self.assertEqual(binary_search(arr, 2), 1, "should be 1")
        self.assertEqual(binary_search(arr, 3), 2, "should be 2")
        self.assertEqual(binary_search(arr, 4), 3, "should be 3")
        self.assertEqual(binary_search(arr, 5), 4, "should be 4")
        self.assertEqual(binary_search(arr, 6), 5, "should be 5")
        self.assertEqual(binary_search(arr, 7), 6, "should be 6")
        self.assertEqual(binary_search(arr, 8), 7, "should be 7")
        self.assertEqual(binary_search(arr, 9), 8, "should be 8")
        self.assertEqual(binary_search(arr, 10), 9, "should be 9")
        self.assertEqual(binary_search(arr, 11), -1, "should be -1")

    def test_recursive_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(recursive_binary_search(arr, 1), 0, "should be 0")
        self.assertEqual(recursive_binary_search(arr, 2), 1, "should be 1")
        self.assertEqual(recursive_binary_search(arr, 3), 2, "should be 2")
        self.assertEqual(recursive_binary_search(arr, 4), 3, "should be 3")
        self.assertEqual(recursive_binary_search(arr, 5), 4, "should be 4")
        self.assertEqual(recursive_binary_search(arr, 6), 5, "should be 5")
        self.assertEqual(recursive_binary_search(arr, 7), 6, "should be 6")
        self.assertEqual(recursive_binary_search(arr, 8), 7, "should be 7")
        self.assertEqual(recursive_binary_search(arr, 9), 8, "should be 8")
        self.assertEqual(recursive_binary_search(arr, 10), 9, "should be 9")
        self.assertEqual(recursive_binary_search(arr, 11), -1, "should be -1")


if __name__ == "__main__":
    unittest.main()
