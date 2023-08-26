import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        unsorted_arr = [5, 3, 1, 2, 4]

        sorted_arr = [1, 2, 3, 4, 5]

        self.assertListEqual(bubble_sort(unsorted_arr), sorted_arr, "should be sorted")


if __name__ == "__main__":
    unittest.main()
