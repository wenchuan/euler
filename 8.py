#!/usr/bin/python

s = open('8.input', 'r').read()
s = s[:-1]

def prod(l):
    r = 1
    for i in l:
        r *= int(i)
    return r

m = 0

for i in xrange(995):
    x = prod(s[i:i+5])
    if x > m:
        m = x

print m

