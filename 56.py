#!/usr/bin/python

v = 0

for a in xrange(1,100):
    for b in xrange(1,100):
        v = max(v,sum(map(int,list(str(a**b)))))

print v

