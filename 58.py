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

step = 2
x = 1
cnt = 0 
i = 0

while True:
    i += 1
    for j in xrange(4):
        x += step
        cnt += isPrime(x)
    step += 2
    if cnt * 10 < 4 * i + 1:
        print cnt, 4 * i + 1, i * 2 + 1
        exit(0)
