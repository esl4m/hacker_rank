#!/usr/bin/python

import math
import os
import random
import re
import sys


def countSwaps(a):
    count = 0

    while True:
        swap = False
        for idx in range(len(a) - 1):
            if a[idx] > a[idx + 1]:
                a[idx], a[idx + 1] = a[idx + 1], a[idx]
                count += 1
                swap = True
        if not swap:
            break

    print('Array is sorted in %s swaps.' % count)
    print('First Element: %s' % a[0])
    print('Last Element: %s' % a[-1])

if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().rstrip().split())
    countSwaps(a)
