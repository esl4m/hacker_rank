#!/bin/python2.6

#  python_write_function.py
#  by: esl4m diaa
#      27 Mar 2018
# years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.


def is_leap(year):
    leap = False
    
    if (year % 4 == 0): 
        if (year % 400 == 0) or (year % 100 != 0):
            leap = True
    return leap

#    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(raw_input())
print is_leap(year)