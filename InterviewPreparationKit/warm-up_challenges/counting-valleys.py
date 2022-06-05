#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'countingValleys' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

def countingValleys(steps, path):
    sea_level = 0
    valleys = 0
    
    for step in path:
        if step == 'U':
            if sea_level == -1:
                valleys += 1
            sea_level += 1
        
        if step == 'D':
            sea_level -= 1

    return valleys

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

"""
Input:
8
UDDDUDUU
-- Output: 1

Input:
12
DDUUDDUDUUUD
-- Output: 2
"""
