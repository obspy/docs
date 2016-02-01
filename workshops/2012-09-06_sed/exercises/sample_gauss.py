#!/usr/bin/env python
"""
Created on Aug 23, 2012

@author: behry
"""

import random
import sys
import math

mu = float(sys.argv[1])
sigma = float(sys.argv[2])
values = []
for i in range(100):
    values.append(random.normalvariate(mu, sigma))

f = open('gauss_dist.txt', 'w')
for i, e in enumerate(values):
    print >> f, "%3d %.4f" % (i, e)
f.close()

values = []
f = open('gauss_dist.txt')
for _l in f.readlines():
    a = _l.split()
    cnt = int(a[0])
    val = float(a[1])
    values.append(val)

mean = sum(values) / len(values)
std = math.sqrt(sum([(x - mean) ** 2 for x in values]) / len(values))
print "mean: ", mean, "standard deviation: ", std

# 1 (b)
# Use the text of this exercise and count the number of occurences for
# every word using collections.defaultdict. 
from collections import defaultdict
text = """Use the text of this exercise and count the number of occurences for
every word using collections.defaultdict."""
words = text.split()
d = defaultdict(int)
for _w in words:
    d[_w] += 1
print d
