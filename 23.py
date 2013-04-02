#!/usr/bin/python

N = 28130

def abundant(n):
    a = []
    for i in xrange(1, n):
        if n % i == 0:
            a.append(i)
    return sum(a) > n

a = [False] * (N + 1)

for i in xrange(N):
    if abundant(i):
        a[i] = True

s = range(1,24)

for i in xrange(24,N):
    add = True
    for j in xrange(i/2, i):
        if a[j] and a[i-j]:
            add = False
            break
    if add:
        s.append(i)

print sum(s)
