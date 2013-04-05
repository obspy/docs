# exercise 11
# - modify program of exercise 10:
#   - use events in the Vogtland swarm region (roughly 50.2 N, 12.2 E) and calculate local magnitudes
#     (there are two magnitude 4+ events in the EMSC catalog in 2008 that you can use)
#   - either use a single event like before or loop over both events in an additional for-loop

from obspy.core import UTCDateTime
import obspy.seishub
from obspy.signal import utlGeoKm
from math import *

client = obspy.seishub.Client("http://localhost:8080")

events = client.event.getList(min_latitude=49, max_latitude=52, min_longitude=11, max_longitude=14,
                              min_datetime="2008-01-01", max_datetime="2009-01-01", min_magnitude=4)

PAZ_WA = {'sensitivity': 2800, 'zeros': [0j], 'gain': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

for event in events:
    
    print event['datetime'], event['magnitude']

    t = UTCDateTime(event['datetime'])

    stations = client.station.getList(network="BW")

    for station in stations:

        try:
            st = client.waveform.getWaveform(network="BW", station=station['station_id'], location="", channel="EH*",
                                             starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)
        except:
            print "no data for station", station['station_id']
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
