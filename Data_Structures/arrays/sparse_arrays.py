#!/bin/python3

#  sparse_arrays.py Arrays Task .. HackerRank
#  by: esl4m diaa
#      07 Nov 2017

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

n2 = int(input())
for _ in range(n2):
    word = input()
    # find how many times s was in arr
    print(arr.count(word))

# other try
#  s = [input() for _ in range(int(input()))]
# for _ in range(int(input())):
#     print(s.count(input()))
