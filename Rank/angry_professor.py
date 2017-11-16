# __author__ = 'eslam'
#!/bin/python

# count = 0
# res = ''
t = int(input().strip())  # the number of test cases

for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, input().strip().split(' '))

    if len([num for num in a if num <= 0]) < k:
        print('YES')
    else:
        print('NO')

#    for i in range (len(a)):
#        if (a[i] <= 0 ):
#            count += 1
#    if count < k:
#        print ('YES')
#    else:
#        print('NO')