import numpy
def determin(input):
    res1=numpy.linalg.det(input)
    res=('{:.2f}'.format(res1))
    return res