import numpy as np
from coordinate_system import coordinate_system

# some constants for now
R_values, y_values = coordinate_system()


def calculate_escape_velocity(R_values):
    R_safe = np.maximum(R_values, 1e-10)  
    v_esc = (42 * 10**5) / np.sqrt(R_safe) 
    return v_esc

v_esc = calculate_escape_velocity(R_values)

def calculate_wind_velocity():
    c_s = 10**5 # sound speed at the wind launching point in cm/s
    f = 0.9 # constant scale factor of the asymptotic terminal
    phi = 0.9 # what is this?
    beta = 0.2 # what is this?
    R_s = ... # what is this?
    l = ... # what is this?
    # denominator = np.maximum(l + R_s, 1e-10)  
    # term = (1 - R_s / denominator) ** beta
    # v_p = c_s + (f * v_esc - c_s) * term 
    v_p = c_s + (f * v_esc - c_s) * beta
    return v_p

v_p = calculate_wind_velocity()

#print(v_p)
