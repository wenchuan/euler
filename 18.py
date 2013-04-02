#!/usr/bin/python
#
#http://projecteuler.net/problem=18
#http://projecteuler.net/index.php?section=problems&id=67

m = open('small.txt', 'r').readlines()

v = map(lambda x: map(int, x.split()), m)

n = len(v)

f = {}

for i in xrange(n):
    f[(n-1,i)] = v[n-1][i]

for i in xrange(n-2, -1, -1):
    print i
    for j in xrange(i+1):
        f[(i,j)] = v[i][j] + max(f[i+1,j], f[i+1,j+1])

print f[0,0]
