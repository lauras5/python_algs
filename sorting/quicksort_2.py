def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if len(arr) < 2:
        return arr
    if low < high:
        prtn = partition(arr, low, high)
        quickSort(arr, low, prtn - 1)
        quickSort(arr, prtn + 1, high)


arr = [10, 7, 8, 9, 1, 5]
print("Unsorted array is:")
print(str(arr) + "\n")
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
print(str(arr) + "\n")
print("O-Notation: \n  Time complexity: O(log n)\n  Space complexity: O(log n)")
