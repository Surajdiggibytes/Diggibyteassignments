import unittest
from Src.assignment3 import util3


class MyTestCase(unittest.TestCase):



    def test_something(self):
        '''
            input: score= [1,55,8,66,22]
            Expected output = 66
            '''
        output3 = 55
        score = [1,55,8,66,22]
        x= util3.runnerup(score)
        try:
            self.assertEqual(x, output3)
        except:
            raise

            # add assertion here


if __name__ == '__main__':
    unittest.main()
