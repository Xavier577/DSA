def linear_search(arr, search_val):  # O(n)
    search_val_idx = -1

    for idx, val in enumerate(arr):
        if val == search_val:
            search_val_idx = idx
            break

    return search_val_idx
