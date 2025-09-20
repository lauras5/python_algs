import unittest
import fib_recursion
import two_sum
from median_sorted_arr import Solution  


class TestAlgs(unittest.TestCase):

    def test_fib_recursion__successful(self):
        self.assertEqual(fib_recursion.recur_fibo(5), 5)
        self.assertEqual(fib_recursion.recur_fibo(8), 21)

    def test_two_sum__successful(self):
        self.assertEqual(two_sum.two_sum([0, 1, 2, 3, 4, 5], 8), [3, 5])

    def test_two_sum__none(self):
        self.assertIsNone(two_sum.two_sum([1, 2, 3], 2))

    def test_median_sorted_arrays_examples(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_median_sorted_arrays_edge_cases(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([], [1]), 1.0)
        self.assertEqual(s.findMedianSortedArrays([2], [3]), 2.5)
        self.assertEqual(s.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8]), 4.5)
        self.assertEqual(s.findMedianSortedArrays([-5, -3, -1], [-2, 0, 2]), -1.5)


if __name__ == '__main__':
    unittest.main()