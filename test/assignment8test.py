import unittest
from Src.assignment8 import util8
class MyTestCase(unittest.TestCase):
    def test_something(self):
        year= 2023
        month = 3
        date = 22
        output="WEDNESDAY"
        res=util8.calender(year,month,date)

        self.assertEqual(res,output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
