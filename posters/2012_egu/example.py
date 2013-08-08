import obspy.core
import obspy.neries
date = obspy.core.UTCDateTime(2011, 10, 23)
client = obspy.neries.Client(user='test@obspy.org')
# get magnitude 7+ event for this date (Turkey) from NERIES webservice
event = client.getEvents(min_magnitude=7,
                         min_datetime=date,
                         max_datetime=date+24*60*60)[0]
# get 2000 seconds of waveform data starting at origin time
start = event['datetime']
stream = client.getWaveform('GR', 'FUR', '', 'BH*', start, start+2000)
stream.filter('lowpass', freq=0.5)
stream.plot()       # the resulting plot is shown to the right  ----->
