#!/usr/bin/python

a,b = 3,2
cnt = 0

for i in xrange(1000):
    if len(str(a)) > len(str(b)):
        cnt += 1
    a,b = a + 2 * b, a + b

print cnt
