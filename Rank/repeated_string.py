# __author__ = 'eslam'

# task link : https://www.hackerrank.com/challenges/repeated-string

s = input()
n = int(input())

segment_length = len(s)  # 3
segment_count = s.count("a")  # 1

ratio = n // segment_length  # 10 // 3 = 3

remainder = segment_length - n % segment_length  # 3 - 1 = 2

# print("rem", remainder)

first_segments_count = ratio * segment_count  # 3 * 1 = 3

last_partial_segment_count = s.count("a", 0, segment_length - remainder)
result = first_segments_count + last_partial_segment_count
print(result)


# another solution :
# s = raw_input().strip()
# n = long(raw_input().strip())
# a = s.count('a')
# x = n/len(s)
# print (x*a + s[:n%len(s)].count('a'))
