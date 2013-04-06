import numpy as np
import matplotlib.pyplot as plt
from obspy.core import read
from obspy.signal import seisSim, cornFreq2Paz
from copy import deepcopy

onehzinst = cornFreq2Paz(1.0, damp=0.707) # 1Hz instrument
trace = read("http://examples.obspy.org/RJOB20090824.ehz")[0]
trace.data = trace.data - trace.data.mean()
sts2 = {'gain': 60077000.0,
        'poles': [(-0.037004000000000002+0.037016j),
                  (-0.037004000000000002-0.037016j),
                  (-251.33000000000001+0j),
                  (-131.03999999999999-467.29000000000002j),
                  (-131.03999999999999+467.29000000000002j)],
        'sensitivity': 2516778400.0,
        'zeros': [0j, 0j]}
data1 = deepcopy(trace.data)
trace.simulate(paz_remove=sts2, paz_simulate=onehzinst)
data2 = trace.data

# The plotting, plain matplotlib
t = np.arange(trace.stats.npts) / trace.stats.sampling_rate
plt.subplot(211)
plt.plot(t, data1, 'k')
plt.ylabel('STS-2 [counts]')
#
plt.subplot(212)
plt.plot(t, data2, 'k')
plt.ylabel('1Hz Instrument [m/s]')
plt.xlabel('Time [s]')
plt.show()
#plt.savefig('sts2onehz.pdf')

