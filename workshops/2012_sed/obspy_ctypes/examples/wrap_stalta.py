import ctypes as C
import numpy as np

head_t = np.dtype([
   ('N', 'u4', 1),
   ('nsta', 'u4', 1),
   ('nlta', 'u4', 1),
], align=True)
data_t = np.dtype('f8')

lib = C.CDLL('./stalta.so')
lib.stalta.argtypes = [
    np.ctypeslib.ndpointer(dtype=head_t, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=data_t, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=data_t, ndim=1, flags='C_CONTIGUOUS'),
]
lib.stalta.restype = C.c_int


def stalta(data, nsta, nlta):
    # initialize C struct / numpy structed array
    head = np.empty(1, dtype=head_t)
    head[:] = (len(data), nsta, nlta)
    # ensure correct type and countiguous of data
    data = np.require(data, dtype=data_t, requirements=['C_CONTIGUOUS'])
    # all memory should be allocated by python
    charfct = np.empty(len(data), dtype=data_t)
    # run and check the errorcode
    errcode = lib.stalta(head, data, charfct)
    if errcode != 0:
        raise Exception('stalta exited with error code %d' % errcode)
    return charfct


if __name__ == '__main__':
    from obspy.core import read
    import matplotlib.pyplot as plt

    tr = read("/path/to/loc_RJOB20050831023349.z")[0]
    charfct = stalta(tr.data, 400, 2000)
    
    plt.plot(tr.data)
    plt.twinx().plot(charfct, 'r')
    plt.show()
