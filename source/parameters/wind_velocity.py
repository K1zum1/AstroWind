import numpy as np
from astro_constants import AU
from coordinate_system import coordinate_system

d = -5 * AU
R_values, y_values, R_plane, z_values = coordinate_system()

def get_source_point(R_plane, z_values, d):
    D = np.sqrt(R_plane**2 + (z_values + d)**2)
    return D

def calculate_vp(y_values, z_values, d):
    lmbda = 1.6
    GM_star = 1.1521e10

    r = np.sqrt(y_values**2 + z_values**2)
    rb = r * np.abs(d) / (np.abs(d)+ np.abs(z_values))
    vp = np.sqrt(2 * lmbda - 3) * np.sqrt(GM_star) / np.sqrt(rb)

    # print("rb:", rb)
    # print("lmbda:", lmbda)
    # print("GM_star:", GM_star)
    return vp

