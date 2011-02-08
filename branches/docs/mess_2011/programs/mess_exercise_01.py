# exercise 1
# - read earthquake data ("RJOB_WA_CUT.MSEED", already simulated and trimmed)
# - estimate peak-to-peak amplitudes as simple min/max on both N and E component
# - use manually specified hypocentral distance to calculate local magnitude

from obspy.core import read
from math import *

st = read("RJOB_WA_CUT.MSEED")

st_n = st.select(component="N")
ampl_n = st_n[0].data.max() - st_n[0].data.min()

st_e = st.select(component="E")
ampl_e = st_e[0].data.max() - st_e[0].data.min()

ampl = (ampl_n + ampl_e) / 2

hypo_dist = 7.1

ml = log10(ampl / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
print ml
