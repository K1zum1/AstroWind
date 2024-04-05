import numpy as np
from astro_constants import AU
from coordinate_system import coordinate_system

R_values, y_values, R_plane, _ = coordinate_system()

def calculate_escape_velocity(R_plane):
    R_safe = np.maximum(R_plane, 1e11) / AU
    v_esc = (42  * 10**5) / np.sqrt(R_safe) 
    return v_esc

v_esc = calculate_escape_velocity(R_values)

def calculate_wind_velocity(R_values):
    c_s = 10**5 
    f = 0.9 
    phi = 0.9 
    beta = 3
    v_p = c_s + (f * v_esc - c_s) * ((R_values / (R_values + 1.5e14)) ** beta)
    return v_p
