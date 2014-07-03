#!/usr/bin/env python
import glob
import numpy as np
from obspy import UTCDateTime
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from matplotlib.transforms import blended_transform_factory


plt.xkcd(scale=0.6)


def str2datenum(string):
    return date2num(UTCDateTime(string))


globmin = np.inf
globmax = 0

plt.figure(figsize=(6, 4))

for files, fixed_time, fixed_count in zip(["old/subscribe*", "neu/subscribe"],
                                          ["2013-03-25", "2014-06-23"],
                                          [236, 300]):
    data = []

    for filename in glob.glob(files):
        with open(filename) as fh:
            lines = fh.readlines()
        for line in lines:
            mon, dom, time, year, num, listname, action = line.split()[:7]
            if listname != "obspy-users:":
                continue
            if action not in ["new", "deleted"]:
                # this 'auto-unsubscribed' line just gives additional info
                # to preceeding 'delete' line in some cases
                if line.split()[7] == "auto-unsubscribed":
                    continue
                if action != "pending":
                    print line
                continue
            time = UTCDateTime().strptime("%s%s%s%s" % (mon, dom, time, year),
                                          "%b%d%H:%M:%S%Y")
            time = date2num(time)
            if action == "new":
                val = 1
            elif action == "deleted":
                val = -1
            else:
                raise Exception("'%s' as action!?!?" % action)
            data.append((time, val))
    print len(data)
    data = sorted(data)
    timestamps, num = np.array(data).T
    num = num.cumsum()
    # correct subscriber offset
    cur_time = UTCDateTime(fixed_time)
    cur_time = date2num(cur_time)
    cur_num = fixed_count
    ind = timestamps.searchsorted(cur_time)
    if ind == len(num):
        ind -= 1
    diff = cur_num - num[ind]
    num += diff
    # plot
    plt.plot_date(timestamps, num, "k-", linestyle="steps", lw=3)
    globmin = min(globmin, num.min())
    globmax = max(globmax, num.max())

plt.gcf().autofmt_xdate()
plt.grid()
plt.title("[obspy-users] Mailing List Member Count")
plt.yticks(np.arange(150, 350, 50))
plt.xticks(map(str2datenum, ["2012-01-01", "2012-07-01",
                             "2013-01-01", "2013-07-01",
                             "2014-01-01", "2014-07-01"]))
ax = plt.gca()
trans = blended_transform_factory(ax.transData, ax.transAxes)
plt.vlines(map(str2datenum, ["2012-01-01", "2013-01-01", "2014-01-01"]), 0, 1,
           lw=2, color="k", transform=trans)
plt.ylim(globmin, globmax)
plt.subplots_adjust(right=0.95, left=0.13)
plt.savefig("/tmp/obspy-users-ml-member-stats.png", dpi=200, transparent=True)
plt.show()
