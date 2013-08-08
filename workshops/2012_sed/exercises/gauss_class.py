#!/usr/bin/env python
"""
Created on Aug 27, 2012

@author: behry
"""
# 2 (a)
# Rewrite your last script into a class that requires
# the standard deviation as a variable in its constructor
# and which has a method that adds Gaussian noise to an
# input trace. Generate a sine wave, add noise to it and plot
# both traces using the matplotlib package.
import random
import math
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

if __name__ == '__main__':
    # make a sine curve and add some noise to it
    f = 3.
    trace = [math.sin(2 * math.pi * f * t * 0.001) for t in range(0, 1001)]
    noise = Gauss(0.1)
    noisy_trace = noise.add_gauss(trace)
    plt.plot(noisy_trace)
    plt.plot(trace, 'r')
    plt.show()
