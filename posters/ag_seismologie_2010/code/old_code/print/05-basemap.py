#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from obspy.imaging.beachball import Beach
import obspy.seishub
import gzip
SERVER = 'http://localhost:7777'

# Get the stations from seishub.
client = obspy.seishub.Client(base_url = SERVER)
stations = client.station.getList('BW', '*',
           min_latitude=47.69, max_latitude=47.81,
           min_longitude=12.75, max_longitude=12.95)
# Gets the latitude, longitue and station_id.
stations_lat = [station['latitude'] for station in stations]
stations_long = [station['longitude'] for station in stations]
stations_id = [station['station_id'] for station in stations]

# Get the events.
events = client.event.getList(min_latitude=47.69,
            max_latitude=47.81, min_longitude=12.75,
            max_longitude=12.95)
# Filter events with fault plane solutions.
events = [event for event in events if event['np1_rake']]
events_lat = [event['latitude'] for event in events]
events_long =[event['longitude'] for event in events]
events_focmec = [[float(event['np1_strike']), float(event['np1_dip']),
                  float(event['np1_rake'])] for event in events]

# Read in topo data (on a regular lat/lon grid).
# (srtm data from: http://srtm.csi.cgiar.org/)
srtm3 = np.loadtxt(gzip.open("../misc/srtm_1240-1300E_4740-4750N.asc.gz"),
                   skiprows=8)
# Origin of data grid as stated in srtm data file header.
x_min = 12. + (40. / 60.)
x_max = 13.
y_min = 47. + (40. / 60.)
y_max = 47. + (50. / 60.)

# Create arrays with all lon/lat values from min to max.
lats = np.linspace(y_max, y_min, srtm3.shape[0])
lons = np.linspace(x_min, x_max, srtm3.shape[1])
# Create Basemap instance with Mercator projection.
m = Basemap(projection='merc',lon_0=13,lat_0=48,resolution="h",
            llcrnrlon=12.75, llcrnrlat=47.69,
            urcrnrlon=12.95, urcrnrlat=47.81)
# Create grids and compute map projection coordinates for lon/lat grid.
x, y = m(*np.meshgrid(lons,lats))

# Make gradient plot.
#ps = m.pcolor(x, y, srtm3)
# Make contour plot.
cs = m.contour(x, y, srtm3, 40, colors=".4", lw=0.5, alpha=0.3)
m.drawcountries(color="red", linewidth=1)

# Draw a lon/lat grid (20 lines for an interval of one degree).
m.drawparallels(np.linspace(47, 48, 21), labels=[1,1,0,0], fmt="%.2f",
                dashes=[2,2])
m.drawmeridians(np.linspace(12, 13, 21), labels=[0,0,1,1], fmt="%.2f",
                dashes=[2,2])

# Calculate map projection for the coordinates.
x, y = m(stations_long, stations_lat)
m.scatter(x, y, 200, color="r", marker="v", edgecolor="k", zorder=3)
for i in range(len(stations_id)):
    plt.text(x[i], y[i], " " + stations_id[i], color='k', va="top", 
             family="monospace", weight="bold")

# Calculate map projectoins for the beachballs.
x, y = m(events_long, events_lat)
# Plot the beachballs.
ax = plt.gca()
for i in range(len(events_focmec)):
    b = Beach(events_focmec[i], xy=(x[i], y[i]), width=1000, linewidth=1)
    b.set_zorder(10)
    ax.add_collection(b)

# Save the figure.
plt.savefig("basemap_beachball_example.pdf")
