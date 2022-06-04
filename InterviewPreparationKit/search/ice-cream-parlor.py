#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'whatFlavors' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money


def whatFlavors(cost, money):
    saved = {}  # saving value & place in dict

    for idx, v in enumerate(cost):
        if (money - v) in saved:
            # return saved[money-v], idx+1
            print(str(saved[money-v])+ ' ' + str(idx+1))
        saved[v] = idx+1
            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)

"""
-- Input --
2           t = 2
4           money = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           money = 4
4           cost[] size n = 4
2 2 4 3     cost = [2, 2, 4, 3]

-- Output
1 4
1 2
"""