#!/bin/python2.6

#  python_if_else.py
#  by: esl4m diaa
#      27 Mar 2018

if __name__ == '__main__':
    n = int(raw_input())
    if (n % 2):  # n is odd
        print ('Weird')
    else:
        if ( 1 < n < 6):
            print ('Not Weird')
        elif ( 20 < n ):
            print ('Not Weird')
        else:
            print ('Weird')
