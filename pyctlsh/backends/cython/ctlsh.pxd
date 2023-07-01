# cython: language_level=3
# cython: cdivision=True

cdef extern from "ctlsh.h" nogil:
    struct tlsh_state:
        pass
    tlsh_state * tlsh_alloc();
    void tlsh_free(tlsh_state * state);
    void tlsh_reset(tlsh_state * state);
    void tlsh_update(tlsh_state * this, const unsigned char * data, unsigned int len, int tlsh_option);
    const char * tlsh_hash(tlsh_state * this);



