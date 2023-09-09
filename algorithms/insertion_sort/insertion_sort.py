def insertion_sort(arr: list[int]) -> list[int]:
    arr_len = len(arr)

    step = 0

    while step < arr_len:
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key

        step += 1

    return arr
