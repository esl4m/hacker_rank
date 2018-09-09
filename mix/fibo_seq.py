# Problem:  Write a function that takes a number n
# and returns an array containing a Fibonacci sequence of length n


def fib_array(n):  # more simple
    if n < 0:
        return []
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    arr = [1, 1]
    for x in range(2, n):
        arr.append(arr[x - 1] + arr[x - 2])

    return arr

print(fib_array(7))


# def fib(n):  # complex algorithm
#     if n <= 1:
#         return 1
#     return fib(n-1) + fib(n-2)
#
#
# def fib_arr(n):
#     res_arr = []
#     for i in range(n):
#         if i < n:
#             print(res_arr)
#             res_arr.append(fib(i))
#     return res_arr
#
# print(fib_arr(7))
