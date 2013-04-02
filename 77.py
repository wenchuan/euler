#!/usr/bin/python

# denominations
d = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,73,79,83,89,97]

# table
t = []
t.append([1] * 25)

l = 101
for i in xrange(1,l):
    t.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    for j in xrange(0,24):
        k = 0
        while i >= k:
            t[i][j] += t[i-k][j-1]
            k += d[j]

for i in xrange(l):
    print i, t[i]
