# XXX STEP 1
# calculate Ml for given origin time, station, data, metadata

from obspy.core import read

st = read("RJOB.MSEED")
print st

st = st.select(component="Z")

st.trigger("recstalta", sta=0.5, lta=10)
st.plot()

samples = st[0].data.argmax()
t = st[0].stats.starttime + (samples / st[0].stats.sampling_rate)
import ipdb;ipdb.set_trace()
