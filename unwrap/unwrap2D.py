import os.path

from cffi import FFI


_ffi = FFI()
_ffi.cdef("""
void unwrap2D(
    float* wrapped_image,
    float* unwrapped_image,
    unsigned char* input_mask,
    int image_width, int image_height,
    int wrap_around_x, int wrap_around_y);
""")

_current_directory = os.path.dirname(__file__)
_lib = _ffi.verify(
    '#include "unwrap2D.c"',
    ext_package="unwrap",
    include_dirs=[_current_directory])
_unwrap2D = _lib.unwrap2D


def unwrap2D(array, mask, unwrapped_array, wrap_around_x, wrap_around_y):
    _unwrap2D(
        _ffi.cast("float *", array.ctypes.data),
        _ffi.cast("float *", unwrapped_array.ctypes.data),
        _ffi.cast("char *", mask.ctypes.data),
        array.shape[1], array.shape[0],
        wrap_around_x, wrap_around_y)
