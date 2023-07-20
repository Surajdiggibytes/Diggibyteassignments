
def happiness(items,a,b):
    happ=0
    for i in items:
        for j in a:
            if j == i:
                happ += 1
        for k in b:
            if k == i:
                happ -= 1
    print(happ)
    return happ