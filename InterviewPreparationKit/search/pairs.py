#!/bin/python3
# Determine the number of pairs of array elements that have a difference equal to a target value.

import math
import os
import random
import re
import sys

# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def pairs(k, arr):
    # res = 0
    # for value in arr:
    #     if (value + k) in arr:
    #         res += 1
    # return res
    set1 = set(arr)  # set : without duplicates
    set2 = [value + k for value in arr]
    return len(set1.intersection(set2))

arr_input = [1, 5, 3, 4, 2]
print(pairs(2, arr_input))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nk = input().split()
#     n = int(nk[0])
#     k = int(nk[1])
#     arr = list(map(int, input().rstrip().split()))
#     result = pairs(k, arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()

# Input
# 5 2
# 1 5 3 4 2
# Output
# 3
# There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1] .
