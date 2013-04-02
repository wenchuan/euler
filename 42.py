#!/usr/bin/python
#http://projecteuler.net/problem=42

s = open('words.txt', 'r').read()

a = s.split('","')

a[0] = a[0][1:]
a[-1] = a[-1][:-1]

b = map(lambda y: sum(map(lambda x: ord(x) - ord('A') + 1, y)), a)

triangles = [0,1,3,6,10]

def isTriangleNumber(n):
    while triangles[-1] <= n:
        x = len(triangles)
        N = x * (x + 1) / 2
        triangles.append(N)
    if n in triangles:
        return 1
    else:
        return 0

c = map(isTriangleNumber, b)

print sum(c)
