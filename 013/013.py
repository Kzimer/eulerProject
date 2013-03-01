#!/usr/bin/python
# -*- coding: utf-8 -*-

print str(sum([int(line[:13]) for line in open('./numbers', 'r')]))[:10]
