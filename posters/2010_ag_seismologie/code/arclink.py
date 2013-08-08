from obspy.core import UTCDateTime
from obspy.arclink import Client

start = UTCDateTime(2010, 1, 1)
end = start+30

from obspy.arclink import Client
client = Client('webdc.eu')
stream = client.getWaveform('CZ', 'PVCC', '', 'BH*', start, end, getPAZ=True, getCoordinates=True)
