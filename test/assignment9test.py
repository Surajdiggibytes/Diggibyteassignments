import unittest
from Src.assignment9 import util9
from collections import namedtuple

'''
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4 
'''
def testtup():
    n= 2
    fields= input("INPUT FOR TEST CASE").split()
    total_marks = 0
    for _ in range(n):
        students = namedtuple('student', fields)
        MARKS, CLASS, NAME, ID = input().split()
        student = students(MARKS, CLASS, NAME, ID)
        total_marks += int(student.MARKS)
    res=(total_marks/n)


    #print('{:.2f}'.format(total_marks / n))
class MyTestCase(unittest.TestCase):
    def test_something(self):
        output= testtup()
        x= util9.tup()
        try:
            self.assertEqual(x, output)
        except:
            raise

          # add assertion here


if __name__ == '__main__':
    unittest.main()
