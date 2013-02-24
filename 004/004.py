#!/usr/bin/python
# -*- coding: utf-8 -*-

def isPalindrome(n):
    s = str(n)
    return (s == s[::-1])

r = None
i = 999

while (i > 99):
    j = i
    while (i * j > r) & (j > 99):
        if isPalindrome(i * j):
            r = i * j
        j -= 1
    i -= 1

print r
