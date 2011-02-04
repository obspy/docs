# XXX STEP 1
# calculate Ml for given origin time, station, data, metadata

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

hypo_dist = 7.1

from math import *
ml_n = log10(ampl_n / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
ml_e = log10(ampl_e / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0

ml = (ml_n + ml_e) / 2
print ml
