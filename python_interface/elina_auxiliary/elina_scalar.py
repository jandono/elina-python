from elina_scalar_h import *

'''
/* ********************************************************************** */
/* II. Operations  */
/* ********************************************************************** */

/* ====================================================================== */
/* Basics */
/* ====================================================================== */
'''

elina_scalar_api = CDLL("libelinaux.so")


def elina_scalar_alloc():
    """ Allocates a scalar, of default type DOUBLE (the most economical) """

    scalar = None
    try:
        elina_scalar_alloc_c = elina_scalar_api.elina_scalar_alloc
        elina_scalar_alloc_c.restype = POINTER(ElinaScalar)
        scalar = elina_scalar_alloc_c()
    except:
        print('Problem with loading/calling "elina_scalar_alloc" from "libelinaux.so"')

    return scalar


def elina_scalar_free(scalar):
    """ Free a scalar """

    try:
        elina_scalar_free_c = elina_scalar_api.elina_scalar_free
        elina_scalar_free_c.restype = None
        elina_scalar_free_c.argtypes = [POINTER(ElinaScalar)]
        elina_scalar_free_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_free" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar)')


def elina_scalar_reinit(scalar, d):
    """  Change the type of an already allocated scalar (mainly for internal use) """

    try:
        elina_scalar_reinit_c = elina_scalar_api.elina_scalar_reinit
        elina_scalar_reinit_c.restype = None
        elina_scalar_reinit_c.argtypes = [POINTER(ElinaScalar), c_uint]
        elina_scalar_reinit_c(scalar, d)
    except:
        print('Problem with loading/calling "elina_scalar_reinit" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and c_uint')


def elina_scalar_fprint(stream, a):
    # TODO take care of FILE*
    """ Print scalar into stream """

    try:
        elina_scalar_fprint_c = elina_scalar_api.elina_scalar_fprint
        elina_scalar_fprint_c.restype = None
        elina_scalar_fprint_c.argtypes = [c_void_p, POINTER(ElinaScalar)]
        elina_scalar_fprint_c(stream, a)
    except:
        print('Problem with loading/calling "elina_scalar_fprint" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a FILE* and POINTER(ElinaScalar)')


'''
/* ====================================================================== */
/* Assignments */
/* ====================================================================== */
'''

def elina_scalar_set(scalar1, scalar2):
    """ Set the value of scalar by using ElinaScalar """

    try:
        elina_scalar_set_c = elina_scalar_api.elina_scalar_set
        elina_scalar_set_c.restype = None
        elina_scalar_set_c.argtypes = [POINTER(ElinaScalar), POINTER(ElinaScalar)]
        elina_scalar_set_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_set" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and POINTER(ElinaScalar)')


def elina_scalar_set_mpq(scalar, mpq):
    """ Set the value of scalar by using Mpq """

    try:
        elina_scalar_set_mpq_c = elina_scalar_api.elina_scalar_set_mpq
        elina_scalar_set_mpq_c.restype = None
        elina_scalar_set_mpq_c.argtypes = [POINTER(ElinaScalar), Mpq]
        elina_scalar_set_mpq_c(scalar, mpq)
    except:
        print('Problem with loading/calling "elina_scalar_set_mpq" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and Mpq')


def elina_scalar_set_int(scalar, i):
    """ Set the value of scalar by using c_long """

    try:
        elina_scalar_set_int_c = elina_scalar_api.elina_scalar_set_int
        elina_scalar_set_int_c.restype = None
        elina_scalar_set_int_c.argtypes = [POINTER(ElinaScalar), c_long]
        elina_scalar_set_int_c(scalar, i)
    except:
        print('Problem with loading/calling "elina_scalar_set_int" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and c_long')


