#!/bin/python3

# python pyramid
def py_pyramid(n):
    for i in range(0, n):
        for j in range (0, i+1):
            print('*', end= ' ')
        print('\r')

n = 5
py_pyramid(n)


# python pyramid list
def py_pyramid_list(n):
    my_list = []
    for i in range(0, n+1):
        my_list.append("* " * i)

    print("\n".join(my_list))

n = 5
py_pyramid_list(n)


# Output
# *
# * *
# * * *
# * * * *
# * * * * *
