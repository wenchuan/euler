#!/usr/bin/python
import sys

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

def good(o_prime,i):
    if int(o_prime) < 10:
        return
    prime = list(o_prime)
    pos = []
    good_count = 0
    x = 0
    while (i != 0):
        if i % 2 != 0:
            pos.append(x)
        x += 1
        i = i / 2
    for m in xrange(10):
        if m == 0 and 0 in pos:
            continue
        for p in pos:
            prime[p] = str(m)
        n = ''
        for d in prime:
            n += d
        if a[int(n)]:
            print n
            good_count += 1
        if good_count == 8:
            print 'bingo!', o_prime, pos
            sys.exit(0)

good('120383',21)

for prime in primes:
    p = str(prime)
    for i in xrange(1, 2 ** len(p)):
        good(p,i)
