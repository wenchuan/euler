#!/usr/bin/python

import math

def reversePentagonal(y):
    delta2 = 24 * y + 1
    delta = int(math.floor(math.sqrt(delta2)))
    if delta * delta != delta2:
        return False
    return (not (delta + 1) % 6)

def reverseTriangle(y):
    delta2 = 8 * y + 1
    delta = int(math.floor(math.sqrt(delta2)))
    if delta * delta != delta2:
        return False
    return (not (delta - 1) % 2)

i = 143
while True:
    i += 1
    h = 2 * i * i - i
    if reversePentagonal(h) and reverseTriangle(h):
        print h
        break
