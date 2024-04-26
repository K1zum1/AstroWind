import numpy as np

from coordinate_system import *

R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system()


def calculate_angle(R_plane, z_values):
    m1 = z_values / R_plane
    delta = np.pi / 2 - np.arctan(m1)
    return delta
