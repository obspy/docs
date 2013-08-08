# exercise 10
# - modify program of exercise 8:
#   - include program from exercise 9 to fetch a list of available stations in network "BW" via arclink from webDC
#   - use this list of stations for the loop
#     (the availability check in arclink is buggy, put a try/except around getWaveform())
#   - estimate magnitude for each station

from obspy.core import UTCDateTime
import obspy.seishub
from obspy.signal import utlGeoKm
from math import *

client = obspy.seishub.Client("http://localhost:8080")

events = client.event.getList(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
                              min_datetime="2008-04-17", max_datetime="2008-04-18", min_magnitude=3)

event = events[0]

t = UTCDateTime(event['datetime'])

PAZ_WA = {'sensitivity': 2800, 'zeros': [0j], 'gain': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

stations = client.station.getList(network="BW")

for station in stations:

    try:
        st = client.waveform.getWaveform(network="BW", station=station['station_id'], location="", channel="EH*",
                                         starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)
    except:
        print "no data for station ", station['station_id']
        continue

    st.simulate(paz_remove="self", paz_simulate=PAZ_WA)

    st_trig = st.select(component="Z")
    st_trig.trigger("recstalta", sta=0.5, lta=10)
    samples = st_trig[0].data.argmax()
    t_trig = st[0].stats.starttime + (samples / st[0].stats.sampling_rate)

    st.trim(t_trig - 1, t_trig + 40)

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
