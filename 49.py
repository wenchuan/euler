#!/usr/bin/python

import itertools

n = 10000

p = [True] * (n+1)
primes = []

p[0] = False
p[1] = False

for i in xrange(2, n+1):
    if p[i]:
        for j in xrange(2 * i, n+1, i):
            p[j] = False

for i in xrange(len(p)):
    if p[i]:
        primes.append(i)

def num(l):
    return l[0]*1000 + l[1]*100 + l[2]*10 + l[3]

def find_series(l):
    ll = len(l)
    for i in xrange(ll - 2):
        for j in xrange(i + 1, ll - 1):
            for k in xrange(j + 1, ll):
                if l[i] + l[k] == l[j] + l[j]:
                    return [l[i],l[j],l[k]]
    return None

for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                i = itertools.permutations([a,b,c,d])
                pool = set()
                try:
                    while True:
                        x = i.next()
                        x = num(x)
                        if len(str(x)) == 4 and p[x]:
                            pool.add(x)
                except StopIteration:
                    pass
                if len(pool) < 3:
                    continue
                series = find_series(list(pool))
                if series:
                    print series, sum(series)
