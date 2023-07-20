import unittest
from Src.assignment15 import util15

def test_word(n):
    counter = {}
    words = []
    for i in range(n):
        word = input().strip()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            words.append(word)

    print(len(words))
    print(' '.join([str(counter[word]) for word in words]))
class MyTestCase(unittest.TestCase):
    def test_something(self):
        n=4
        x=util15.word_order(n)
        self.assertEqual(x,test_word(n))  # add assertion here


if __name__ == '__main__':
    unittest.main()
