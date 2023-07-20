import unittest
import numpy
from Src.assignment11 import util11
def test_case(elem):

    test_floor1 = numpy.floor(elem)
    test_ceil1=numpy.ceil(elem)
    test_rint1= numpy.rint(elem)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        global elem
        elem = list(map(float, input("Enter inputs for test:").strip().split()))
        self.assertEqual(test_case(elem),util11.floor_ceil_rint(elem))  # add assertion here


if __name__ == '__main__':
    unittest.main()
