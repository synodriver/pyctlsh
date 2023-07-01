"""
Copyright (c) 2008-2023 synodriver <diguohuangjiajinweijun@gmail.com>
"""
from pyctlsh.backends.cffi._ctlsh import ffi, lib


class TlshState:
    # cdef tlsh_state * _state

    def __init__(self):
        self._state = lib.tlsh_alloc()
        if self._state == ffi.NULL:
            raise MemoryError

    def __dealloc__(self):
        if self._state:
            lib.tlsh_free(self._state)
        self._state = ffi.NULL

    def reset(self):
        lib.tlsh_reset(self._state)

    def update(self, data, tlsh_option: int):
        lib.tlsh_update(self._state, ffi.cast("const unsigned char *", ffi.from_buffer(data)), len(data), tlsh_option)

    def hash(self) -> bytes:
        ret = lib.tlsh_hash(self._state)
        if ret == ffi.NULL:
            raise ValueError
        return ffi.string(ret)
