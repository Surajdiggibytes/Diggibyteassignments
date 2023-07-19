import unittest
from Src.assignment5 import util5

def testfun(string, k):
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            ''.join(temp)
            temp = []
            len_temp = 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string="AAVVBBCCDD"
        k=3
        output = testfun(string,k)
        try:
            self.assertEqual(util5.merge_the_tools(string, k), output)
        except:
            raise

          # add assertion here


if __name__ == '__main__':
    unittest.main()
