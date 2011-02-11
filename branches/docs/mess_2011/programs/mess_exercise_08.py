# exercise 8
# - modify program of exercise 7:
#   - use a list of stations (RJOB, RMOA, RNON)
#   - do the magnitude estimation looping over this list

import obspy.neries
from obspy.core import UTCDateTime
import obspy.arclink
#import obspy.seishub
from obspy.signal import utlGeoKm
from math import *

client_N = obspy.neries.Client()
#client = obspy.seishub.Client("http://localhost:8080")

events = client_N.getEvents(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
                            min_datetime="2008-04-17", max_datetime="2008-04-18")
#events = client.event.getList(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
#                              min_datetime="2008-04-17", max_datetime="2008-04-18", min_magnitude=3)

event = events[0]

t = UTCDateTime(event['datetime'])

client_A = obspy.arclink.Client()

PAZ_WA = {'sensitivity': 2800, 'zeros': [0j], 'gain': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

stations = ["RJOB", "RMOA", "RNON"]

for station in stations:

    st = client_A.getWaveform(network="BW", station=station, location="", channel="EH*",
                              starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)
    #st = client.waveform.getWaveform(network="BW", station=station, location="", channel="EH*",
    #                                 starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)

    st.simulate(paz_remove="self", paz_simulate=PAZ_WA)

    st_trig = st.select(component="Z")
    st_trig.trigger("recstalta", sta=0.5, lta=10)
    num_samples = st_trig[0].data.argmax()
    t_trig = st[0].stats.starttime + (num_samples / st[0].stats.sampling_rate)

    st.trim(t_trig-1, t_trig+40)

    st_n = st.select(component="N")
    ampl_n = st_n[0].data.max() - st_n[0].data.min()
    st_e = st.select(component="E")
    ampl_e = st_e[0].data.max() - st_e[0].data.min()
    ampl = (ampl_n + ampl_e) / 2 / 2

    dx, dy = utlGeoKm(event['longitude'], event['latitude'],
                      st[0].stats.coordinates['longitude'], st[0].stats.coordinates['latitude'])
    dz = event['depth'] - (st[0].stats.coordinates['elevation'] / 1000.0)
    hypo_dist = sqrt(dx**2 + dy**2 + dz**2)

    ml = log10(ampl * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0

    print st[0].stats.station
    print ml
