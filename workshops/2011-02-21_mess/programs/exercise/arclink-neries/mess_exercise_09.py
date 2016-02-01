# exercise 9
# - fetch a list of available stations in network "BW" via arclink from webDC
# - print the station code for all stations in a loop

from obspy.core import UTCDateTime
import obspy.arclink

client = obspy.arclink.Client()

t = UTCDateTime("2008-04-17T16:00:32Z")

stations = client.getStations(t-100, t+100, "BW")

for station in stations:

    print station['code']
