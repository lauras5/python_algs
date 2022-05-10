"""
    Quicksort:  Time Complexity
                    Best:   O(log(n))
                    Worst:  O(n^2)
                Space Complexity:
                    Worst:  O(log(n))

    4, 2, 7, 3, 1, 6
    pivot = 4

"""


def quickSort(arr):
    elements = len(arr)     # get number of elements
    # Base case
    if elements < 2:        # if only zero or one element return original array
        return arr

    pivot = 0    # Position of the partitioning element

    for i in range(1, elements):            # Partitioning loop
        if arr[i] <= arr[0]:                # compare, if new position is less than prev
            pivot += 1           # swap
            temp = arr[i]
            arr[i] = arr[pivot]
            arr[pivot] = temp

    temp = arr[0]
    arr[0] = arr[pivot]
    arr[pivot] = temp                            # Brings pivot to it's appropriate position

    left = quickSort(arr[0:pivot])               # Sorts the elements to the left of pivot
    right = quickSort(arr[pivot + 1:elements])   # sorts the elements to the right of pivot

    arr = left + [arr[pivot]] + right            # Merging everything together

    return arr


array_to_be_sorted = [4, 2, 7, 3, 1, 6]
print("Original Array: ", array_to_be_sorted)
print("Sorted Array: ", quickSort(array_to_be_sorted))
# output:
# Original Array:  [4, 2, 7, 3, 1, 6]
# Sorted Array:  [1, 2, 3, 4, 6, 7]
