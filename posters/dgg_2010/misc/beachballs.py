from matplotlib import rc as matplotlibrc
matplotlibrc('figure.subplot', right=1.00, bottom=0.00, top=1.00, left = 0.00)
import matplotlib.pyplot as plt
from obspy.imaging.beachball import Beach

mt = [[0.91, -0.89, -0.02, 1.78, -1.55, 0.47],
      [274, 13, 55],
      [130, 79, 98],
      [264.98, 45.00, -159.99],
      [160.55, 76.00, -46.78],
      [1.45, -6.60, 5.14, -2.67, -3.16, 1.36],
      [235, 80, 35],
      [138, 56, 168],
      [1, 1, 1, 0, 0, 0],
      [-1, -1, -1, 0, 0, 0],
      [1, -2, 1, 0, 0, 0],
      [1, -1, 0, 0, 0, 0],
      [1, -1, 0, 0, 0, -1],
      [179, 55, -78],
      [10, 42.5, 90],
      [10, 42.5, 92],
      [150, 87, 1],
      [0.99, -2.00, 1.01, 0.92, 0.48, 0.15],
      [5.24, -6.77, 1.53, 0.81, 1.49, -0.05],
      [16.578, -7.987, -8.592, -5.515, -29.732, 7.517],
      [-2.39, 1.04, 1.35, 0.57, -2.94, -0.94],
      [150, 87, 1]]

# Initialize figure
fig = plt.figure(1, figsize=(3, 3), dpi=100)
ax = fig.add_subplot(111, aspect='equal')


x = -100
y = -100
for i, t in enumerate(mt):
    # add the beachball (a collection of two patches) to the axis
    ax.add_collection(Beach(t, size=100, width=30, xy=(x,y),
                            linewidth=.6))
    x += 50
    if (i+1) % 5 == 0:
        x = -100
        y += 50

# Set the x and y limits and save the output
ax.axis([-120, 120, -120, 120])
ax.set_yticks([])
ax.set_xticks([])
fig.savefig('beachball-collection.pdf')
