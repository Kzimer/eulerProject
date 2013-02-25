#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt

def isSquare(x):
    return x == (int(sqrt(x))**2)

def sumTriplet(a, b):
    if isSquare(a**2 + b**2):
        return a + b + int(sqrt(a**2 + b**2))
    return 0

a = 3

while (a < 333):
    b = a + 1
    while(b < 500):
        if (sumTriplet(a, b) == 1000):
            print a * b * (sumTriplet(a, b) - a - b)
            break
        b += 1
    a += 1
