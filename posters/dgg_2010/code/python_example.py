#!/usr/bin/env python
import glob
from obspy.core import read

for file in glob.glob("*.z"):
    st = read(file)
    print "%s %s %f %f" % (st[0].stats.station, str(st[0].stats.starttime),
                           st[0].data.mean(), st[0].data.std())
