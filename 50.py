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


done = False

for i in xrange(len(primes), 2, -1):
    for j in xrange(len(primes) - i):
        s = sum(primes[j:j+i])
        if s > n:
            break
        if a[s]:
            print s, i
            done = True
    if done:
        break
    else:
        print i
