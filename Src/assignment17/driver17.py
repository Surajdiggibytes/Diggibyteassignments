import util17
num_of_tests = int(input())

for i in range(num_of_tests):
    n = int(input())
    sideLengths = [int(num) for num in input().split()]
    util17.myFunction(sideLengths)