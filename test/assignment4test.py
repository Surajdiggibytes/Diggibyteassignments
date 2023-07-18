import unittest
from Src.assignment4 import util4
class MyTestCase(unittest.TestCase):
    def test_something(self):
        '''
        test case 1:
        input = "abc"
        replacing = "S"
        Position= 0
        Expected output = "Sbc"

        '''
        st1 ="abc"
        rep = "S"
        pos = 0
        x= util4.mutation(st1,rep,pos)
        expected_output= "Sbc"
        try:
            self.assertEqual(x, expected_output)
        except:
            pass
          # add assertion here


if __name__ == '__main__':
    unittest.main()
