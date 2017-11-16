# __author__ = 'eslam'
#!/bin/python
from collections import Counter

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

socks = Counter(c)
pairs = 0

if len(c) == n :
    for s in socks:
        pairs += socks[s]//2
    print(pairs)

else:
    print("n must be equal to enteries")
