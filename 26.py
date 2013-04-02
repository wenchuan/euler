#!/usr/bin/python

# look for previous observed remainder
def get_recur_cycle(num):
    lookup = {}
    n = 0
    x = 1
    while True:
        if x < num:
            x *= 10
        else:
            x = x % num
            if x == 0:
                return 0
            if lookup.has_key(x):
                return n - lookup[x]
            else:
                lookup[x] = n
                n += 1

for i in xrange(1, 1000):
    print i, get_recur_cycle(i)
