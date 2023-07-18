import unittest
from Src.assignment1 import util1

class MyTestCase(unittest.TestCase):
    def test_something(self):
        '''4
          append 5
          append 6
          insert 0 2
           print
         [2, 5, 6]   '''
        N=4
        output=[2, 5, 6]
        x=util1.listoperations(N)
        self.assertEqual(x,output)  # add assertion here



if __name__ == '__main__':
    unittest.main()
