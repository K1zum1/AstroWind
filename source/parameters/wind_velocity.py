import numpy as np
from parameters import *
from coordinate_system import coordinate_system

R_values, y_values, R_plane, z_values = coordinate_system()

def get_source_point(R_plane, z_values, d):
    D = np.sqrt(R_plane**2 + (np.abs(z_values) + np.abs(d))**2)
    return D

def calculate_vp(R_plane, z_values, d, GM_star, lmbda):

    r_base = R_plane * np.abs(d) / (np.abs(d) + np.abs(z_values))
    factor = 2 * lmbda - 3
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")
    vp = np.sqrt(factor) * np.sqrt(GM_star) / np.sqrt(r_base)

    # print("rb:", rb)
    # print("lmbda:", lmbda)
    # print("GM_star:", GM_star)
    return vp

