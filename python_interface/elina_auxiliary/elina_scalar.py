from elina_scalar_h import *


# ********************************************************************** #
# II. Operations
# ********************************************************************** #
#
# ====================================================================== #
# Basics
# ====================================================================== #


elina_scalar_api = CDLL("libelinaux.so")


def elina_scalar_alloc():
    """
    Allocates a scalar, of default type DOUBLE (the most economical)
    
    Parameters
    -----------
    None
    
    Returns
    -------
    scalar : ElinaScalarPtr
        Pointer to the newly allocated ElinaScalar
        
    """

    scalar = None
    try:
        elina_scalar_alloc_c = elina_scalar_api.elina_scalar_alloc
        elina_scalar_alloc_c.restype = ElinaScalarPtr
        scalar = elina_scalar_alloc_c()
    except:
        print('Problem with loading/calling "elina_scalar_alloc" from "libelinaux.so"')

    return scalar


def elina_scalar_free(scalar):
    """
    Free a scalar
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Pointer to the ElinaScalar that needs to be freed
        
    Returns
    -------
    None
    
    """

    try:
        elina_scalar_free_c = elina_scalar_api.elina_scalar_free
        elina_scalar_free_c.restype = None
        elina_scalar_free_c.argtypes = [ElinaScalarPtr]
        elina_scalar_free_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_free" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr to the function')


def elina_scalar_reinit(scalar, d):
    """
    Change the type of an already allocated scalar (mainly for internal use)
     
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Pointer to the ElinaScalar that needs to be reinitialised
    d : c_uint
        Enum of type ElinaScalarDiscr that defines the core of the ElinaScalar (0 = double, 1 = mpq, 2 = mpfr)
    
    Returns
    -------
    None
    
    """

    try:
        elina_scalar_reinit_c = elina_scalar_api.elina_scalar_reinit
        elina_scalar_reinit_c.restype = None
        elina_scalar_reinit_c.argtypes = [ElinaScalarPtr, c_uint]
        elina_scalar_reinit_c(scalar, d)
    except:
        print('Problem with loading/calling "elina_scalar_reinit" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and c_uint to the function')


def elina_scalar_fprint(stream, scalar):
    """
    Print scalar to stream
    
    Parameters
    -----------
    stream : c_void_p
        Stream on which the output should be printed
    scalar : ElinaScalarPtr
        ElinaScalar that needs to be printed
    
    Returns
    -------
    None
    
    """

    try:
        elina_scalar_fprint_c = elina_scalar_api.elina_scalar_fprint
        elina_scalar_fprint_c.restype = None
        elina_scalar_fprint_c.argtypes = [c_void_p, ElinaScalarPtr]
        elina_scalar_fprint_c(stream, scalar)
    except:
        print('Problem with loading/calling "elina_scalar_fprint" from "libelinaux.so"')
        print('Make sure you are passing c_void_p and ElinaScalarPtr to the function')


# ====================================================================== #
# Assignments
# ====================================================================== #


def elina_scalar_set(scalar1, scalar2):
    """
    Set the value of scalar1 to scalar2
    
    Parameters
    -----------
    scalar1 : ElinaScalarPtr
        Destination
    scalar2 : ElinaScalarPtr
        Source
    
    Returns
    -------
    None  
      
    """

    try:
        elina_scalar_set_c = elina_scalar_api.elina_scalar_set
        elina_scalar_set_c.restype = None
        elina_scalar_set_c.argtypes = [ElinaScalarPtr, ElinaScalarPtr]
        elina_scalar_set_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_set" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and ElinaScalarPtr to the function')


def elina_scalar_set_mpq(scalar, mpq_t):
    """
    Set the value of scalar to mpq
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Destination
    mpq_t : Mpq_t
        Source
    
    Returns
    -------
    None   
     
    """

    try:
        elina_scalar_set_mpq_c = elina_scalar_api.elina_scalar_set_mpq
        elina_scalar_set_mpq_c.restype = None
        elina_scalar_set_mpq_c.argtypes = [ElinaScalarPtr, Mpq_t]
        elina_scalar_set_mpq_c(scalar, mpq_t)
    except:
        print('Problem with loading/calling "elina_scalar_set_mpq" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and Mpq_t to the function')


