# XXX STEP 1
# calculate Ml for given origin time, station, data, metadata

from obspy.core import UTCDateTime, read

st = read("RJOB.MSEED")
print st

paz_sts2 = {'poles': [-0.037004+0.037016j, -0.037004-0.037016j, -251.33+0j, -131.04-467.29j, -131.04+467.29j],
            'sensitivity': 2516778600.0, 'zeros': [0j, 0j], 'gain': 60077000.0}
paz_wa = {'gain': 2800, 'zeros': [0j], 'sensitivity': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

st.simulate(paz_remove=paz_sts2, paz_simulate=paz_wa)

t = UTCDateTime("2008-04-17T16:00:32Z")
st.trim(t-5, t+20)

st_n = st.select(component="N")
tr_n = st_n[0]
print tr_n

ampl_n = tr_n.data.max() - tr_n.data.min()

st_e = st.select(component="E")
tr_e = st_e[0]
print tr_e

ampl_e = tr_e.data.max() - tr_e.data.min()

hypo_dist = 7.1

from math import *
ml_n = log10(ampl_n / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
ml_e = log10(ampl_e / 2.0 * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0

ml = (ml_n + ml_e) / 2
print ml


# XXX STEP 2
# check determined magnitude information against EMSC catalog data

#from obspy.core import UTCDateTime

import obspy.neries
client_n = obspy.neries.Client()
events = client_n.getEvents(min_latitude=47.6, max_latitude=47.8, min_longitude=12.7, max_longitude=13,
                            min_datetime="2008-04-17", max_datetime="2008-04-18")

print events

event = events[0]
t = UTCDateTime(event['datetime'])

#import obspy.seishub
#client_s = obspy.seishub.Client()
#events = client_s.event.getList(min_datetime=t-100,
#                                max_datetime=t+100)

import obspy.arclink
client_a = obspy.arclink.Client()
#stations = client_a.getStations(network="BW", starttime=t-100, endtime=t-100)
#stations = [sta for sta in stations if sta['']]

stations = ["BGLD", "RJOB", "RMOA", "RNHA", "RNON", "RTBE", "RTSH", "RWMO"]

#for station in stations:
station = stations[1]

st = client_a.getWaveform(network="BW", station=station, location="",
                          channel="EH*", starttime=t-30, endtime=t+120,
                          getPAZ=True, getCoordinates=True)
st.merge()

paz_wa = {'gain': 2800, 'zeros': [0j], 'sensitivity': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}
          

st.simulate(paz_remove="self", paz_simulate=paz_wa)

st_trigger = st.copy()
st_trigger = st_trigger.select(component="Z")
st_trigger.trigger("recstalta", sta=1, lta=10)

t_event = st[0].stats.starttime + (st_trigger[0].data.argmax() / st[0].stats.sampling_rate)

st.trim(t_event-5, t_event+10)

data_n = st.select(component="N")[0].data
ampl_n = data_n.max() - data_n.min()

from math import log10, sqrt
#coords_ev = 
dist_x = bla
ml_n = log10(ampl_n / 2.0 * 1000) + log10(hypo_dist / 100.0) + \
        0.00301 * (hypo_dist - 100.0) + 3.0







import ipdb;ipdb.set_trace()
