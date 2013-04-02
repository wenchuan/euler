#!/usr/bin/python

def isPalindrome(x):
    a = []
    while x:
        a.append(x%10)
        x /= 10
    for i in xrange(len(a) / 2):
        if a[i] != a[-i-1]:
            return False
    return True

def factorable(x):
    for i in xrange(max(x/999,100), x):
        if i > x/i:
            return False
        if x % i == 0:
            print i, x/i, x
            return True

print factorable(12423)

for x in xrange(998001, 10000, -1):
    if isPalindrome(x):
        if factorable(x):
            print x
            break;