def elina_scalar_set_int(scalar, i):
    """
    Set the value of scalar to i
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Destination
    i : c_long
        Source
    
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_set_int_c = elina_scalar_api.elina_scalar_set_int
        elina_scalar_set_int_c.restype = None
        elina_scalar_set_int_c.argtypes = [ElinaScalarPtr, c_long]
        elina_scalar_set_int_c(scalar, i)
    except:
        print('Problem with loading/calling "elina_scalar_set_int" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and c_long to the function')


def elina_scalar_set_frac(scalar, i, j):
    """
    Set the value of scalar to i/j and assuming j!=0

    Parameters
    -----------
    scalar : ElinaScalarPtr
        Destination
    i : c_long
        Nominator
    j : c_ulong
        Denominator
    
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_set_frac_c = elina_scalar_api.elina_scalar_set_frac
        elina_scalar_set_frac_c.restype = None
        elina_scalar_set_frac_c.argtypes = [ElinaScalarPtr, c_long, c_ulong]
        elina_scalar_set_frac_c(scalar, i, j)
    except:
        print('Problem with loading/calling "elina_scalar_set_frac" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr, c_long, c_long to the function')


def elina_scalar_set_double(scalar, k):
    """
    Set the value of scalar to k
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Destination
    k : c_double
        Source
    
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_set_double_c = elina_scalar_api.elina_scalar_set_double
        elina_scalar_set_double_c.restype = None
        elina_scalar_set_double_c.argtypes = [ElinaScalarPtr, c_double]
        elina_scalar_set_double_c(scalar, k)
    except:
        print('Problem with loading/calling "elina_scalar_set_double" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and c_double to the function')


def elina_scalar_set_mpfr(scalar, mpfr_t):
    """
    Set the value of scalar mpfr_t
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Destination
    k : c_double
        Source
    
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_set_mpfr_c = elina_scalar_api.elina_scalar_set_mpfr
        elina_scalar_set_mpfr_c.restype = None
        elina_scalar_set_mpfr_c.argtypes = [ElinaScalarPtr, Mpfr_t]
        elina_scalar_set_mpfr_c(scalar, mpfr_t)
    except:
        print('Problem with loading/calling "elina_scalar_set_mpfr" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and Mpfr_t to the function')


