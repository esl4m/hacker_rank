#!/bin/python3

# special palindromic substrings
import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substr_count(n, s):
    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = substr_count(n, s)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()


# Sample Input -- 0
# 5
# asasd
# Sample Output -- 0
# 7 
# Explanation -- 0
## --> {a, s, a, s, d, asa, sas}

### -------------------- ###

# Sample Input 1
# 7
# abcbaba
# Sample Output 1
# 10 
# Explanation -- 1
## --> {a, b, c, b, a, b, a, bcb, bab, aba}

### -------------------- ###

# Sample Input 2
# 4
# aaaa
# Sample Output 2
# 10
# Explanation 2
## --> {a,a,a,a, aa,aa,aa, aaa,aaa, aaaa}

# temp solution
"""
def substr_count(n, s):
    l = []
    count = 0
    cur = None

    # 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    print(l)

    ans = 0
		
    # 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

    # 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans
"""
