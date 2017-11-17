#!/bin/python3

# Input Format
# The first line contains a single integer, q , denoting the number of queries.
# Each of the q subsequent lines contains three space-separated integers describing the respective values of
# x (cat A's location), y (cat B's location), and z (mouse C's location).

q = int(input().strip())
for a0 in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]

    # we have 3 conditions
    # Cat B wins
    if abs(x-z) > abs(y-z):
        print('Cat B')

    # Cat A wins
    elif abs(y-z) > abs(x-z):
        print('Cat A')

    # Mouse run
    else:
        print('Mouse C')

# Sample Input 0
# 3
# 1 2 3
# 1 3 2
# 2 1 3
#
# Sample Output 0
# Cat B
# Mouse C
# Cat A
