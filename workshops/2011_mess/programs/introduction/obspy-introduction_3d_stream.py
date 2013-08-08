from obspy.seishub import Client

client = Client("http://localhost:8080")
st = client.waveform.getWaveform(network="BW", station="HROE", starttime="2008-04-17T16:00:00Z", endtime="2008-04-17T16:10:00Z")
print st
st.plot()

events = client.event.getList(min_datetime="2008-10-10T08:05:00Z", max_datetime="2008-10-10T08:15:00Z")
print events

event = events[0]
print "origin time is", event['datetime']
print "magnitude is", event['magnitude']
print "longitude is", event['longitude']
print "latitude is", event['latitude']
print "depth is", event['depth']
