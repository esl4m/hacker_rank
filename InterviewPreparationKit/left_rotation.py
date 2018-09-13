#!/bin/python


# Complete the rot_left function below.
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
