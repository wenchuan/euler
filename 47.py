#!/usr/bin/python

n = 1000000

a = [True] * (n+1)
primes = []

a[0] = False
a[1] = False

for i in xrange(2, n+1):
    if a[i]:
        for j in xrange(2 * i, n+1, i):
            a[j] = False

for i in xrange(len(a)):
    if a[i]:
        primes.append(i)

table = {}
def factorize(n):
    if table.has_key(n):
        return table[n]
    r = []
    for i in primes:
        if i > n:
            table[n] = r
            return table[n]
        if n % i == 0:
            if table.has_key(n / i):
                if i in table[n/i]:
                    table[n] = table[n/i]
                else:
                    table[n] = list(table[n/i])
                    table[n].append(i)
                    table[n].sort()
                return table[n]
            r.append(i)

print factorize(123)
print factorize(246)

seen = 0
x = 4
for i in xrange(n):
    if len(factorize(i)) == x:
        seen += 1
        if (seen == x):
            print i - x + 1
            break
    else:
        seen = 0
