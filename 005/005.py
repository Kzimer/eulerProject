#!/usr/bin/python
# -*- coding: utf-8 -*-

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if (a % b == 0):
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

r = 1

for n in xrange(2, 20):
    r = lcm(r, n)

print r
