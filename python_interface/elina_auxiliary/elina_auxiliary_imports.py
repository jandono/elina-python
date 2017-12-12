from ctypes import *
from enum import IntEnum

elina_auxiliary_api = CDLL("libelinaux.so")


class CtypesEnum(IntEnum):
    """ A ctypes compatible IntEnum superclass """

    @classmethod
    def from_param(cls, obj):
        return int(obj)