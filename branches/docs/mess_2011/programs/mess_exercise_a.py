# exercise A
# - read earthquake data
# - use manually specified PAZ to simulate Wood Anderson seismometer
# - trim to around manually specified origin time
# - determine peak-to-peak amplitudes as simple min/max on both N and E component
# - use manually specified hypocentral distance to calculate local magnitude

from obspy.core import UTCDateTime, read

st = read("RJOB.MSEED")
print st

paz_sts2 = {'poles': [-0.037004+0.037016j, -0.037004-0.037016j, -251.33+0j, -131.04-467.29j, -131.04+467.29j],
            'sensitivity': 2516778600.0, 'zeros': [0j, 0j], 'gain': 60077000.0}
paz_wa = {'gain': 2800, 'zeros': [0j], 'sensitivity': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

st.simulate(paz_remove=paz_sts2, paz_simulate=paz_wa)

t = UTCDateTime("2008-04-17T16:00:32Z")
st.trim(t-5, t+40)

st_n = st.select(component="N")
tr_n = st_n[0]
print tr_n
ampl_n = tr_n.data.max() - tr_n.data.min()

st_e = st.select(component="E")
tr_e = st_e[0]
print tr_e
ampl_e = tr_e.data.max() - tr_e.data.min()

ampl = (ampl_n + ampl_e) / 2

hypo_dist = 7.1

from math import *
ml = log10(ampl / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
print ml
