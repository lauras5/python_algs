import unittest


def avg_word_len(sentence):
    for p in "!?',;.":
        # remove punctuation marks
        sentence = sentence.replace(p, '')
    # create arr of sentence
    words = sentence.split()
    # return rounded num --> add all word lengths divide by number of words, 2 decimal points
    return round(sum(len(word) for word in words) / len(words), 2)


# unit tests
class Test(unittest.TestCase):

    def test_sentence1(self):
        print("Testing sentence1.. \n")
        self.assertEqual(3.86, avg_word_len("Nice to meet you Tom from MySpace."))

    def test_sentence2(self):
        print("Testing sentence...\n")
        self.assertEqual(4.2, avg_word_len("This is another sentence, it won't make sense so? yeah."))


if __name__ == '__main__':
    unittest.main()