#!/usr/bin/python

n = 1001

a = [1,3,5,7,9]

d = 10

for i in xrange(5, 2 * n - 1):
    a.append(a[i-4] + d)
    d += 2

print sum(a)
