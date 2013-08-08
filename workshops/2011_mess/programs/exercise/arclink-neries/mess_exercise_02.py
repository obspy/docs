# exercise 2
# - change program of exercise 1:
#   - read raw earthquake data ("RJOB.MSEED")
#   - use manually specified PAZ to simulate Wood-Anderson seismometer
#   - trim to around manually specified origin time
# - estimate magnitude like in 1

from obspy.core import UTCDateTime, read
from math import *

st = read("RJOB.MSEED")

PAZ_STS2 = {'poles': [-0.037004+0.037016j, -0.037004-0.037016j, -251.33+0j, -131.04-467.29j, -131.04+467.29j],
            'sensitivity': 2516778600.0, 'zeros': [0j, 0j], 'gain': 60077000.0}
PAZ_WA = {'sensitivity': 2800, 'zeros': [0j], 'gain': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

st.simulate(paz_remove=PAZ_STS2, paz_simulate=PAZ_WA)

t = UTCDateTime("2008-04-17T16:00:32Z")
st.trim(t - 5, t + 40)

st_n = st.select(component="N")
ampl_n = st_n[0].data.max() - st_n[0].data.min()
st_e = st.select(component="E")
ampl_e = st_e[0].data.max() - st_e[0].data.min()
ampl = (ampl_n + ampl_e) / 2 / 2

hypo_dist = 7.1

ml = log10(ampl * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
print ml
