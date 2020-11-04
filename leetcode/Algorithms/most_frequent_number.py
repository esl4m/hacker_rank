#!/usr/bin/python3

def most_frequent(given_list):
    d = {}

    for i in given_list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1  # increase the value in the dict (h)
        
    max_count = 0
    res = None
    
    for item in d:
        if max_count < d[item]:
            res = item
            max_count = d[item]
    
    return res


# NOTE: The following input values will be used for testing your solution.

list1 = [1, 3, 1, 3, 2, 1]  # most_frequent(list1) should return 1
list2 = [3, 3, 1, 3, 2, 1]  # most_frequent(list2) should return 3
list3 = []  # most_frequent(list3) should return None
list4 = [0]  # most_frequent(list4) should return 0
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]  # most_frequent(list5) should return -1


if __name__ == "__main__":
    print(most_frequent(list1))
    print(most_frequent(list2))
    print(most_frequent(list3))
    print(most_frequent(list4))
    print(most_frequent(list5))
