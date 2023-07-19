import unittest
from Src.assignment6 import util6

def funtest6(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        #print(deci,octa,hexa, bina, sep=' ',end=' ')
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
class MyTestCase(unittest.TestCase):
    def test_something(self):
        number=3
        x= util6.print_formatted(number)
        output = funtest6(number)
        self.assertEqual(x,output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
