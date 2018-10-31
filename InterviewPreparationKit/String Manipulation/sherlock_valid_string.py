#!/bin/python3
# validate if string is valid --- return YES or NO
import collections


def is_valid(s):
    # split s to dict
    freq = collections.Counter(s)
    values = list(freq.values())

    values.sort()

    if values.count(values[0]) == len(values) \
            or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) \
            or (values.count(values[-1]) == len(values) - 1 and values[0] == 1):
        return 'YES'
    else:
        return 'NO'

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = is_valid(s)
#     fptr.write(result + '\n')
#     fptr.close()

# Sample Input:
# aabbcd
# Sample Output:
# NO

# Sample Input:
# abcdefghhgfedecba
# Sample Output:
# YES
s = 'aaabbbdddccc'
print(is_valid(s))
