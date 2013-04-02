#!/usr/bin/python

n = 10000

a = {}

def d(x):
    if a.has_key(x):
        return a[x]
    s = 0
    for i in xrange(1,x/2+1):
        if x%i == 0:
            s += i
    a[x] = s
    return s

aa = []

for i in xrange(n):
    if d(i) != i and d(d(i)) == i:
        aa.append(i)

print aa
print sum(aa)
