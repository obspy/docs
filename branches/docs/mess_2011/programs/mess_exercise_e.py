# exercise E
# - read earthquake data and run a recursive STALTA trigger (e.g. 0.5 and 10 sec) on the data
# - determine the event onset as maximum of the trigger function

from obspy.core import read

st = read("RJOB.MSEED")
print st

st = st.select(component="Z")

st.trigger("recstalta", sta=0.5, lta=10)
st.plot()

samples = st[0].data.argmax()
t = st[0].stats.starttime + (samples / st[0].stats.sampling_rate)
import ipdb;ipdb.set_trace()
