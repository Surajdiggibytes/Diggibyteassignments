import unittest
from Src.assignment13 import util13
class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_input = [[1, 2], [2, 1]]
        output='-3.00'

        self.assertEqual(util13.determin(test_input), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
