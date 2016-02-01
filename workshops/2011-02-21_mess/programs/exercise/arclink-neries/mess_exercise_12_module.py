from obspy.signal import utlGeoKm
from math import *

PAZ_WA = {'sensitivity': 2800, 'zeros': [0j], 'gain': 1,
          'poles': [-6.2832-4.7124j, -6.2832+4.7124j]}

def estimate_magnitude(st, event_longitude, event_latitude, event_depth):
    """
    Estimates the magnitude for a given Stream object (Z, N and E components)
    with attached PAZ and coordinate information. Longitude, latitude and depth
    (km, positive up) of event must also be specified.

    Returns estimated magnitude as a float.
    """
    st.simulate(paz_remove="self", paz_simulate=PAZ_WA)

    st_trig = st.select(component="Z")
    st_trig.trigger("recstalta", sta=0.5, lta=10)
    samples = st_trig[0].data.argmax()
    t_trig = st[0].stats.starttime + (samples / st[0].stats.sampling_rate)

    st.trim(t_trig - 1, t_trig + 40)

    st_n = st.select(component="N")
    ampl_n = st_n[0].data.max() - st_n[0].data.min()

    st_e = st.select(component="E")
    ampl_e = st_e[0].data.max() - st_e[0].data.min()

    ampl = (ampl_n + ampl_e) / 2 / 2

    dx, dy = utlGeoKm(event_longitude, event_latitude,
                      st[0].stats.coordinates['longitude'], st[0].stats.coordinates['latitude'])
    dz = event_depth - (st[0].stats.coordinates['elevation'] / 1000.0)
    hypo_dist = sqrt(dx**2 + dy**2 + dz**2)

    ml = log10(ampl * 1000) + log10(hypo_dist / 100.0) + 0.00301 * (hypo_dist - 100.0) + 3.0
    return ml
