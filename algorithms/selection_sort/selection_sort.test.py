from selection_sort import selection_sort
import unittest


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_1(self):
        unsorted_arr = [5, 3, 1, 2, 4]

        sorted_arr = [1, 2, 3, 4, 5]

        self.assertListEqual(selection_sort(unsorted_arr), sorted_arr, "should be sorted")

    def test_selection_sort_2(self):
        unsorted_arr = [5, 1, -6, 2, 4, 3, 1, -3, 0]

        sorted_arr = [-6, -3, 0, 1, 1, 2, 3, 4, 5]

        self.assertListEqual(selection_sort(unsorted_arr), sorted_arr, "should be sorted")


if __name__ == "__main__":
    unittest.main()
