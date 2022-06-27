#!/bin/python3

# number pattern
def py_num_pattern(n):

    for i in range(0, n):
        num = 1
        for j in range (0, i+1):
            print(num, end= ' ')
            num += 1
        print('\r')

n = 5 
py_num_pattern(n)


# Output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
