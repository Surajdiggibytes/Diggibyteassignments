# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

def tup():
    total_marks = 0
    n = 2
    fields = input("INPUT").split()
    for _ in range(n):
        students = namedtuple('student', fields)
        MARKS, CLASS, NAME, ID = input().split()
        student = students(MARKS, CLASS, NAME, ID)
        total_marks += int(student.MARKS)
    print('{:.2f}'.format(total_marks / n))


