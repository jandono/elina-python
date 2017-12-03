from ctypes import c_bool, c_int, c_uint, c_long, c_ulong, c_longlong, c_ulonglong, c_double, POINTER, Structure, Union , CDLL, c_void_p
from enum import IntEnum

'''
/* ********************************************************************** */
/* I. Datatypes  */
/* ********************************************************************** */
'''

class Mpz(Structure):
    """ Mpz ctype compatible with mpz_t from gmp.h """

    _fields_ = [('_mp_alloc', c_int), ('_mp_size', c_int), ('_mp_d', POINTER(c_long))]

Mpz_t = Mpz * 1


class Mpq(Structure):
    """ Mpq ctype compatible with mpq_t from gmp.h """

    _fields_ = [('_mp_num', Mpz), ('_mp_den', Mpz)]

Mpq_t = Mpq * 1


class Mpfr(Structure):
    """ Mpfr ctype compatible with mpfr_t from mpfr.h """

    _fields_ = [('_mpfr_prec', c_long), ('_mpfr_sign', c_int), ('_mpfr_exp', c_longlong), ('_mpfr_d', POINTER(c_ulonglong))]

Mpfr_t = Mpfr * 1


class CtypesEnum(IntEnum):
    """ A ctypes compatible IntEnum superclass """

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class MpfrRnd(CtypesEnum):
    """ Rounding enums compatible with roundings from mpfr.h """

    MPFR_RNDN = 0  # round to nearest with ties to even
    MPFR_RNDZ = 1  # round toward zero
    MPFR_RNDU = 2  # round toward +Inf
    MPFR_RNDD = 3  # round toward -Inf
    MPFR_RNDA = 4  # round away from zero
    MPFR_RNDF = 5  # faithful rounding ( not implemented yet)
    MPFR_RNDNA = -1  # round to nearest, with ties away from zero (mpfr_round)


class ElinaScalarDiscr(CtypesEnum):
    """ Enum compatible with discr field in elina_scalar_t from elina_scalar.h """

    ELINA_SCALAR_DOUBLE = 0
    ELINA_SCALAR_MPQ = 1
    ELINA_SCALAR_MPFR = 2


class ElinaScalarUnion(Union):
    """ Ctype representing the union field in elina_scalar_t from elina_scalar.h """
    _fields_ = [('dbl', c_double), ('mpq_ptr', POINTER(Mpq)), ('mpfr_ptr', POINTER(Mpfr))]


class ElinaScalar(Structure):
    """ ElinaScalar ctype compatible with elina_scalar_t from elina_scalar.h """
    _fields_ = [('discr', c_uint), ('val', ElinaScalarUnion)]


ElinaScalarPtr = POINTER(ElinaScalar)

elina_scalar_print_prec = c_int(20)
