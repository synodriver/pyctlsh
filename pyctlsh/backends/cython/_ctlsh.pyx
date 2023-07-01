# cython: language_level=3
# cython: cdivision=True
from libc.stdint cimport uint8_t
cimport cython

from pyctlsh.backends.cython.ctlsh cimport tlsh_state, tlsh_alloc, tlsh_free, tlsh_reset, tlsh_update, tlsh_hash

@cython.final
@cython.freelist(8)
@cython.no_gc
cdef class TlshState:
    cdef tlsh_state * _state

    def __cinit__(self):
        self._state = tlsh_alloc()
        if self._state == NULL:
            raise MemoryError

    def __dealloc__(self):
        if self._state:
            tlsh_free(self._state)
        self._state = NULL

    cpdef reset(self):
        with nogil:
            tlsh_reset(self._state)

    cpdef update(self, const uint8_t[::1] data, int tlsh_option):
        with nogil:
            tlsh_update(self._state, <const unsigned char *>&data[0], <unsigned int>data.shape[0], tlsh_option)

    cpdef inline bytes hash(self):
        cdef const char *ret = NULL
        with nogil:
            ret = tlsh_hash(self._state)
        if ret == NULL:
            raise ValueError
        return <bytes>ret