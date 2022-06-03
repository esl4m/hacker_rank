#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'two_strings' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def two_strings(s1, s2):
    for s in s2:
        if s in s1:
            return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = two_strings(s1, s2)
        # fptr.write(result + '\n')
    # fptr.close()
