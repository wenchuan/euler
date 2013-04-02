#!/usr/bin/python

m = map(lambda x: map(int, x.split()), open('11.input', 'r').readlines())

L = len(m)

M = 1788696

# horizontal
for i in xrange(L):
    for j in xrange(L - 3):
        p = 1
        for x in xrange(4):
            p *= m[i][j+x]
        M = max(p,M)

# vertical
for i in xrange(L - 3):
    for j in xrange(L):
        p = 1
        for x in xrange(4):
            p *= m[i + x][j]
        M = max(p,M)

# diagonal, NW->SE
for i in xrange(L - 3):
    for j in xrange(L - 3):
        p = 1
        for x in xrange(4):
            p *= m[i + x][j + x]
        M = max(p,M)

# diagonal, NE->SW
for i in xrange(L - 3):
    for j in xrange(3, L):
        p = 1
        for x in xrange(4):
            p *= m[i + x][j - x]
        M = max(p,M)

print M
