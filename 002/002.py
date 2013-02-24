#!/usr/bin/python
# -*- coding: utf-8 -*-

r = 0
f0 = 1
f1 = 2

while(f1<4000000):
    t = f1
    f1 += f0
    f0 = t
    if (f1 % 2 == 0):
        r += f1

print r
