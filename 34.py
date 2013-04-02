#!/usr/bin/python

factorials = [1,1,2,6,24,120,720,5040,40320,362880]

for i in xrange(100,10000000):
    if sum(map(lambda x: factorials[int(x)], str(i))) == i:
        print i
