# ************************************************************************* #
# elina_tcons0.c: tree expressions
# ************************************************************************* #

from elina_dimension_h import *
from elina_coeff_h import *
from elina_linexpr0_h import *

# ====================================================================== #
# Datatypes
# ====================================================================== #

# IMPORTANT NOTE
# --------------
# correct use of floating-point ELINA_RTYPE_xxx currently supposes that the
# FPU rounds towards +oo


class ElinaTexprOp(CtypesEnum):

    ELINA_TEXPR_ADD = 0
    ELINA_TEXPR_SUB = 1
    ELINA_TEXPR_MUL = 2
    ELINA_TEXPR_DIV = 3
    ELINA_TEXPR_MOD = 4
    ELINA_TEXPR_POW = 5

    ELINA_TEXPR_NEG = 6
    ELINA_TEXPR_CAST = 7
    ELINA_TEXPR_SQRT = 8

class ElinaTexprRtype(CtypesEnum):

