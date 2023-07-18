import unittest
from Src.assignment2 import util2
class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 2
        marks = {"abc": [10, 20, 30], "bcd": [20, 20, 20]}
        qname = "bcd"
        expected_output = 20.0
        z = util2.average(n,marks,qname)
        try:
            self.assertEqual(z,expected_output)  # add assertion here
        except AssertionError:
            print("Assertion Error")
            raise


if __name__ == '__main__':
    unittest.main()
