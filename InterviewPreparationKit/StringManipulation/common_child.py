#!/bin/python3

# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?


import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # check limits
    ls1 = len(s1)
    ls2 = len(s2)
    if 1 > ls1 & ls2 > 5000:
        return 'out of memory'
    
    max_at = {}
    for item1 in s1:
        current_max = 0

        for i, item2 in enumerate(s2):
            potential_sum = current_max + 1
            current_max = max(current_max, max_at.get(i, 0))
            if item1 == item2:
                max_at[i] = potential_sum
    return max(max_at.values(), default=0)

    """
    .... OLD .... ---> wrong: matching shouldn't intersect --> sequence is important
    res = []
    for item in s2:
        if item in s1 and item not in res:
            res.append(item)
    print(res)
    return len(res)
    """

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = 'SHINCHAN' # input()  # SHINCHAN
    s2 = 'NOHARAAA' # input()  # NOHARAAA
    result = commonChild(s1, s2)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
