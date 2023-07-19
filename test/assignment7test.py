import unittest
from Src.assignment7 import util7
def testalign7(thickness,c):

    for i in range(thickness):
        output =((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))


    for i in range(thickness + 1):
        output =((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))


    for i in range((thickness + 1) // 2):
        output =((c * thickness * 5).center(thickness * 6))


    for i in range(thickness + 1):
        output =((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))


    for i in range(thickness):
        output =(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))

class MyTestCase(unittest.TestCase):

    def test_something(self):
        thickness=3
        c='H'
        output= testalign7(thickness,c)
        x= util7.align(thickness,c)
        self.assertEqual(x, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
