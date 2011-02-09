# exercise 12
# - modify program of exercise 11:
#   - put the magnitude estimation in a separate python module "my_module.py"
#   - define a function estimate_magnitude(st, ev_lon, ev_lat, ev_depth) that
#     works on a Stream object with attached paz and coordinate information and
#     returns the estimated magnitude for an event with given longitude,
#     latitude and depth

import obspy.neries
from obspy.core import UTCDateTime
import obspy.arclink
from mess_exercise_12_module import estimate_magnitude

client_N = obspy.neries.Client()

events = client_N.getEvents(min_latitude=49, max_latitude=52, min_longitude=11, max_longitude=14,
                            min_datetime="2008-01-01", max_datetime="2009-01-01", min_magnitude=4)

client_A = obspy.arclink.Client()

for event in events:
    
    print event['datetime']

    t = UTCDateTime(event['datetime'])

    stations = client_A.getStations(t-100, t+100, "BW")

    for station in stations:

        try:
            st = client_A.getWaveform(network="BW", station=station['code'], location="", channel="EH*",
                                      starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)
        except:
            print "no data for station ", station['code']
            continue

        ml = estimate_magnitude(st, event['longitude'], event['latitude'], event['depth'])
        print st[0].stats.station
        print ml
