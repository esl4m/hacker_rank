#!/bin/python3

#  sum_them_all.py
#  by: esl4m
#      Mar11 2020


# class MySum:
#     def __init__(self):
#         #
#         self.start = 0
#
#     def sum_them(self):
#         res = 0
#         numbers = [1, 2, 3, 4, 5, 8]
#
#         for x in numbers:
#             res = self.start + x  # result will be self + the current number (x) .. at first self.start is zero ;)
#             self.start = res  # changing the start value to be the current result.
#
#         return res
#
# s = MySum()
# print(s.sum_them())

start = 0

def sum_them():
    global start
    res = 0
    numbers = [1, 2, 3, 4, 5, 8]

    for x in numbers:
        res = start + x  # result will be self + the current number (x) .. at first self.start is zero ;)
        start = res  # changing the start value to be the current result.

    return res

print(sum_them())
