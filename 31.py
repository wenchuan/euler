#!/usr/bin/python

# denominations
d = [1,2,5,10,20,50,100,200]

# table
t = []
t.append([1] * 8)
t.append([1] * 8)

l = 201
for i in xrange(2,l):
    t.append([1,0,0,0,0,0,0,0])
    for j in xrange(1,8):
        k = 0
        while i >= k:
            t[i][j] += t[i-k][j-1]
            k += d[j]

for i in xrange(l):
    print t[i]
