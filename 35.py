#!/usr/bin/python

n = 1000000

a = [True] * (n+1)
primes = []

a[0] = False
a[1] = False

for i in xrange(2, n+1):
    if a[i]:
        for j in xrange(2 * i, n+1, i):
            a[j] = False

for i in xrange(len(a)):
    if a[i]:
        primes.append(i)

def isCircularPrime(p):
    p = str(p)
    for i in xrange(len(p)):
        if not a[int(p[i:] + p[:i])]:
            return False
    return True

cnt = 0
for p in primes:
    if isCircularPrime(p):
        cnt += 1
        print p

print cnt
