===========================
MESS ObsPy/Python Practical
===========================

.. sectnum::
    :depth: 2

Python Introduction
===================

*Slides + interactive presentation*

 - Python data types
 - manipulating these (esp. ``str``, ``list``, ``dict``, ``np.ndarray``)
 - working with ``IPython`` (help, tab completion, history), running Python programs
 - control flow (``if``/``for``/``while``/``continue``/``break``/``try``/...)
 - (functions/classes just very briefly)
 - importing standard modules (brief note on easy_install, http://pypi.python.org)
 - short overview of available standard library modules (http://docs.python.org/library/)

*15 minutes playing around*

 - just a few very simple manipulations on lists, dictionaries, arrays etc.

ObsPy Introduction
==================

*Slides + interactive presentation*

 - ObsPy data types (``UTCDateTime``, ``Stats``, ``Trace``, ``Stream``)
 - overview of online resources (API, ObsPy Tutorial, Ticket System, Mailing Lists)
 - working with ObsPy data types

   - plotting data
   - using predefined methods of ``Stream``
   - working on the data manually (e.g. doing an fft using numpy)

*15 minutes playing around*

 - short, simple tasks like: ``copy``, ``filter``, ``trim``, ``select``, ``simulate``, ``write``

*Slides + interactive presentation*

 - how to get data/metadata: ``read``, ``Client``, ``Parser``

*15 minutes playing around*

 - exercises with combined tasks:

   - getting data (local files, online)
   - check for available stations/networks on servers
   - get data for stations in a certain network
   - get metadata for these stations
   - write to file locally

*5 minutes interactive solutions to exercises*

Exercise
========

*30 minutes*

 - fetch data of one station for given time span (some hours)
 - use trigger routine to get P onset time
 - simulate Wood Anderson seismometer
 - trim to e.g. 20 sec after P onset
 - determine peak-to-peak amplitude (simple min/max)
 - calculate local magnitude
 - if it works: do it automated in a loop over several stations and calculate network magnitude

*5 minutes interactive solution to exercise*

Additional Problems
===================

*for quick guys or if someone wants to play around some more later*

 - fetch big eq data, visualize normal modes
 - load/fetch DHFO data, run a trigger over it, stack the signal according to the trigger onset times
 - load data (24 hours), make probability density function of psd
 - cross-correlation pick refinement
 - waveform similarity analysis, clustering