def elina_scalar_set_frac(scalar, i, j):
    """ Set the value of scalar by using fraction i/j and assuming j!=0 """

    try:
        elina_scalar_set_frac_c = elina_scalar_api.elina_scalar_set_frac
        elina_scalar_set_frac_c.restype = None
        elina_scalar_set_frac_c.argtypes = [POINTER(ElinaScalar), c_long, c_ulong]
        elina_scalar_set_frac_c(scalar, i, j)
    except:
        print('Problem with loading/calling "elina_scalar_set_frac" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar), c_long, c_long')


def elina_scalar_set_double(scalar, k):
    """ Set the value of scalar by using c_double """

    try:
        elina_scalar_set_double_c = elina_scalar_api.elina_scalar_set_double
        elina_scalar_set_double_c.restype = None
        elina_scalar_set_double_c.argtypes = [POINTER(ElinaScalar), c_double]
        elina_scalar_set_double_c(scalar, k)
    except:
        print('Problem with loading/calling "elina_scalar_set_double" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and c_double')


def elina_scalar_set_mpfr(scalar, mpfr):
    """ Set the value of scalar by using Mpfr """

    try:
        elina_scalar_set_mpfr_c = elina_scalar_api.elina_scalar_set_mpfr
        elina_scalar_set_mpfr_c.restype = None
        elina_scalar_set_mpfr_c.argtypes = [POINTER(ElinaScalar), Mpfr]
        elina_scalar_set_mpfr_c(scalar, mpfr)
    except:
        print('Problem with loading/calling "elina_scalar_set_mpfr" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and Mpfr')


def elina_scalar_set_infty(scalar, sgn):
    """ Set the value of scalar to sgn*infty. If sign == 0 set scalar to zero """

    try:
        elina_scalar_set_infty_c = elina_scalar_api.elina_scalar_set_infty
        elina_scalar_set_infty_c.restype = None
        elina_scalar_set_infty_c.argtypes = [POINTER(ElinaScalar), c_int]
        elina_scalar_set_infty_c(scalar, sgn)
    except:
        print('Problem with loading/calling "elina_scalar_set_infty" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and c_int')


'''
/* ====================================================================== */
/* Combined allocation and assignment */
/* ====================================================================== */
'''

def elina_scalar_alloc_set(scalar2):
    """ Allocate an ElinaScalar and initialise it with ElinaScalar """

    scalar = None
    try:
        elina_scalar_alloc_set_c = elina_scalar_api.elina_scalar_alloc_set
        elina_scalar_alloc_set_c.restype = POINTER(ElinaScalar)
        elina_scalar_alloc_set_c.argtypes = [POINTER(ElinaScalar)]
        scalar1 = elina_scalar_alloc_set_c(scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar)')

    return scalar


def elina_scalar_alloc_set_mpq(mpq):
    """ Allocate an ElinaScalar and initialise it with existing Mpq """

    scalar = None
    try:
        elina_scalar_alloc_set_mpq_c = elina_scalar_api.elina_scalar_alloc_set_mpq
        elina_scalar_alloc_set_mpq_c.restype = POINTER(ElinaScalar)
        elina_scalar_alloc_set_mpq_c.argtypes = [Mpq]
        scalar = elina_scalar_alloc_set_mpq_c(mpq)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set_mpq" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a Mpq')

    return scalar


def elina_scalar_alloc_set_double(k):
    """ Allocate an ElinaScalar and initialise it with c_double """

    scalar = None
    try:
        elina_scalar_alloc_set_double_c = elina_scalar_api.elina_scalar_alloc_set_double
        elina_scalar_alloc_set_double_c.restype = POINTER(ElinaScalar)
        elina_scalar_alloc_set_double_c.argtypes = [c_double]
        scalar = elina_scalar_alloc_set_double_c(k)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set_double" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a c_double')

    return scalar


