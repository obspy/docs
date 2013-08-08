from obspy.core import UTCDateTime

t = UTCDateTime(2011, 2, 21, 8)
t_cb = t + (3 * 60 * 60) - (1234 + 5e-6)
print "coffee break is at", t_cb.time

t_bf = UTCDateTime(2011, 2, 20, 11)
dt = t_cb - t_bf
print dt / 60, "minutes without coffee"
