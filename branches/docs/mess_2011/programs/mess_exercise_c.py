# exercise C
# - modify program of exercise A:
# - fetch waveform data and response information via arclink from WebDC

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

ampl = (ampl_n + ampl_e) / 2

hypo_dist = 7.1

from math import *
ml = log10(ampl / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
print ml
