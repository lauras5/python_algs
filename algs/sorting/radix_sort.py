import unittest
import numpy as np

def counting_sort(arr, exp):
    n = len(arr)
    output = np.empty(n, dtype=int)
    count = np.zeros(10, dtype=int)

    for i in range(n):
        index = int(arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(unsorted_list):
    exp = 1
    max_num = int(np.max(unsorted_list))

    while max_num // exp > 0:
        counting_sort(unsorted_list, exp)
        exp *= 10

    return unsorted_list

class TestRadixSort(unittest.TestCase):

    def test_radix_sort(self):
        input_arr = [42, 32, 33, 52, 37, 47, 51, 48, 47, 120]
        expected_sorted = [32, 33, 37, 42, 47, 47, 48, 51, 52, 120]
        sorted_list = radix_sort(input_arr)
        self.assertEqual(sorted_list, expected_sorted)

if __name__ == '__main__':
    unittest.main()
