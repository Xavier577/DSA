def binary_search(input_array, value):  # O(log(n))
    right = 0
    left = input_array.__len__() - 1
    isPresent = False
    while right <= left:
        middle = (left + right) // 2
        if input_array[middle] == value:
            isPresent = True
            break
        if input_array[middle] < value:
            right = middle + 1
        if input_array[middle] > value:
            left = middle - 1
    return -1 if isPresent == False else middle


def recursive_binary_search(arr, search_val):
    return recursive_binary_search_fn(arr, 0, len(arr) - 1, search_val)


def recursive_binary_search_fn(arr, right, left, value):
    # Check base case
    if left >= right:
        middle = (left + right) // 2

        # If element is present at the middle itself
        if arr[middle] == value:
            return middle

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[middle] > value:
            return recursive_binary_search_fn(arr, right, middle - 1, value)

        # Else the element can only be present in right subarray
        else:
            return recursive_binary_search_fn(arr, middle + 1, left, value)

    else:
        # Element is not present in the array
        return -1
