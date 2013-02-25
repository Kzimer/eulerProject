#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt

def hasFactors(x, l):
    '''If x has a factor in l (i.e. if there exists y in l so that x % y == 0),
       return True
       else return False
       l is supposed to be sorted. If y > sqrt(x), y can not be a factor of x,
       therefore we can reduce the number of cases to examine, thus reducing
       drastically the computation time.
    '''
    i = 0
    sx = sqrt(x)
    while (i < len(l)):
        if not (x % l[i]):
            return True
        if (l[i] > sx):
            return False
        i += 1

l = [2]
x = 3
r = 2

while (x < 2000000):
    if not hasFactors(x,l):
        l += [x]
        r += x
    x += 2

print r
