#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # num_of_triplet = 0
    pairs = {}  # Takes note of pair in order i < j
    counts = {}  # Counts each number's occurence
    triplet_count = 0  # Takes note of triplet count.
    
    for i in reversed(arr):
        if i*r in pairs:
            print(pairs, ' --- ', counts)  # -- lets see
            triplet_count += pairs[i*r]

        if i*r in counts:
            pairs[i] = pairs.get(i, 0) + counts[i*r]
        
        counts[i] = counts.get(i,0) + 1
        print('counts: ', counts, ' pairs: ', pairs)

    return triplet_count

    """
    !!!!! not optimized / passing all cases !!!!

    triplet_arr = []
    for idx, item in enumerate(arr):
        if arr[idx+1] == arr[idx+2]:
            # skip and count triplet
            triplet_arr.extend([arr[idx], arr[idx+1], arr[idx+3]])
            
        else:
            # count triplet
            triplet_arr.extend([arr[idx], arr[idx+1], arr[idx+2]])
    return len(triplet_arr)
    """

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    # fptr.write(str(ans) + '\n')
    # fptr.close()

"""
-- Input --
4 2
1 2 2 4

Output: 2

--

-- input --
6 3
1 3 9 9 27 81

Output: 6
"""
