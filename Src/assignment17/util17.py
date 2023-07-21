from itertools import combinations

def iters(mylist, k):

  c = list(combinations(mylist, k))

  r = [i for i in c if 'a' in i]

  result = ('{:.3f}'.format(len(r) / len(c)))

  print(result)

  return(result)