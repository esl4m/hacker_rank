#!/bin/python3

# We have one candle of height1 , one candle of height2 , and two candles of height3 .
# Colleen only blows out the tallest candles, meaning the candles where height=3
# Because there are 2 such candles, we print 2 on a new line.


def birthday_cake_candles(n, ar):
    if len(ar) == n:
        highest_candles = max(ar)
        return ar.count(highest_candles)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

result = birthday_cake_candles(n, ar)
print(result)

# input
# 4
# 3 2 1 3

# output
# 2
