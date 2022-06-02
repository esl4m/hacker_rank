#!/bin/python3

def rot_left(a, d):
    for i in range(len(a) - 1):
        if i < d:
            a.append(a[0])
            a.pop(0)
    return a

if __name__ == '__main__':
    # 5 4
    # 1 2 3 4 5
    nd = [5, 4]
    n = int(nd[0])
    d = int(nd[1])
    a = [1, 2, 3, 4, 5]

    print(rot_left(a, d))

# Complete the 'rotLeft' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d