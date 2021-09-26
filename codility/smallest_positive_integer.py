# return smallest positive integer

def solution(arr):
    res = 1
    smallest = []

    """
    arr = sorted(arr)  # sorting arr before starting
    # print(arr)
    for i in arr:
        if i + 1 not in arr:
            # print("current =", i+1)
            smallest.append(i+1)
        if i < 0:
            res = 1
            return res:q
    return smallest[0]
    """

    for i in arr:
        if i < 0:
            return 1

        if i > 0:
            if i + 1 not in arr:
                res = i + 1
                smallest.append(res)
    smallest = sorted(smallest)  # --> sorting smallest array
    return smallest[0]


A = [1, 3, 6, 4, 1, 2]  # --> 5
A1 = [1, 3, 6, 4, 1, 7]  # --> 2
A2 = [1, 2, 3]  # --> 4
A3 = [-1, -3]  # --> 1
print(solution(A))
print(solution(A1))
print(solution(A2))
print(solution(A3))
