# given an number, return w/ reversed digits
# int or float: signed, can be positive or negative
import unittest


def reverse_num(x):
    # first we turn int into a string
    string = str(x)
    float_num = isinstance(x, float)

    # check if it's negative
    if string[0] == '-':
        return float('-' + string[:0:-1]) if float_num else int('-' + string[:0:-1])
    return float(string[::-1]) if float_num else int(string[::-1])


# unit tests
class Test(unittest.TestCase):

    def test_negative(self):
        print("Testing reverse num\n")
        self.assertEqual(-132, reverse_num(-231))

    def test_float(self):
        print("Testing float num.\n")
        self.assertEqual(1.32, reverse_num(23.1))


if __name__ == '__main__':
    unittest.main()

# still works if user gives float?
# do we want decimal in same spot?
# return as float or int?
# min or max number?
