#!/bin/python3

#  arrays-ds.py Arrays Task .. HackerRank
#  by: esl4m diaa
#      07 Nov 2017

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

if len(arr) == n:
    for x in reversed(arr):
        print(x, end=" ")
else:
    print('N should equal the number of integers in array')

# another solution #
# c = ""
# for x in arr[::-1]:
#     print(c)
#     c += str(x) + " "
#     print("c again", c)
# print(c)