def elina_scalar_alloc_set_mpfr(mpfr):
    """ Allocate an ElinaScalar and initialise it with Mpfr """

    scalar = None
    try:
        elina_scalar_alloc_set_mpfr_c = elina_scalar_api.elina_scalar_alloc_set_mpfr
        elina_scalar_alloc_set_mpfr_c.restype = POINTER(ElinaScalar)
        elina_scalar_alloc_set_mpfr_c.argtypes = [Mpfr]
        scalar = elina_scalar_alloc_set_mpfr_c(mpfr)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set_mpfr" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a Mpfr')

    return scalar


'''
/* ====================================================================== */
/* Conversions */
/* ====================================================================== */
'''

def elina_mpq_set_scalar(mpq, scalar, rnd):
    """ Convert ElinaScalar to Mpq using rounding mode rnd. 
        Return 0 if conversation is exact, positive if result is greater and negative if result is lesser """

    result = None
    try:
        elina_mpq_set_scalar_c = elina_scalar_api.elina_mpq_set_scalar
        elina_mpq_set_scalar_c.restype = c_int
        elina_mpq_set_scalar_c.argtypes = [Mpq, POINTER(ElinaScalar), c_int]
        result = elina_mpq_set_scalar_c(mpq, scalar, rnd)
    except:
        print('Problem with loading/calling "elina_mpq_set_scalar" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a Mpq, POINTER(ElinaScalar) and c_int')

    return result


def elina_double_set_scalar(k, scalar, rnd):
    """ Convert ElinaScalar to double using rounding mode rnd. 
        Return 0 if conversation is exact, positive if result is greater and negative if result is lesser """

    result = None
    try:
        elina_double_set_scalar_c = elina_scalar_api.elina_double_set_scalar
        elina_double_set_scalar_c.restype = c_int
        elina_double_set_scalar_c.argtypes = [POINTER(c_double), POINTER(ElinaScalar), c_int]
        result = elina_double_set_scalar_c(k, scalar, rnd)
    except:
        print('Problem with loading/calling "elina_double_set_scalar" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(c_double), POINTER(ElinaScalar) and c_int')

    return result

def elina_mpfr_set_scalar(mpfr, scalar, rnd):
    """ Convert scalar to Mpfr using rounding mode rnd. 
        Return 0 if conversation is exact, positive if result is greater and negative if result is lesser """

    result = None
    try:
        elina_mpfr_set_scalar_c = elina_scalar_api.elina_mpfr_set_scalar
        elina_mpfr_set_scalar_c.restype = c_int
        elina_mpfr_set_scalar_c.argtypes = [Mpfr, POINTER(ElinaScalar), c_int]
        result = elina_mpfr_set_scalar_c(mpfr, scalar, rnd)
    except:
        print('Problem with loading/calling "elina_mpfr_set_scalar" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a Mpfr, POINTER(ElinaScalar) and c_int')

    return result


'''
/* ====================================================================== */
/* Tests */
/* ====================================================================== */
'''

def elina_scalar_infty(scalar):
    """ Return -1 if scalar is -infty, 0 if scalar is finite and 1 if scalar is +infty """

    result = None
    try:
        elina_scalar_infty_c = elina_scalar_api.elina_scalar_infty
        elina_scalar_infty_c.restype = c_int
        elina_scalar_infty_c.argtypes = [POINTER(ElinaScalar)]
        result = elina_scalar_infty_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_infty" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar)')

    return result

def elina_scalar_cmp(scalar1, scalar2):
    """ Return -1 if scalar1 < scalar2, 0 if scalar1 == scalar2, 1 if scalar1 > scalar2 """

    result = None
    try:
        elina_scalar_cmp_c = elina_scalar_api.elina_scalar_cmp
        elina_scalar_cmp_c.restype = c_int
        elina_scalar_cmp_c.argtypes = [POINTER(ElinaScalar), POINTER(ElinaScalar)]
        result = elina_scalar_cmp_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_cmp" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and POINTER(ElinaScalar)')

    return result

