#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'jumpingOnClouds' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.


def jumpingOnClouds(c):
    # Write your code here
    count = i = 0
    while i < len(c) - 2:
        if c[i+2] == 0:
            i += 2  # skip same two (0) clouds, get less jumps
        else:
            i += 1        
        count += 1
    if i == len(c) - 2:
        count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()

"""
-- Input --
7
0 0 1 0 0 1 0

Output: 4

--

-- Input --
6
0 0 0 0 1 0

Output: 3

"""
