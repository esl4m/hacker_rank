# __author__ = 'eslam'

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))

# n, k = 6, 3
# a = 1 3 2 6 1 2

res = 0

for i in range(n):
    for j in range(i):
        if (a[i] + a[j]) % k == 0:
            res += 1

# another solutions
#  in python 2
# print(sum([1 for i in range(n) for j in range(i) if (a[i]+a[j])%k==0]))
# # #
#  in python 3
# res = sum((i+j) % k == 0 for x, i in enumerate(a) for j in a[x+1:])

print("res ", res)
