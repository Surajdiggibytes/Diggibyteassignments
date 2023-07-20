import unittest
from Src.assignment10 import util10



class MyTestCase(unittest.TestCase):
    def test_something(self):
        t=1
        t1= "Sun 10 May 2015 13:54:36 -0700"
        t2= "Sun 10 May 2015 13:54:36 -0000"
        output= 25200
        x= util10.time_delta(t1,t2)
        self.assertEqual(x, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
