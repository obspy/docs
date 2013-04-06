import numpy as np
import matplotlib.pyplot as plt
from obspy.core import read
from obspy.signal import seisSim, cornFreq2Paz

onehzinst = cornFreq2Paz(1.0, damp=0.707) # 1Hz instrument
tr = read("http://examples.obspy.org/RJOB20090824.ehz")[0]
tr.data = tr.data - tr.data.mean()
sts2 = {'gain': 60077000.0,
        'poles': [(-0.037004000000000002+0.037016j),
                  (-0.037004000000000002-0.037016j),
                  (-251.33000000000001+0j),
                  (-131.03999999999999-467.29000000000002j),
                  (-131.03999999999999+467.29000000000002j)],
        'sensitivity': 2516778400.0,
        'zeros': [0j, 0j]}
data2 = seisSim(tr.data,
        tr.stats.sampling_rate, sts2,
        inst_sim=onehzinst,water_level=600.0)
data2 = data2 / sts2["sensitivity"] 

# The plotting, plain matplotlib
t = np.arange(tr.stats.npts) / tr.stats.sampling_rate
plt.subplot(211)
plt.plot(t, tr.data, 'k')
plt.ylabel('STS-2 [counts]')
#
plt.subplot(212)
plt.plot(t, data2, 'k')
plt.ylabel('1Hz Instrument [m/s]')
plt.xlabel('Time [s]')
plt.savefig('sts2onehz.pdf')
#plt.show()

