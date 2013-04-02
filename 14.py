#!/usr/bin/python

n = 100

t = {}
t[1] = 1
t[2] = 2

def chain(n):
    if not t.has_key(n):
        if n%2:
            x = chain(3 * n + 1) + 1
        else:
            x = chain(n/2) + 1
        t[n] = x
    return t[n]

maax = 1
maax_i = 1

for i in xrange(1,1000000):
    if chain(i) > maax:
        (maax, maax_i) = (chain(i), i)

print maax, maax_i


