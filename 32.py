#!/usr/bin/python

# figure out what's possible
# xx * xxx = xxxx
for i in xrange(1,10):
    for j in xrange(1,9-i):
        if (9 - i - j >= j and j >= i):
            print i, j, 9 - i - j

def isPandigital(s):
    x = list(s)
    x.sort()
    r = ''
    for i in x:
        r += i
    return r == '123456789'

# x * xxxx = xxxx
for a in xrange(1,10):
    for b in xrange(1234, 9877):
        c = a * b
        s = str(a) + str(b) + str(c)
        if (isPandigital(s)):
            print c

# xx * xxx = xxxx
for a in xrange(12,99):
    for b in xrange(123, 988):
        c = a * b
        s = str(a) + str(b) + str(c)
        if (isPandigital(s)):
            print c
