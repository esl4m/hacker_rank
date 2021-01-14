#!/usr/bin/python3

def is_one_away(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    
    if abs(l1 - l2) > 1 :
        return False
    if l1 == l2:
        return is_one_away_same_length(s1, s2)
    if l1 > l2:
        return is_one_way_diff_length(s1, s2)
    if l2 > l1:
        return is_one_way_diff_length(s2, s1)

def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

def is_one_way_diff_length(s1, s2):    
    idx = 0
    count_diff = 0
    while(idx < len(s2)):
        if s1[idx + count_diff] == s2[idx]:  # check if char in both s1, s2 are equal in same index
            idx += 1  # move to the next index and next char
        else:
            count_diff += 1  # increment counter only with 1 incase char are not same
            if count_diff > 1:
                return False
    return True


if __name__ == "__main__":
    print(is_one_away("abcde", "abcd"))  # should return True
    print(is_one_away("abde", "abcde"))  # should return True
    print(is_one_away("a", "a"))  # should return True
    print(is_one_away("abcdef", "abqdef"))  # should return True
    print(is_one_away("abcdef", "abccef"))  # should return True
    print(is_one_away("abcdef", "abcde"))  # should return True
    print(is_one_away("aaa", "abc"))  # should return False
    print(is_one_away("abcde", "abc"))  # should return False
    print(is_one_away("abc", "abcde"))  # should return False
    print(is_one_away("abc", "bcc"))  # should return False
