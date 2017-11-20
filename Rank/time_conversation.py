#!/bin/python3

# from _datetime import datetime
from datetime import datetime


def timeConversion(s):
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    return datetime.strftime(in_time, "%H:%M:%S")

s = input().strip()
result = timeConversion(s)
print(result)

# input 07:05:45PM
# output 19:05:45
