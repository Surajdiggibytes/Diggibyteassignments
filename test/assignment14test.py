import unittest
from Src.assignment14 import util14
class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = [1, 3, 5, 7, 9]
        b = [2, 4, 6, 8]
        items= [1,2,3,4,5,6,7]
        output=1
        self.assertEqual(util14.happiness(items,a,b), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
