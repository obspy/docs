from obspy.core import read

st = read()

paz = {'poles': [-0.037+0.037j, -0.037-0.037j],
       'zeros': [0j, 0j], 'sensitivity': 2.517e9, 'gain': 1}
print "paz information is:"
print paz

st.simulate(paz_remove=paz)
tr = st[0]
print "maximum on first trace is %s m/s" % tr.data.max()
print "minimum on first trace is %s m/s" % tr.data.min()

st.write("myfile.mseed", format="MSEED")
