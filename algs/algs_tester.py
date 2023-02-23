import unittest
import fib_recursion
import two_sum


class TestAlgs(unittest.TestCase):

    def test_fib_recursion__successful(self):
        self.assertEqual(fib_recursion.recur_fibo(5), 5)
        self.assertEqual(fib_recursion.recur_fibo(8), 21)

    def test_two_sum__successful(self):
        self.assertEqual(two_sum.two_sum([0, 1, 2, 3, 4, 5], 8), [3, 5])

    def test_two_sum__none(self):
        self.assertIsNone(two_sum.two_sum([1, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()