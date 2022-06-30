#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'alternatingCharacters' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    num_of_del = 0

    for idx in range(0, len(s)-1):
        if s[idx] == s[idx+1]:
            num_of_del += 1
    return num_of_del

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()

"""
-- Input
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Output
3
4
0
0
4
"""
