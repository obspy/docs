from matplotlib import rc as matplotlibrc
matplotlibrc('figure.subplot', right=1.00, bottom=0.00, left = 0.00, top=1.00)
import matplotlib.pylab as plt
from obspy.imaging.beachball import Beach
import os

# Moment tensors.
mt = [[264.98,45.00,-159.99], [130,79,98],
      [0.99,-2.00,1.01,0.92,0.48,0.15],
      [-2.39,1.04,1.35,0.57,-2.94,-0.94]]
    
# Initialize figure
fig = plt.figure(1, figsize=(4, 1), dpi=100)
ax = fig.add_subplot(111, aspect='equal')

x = -100
y = -100
for i, t in enumerate(mt):
    ax.add_collection(Beach(t, size=100, width=35, xy=(x,y), linewidth=.6))
    x += 50
    if (i+1) % 5 == 0:
        x = -100
        y += 50
# Set the x and y limits, disable the ticks and save the output
ax.axis([-125, 75, -125, -75])
ax.set_xticks([])
ax.set_yticks([])
for _i in ax.spines.values():
    _i.set_linewidth(0)
fig.savefig('beachball-collection.pdf')
