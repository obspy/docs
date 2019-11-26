from pyasdf import ASDFDataSet

ds = ASDFDataSet("observed.h5")

# All data is read on demand as they are accessed. This enables users to
# analyze arbitrarily large data sets.

# Get an event as an ObsPy Event object.
ev = ds.events[0]

# Get an ObsPy Stream object.
st = ds.waveforms.IU_ANMO.raw_recording

# Get the corresponding StationXML files as an ObsPy
# inventory object.
inv = ds.waveforms.IU_ANMO.StationXML

# Data relations are kept. Get the event for a certain waveform.
event = st[0].stats.asdf.event_id.getReferredObject()
