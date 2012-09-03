#!/usr/bin/env python
"""
Created on Sep 3, 2012

@author: behry
"""

# 1 (a)
# Using the modules random, sys and math write a
# script that reads mean and standard deviation of a normal distribution from 
# the command line and writes 100
# normally distributed random numbers to a file.
# Read those numbers back in and write their mean
# and standard deviation to stdout.
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


# 2 (a)
# Rewrite your last script into a class that requires
# the standard deviation as a variable in its constructor
# and which has a method that adds Gaussian noise to an
# input trace. Generate a sine wave, add noise to it and plot
# both traces using the matplotlib package.
import matplotlib.pyplot as plt

class Gauss:

    def __init__(self, sigma):
        self.sigma = sigma

    def add_gauss(self, values):
        nval = []
        for i in values:
            ns = random.normalvariate(i, self.sigma)
            nval.append(ns)
        return nval

# make a sine curve and add some noise to it
f = 3.
trace = [math.sin(2 * math.pi * f * t * 0.001) for t in range(0, 1001)]
noise = Gauss(0.1)
noisy_trace = noise.add_gauss(trace)
plt.plot(noisy_trace)
plt.plot(trace, 'r')
plt.show()

# 2 (b)
# Write a function that takes a list of program 
# names as input and returns a dictionary with 
# the programs' complete path on the current computer
# system as values. Programs that are not found should
# have the value None.

import os

def findprograms(proglist):
    outdict = {}
    dirlist = os.environ['PATH'].split(":")
    for prog in proglist:
        for dir in dirlist:
            fname = os.path.join(dir, prog)
            if os.path.isfile(fname):
                outdict[prog] = fname
        if prog not in outdict.keys():
            outdict[prog] = None
    return outdict


print findprograms(['psxy', 'emacs', 'blub', 'blub'])

import numpy as np
import sys

# 3 (a)
# Define a 3 x 3 matrix, e.g. A = np.matrix('1 2 3; 4 5 6; 7 8 9'). 
# Extract the 2 x 2 matrix in the lower right corner of the matrix 
# A as a slice. Add this slice to another 2 x 2 matrix, multiply 
# the result by a 2 x 2 matrix and insert this final result in 
# the upper left corner of the original matrix A.
# Control the result by hand calculation. 
A = np.matrix('1 2 3; 4 5 6; 7 8 9')
c = np.dot(A[1:, 1:] + np.array([[-4, -5], [-7, -8]]), np.array([[1, 0], [0, 1]]))
A[0:2, 0:2] = c
print A

# 3 (b)
# Take the original matrix A from the previous exercise and
# replace all values greater than 1 but smaller than 5 with 0 using the
# numpy function 'where'.
A = np.matrix('1 2 3; 4 5 6; 7 8 9')
print np.where((A > 1) & (A < 5), 0, A)

# 3 (c)
# Redo exercise 1 (a) using only numpy functions.
mu = float(sys.argv[1])
sigma = float(sys.argv[2])
values = np.random.randn(100) * sigma + mu
np.savetxt('gauss_dist.txt', values, fmt='%.4f')
values = np.loadtxt('gauss_dist.txt')
mean = values.mean()
std = values.std()
print "mean: ", mean, "standard deviation: ", std

# 3 (d)
# If $x_i = x_1, ..., x_n$ are uniformly distributed numbers
# between $a$ and $b$, then $\frac{b-a}{n}\sum_{i=0}^n f(x_i)$ is an
# approximation to the integral $\int_a^b f(x)dx$ (Monte Carlo integration).
# Implement this menthod using the numpy.random module for $f(x) =
# sin(x)$ and compare the result with any of the integration methods from
# scipy.integrate and the analytical result.

import scipy.integrate

a = 0
b = np.pi
n = 1000

x = np.linspace(a, b, n)
y = np.sin(x)
print scipy.integrate.trapz(y, x)

xi = (b - a) * np.random.random_sample(n) + a
fi = np.sin(xi)
print (b - a) / n * fi.sum()

# 4 (a)
# Plot the following two stations as red triangles on a map and calculate
# their distance, azimuth and back-azimuth for a spherical earth.
# SULZ: lat=47.52748, lon=8.11153
# SALO: lat=45.6183, lon=10.5243
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pyproj

lats = [47.52748, 45.6183]
lons = [8.11153, 10.5243]
names = ['SULZ', 'SALO']
m = Basemap(projection='merc', llcrnrlat=43, urcrnrlat=48, \
            llcrnrlon=4, urcrnrlon=12, lat_ts=45, resolution='i')
x, y = m(lons, lats)
m.drawcountries()
m.scatter(x, y, 100, color="r", marker="^")
for i, name in enumerate(names):
    plt.text(x[i], y[i], name, va='top')
gc = pyproj.Geod(ellps='sphere')
az, baz, dist = gc.inv(lons[0], lats[0], lons[1], lats[1])
print "azimuth=%.2f, back-azimuth=%.2f, distance=%.2f km" % (az, baz, dist / 1000.)
plt.show()

# 4 (b)
# Plot the real component of the spherical harmonics of order 
# 2 and degree 5 on a sphere.
# The modules that you will need are:
# scipy.special (the function sph_harm)
# numpy
# basemap
# matplotlib
#
# Note: Spherical harmonics are computed in colatitude and basemap
# uses latitude. 
from scipy.special import sph_harm

lats = np.linspace(-90, 90, 100)
lons = np.linspace(0, 360, 100)
colats = 90 - lats
X, Y = np.meshgrid(lons, colats)
X1, Y1 = np.meshgrid(lons, lats)
zval = sph_harm(2, 5, X * 2 * np.pi / 360., Y * np.pi / 180.)
m = Basemap(projection='ortho', lon_0= -120, lat_0=20, resolution='l')
m.drawparallels(np.arange(-90., 120., 30.))
m.drawmeridians(np.arange(0., 420., 60.))
X2, Y2 = m(X1, Y1)
m.contourf(X2, Y2, np.real(zval), 30)
m.colorbar()
plt.show()

