#!/usr/bin/python

s = open('names.txt', 'r').read()

a = s.split('","')

a[0] = a[0][1:]
a[-1] = a[-1][:-1]

a.sort()

b = map(lambda y: sum(map(lambda x: ord(x) - ord('A') + 1, y)), a)

r = 0L
for i in xrange(len(a)):
    r += (b[i] * (i+1))

print r
