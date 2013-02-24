#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt

def hasFactors(x, l):
    i = 0
    sx = sqrt(x)
    while (i < len(l)):
        if not (x % l[i]):
            return True
        if (l[i] > sx):
            return False
        i += 1
    return False

l = [2]
x = 3

while (len(l) < 10001):
    if not hasFactors(x,l):
        l += [x]
    x += 2

print l[-1]
