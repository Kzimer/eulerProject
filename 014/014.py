#!/usr/bin/python
# -*- coding: utf8 -*-

def gen(n):
    yield n
    while (n != 1):
        if (n % 2):
            n = 3 * n +1
        else:
            n /= 2
        yield n

n = 1
r = 0
m = 0

for n in xrange(1, 1000000):
    l = len([a for a in gen(n)])
    if (m < l):
        r = n
        m = l

print r
