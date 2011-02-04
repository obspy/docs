# XXX STEP 3
# modify program of part a) to fetch data and response information for station RJOB via arclink from WebDC

from obspy.core import UTCDateTime
import obspy.arclink

client = obspy.arclink.Client()

t = UTCDateTime("2008-04-17T16:00:32Z")

st = client.getWaveform(network="BW", station="RJOB", location="", channel="EH*",
                        starttime=t-30, endtime=t+120, getPAZ=True)

paz_wa = {'gain': 2800, 'zeros': [0j], 'sensitivity': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

st.simulate(paz_remove="self", paz_simulate=paz_wa)

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
