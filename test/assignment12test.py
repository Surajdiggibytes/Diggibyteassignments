import unittest
import numpy
from Src.assignment12 import util12



class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_my_array = numpy.array([[2, 5],
                                [3, 7],
                                [1, 3],
                                [4, 0]])
        output = 3
        self.assertEqual(util12.min_max(test_my_array), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
