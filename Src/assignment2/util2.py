import numpy as np
def average(n,student_marks,query_name):
    for _ in range(n):
        ls = student_marks[query_name]
        avg = np.average(ls)
        print(avg)
        return avg


    '''n = int(input("The number of students :"))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    l1 = list(student_marks[query_name])
    addition = sum(l1)
    result = addition / len(l1)
    print('%.2f' % result)'''

