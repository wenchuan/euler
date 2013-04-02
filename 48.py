#!/usr/bin/python

#calculate n^n
def power(n):
    r = 1
    for i in xrange(n):
        r *= n
        if len(str(r)) > 12:
            r = int(str(r)[-12:])
    return r

print str(sum(map(power,range(1,1001))))[-10:]
