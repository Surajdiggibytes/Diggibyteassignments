import  numpy
def min_max(my_array):
    min= (numpy.min(my_array, axis=1))  # Output : [2 3 1 0]
    max= (numpy.max(min))
    print(max)
    return max