def elina_scalar_set_infty(scalar, sgn):
    """
    Set the value of scalar to sgn*infty. If sign == 0 set scalar to zero
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Destination
    sgn : c_int
        Integer defining the sign of the infity
    
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_set_infty_c = elina_scalar_api.elina_scalar_set_infty
        elina_scalar_set_infty_c.restype = None
        elina_scalar_set_infty_c.argtypes = [ElinaScalarPtr, c_int]
        elina_scalar_set_infty_c(scalar, sgn)
    except:
        print('Problem with loading/calling "elina_scalar_set_infty" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and c_int to the function')


# ====================================================================== #
# Combined allocation and assignment
# ====================================================================== #


def elina_scalar_alloc_set(scalar2):
    """
    Allocate an ElinaScalar and initialise it with scalar2
    
    Parameters
    -----------
    scalar2 : ElinaScalarPtr
        Source
    
    Returns
    -------
    scalar1 : ElinaScalarPtr
        Pointer to the newly allocated ElinaScalar
        
    """

    scalar1 = None
    try:
        elina_scalar_alloc_set_c = elina_scalar_api.elina_scalar_alloc_set
        elina_scalar_alloc_set_c.restype = ElinaScalarPtr
        elina_scalar_alloc_set_c.argtypes = [ElinaScalarPtr]
        scalar1 = elina_scalar_alloc_set_c(scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr to the function')

    return scalar1


def elina_scalar_alloc_set_mpq(mpq_t):
    """
    Allocate an ElinaScalar and initialise it with mpq_t
    
    Parameters
    -----------
    mpq_t : Mpq_t
        Source
    
    Returns
    -------
    scalar : ElinaScalarPtr
        Pointer to the newly allocated ElinaScalar
        
    """

    scalar = None
    try:
        elina_scalar_alloc_set_mpq_c = elina_scalar_api.elina_scalar_alloc_set_mpq
        elina_scalar_alloc_set_mpq_c.restype = ElinaScalarPtr
        elina_scalar_alloc_set_mpq_c.argtypes = [Mpq_t]
        scalar = elina_scalar_alloc_set_mpq_c(mpq_t)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set_mpq" from "libelinaux.so"')
        print('Make sure you are passing Mpq_t to the function')

    return scalar


def elina_scalar_alloc_set_double(k):
    """Allocate an ElinaScalar and initialise it with k
    
    Parameters
    -----------
    k : c_double
        Source
    
    Returns
    -------
    scalar : ElinaScalarPtr
        Pointer to the newly allocated ElinaScalar
        
    """

    scalar = None
    try:
        elina_scalar_alloc_set_double_c = elina_scalar_api.elina_scalar_alloc_set_double
        elina_scalar_alloc_set_double_c.restype = ElinaScalarPtr
        elina_scalar_alloc_set_double_c.argtypes = [c_double]
        scalar = elina_scalar_alloc_set_double_c(k)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set_double" from "libelinaux.so"')
        print('Make sure you are passing c_double to the function')

    return scalar


def elina_scalar_alloc_set_mpfr(mpfr_t):
    """
    Allocate an ElinaScalar and initialise it with mpfr_t
    
    Parameters
    -----------
    mpfr_t : Mpfr_t
        Source
    
    Returns
    -------
    scalar : ElinaScalarPtr
        Pointer to the newly allocated ElinaScalar
        
    """

    scalar = None
    try:
        elina_scalar_alloc_set_mpfr_c = elina_scalar_api.elina_scalar_alloc_set_mpfr
        elina_scalar_alloc_set_mpfr_c.restype = ElinaScalarPtr
        elina_scalar_alloc_set_mpfr_c.argtypes = [Mpfr_t]
        scalar = elina_scalar_alloc_set_mpfr_c(mpfr_t)
    except:
        print('Problem with loading/calling "elina_scalar_alloc_set_mpfr" from "libelinaux.so"')
        print('Make sure you are passing Mpfr_t to the function')

    return scalar


# ====================================================================== #
# Conversions
# ====================================================================== #


def elina_mpq_set_scalar(mpq_t, scalar, rnd):
    """
    Convert ElinaScalar to Mpq using rounding mode rnd and save the result in mpq_t
    Return 0 if conversation is exact, positive if result is greater and negative if result is lesser
    
    Parameters
    -----------
    mpq_t : Mpq_t
        Destination
    scalar : ElinaScalarPtr
        Source
    rnd : c_int
        Rounding mode enum as defined by MpfrRnd
    
    Returns
    -------
    result : c_int
        Integer stating the result of the rounding
        
    """

    result = None
    try:
        elina_mpq_set_scalar_c = elina_scalar_api.elina_mpq_set_scalar
        elina_mpq_set_scalar_c.restype = c_int
        elina_mpq_set_scalar_c.argtypes = [Mpq_t, ElinaScalarPtr, c_int]
        result = elina_mpq_set_scalar_c(mpq_t, scalar, rnd)
    except:
        print('Problem with loading/calling "elina_mpq_set_scalar" from "libelinaux.so"')
        print('Make sure you are passing Mpq_t, ElinaScalarPtr and c_int to the function')

    return result


def elina_double_set_scalar(k, scalar, rnd):
    """
    Convert ElinaScalar to double using rounding mode rnd and save the result in k
    Return 0 if conversation is exact, positive if result is greater and negative if result is lesser
    
    Parameters
    -----------
    k: c_double
        Destination
    scalar : ElinaScalarPtr
        Source
    rnd : c_int
        Rounding mode enum as defined by MpfrRnd
    
    Returns
    -------
    result : c_int
        Integer stating the result of the rounding
        
    """

    result = None
    try:
        elina_double_set_scalar_c = elina_scalar_api.elina_double_set_scalar
        elina_double_set_scalar_c.restype = c_int
        elina_double_set_scalar_c.argtypes = [POINTER(c_double), ElinaScalarPtr, c_int]
        result = elina_double_set_scalar_c(k, scalar, rnd)
    except:
        print('Problem with loading/calling "elina_double_set_scalar" from "libelinaux.so"')
        print('Make sure you are passing POINTER(c_double), ElinaScalarPtr and c_int to the function')

    return result


def elina_mpfr_set_scalar(mpfr_t, scalar, rnd):
    """
    Convert scalar to Mpfr using rounding mode rnd and save the result in mpfr_t
    Return 0 if conversation is exact, positive if result is greater and negative if result is lesser
    
    Parameters
    -----------
    mpfr_t : Mpfr_t
        Destination
    scalar : ElinaScalarPtr
        Source
    rnd : c_int
        Rounding mode enum as defined by MpfrRnd
    
    Returns
    -------
    result : c_int
        Integer stating the result of the rounding
        
    """

    result = None
    try:
        elina_mpfr_set_scalar_c = elina_scalar_api.elina_mpfr_set_scalar
        elina_mpfr_set_scalar_c.restype = c_int
        elina_mpfr_set_scalar_c.argtypes = [Mpfr_t, ElinaScalarPtr, c_int]
        result = elina_mpfr_set_scalar_c(mpfr_t, scalar, rnd)
    except:
        print('Problem with loading/calling "elina_mpfr_set_scalar" from "libelinaux.so"')
        print('Make sure you are passing Mpfr_t, ElinaScalarPtr and c_int to the function')

    return result


# ====================================================================== #
# Tests
# ====================================================================== #


def elina_scalar_infty(scalar):
    """
    Return -1 if scalar is -infinity, 0 if scalar is finite and 1 if scalar is +infinity
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Scalar to be tested for infinity
    
    Returns
    -------
    result : c_int
        Integer stating the result of the testing
        
    """

    result = None
    try:
        elina_scalar_infty_c = elina_scalar_api.elina_scalar_infty
        elina_scalar_infty_c.restype = c_int
        elina_scalar_infty_c.argtypes = [ElinaScalarPtr]
        result = elina_scalar_infty_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_infty" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr to the function')

    return result


def elina_scalar_cmp(scalar1, scalar2):
    """
    Return -1 if scalar1 < scalar2, 0 if scalar1 == scalar2, 1 if scalar1 > scalar2
    
    Parameters
    -----------
    scalar1 : ElinaScalarPtr
        Scalar to be compared
    scalar2 : ElinaScalarPtr
        Scalar to be compared
    
    Returns
    -------
    result : c_int
        The result of the comparison
        
    """

    result = None
    try:
        elina_scalar_cmp_c = elina_scalar_api.elina_scalar_cmp
        elina_scalar_cmp_c.restype = c_int
        elina_scalar_cmp_c.argtypes = [ElinaScalarPtr, ElinaScalarPtr]
        result = elina_scalar_cmp_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_cmp" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and ElinaScalarPtr to the function')

    return result


def elina_scalar_cmp_int(scalar, b):
    """
    Return -1 if scalar < b, 0 if scalar == b, 1 if scalar > b
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Scalar to be compared
    b : c_int
        Integer to be compared
    
    Returns
    -------
    result : c_int
        The result of the comparison
        
    """

    result = None
    try:
        elina_scalar_cmp_int_c = elina_scalar_api.elina_scalar_cmp_int
        elina_scalar_cmp_int_c.restype = c_int
        elina_scalar_cmp_int_c.argtypes = [ElinaScalarPtr, c_int]
        result = elina_scalar_cmp_int_c(scalar, b)
    except:
        print('Problem with loading/calling "elina_scalar_cmp_int" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and c_int')

    return result


def elina_scalar_equal(scalar1, scalar2):
    """
    Return true if scalar1 == scalar2, false otherwise
    
    Parameters
    -----------
    scalar1 : ElinaScalarPtr
        Scalar to be tested for equality
    scalar2 : ElinaScalarPtr
        Scalar to be tested for equality
    
    Returns
    -------
    result : c_bool
        The result of the equality test
        
    """

    result = None
    try:
        elina_scalar_equal_c = elina_scalar_api.elina_scalar_equal
        elina_scalar_equal_c.restype = c_bool
        elina_scalar_equal_c.argtypes = [ElinaScalarPtr, ElinaScalarPtr]
        result = elina_scalar_equal_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_equal" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and ElinaScalarPtr')

    return result


def elina_scalar_equal_int(scalar, b):
    """
    Return true if scalar == b, false otherwise
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Scalar to be tested for equality
    b : c_int
        Integer to be tested for equality
    
    Returns
    -------
    result : c_int
        The result of the equality test
        
    """

    result = None
    try:
        elina_scalar_equal_int_c = elina_scalar_api.elina_scalar_equal_int
        elina_scalar_equal_int_c.restype = c_bool
        elina_scalar_equal_int_c.argtypes = [ElinaScalarPtr, c_int]
        result = elina_scalar_equal_int_c(scalar, b)
    except:
        print('Problem with loading/calling "elina_scalar_equal_int" from "libelinaux.so"')
        print('Make sure you are passing ElinaScalarPtr and c_int)')

    return result


def elina_scalar_sgn(scalar):
    """
    Return -1 if scalar is negative, 0 if scalar is None and +1 if scalar is positive
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Scalar to be tested for the sign
    
    Returns
    -------
    result : c_int
        The result of the sign test
        
    """

    result = None
    try:
        elina_scalar_sgn_c = elina_scalar_api.elina_scalar_sgn
        elina_scalar_sgn_c.restype = c_int
        elina_scalar_sgn_c.argtypes = [ElinaScalarPtr]
        result = elina_scalar_sgn_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_sgn" from "libelinaux.so"')
        print('Make sure you are passing a ElinaScalarPtr')

    return result


'''
/* ====================================================================== */
/* Other operations */
/* ====================================================================== */
'''


def elina_scalar_neg(scalar1, scalar2):
    """
    Set scalar1 to -scalar2
    
    Parameters
    -----------
    scalar1 : ElinaScalarPtr
        Destination
    scalar2 : ElinaScalarPtr
        Source
        
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_neg_c = elina_scalar_api.elina_scalar_neg
        elina_scalar_neg_c.restype = None
        elina_scalar_neg_c.argtypes = [ElinaScalarPtr, ElinaScalarPtr]
        elina_scalar_neg_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_neg" from "libelinaux.so"')
        print('Make sure you are passing a ElinaScalarPtr and POINTER(ElinaScalar')


