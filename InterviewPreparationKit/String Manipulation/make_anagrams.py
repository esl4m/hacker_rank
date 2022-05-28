#!/bin/python3

import math
import os
import random
import re
import sys

# Strings: Making Anagrams

# A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.
# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.


# Complete the 'makeAnagram' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b

def make_anagram(a, b):
    first = second = 0
    d = {}
    count = 0
    for x in a:
        d[x] = d.get(x, 0) + 1

    for y in b:
        if d.get(y, 0) != 0:
            d[y] -= 1
        else:
            count += 1
    # for w in sorted(d, key=d.get, reverse=True): print(w, d[w])  # -- sorting desending
    return count + sum(d.values())

    # return sum(abs(a.count(i) - b.count(i)) for i in 'abcdefghijklmnopqrstuvwxyz')  # one sentence


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = make_anagram(a, b)
    print(str(res))
    # fptr.write(str(res) + '\n')
    # fptr.close()
