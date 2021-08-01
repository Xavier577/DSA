def bubble_sort(array):  # O(n^2)
    length = len(array)
    for i in range(length-1):
        for j in range(length - i - 1):
            if array[j] > array[j+1]:  # check if left index is greater than right index
                # swap heigher value for lower value
                array[j+1], array[j] = array[j], array[j+1]

    return array
