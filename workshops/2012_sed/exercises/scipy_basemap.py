#!/usr/bin/env python
"""
Created on Aug 27, 2012

@author: behry
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pyproj

# Plot the following two stations as red triangles on a map and calculate
# their distance, azimuth and back-azimuth for a spherical earth.
# SULZ: lat=47.52748, lon=8.11153
# SALO: lat=45.6183, lon=10.5243
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



