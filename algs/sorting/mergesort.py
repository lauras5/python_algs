"""
    MergeSort:  Time Complexity
                    Best:   O(nlog(n))
                    Worst:  O(nlog(n))
                Space Complexity:
                    Worst:  O(n)

"""
import unittest

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

        return arr

class TestBucketSort(unittest.TestCase):

    def test_merge_sort(self):
        input_arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51, 0.48, 0.47, 1.20]
        expected_sorted = [0.32, 0.33, 0.37, 0.42, 0.47, 0.47, 0.48, 0.51, 0.52, 1.20]
        sorted_list = mergeSort(input_arr)
        self.assertEqual(sorted_list, expected_sorted)

if __name__ == '__main__':
    unittest.main()
