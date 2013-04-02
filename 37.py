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

summ = 0
cnt = 0
for i in primes[4:]:
    i = str(i)
    l = len(i)
    truncatable = True
    for x in xrange(1,l):
        left,right = i[:x], i[x:]
        if not a[int(left)] or not a[int(right)]:
            truncatable = False
    if truncatable:
        summ += int(i)
        cnt += 1
        print i
    if cnt == 11:
        print 'total = ', summ
        break
