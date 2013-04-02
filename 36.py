#!/usr/bin/python

n = 1000000

def palin_dec(n):
    d = []
    while n:
        d.append(n%10)
        n /= 10
    for i in xrange(len(d) / 2):
        if d[i] != d[-i-1]:
            return False
    return True

def palin_bin(n):
    d = []
    while n:
        d.append(n%2)
        n /=2 
    for i in xrange(len(d) / 2):
        if d[i] != d[-i-1]:
            return False
    return True

r = []

for i in xrange(1, n, 2):
    if palin_dec(i) and palin_bin(i):
        r.append(i)

print r
print sum(r)
