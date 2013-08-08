#!/usr/bin/env python

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from obspy.imaging.beachball import Beach
import gzip

# read in topo data (on a regular lat/lon grid)
# (srtm data from: http://srtm.csi.cgiar.org/)
srtm3 = np.loadtxt(gzip.open("srtm_1240-1300E_4740-4750N.asc.gz"), skiprows=8)
# origin of data grid as stated in srtm data file header
x_min = 12. + (40. / 60.)
x_max = 13.
y_min = 47. + (40. / 60.)
y_max = 47. + (50. / 60.)

# create arrays with all lon/lat values from min to max and
lats = np.linspace(y_max, y_min, srtm3.shape[0])
lons = np.linspace(x_min, x_max, srtm3.shape[1])

# create Basemap instance with Mercator projection
# we want a slightly smaller region than covered by our srtm data
left = 12.75
right = 12.95
bottom = 47.69
top = 47.81

m = Basemap(projection='merc', lon_0=13, lat_0=48, resolution="h",
            llcrnrlon=left, llcrnrlat=bottom, urcrnrlon=right, urcrnrlat=top)

# create grids and compute map projection coordinates for lon/lat grid
x, y = m(*np.meshgrid(lons,lats))

# make gradient plot
#ps = m.pcolor(x, y, srtm3)
# make contour plot
cs = m.contour(x, y, srtm3, 40, colors=".4", lw=0.5, alpha=0.3)
m.drawcountries(color="red", linewidth=1)

# draw a lon/lat grid (20 lines for an interval of one degree)
m.drawparallels(np.linspace(47, 48, 21), labels=[1,1,0,0], fmt="%.2f", dashes=[2,2])
m.drawmeridians(np.linspace(12, 13, 21), labels=[0,0,1,1], fmt="%.2f", dashes=[2,2])

# plot station positions and names into the map
# again we have to compute the projection of our lon/lat values

lats = [47.737166999999999,
  47.737166999999999,
  47.761657999999997,
  47.805720999999998,
  47.740501000000002,
  47.745097999999999,
  47.745097999999999,
  47.751190000000001,
  47.754452000000001,
  47.751601999999998]

lons = [12.795714,
         12.795714,
         12.864466,
         12.818837,
         12.867100000000001,
         12.824082000000001,
         12.824082000000001,
         12.836045,
         12.849878,
         12.866491999999999]

names = ['RJOB',
          'RJOB',
          'RMOA',
          'RNHA',
          'RNON',
          'RTBE',
          'RTBE',
          'RTBM',
          'RTSH',
          'RTVS']

x, y = m(lons, lats)
m.scatter(x, y, 200, color="r", marker="v", edgecolor="k", zorder=3)
for i in range(len(names)):
    plt.text(x[i], y[i], " " + names[i], color='k', va="top", 
             family="monospace", weight="bold")


# add beachballs for three events
lats = [47.74750100000, 47.74878700000, 47.76233333330]
longs = [12.88500000000, 12.82278700000, 12.83816666670]
# three focal mechanisms for the beachball routine, specified as [strike, dip, rake]
focmecs = [[60.00000000000, 65.00000000000, -60.00000000000],
           [80.00000000000, 60.00000000000, 80.00000000000],
           [40.00000000000, 80.00000000000, 90.00000000000]]
x, y = m(longs, lats)


ax = plt.gca()
print focmecs
print x
print y
for i in range(len(focmecs)):
    b = Beach(focmecs[i], xy=(x[i], y[i]), width=1000, linewidth=1)
    b.set_zorder(10)
    ax.add_collection(b)

plt.savefig("basemap_beachball_demo2.pdf")
