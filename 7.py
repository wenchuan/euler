#!/usr/bin/python

N = 200000

p = range(N + 1)
for i in xrange(N):
    p[i] = 1

p[0] = 0
p[1] = 0

for i in xrange(2, N):
    for j in xrange(2, N/i + 1):
        p[i*j] = 0

s = 0
for i in xrange(N):
    if p[i]:
        s += 1
        if s == 10001:
            print i
