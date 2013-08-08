import numpy as np
from obspy.core import Trace, UTCDateTime

x = np.zeros(200)
x[100] = 1
tr = Trace(x)
tr.stats.network = "XX"
tr.stats.station = "SDFD1"
print tr
print "showing original trace"
tr.plot()
tr.stats.sampling_rate = 20
tr.stats.starttime = UTCDateTime(2011, 2, 21, 8)
print tr
tr.plot()

tr.filter("lowpass", freq=1)
print "showing filtered trace"
tr.plot()
tr.trim(tr.stats.starttime + 4.5, tr.stats.endtime - 2)
print "showing trimmed trace"
tr.plot()

tr.data = tr.data * 500
tr2 = tr.copy()
tr2.data = tr2.data + np.random.randn(len(tr2))
tr2.stats.station = "SDFD2"
print tr2
print "showing trace with gaussian noise added"
tr2.plot()
