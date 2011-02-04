# XXX STEP 4
# modify program of part c) to trim waveform based on a stalta trigger time

import obspy.neries
client_n = obspy.neries.Client()

events = client_n.getEvents(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
                            min_datetime="2008-04-17", max_datetime="2008-04-18")

event = events[0]

from obspy.core import UTCDateTime
import obspy.arclink

client = obspy.arclink.Client()

t = UTCDateTime("2008-04-17T16:00:32Z")

st = client.getWaveform(network="BW", station="RJOB", location="", channel="EH*",
                        starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)

paz_wa = {'gain': 2800, 'zeros': [0j], 'sensitivity': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

st.simulate(paz_remove="self", paz_simulate=paz_wa)

st_trig = st.select(component="Z")
st_trig.trigger("recstalta", 0.5, 10)
samples = st_trig[0].data.argmax()
t_trig = st[0].stats.starttime + (samples / st[0].stats.sampling_rate)

st.trim(t_trig-1, t_trig+40)

st_n = st.select(component="N")
tr_n = st_n[0]
print tr_n

ampl_n = tr_n.data.max() - tr_n.data.min()

st_e = st.select(component="E")
tr_e = st_e[0]
print tr_e

ampl_e = tr_e.data.max() - tr_e.data.min()

from obspy.signal import utlGeoKm
dx, dy = utlGeoKm(event['longitude'], event['latitude'],
                  st[0].stats.coordinates['longitude'], st[0].stats.coordinates['latitude'])
dz = event['depth'] - (st[0].stats.coordinates['elevation'] / 1000.0)
from math import *
hypo_dist = sqrt(dx**2 + dy**2 + dz**2)

ml_n = log10(ampl_n / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
ml_e = log10(ampl_e / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0

ml = (ml_n + ml_e) / 2
print ml
