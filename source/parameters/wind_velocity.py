# Based on the canonical β velocity law of hotstellar winds(cf.Castor,
# Abbott & Klein 1975), the poloidal component of the wind velocity
# V_p parametrized as equation 5 on page 4 of Kurosawa et al. (2006)

import numpy as np
from coordinate_system import coordinate_system

# some constants for now

R = coordinate_system()
c_s = 10**5 # sound speed at the wind launching point in cm/s
f = 0.9 # constant scale factor of the asymptotic terminal
phi = 0.9 # what is this?
beta = 0.2 # what is this?
R_s = ... # what is this?
l = ... # what is this?


def calculate_escape_velocity(R):
    R_safe = np.maximum(R, 1e-10)  
    v_esc = (42 * 10**5) / np.sqrt(R_safe) 
    return v_esc

v_esc = calculate_escape_velocity(R)

def calculate_wind_velocity(c_s, f, v_esc, phi, beta, R_s, l):
    # denominator = np.maximum(l + R_s, 1e-10)  
    # term = (1 - R_s / denominator) ** beta
    # v_p = c_s + (f * v_esc - c_s) * term 
    v_p = c_s + (f * v_esc - c_s) * beta
    return v_p

v_p = calculate_wind_velocity(c_s, f, v_esc, phi, beta, R_s=None, l=None)


print(v_p) 
np