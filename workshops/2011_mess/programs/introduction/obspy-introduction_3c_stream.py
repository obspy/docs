from obspy.core import read

st = read()

for tr in st:
    tr.stats.station = "NEW"

st += read()
print st
st.plot()

stZ = st.select(component="Z")
stZ.filter("highpass", freq=5)

print "showing stream with the Z traces"
stZ.plot()
print "showing original stream"
print "note: the traces in the new stream are only references to the original traces"
print "use st.copy() to really duplicate the information in the memory"
st.plot()
