from obspy import UTCDateTime
from obspy.fdsn import Client

# connect to an FDSN webservice
client = Client("http://erde.geophysik.uni-muenchen.de:8080")

# use origin time of devastating Japan earthquake
start = UTCDateTime("2011-03-11 05:46:23") + 10 * 60
end = start + 70 * 60

# download waveform and station metadata of station FUR
stream = client.get_waveforms(
    network="GR", station="FUR", location="", channel="BH*",
    starttime=start, endtime=end, attach_response=True)

# do basic signal processing and plot the data! ---->
stream.remove_response()
stream.filter("bandpass", freqmin=0.01, freqmax=1)
stream.plot()