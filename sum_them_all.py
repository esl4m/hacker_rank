#!/bin/python3

#  sum_them_all.py
#  by: esl4m diaa
#      16 Oct 2016


def sum_arr(numbers):
    s = set()
    for i in numbers:
        s.add(i)
    print(sum(s))

sum_arr([5,1,2,3,4,5])
