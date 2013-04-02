#!/usr/bin/python

for a in xrange(1,10):
    for b in xrange(1,10):
        for c in xrange(10):
            if (a * 10 + b) * c == (b * 10 + c) * a:
                print a,b,c
