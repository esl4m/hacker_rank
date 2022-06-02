#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    num_of_swaps = 0
    i = 0
    
    while i < len(arr):
        # compare current item (arr[i]) with it's current index
        if arr[i] != i+1:
            temp = arr[i] - 1
            arr[i], arr[temp] = arr[temp], arr[i]
            num_of_swaps += 1
        else:
            i += 1
    
    return num_of_swaps


    # num_of_swaps = 0
    # new_arr = []
    # for i, value in enumerate(arr[:-1]):
    #     for second in arr[i+1:]:
    #         if value > second:
    #             # swap the values
    #             new_arr.insert(arr.index(value), value)
    #             new_arr.insert(arr.index(second), second)
    #             
    #             num_of_swaps += 1
    #             print(new_arr)
    #         else:
    #             new_arr.extend([value, second])
    # return num_of_swaps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    
    arr = [4, 3, 1, 2]  # min --> 3
    # arr = [2, 3, 4, 1, 5]  # min --> 3
    # arr = [1, 3, 5, 2, 4, 6, 7]  # min --> 3

    res = minimumSwaps(arr)
    print(res)
    # fptr.write(str(res) + '\n')
    # fptr.close()
