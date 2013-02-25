#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
def divisors(n):
    sn = int(sqrt(n)) + 1
    i = 1
    r = 0
    while i < sn:
        if (n % i == 0):
            r += 1
        i += 1
    return r * 2

t = 0
i = 1

while (divisors(t) < 500):
    t += i
    i += 1

print t
