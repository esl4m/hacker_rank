# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
# arr = [2,5,8,12,16,23,38,56,72,91]
# -- # Python Program for Recursive implementation of Binary Search --
# -- Returns index of "x" in arr if present, else -1  --


def binary_search(arr, left, x, right):
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == x:  # Check if x is present at mid
            return mid

        elif arr[mid] < x:  # If x is greater, ignore left half
            left = mid + 1

        else:  # If x is smaller, ignore right half
            right = mid - 1

    return -1  # if element is not in array

arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, x, len(arr)-1)

if result != -1 :
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
