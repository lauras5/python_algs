"""
    MergeSort:  Time Complexity
                    Best:   O(nlog(n))
                    Worst:  O(nlog(n))
                Space Complexity:
                    Worst:  O(n)

"""


def mergeSort(arr):
    if len(arr) > 1:
        # find mid
        mid = len(arr) // 2
        # left elements
        left = arr[:mid]
        # right elements
        right = arr[mid:]

        # recursively call to order
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            # add smaller # to temp arr
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # checking for leftover elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
