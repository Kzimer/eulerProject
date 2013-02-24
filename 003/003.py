#!/usr/bin/python
# -*- coding: utf-8 -*-

def factors(x):
    if (x == 1):
        return []
    f = 2
    while (x % f):
        f+=1
    return factors(x / f) + [f]

print max(factors(600851475143))
