import os.path

from cffi import FFI


_ffi = FFI()
_ffi.cdef("""
void unwrap3D(
    float* wrapped_volume,
    float* unwrapped_volume,
    unsigned char* input_mask,
    int image_width, int image_height, int volume_depth,
    int wrap_around_x, int wrap_around_y, int wrap_around_z);
""")

_current_directory = os.path.dirname(__file__)
_lib = _ffi.verify(
    '#include "unwrap3D.c"',
    ext_package="unwrap",
    include_dirs=[_current_directory])
_unwrap3D = _lib.unwrap3D


def unwrap3D(array, mask, unwrapped_array, wrap_around_x, wrap_around_y, wrap_around_z):
    _unwrap3D(
        _ffi.cast("float *", array.ctypes.data),
        _ffi.cast("float *", unwrapped_array.ctypes.data),
        _ffi.cast("char *", mask.ctypes.data),
        array.shape[2], array.shape[1], array.shape[0], #TODO: check!!!
        wrap_around_x, wrap_around_y, wrap_around_z)
