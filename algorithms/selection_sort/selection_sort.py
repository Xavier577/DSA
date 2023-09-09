def selection_sort(arr: list[int]) -> list[int]:
    arr_len = len(arr)
    step = 0
    while step < arr_len:
        min_idx = step
        i = step + 1  # next step and up
        while i < arr_len:
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if arr[i] < arr[min_idx]:
                min_idx = i
            i += 1
        # put minimum element in correct position
        arr[step], arr[min_idx] = arr[min_idx], arr[step]

        step += 1
    return arr
