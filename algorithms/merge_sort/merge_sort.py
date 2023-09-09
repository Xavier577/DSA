def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(arr) // 2
        L = arr[:r]
        M = arr[r:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1

        return arr


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
