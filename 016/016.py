#!/usr/bin/python
# -*- coding: utf8 -*-

def fastExp(base, exponent):
    if (exponent == 0):
        return 1
    elif (exponent > 0):
        aux = fastExp(base, (exponent // 2))
        if (exponent % 2 == 1):
            return (aux * aux * base)
        else:
            return (aux * aux)

def sumDigits(n):
    if n:
        return sumDigits(n / 10) + (n % 10)
    else:
        return 0

print sumDigits(fastExp(2, 1000))
