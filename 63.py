#!/usr/bin/python

for i in xrange(1,10):
    for j in xrange(1000):
        if len(str(i ** j)) == j:
            print i, '^', j, '=', i**j
