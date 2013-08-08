from obspy.core import read

st = read()
print st
st.plot()

tr = st[0]
st.remove(tr)
print tr
print st
