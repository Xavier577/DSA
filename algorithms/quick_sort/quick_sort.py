def quick_sort(arr: list[int]) -> list[int]:
    arr_len = len(arr)
    low = 0
    high = arr_len - 1

    return sort_fn(arr, low, high)


def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def sort_fn(arr: list[int], low: int, high: int) -> list[int]:
    if low < high:
        partition_idx = partition(arr, low, high)

        sort_fn(arr, low, partition_idx - 1)

        sort_fn(arr, partition_idx + 1, high)

    return arr
