from obspy.core import UTCDateTime
from obspy.arclink import Client

client = Client()
t = UTCDateTime("2008-04-17T16:00:00Z")
st = client.getWaveform("BW", "HROE", "", "EH*", t, t + 10*60)
print st
st.plot()

from obspy.neries import Client

client = Client()
events = client.getEvents(min_datetime="2008-10-10T08:05:00Z", max_datetime="2008-10-10T08:15:00Z")
print events

event = events[0]
print "origin time is", event['datetime']
print "magnitude is", event['magnitude']
print "longitude is", event['longitude']
print "latitude is", event['latitude']
print "depth is", event['depth']
