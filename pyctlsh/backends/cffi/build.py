"""
Copyright (c) 2008-2023 synodriver <diguohuangjiajinweijun@gmail.com>
"""
import glob

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(
    """
struct tlsh_state;

struct tlsh_state * tlsh_alloc();
void tlsh_free(struct tlsh_state * state);
void tlsh_reset(struct tlsh_state * state);
void tlsh_update(struct tlsh_state * this, const unsigned char * data, unsigned int len, int tlsh_option);
const char * tlsh_hash(struct tlsh_state * this);
    """
)

source = """
#include "ctlsh.h"
"""
c_sources = glob.glob("./ctlsh/*.c")
# c_sources = list(filter(lambda x: "main" not in x, c_sources))
print(c_sources)

ffibuilder.set_source(
    "pyctlsh.backends.cffi._ctlsh",
    source,
    sources=c_sources,
    include_dirs=["./ctlsh"],
)

if __name__ == "__main__":
    ffibuilder.compile()