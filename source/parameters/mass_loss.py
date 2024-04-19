import numpy as np
from parameters import *  
from coordinate_system import *

def calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k):
    mass_loss_rate = np.zeros_like(r_base)
    mask = (r_base >= r_in) & (r_base <= r_out)
    if np.any(mask):
        mass_loss_rate[mask] = k * (R_plane[mask]**p)
    return mass_loss_rate
