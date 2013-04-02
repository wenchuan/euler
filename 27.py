#!/usr/bin/python

p = [False,False,True,True,False,True]

def isP(n):
    for i in xrange(2,n):
        if i * i > n:
            return True
        if n % i == 0:
            return False

def isPrime(n):
    if n < 0:
        return False
    if len(p) > n:
        return p[n]
    for i in xrange(len(p), n+1):
        p.append(isP(i))
    return p[n]

def numPrimes(a,b):
    n = 0
    while True:
        nn = n*n
        x = nn + a * n + b
        if not isPrime(x):
            return n
        n += 1

m,r = 0,0

l = 1000

for a in xrange(-l + 1,l):
    for b in xrange(-l + 1,l):
        x = numPrimes(a,b)
        if x > m:
            m = x
            r = a * b

print m,r
