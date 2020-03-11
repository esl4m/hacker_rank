#!/bin/python3

#  sum_them_all.py
#  by: esl4m
#      Mar11 2020


class MySum:
    def __init__(self):
        self.start = 0

    def sum_them(self):
        res = 0
        numbers = [1, 2, 3, 4, 5, 8]

        for x in numbers:
            res = self.start + x
            self.start = res

        return res

s = MySum()
print(s.sum_them())
