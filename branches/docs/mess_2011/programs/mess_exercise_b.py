# exercise B
# - fetch earthquake information used in exercise A from EMSC catalog
# - compare magnitude in catalog to magnitude determined in exercise A

import obspy.neries
client_n = obspy.neries.Client()

events = client_n.getEvents(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
                            min_datetime="2008-04-17", max_datetime="2008-04-18")

print events