def elina_scalar_inv(scalar1, scalar2):
    """
    Set scalar1 to 1/scalar2. Not exact for floating-point type
    
    Parameters
    -----------
    scalar1 : ElinaScalarPtr
        Destination
    scalar2 : ElinaScalarPtr
        Source
    
    Returns
    -------
    None
        
    """

    try:
        elina_scalar_inv_c = elina_scalar_api.elina_scalar_inv
        elina_scalar_inv_c.restype = None
        elina_scalar_inv_c.argtypes = [ElinaScalarPtr, ElinaScalarPtr]
        elina_scalar_inv_c(scalar1, scalar2)
    except:
        print('Problem with loading/calling "elina_scalar_inv" from "libelinaux.so"')
        print('Make sure you are passing a ElinaScalarPtr and ElinaScalarPtr')


def elina_scalar_hash(scalar):
    """
    Return hash of scalar
    
    Parameters
    -----------
    scalar : ElinaScalarPtr
        Scalar to be hashed
        
    Returns
    -------
    result : c_long
        The resulting hash
        
    """

    result = None
    try:
        elina_scalar_hash_c = elina_scalar_api.elina_scalar_hash
        elina_scalar_hash_c.restype = c_long
        elina_scalar_hash_c.argtypes = [ElinaScalarPtr]
        result = elina_scalar_hash_c(scalar)
    except:
        print('Problem with loading/calling "elina_scalar_hash" from "libelinaux.so"')
        print('Make sure you are passing a ElinaScalarPtr')

    return result
