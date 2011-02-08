# exercise 3
# - fetch earthquake information used in exercise 1 from EMSC catalog
# - compare magnitude in catalog to magnitude determined in exercise 1

import obspy.neries
client = obspy.neries.Client()

events = client.getEvents(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
                          min_datetime="2008-01-01", max_datetime="2009-01-01")
print events
