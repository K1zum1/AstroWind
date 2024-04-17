import numpy as np
from parameters import *
from coordinate_system import coordinate_system

R_values, y_values, R_plane, z_values = coordinate_system()

def get_source_point(R_plane, z_values, d):
    D = np.sqrt(R_plane**2 + (z_values + d)**2)
    return D

def calculate_vp(y_values, z_values, d, GM_star, lmbda):

    r = np.sqrt(y_values**2 + z_values**2)
    rb = r * np.abs(d) / (np.abs(d + z_values) + 1e-10)
    factor = 2 * lmbda - 3
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")
    vp = np.sqrt(factor) * np.sqrt(GM_star) / np.sqrt(rb)

    # print("rb:", rb)
    # print("lmbda:", lmbda)
    # print("GM_star:", GM_star)
    return vp

