import unittest


def is_valid_palindrome(word):
    # base case
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_valid_palindrome(word[1:-1])


# we can also do a one liner but like who are we trying to impress
def is_palindrome(word):
    return word == word[::-1]


# unit tests
class Test(unittest.TestCase):

    def test_is_valid_palindrome_success(self):
        print("Testing valid palindrome...")
        self.assertEqual(True, is_valid_palindrome("redder"))

    def test_is_valid_palindrome_fail(self):
        print("Testing invalid palindrome...")
        self.assertEqual(False, is_valid_palindrome("avatar"))

    def test_is_palindrome_success(self):
        print("Testing valid palindrome 2...")
        self.assertEqual(True, is_palindrome("racecar"))

    def test_is_palindrome_fail(self):
        print("Testing invalid palindrome 2...")
        self.assertEqual(False, is_palindrome("guitar"))


if __name__ == '__main__':
    unittest.main()
