#!/usr/bin/env python
"""
Created on Aug 27, 2012

@author: behry
"""
import numpy as np
import sys

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

# Take the original matrix A from the previous exercise and
# replace all values greater than 1 but smaller than 5 with 0 using the
# numpy function 'where'.
A = np.matrix('1 2 3; 4 5 6; 7 8 9')
print np.where((A > 1) & (A < 5), 0, A)

# Redo exercise 1 (a) using only numpy functions.
mu = float(sys.argv[1])
sigma = float(sys.argv[2])
values = np.random.randn(100) * sigma + mu
np.savetxt('gauss_dist.txt', values, fmt='%.4f')
values = np.loadtxt('gauss_dist.txt')
mean = values.mean()
std = values.std()
print "mean: ", mean, "standard deviation: ", std

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
