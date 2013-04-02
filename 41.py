#!/usr/bin/python

def isPandigital(s):
    x = list(s)
    x.sort()
    r = ''
    for i in x:
        r += i
    return r == '123456789'[:len(r)]

n = 7654321

a = [True] * (n+1)
primes = []

for i in xrange(2, n+1):
    if a[i]:
        for j in xrange(2*i, n+1, i):
            a[j] = False

for i in xrange(len(a)):
    if a[i] and isPandigital(str(i)):
        print i
