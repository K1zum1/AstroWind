import numpy as np
from coordinate_system import coordinate_system

_, _, R_plane, z_values = coordinate_system()

def calculate_angle(R_plane, z_values):
    with np.errstate(divide='ignore', invalid='ignore'):
        m1 = z_values / R_plane
        delta = np.pi / 2 - np.arctan(m1)
    return delta
