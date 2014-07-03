#!/usr/bin/env python
from obspy import UTCDateTime
from matplotlib.dates import date2num
import matplotlib.pyplot as plt


plt.xkcd(scale=0.6)


def str2datenum(string):
    if len(string) == 7:
        string += "-01"
    return date2num(UTCDateTime(string))

publications = [
    ("2010-05", "SRL"),
    ("2011-01", "Annals of Geophysics"),
    ("2014-07", "CSD"),
]
agu = [
    ("2011-12", "AGU"),
    ("2013-12", "AGU"),
    ]
egu = [
    ("2010-04", "EGU"),
    ("2011-04", "EGU"),
    ("2012-04", "EGU"),
    ("2013-04", "EGU"),
    ]
conferences = [
    ("2010-03", "DGG"),
    ("2010-09", "AG Seismologie"),
    ("2011-03", "Edinburgh (Atkins)"),
    ("2012-05", "Erice (EPOS)"),
    ]
workshops = [
    ("2011-03", "MESS"),
    ("2012-09", "SED/ETHZ"),
    ("2013-02", "IPGP"),
    ("2013-03", "MESS"),
    ("2013-05", "QUEST"),
    ("2014-03", "MESS"),
    ]

iris = [
    ("2010-08", 'Foz do Iguassu: IRIS Workshop: "Managing Waveform Data and Related Metadata for Seismic Networks"'),
    ("2012-01", 'Bangkok: IRIS Workshop:  "Managing Waveform Data and Related Metadata for Seismic Networks"'),
    ("2012-11", 'Puerto Vallarta (Mexico): "Annual Meeting of the UGM": Short course: "Python/Obspy introduction (data retrieval and simple manipulation using ObsPy)"'),
    ("2013-01", 'Kuwait City: IRIS Workshop'),
    ("2013-08", "IRIS/EarthScope"),
    ("2014-07", 'Bogota: IRIS Workshop: "Managing Data from SeismicNetworks"'),
    ]

stable_releases = [
    ("2010-02-26", "0.3.0"),
    ("2010-04-27", "0.3.3"),
    ("2010-05-03", "0.3.4"),
    ("2010-05-16", "0.3.5"),
    ("2010-07-28", "0.3.6"),
    ("2010-09-22", "0.4.0"),
    ("2010-11-25", "0.4.5"),
    ("2011-11-30", "0.5.0"),
    ("2012-01-15", "0.6.0"),
    ("2012-06-26", "0.7.0"),
    ("2012-12-09", "0.8.0"),
    ("2012-12-10", "0.8.1"),
    ("2012-12-14", "0.8.2"),
    ("2012-12-17", "0.8.3"),
    ("2013-06-28", "0.8.4"),
    ("2014-01-13", "0.9.0"),
    ("2014-04-30", "0.9.2"),
    ]


plt.figure(figsize=(6, 4))


lists = [stable_releases, publications,
         agu, egu,
         conferences,
         iris,
         workshops,
         ]
labels = ["releases", "publications",
          "AGU", "EGU",
          "other meetings",
          "IRIS workshops", "other workshops"]
offsets = range(1, len(lists) + 1)


for offset, items in zip(offsets, lists):
    items = sorted(items)
    t = map(str2datenum, [item[0] for item in items])
    annotations = [item[1] for item in items]
    plt.plot(t, [offset] * len(t), marker="o", ms=17, ls="")

ax = plt.gca()

# spines
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_position(('axes', 0))
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.xaxis_date()
plt.gcf().autofmt_xdate()
#plt.grid()
#plt.title("[obspy-users] Mailing List Member Count")
#plt.yticks(np.arange(150, 350, 50))
plt.xticks(map(str2datenum, [
#                             "2008-01-01",
#                             "2009-01-01",
                             "2010-01-01",
                             "2011-01-01",
                             "2012-01-01",
                             "2013-01-01",
                             "2014-01-01"]))
#trans = blended_transform_factory(ax.transData, ax.transAxes)
#plt.vlines(map(str2datenum, ["2012-01-01", "2013-01-01", "2014-01-01"]), 0, 1,
#           lw=2, color="k", transform=trans)
#plt.ylim(globmin, globmax)
plt.subplots_adjust(right=0.95, left=0.35, top=0.99)

# y ticks
ax.set_yticks(offsets)
ax.set_yticklabels(labels)

ax.set_ylim(0, offsets[-1] + 1)
ax.set_xlim(left=str2datenum("2009-05"))

plt.savefig("/tmp/obspy-timeline.png", dpi=200, transparent=True)
plt.show()
