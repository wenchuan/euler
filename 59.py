#!/usr/bin/python

import sys

secret = map(int,open('cipher1.txt','r').read()[:-1].split(','))
clear = secret * 1

alphabet = range(97,123)

def decrypt(cipher):
    for i in xrange(len(secret)):
        c = secret[i] ^ cipher[i % len(cipher)]
        # text should be printable
        if c < ord(' ') or c > ord('~'):
            return
    name = ''
    for c in cipher:
        name += chr(c)
    fp = open('59/' + name + '.txt', 'w')
    for i in xrange(len(secret)):
        c = secret[i] ^ cipher[i % len(cipher)]
        fp.write(chr(c))
    fp.close()

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            decrypt([a,b,c])

cipher = [ord('g'), ord('o'), ord('d')]
s = 0
for i in xrange(len(secret)):
    s += secret[i] ^ cipher[i % len(cipher)]

print s
