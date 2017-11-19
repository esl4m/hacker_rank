#!/bin/python3

#  staircase.py
#  by: esl4m diaa
#      16 Oct 2016


def stair_case(n):
    # for i in xrange(n):
    #     print('#')
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)

stair_case(6)
