import numpy as np

from coordinate_system import coordinate_system

R_plane, z_values, *rest = coordinate_system()

def calculate_angle(R_plane, z_values):
    m1 = z_values / R_plane
    delta = np.pi / 2 - np.arctan(m1)
    return delta
