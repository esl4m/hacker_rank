#!/bin/python3


# character pattern to return one single char in each line.
def py_char_pattern(n):
    char_num = 65  # Latin capital letter A
    for i in range(0, n):
        for j in range (0, i+1):
            ch = chr(char_num)
            print(ch, end=' ')
        char_num += 1
        print('\r')

n = 5 
py_char_pattern(n)


# Output
# A 
# B B 
# C C C 
# D D D D 
# E E E E E

# --- #

def py_continuous_char_pattern(n):
    char_num = 65  # Latin capital letter A
    for i in range(0, n):
        for j in range (0, i+1):
            ch = chr(char_num)
            print(ch, end=' ')
            char_num += 1
        print('\r')

n = 5 
py_continuous_char_pattern(n)

# Output
# A 
# B C 
# D E F 
# G H I J 
# K L M N O
