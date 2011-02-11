# exercise 9
# - fetch a list of available stations in network "BW" via arclink from webDC
# - print the station code for all stations in a loop

from obspy.core import UTCDateTime
import obspy.arclink
#import obspy.seishub

client = obspy.arclink.Client()
#client = obspy.seishub.Client("http://localhost:8080")

t = UTCDateTime("2008-04-17T16:00:32Z")

stations = client.getStations(t-100, t+100, "BW")
#stations = client.station.getList(network="BW")

for station in stations:

    print station['code']
    #print station['station_id']
