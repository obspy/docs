from obspy.core import read
from obspy.signal import classicSTALTA
from wrap_stalta import stalta
import cProfile
import pstats

tr = read("/path/to/loc_RJOB20050831023349.z")[0]

#cProfile.run("classicSTALTA(tr.data, 400, 2000)", "Profile.prof")
cProfile.run("charfct = stalta(tr.data, 400, 2000)", "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()

