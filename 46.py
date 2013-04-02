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

def goldbach(n):
    if n % 2 == 0:
        return 0
    if isPrime(n):
        return 0
    for i in xrange(n):
        if 2 * i * i > n:
            return 2
        if isPrime(n - 2 * i * i):
            return 1

l = 10000
for i in xrange(l):
    if goldbach(i) == 2:
        print i
