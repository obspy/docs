# exercise 12
# - modify program of exercise 11:
#   - put the magnitude estimation in a separate python module "my_module.py"
#   - define a function estimate_magnitude(st, ev_lon, ev_lat, ev_depth) that
#     works on a Stream object with attached paz and coordinate information and
#     returns the estimated magnitude for an event with given longitude,
#     latitude and depth

from obspy.core import UTCDateTime
import obspy.seishub
from mess_exercise_12_module import estimate_magnitude

client = obspy.seishub.Client("http://localhost:8080")

events = client.event.getList(min_latitude=49, max_latitude=52, min_longitude=11, max_longitude=14,
                              min_datetime="2008-01-01", max_datetime="2009-01-01", min_magnitude=4)

for event in events:
    
    print event['datetime'], event['magnitude']

    t = UTCDateTime(event['datetime'])

    stations = client.station.getList("BW")

    for station in stations:

        try:
            st = client.waveform.getWaveform(network="BW", station=station['station_id'], location="", channel="EH*",
                                             starttime=t-30, endtime=t+120, getPAZ=True, getCoordinates=True)
        except:
            print "no data for station", station['station_id']
            continue

        ml = estimate_magnitude(st, event['longitude'], event['latitude'], event['depth'])
        print st[0].stats.station
        print ml
