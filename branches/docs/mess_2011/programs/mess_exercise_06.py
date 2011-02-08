# exercise 6
# - read earthquake data ("RJOB.MSEED")
# - run a recursive STALTA trigger on the data
# - estimate the event onset time as the maximum of the trigger function

from obspy.core import read

st = read("RJOB.MSEED")

st = st.select(component="Z")

st.trigger("recstalta", sta=0.5, lta=10)

num_samples = st[0].data.argmax()
t = st[0].stats.starttime + (num_samples / st[0].stats.sampling_rate)
print t
