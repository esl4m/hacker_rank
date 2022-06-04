#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    results = []
    lookup = {}
    freqs = defaultdict(set)

    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        
        elif command == 3:
            results.append(1 if freqs[value] else 0)

    return results  


"""
!!!!! not optimized / passing all cases !!!!

def freqQuery(queries):
    d = {}
    arr = []
    res = []
    for i in queries:
        if i[0]==1:
            arr.append(i[1])
            if i[1] in d:
                d[i[1]]+=1
            else:
                d[i[1]]=1
        elif i[0]==2:
            if i[1] in arr:
                arr.remove(i[1])
                d[i[1]]-=1
        else:
            if len(arr) >= i[1] and i[1] in d.values():
                res.append(1)
            else:
                res.append(0) 
    return res
"""

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    # fptr.close()
"""
-- Input --
4
3 4
2 1003
1 16
3 1

output:
0
1
"""