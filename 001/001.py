#!/usr/bin/python
# -*- coding: utf-8 -*-

r = 0

for i in xrange(1000):
    if (i % 3 == 0) | (i % 5 == 0):
        r += i

print r
