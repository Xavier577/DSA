def bubble_sort(array: list[int]) -> list[int]:  # O(n^2)
    length = len(array)
    for i in range(length - 1):
        for j in range(length - i - 1):
            left = array[j]
            right = array[j + 1]
            if left > right:  # check if left index is greater than right index
                # swap heigher value for lower value
                array[j + 1], array[j] = left, right

    return array
