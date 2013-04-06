>>> from obspy.core import read
>>> stream_object = read('BW.FURT..EHZ')
>>> print stream_object
      1 Trace(s) in Stream:
          BW.FURT..EHZ | 2010-02-06T04:53:00.000000Z - 2010-02-06T05:03:00.000000Z | 200.0 Hz, 120001 samples

>>> stream_object.plot()

>>> stream_object.write('BW.FURT..EHZ', format = 'GSE2')
