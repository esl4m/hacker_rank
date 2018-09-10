# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
# arr = [2,5,8,12,16,23,38,56,72,91]
# -- # Python Program for Recursive implementation of Binary Search --
# -- Returns index of "x" in arr if present, else -1  --
import sys


def binary_search(arr, left, x, right):
    if right >= left:
        mid = left + (right - left)//2  # the division // to get the middle element

        if arr[mid] == x:  # If element is in the middle of arr
            return mid

        # elif x == arr[0]:
        #     return arr.index(arr[0])  # if element is in the first in arr .. - return : left
        #
        # elif x == arr[-1]:
        #     return right  # if element is in the end of arr .. - return : arr.index(arr[-1])

        elif arr[mid] > x:
            # If element is smaller than mid, then it can only be present in left subarray "replace right with mid-1 "
            return binary_search(arr, left, x, mid-1)

        else:
            # If element is greater than mid, then it can only be present in right subarray "replace left with mid+1"
            return binary_search(arr, mid+1, x, right)
    else:
        return -1  # If element is not in array


arr = [2, 3, 4, 10, 40]
x = 2
result = binary_search(arr, 0, x, len(arr)-1)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
