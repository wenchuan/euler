#!/usr/bin/python
#http://projecteuler.net/problem=30

p = 5

for a in xrange(10):
    aa = a * 100000
    ap = a**p
    for b in xrange(10):
        bb = b * 10000
        bp = b**p
        for c in xrange(10):
            cc = c * 1000
            cp = c**p
            for d in xrange(10):
                dd = d * 100
                dp = d**p
                for e in xrange(10):
                    ee = e * 10
                    ep = e**p
                    for f in xrange(10):
                        ff = f
                        fp= f**p
                        if aa + bb + cc + dd + ee + ff == ap + bp + cp + dp + ep + fp:
                            print a,b,c,d,e,f
