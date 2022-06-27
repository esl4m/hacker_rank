#!/bin/python3

# number sequential pattern
def py_num_seq_pattern(n):

    num = 1
    for i in range(0, n):
        for j in range (0, i+1):
            print(num, end= ' ')
            num += 1
        print('\r')

n = 5 
py_num_seq_pattern(n)


# Output
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
