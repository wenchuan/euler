#!/usr/bin/python

import itertools

def num(l):
    r = 0
    for i in l:
        r = r * 10 + i
    return r

def substring_divisible(l):
    return ( num(l[1:4]) % 2 == 0 and
            num(l[2:5]) % 3 == 0 and
            num(l[3:6]) % 5 == 0 and
            num(l[4:7]) % 7 == 0 and
            num(l[5:8]) % 11 == 0 and
            num(l[6:9]) % 13 == 0 and
            num(l[7:10]) % 17 == 0)

print substring_divisible(map(int,list("1406357289")))

a = itertools.permutations(range(10))

s = 0
try:
    while True:
        p = a.next()
        if substring_divisible(p):
            p = num(p)
            print p
            s += p
except StopIteration:
    print s
