def findTF(x):
    i, res = 0, 0
    while i < x:
        if i%3 == 0 or i%5 == 0:
            res += i
        i += 1
    return res

findTF(1000)
