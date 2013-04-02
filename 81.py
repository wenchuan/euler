#!/usr/bin/python

f = open('matrix.txt','r')

m = []

for l in f:
    m.append(map(int,l[:-1].split(',')))

l = len(m)

r = []
for i in xrange(l):
    r.append([0] * l)

r[0][0] = m[0][0]
for i in xrange(1,l):
    r[i][0] = r[i-1][0] + m[i][0]
    r[0][i] = r[0][i-1] + m[0][i]

for i in xrange(1,l):
    for j in xrange(1,l):
        r[i][j] = min(r[i-1][j], r[i][j-1]) + m[i][j]

print r
