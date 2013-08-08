>>> from obspy.core import read
>>> stream = read('BW.FURT..EHZ')
>>> print stream
1 Trace(s) in Stream:
BW.FURT..EHZ | 2010-02-06T04:53:00.000000Z - 2010-02-06T05:03:00.000000Z | 200.0 Hz, 120001 samples

>>> stream.plot()

>>> stream.write('BW.FURT..EHZ', format='GSE2')
