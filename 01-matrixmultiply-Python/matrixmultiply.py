# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

import numpy as np


def fun_matrixmultiply(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    if M1.dim != M2.dim:
        return None
    return M1.dot(M2)