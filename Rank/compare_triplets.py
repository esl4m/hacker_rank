#!/bin/python

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0),int(a1),int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0),int(b1),int(b2)]

alice = 0
bob = 0
A = [a0, a1, a2]
B = [b0, b1, b2]
i = 0
while i < len(A):
    if A[i] > B[i]:
        alice += 1
    if B[i] > A[i]:
        bob += 1
    i += 1
print(alice, bob)
