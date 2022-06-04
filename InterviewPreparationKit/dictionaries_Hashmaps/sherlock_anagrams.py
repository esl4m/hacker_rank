#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlock_anagrams(s):
    anagram_dict = {}
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s) - i+1):
            current_sorted = str(sorted(s[j:j+i]))
            if (current_sorted not in anagram_dict):
                anagram_dict[current_sorted] = 1
            else:
                count += anagram_dict[current_sorted]
                anagram_dict[current_sorted] += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlock_anagrams(s)
        # fptr.write(str(result) + '\n')
    # fptr.close()

# ---- #
# Input
# 2
# abba
# abcd
# ..
# Expected Output
# 4
# 0

# ---- #
# Input (stdin)
# 1
# cdcd
# ..
# Expected Output
# 5
