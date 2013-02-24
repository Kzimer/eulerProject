#!/usr/bin/python
# -*- coding: utf-8 -*-
"""1^2 + 2^2 + ... + n^2 = (2n^3 + 3n^2 + n) / 12
and (1 + 2 + ... + n)^2 = (n^2 - n) / 2
so the difference is (n^2 (3n^2 + 2n - 3) - 2n) / 12
"""

def diff(n):
    n2 = n * n
    return (n2*(3*n2 + 2*n - 3) - 2*n) / 12
    
print diff(100)