def elina_scalar_cmp_int(scalar, b):
    """ Return -1 if scalar < b, 0 if scalar == b, 1 if scalar > b """

    result = None
    try:
        elina_scalar_cmp_int_c = elina_scalar_api.elina_scalar_cmp_int
        elina_scalar_cmp_int_c.restype = c_int
        elina_scalar_cmp_int_c.argtypes = [POINTER(ElinaScalar), c_int]
        result = elina_scalar_cmp_int_c(scalar, b)
    except:
        print('Problem with loading/calling "elina_scalar_cmp_int" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and c_int')

    return result


def elina_scalar_equal(scalar1, scalar2):
    """ Return true if scalar1 == scalar2, false otherwise """

    result = None
    try:
        elina_scalar_equal_c = elina_scalar_api.elina_scalar_equal
        elina_scalar_equal_c.restype = c_bool
        elina_scalar_equal_c.argtypes = [POINTER(ElinaScalar), POINTER(ElinaScalar)]
        result = elina_scalar_equal_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_equal" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and POINTER(ElinaScalar)')

    return result

def elina_scalar_equal_int(scalar, b):
    """ Return true if scalar == b, false otherwise """

    result = None
    try:
        elina_scalar_equal_int_c = elina_scalar_api.elina_scalar_equal_int
        elina_scalar_equal_int_c.restype = c_bool
        elina_scalar_equal_int_c.argtypes = [POINTER(ElinaScalar), c_int]
        result = elina_scalar_equal_int_c(scalar, b)
    except:
        print('Problem with loading/calling "elina_scalar_equal_int" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and c_int)')

    return result

def elina_scalar_sgn(scalar):
    """ Return -1 if scalar is negative, 0 if scalar is None and +1 if scalar is positive """
    result = None

    try:
        elina_scalar_sgn_c = elina_scalar_api.elina_scalar_sgn
        elina_scalar_sgn_c.restype = c_int
        elina_scalar_sgn_c.argtypes = [POINTER(ElinaScalar)]
        result = elina_scalar_sgn_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_sgn" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar)')

    return result


'''
/* ====================================================================== */
/* Other operations */
/* ====================================================================== */
'''

def elina_scalar_neg(scalar1, scalar2):
    """ Negation """

    try:
        elina_scalar_neg_c = elina_scalar_api.elina_scalar_neg
        elina_scalar_neg_c.restype = None
        elina_scalar_neg_c.argtypes = [POINTER(ElinaScalar), POINTER(ElinaScalar)]
        elina_scalar_neg_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_neg" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and POINTER(ElinaScalar')


def elina_scalar_inv(scalar1, scalar2):
    """ Inversion. Not exact for floating-point type """

    try:
        elina_scalar_inv_c = elina_scalar_api.elina_scalar_inv
        elina_scalar_inv_c.restype = None
        elina_scalar_inv_c.argtypes = [POINTER(ElinaScalar), POINTER(ElinaScalar)]
        elina_scalar_inv_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_inv" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar) and POINTER(ElinaScalar)')


def elina_scalar_hash(scalar):
    """ Return a hash code of scalar """

    result = None
    try:
        elina_scalar_hash_c = elina_scalar_api.elina_scalar_hash
        elina_scalar_hash_c.restype = c_long
        elina_scalar_hash_c.argtypes = [POINTER(ElinaScalar)]
        result = elina_scalar_hash_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_hash" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar)')

    return result


'''
/* ********************************************************************** */
/* III. FOR INTERNAL USE ONLY */
/* ********************************************************************** */
'''

def elina_scalar_print(scalar):
    """ Prints a scalar to stdout """

    try:
        elina_scalar_print_c = elina_scalar_api.elina_scalar_print
        elina_scalar_print_c.restype = None
        elina_scalar_print_c.argtypes = [POINTER(ElinaScalar)]
        elina_scalar_print_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_print" from "libelinaux.so"')
        print('If loading is fine make sure you are passing a POINTER(ElinaScalar)')
