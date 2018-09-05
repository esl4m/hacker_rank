#!/usr/bin/python

# linear_search ..
#  By Eslam Diaa

# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].


# Python code for linearly search x in arr[].
# If x is present then return its location in array, otherwise return -1
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
print(search(arr, x=175))


# Examples :
# Input : arr[] = {10, 20, 80, 30, 60, 50,
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6
# Element x is present at index 6
#
# Input : arr[] = {10, 20, 80, 30, 60, 50,
#                      110, 100, 130, 170}
#            x = 175;
# Output : -1 ... Element x is not present in arr[].
