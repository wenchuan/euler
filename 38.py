#!/usr/bin/python

def isPandigital(s):
    x = list(s)
    x.sort()
    r = ''
    for i in x:
        r += i
    return r == '123456789'

for i in xrange(9876, 0, -1):
    s = ''
    x = 1
    while len(s) < 9:
        s += str(i * x)
        x += 1
    if isPandigital(s):
        print i, s
