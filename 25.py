#!/usr/bin/python

dropped = 0

f_1 = 1
f_2 = 1

l = 1000

for i in xrange(2000000):
    f = f_1 + f_2
    if len(str(f)) >= l:
        print i + 3, f
        break
    f_1, f_2 = f, f_1
