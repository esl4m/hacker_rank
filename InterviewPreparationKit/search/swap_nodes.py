#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries

# Using concept of recurssion and deque library from collections.
from collections import deque
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None
        

def swapNodes(indexes, queries):
    # start by creating the node
    def create(root,indexes):
        q = deque([root])

        for i, j in indexes:
            temp = q.popleft()
            if i != -1:
                temp.left = Node(i)
                q.append(temp.left)
            if j != -1:
                temp.right = Node(j)
                q.append(temp.right)
        return root
    
    def swap(root, k, level, l):
        if root:
            if level%k == 0:
                root.left, root.right = root.right, root.left
            
            swap(root.left, k, level+1, l)
            l.append(root.info)
            swap(root.right, k, level+1, l)
        return l
    
    root = Node(1)
    root = create(root, indexes)
    
    result = []
    for k in queries:
        temp_list = []
        swap(root, k, 1, temp_list)
        result.append(temp_list)

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')
    # fptr.close()
