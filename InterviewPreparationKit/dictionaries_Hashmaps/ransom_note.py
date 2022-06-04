#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # check if word is repeated in notes
    for word in note:
        try:
            magazine.remove(word)
        except:
            print("No")
            return 0
        
    print("Yes")

    """
    !!!!! not optimized / passing all cases !!!!
    if len(note) != len(set(note)):
        print('No')
        return None

    for word in note:
        if word not in magazine:
            print('No')
            return None
    else:
        print('Yes')
    """


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)


"""
-- Input --
6 4
give me one grand today night
give one grand today

output: Yes

----

-- input --
7 4
ive got a lovely bunch of coconuts
ive got some coconuts

output: No ---> some not in magazine
"""
