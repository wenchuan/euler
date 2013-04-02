#!/usr/bin/python

import time

def table(nn):
    n = nn ** 5
    t0 = time.time()
    points = []
    lookup = set()
    for i in xrange(0, 2 * n + 1):
        p = pow(2,i,n),pow(3,i,n)
        if p not in lookup:
            lookup.add(p)
            points.append(p)
    t1 = time.time()
    print 'calculating', nn, '** 5', n, 'has', len(points), 'points'
    print t1-t0
    points.sort()
    t0 = time.time()
    print t0 - t1
    v = []
    high = []
    for i in xrange(len(points)):
        if i % 1000 == 0:
            print i, len(high)
        v.append(0)
        for j in high:
            if points[j][1] <= points[i][1] and v[j] + 1> v[i]:
                v[i] = v[j] + 1
        if v[i] >= len(high):
            high.append(i)
        elif points[high[v[i]]][1] > points[i][1]:
            high[v[i]] = i
    t1 = time.time()
    print t1-t0
    return max(v) + 1


result = 0
for i in xrange(1,31):
    if i not in [9,16,27]:
        result += table(i)
print result
