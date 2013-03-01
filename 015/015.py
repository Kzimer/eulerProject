#!/usr/bin/python
# -*- coding: utf8 -*-

def nParmi2n(n):
    prod = 1
    quot = 1
    for i in xrange(1, n+1):
        if (prod % quot):
            prod *= (n + i) / quot
            quot = i
        else:
            prod *= (n + i)
            quot *= i
    return prod / quot

print nParmi2n(20)
