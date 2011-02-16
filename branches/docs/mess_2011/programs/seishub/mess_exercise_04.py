# exercise 4
# - modify program of exercise 2:
#   - fetch waveform data and response information via arclink from WebDC
# - estimate magnitude like in 2

from obspy.core import UTCDateTime
import obspy.seishub
from math import *

client = obspy.seishub.Client("http://localhost:8080")

t = UTCDateTime("2008-04-17T16:00:32Z")

st = client.waveform.getWaveform(network="BW", station="RJOB", location="", channel="EH*",
                                 starttime=t-30, endtime=t+120, getPAZ=True)

PAZ_WA = {'sensitivity': 2800, 'zeros': [0j], 'gain': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

st.simulate(paz_remove="self", paz_simulate=PAZ_WA)

st.trim(t - 5, t + 40)

st_n = st.select(component="N")
ampl_n = st_n[0].data.max() - st_n[0].data.min()
st_e = st.select(component="E")
ampl_e = st_e[0].data.max() - st_e[0].data.min()
ampl = (ampl_n + ampl_e) / 2 / 2

hypo_dist = 7.1

ml = log10(ampl * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
print ml
