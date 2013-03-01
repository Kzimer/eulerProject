#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def numberInWords(n):
    if (n == 1):
        return 'one'
    elif (n == 2):
        return 'two'
    elif (n == 3):
        return 'three'
    elif (n == 4):
        return 'four'
    elif (n == 5):
        return 'five'
    elif (n == 6):
        return 'six'
    elif (n == 7):
        return 'seven'
    elif (n == 8):
        return 'eight'
    elif (n == 9):
        return 'nine'
    elif (n == 1000):
        return 'one thousand'
    else:
        h = (n / 100) % 10
        if (h > 0):
            w = '%s hundred' % numberInWords(h)
            if (n - (h * 100) > 0):
                return '%s and %s' % (w, numberInWords(n - (h * 100)))
            else:
                return w
        else:
            t = (n / 10) % 10
            d = n - (t * 10)
            if (t == 1):
                if (d == 0):
                    return 'ten'
                elif (d == 1):
                    return 'eleven'
                elif (d == 2):
                    return 'twelve'
                elif (d == 3):
                    return 'thirteen'
                elif (d == 5):
                    return 'fifteen'
                elif (d == 8):
                    return 'eighteen'
                else:
                    return '%steen' % numberInWords(d)
            elif (d == 0):
                if (t == 2):
                    return 'twenty'
                elif (t == 3):
                    return 'thirty'
                elif (t == 4):
                    return 'forty'
                elif (t == 5):
                    return 'fifty'
                elif (t == 8):
                    return 'eighty'
                else:
                    return '%sty' % numberInWords(t)
            else:
                return '%s-%s' % (numberInWords(10 * t), numberInWords(d))
regex = re.compile(r'[\s-]')
print len(''.join([re.sub(regex, '', numberInWords(i)) for i in xrange(1, 1001)]))









