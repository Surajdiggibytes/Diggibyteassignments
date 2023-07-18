'''The provided code stub will read in a dictionary containing key/value pairs
 of name:[marks] for a list of students. Print the average of the marks array for
  the student name provided, showing 2 places after the decimal.'''

import  util2
n = int(input())
name, *line = input().split()
scores = list(map(float, line))
student_marks = {}
student_marks[name] = scores
query_name = input()
util2.average(n,student_marks,query_name)