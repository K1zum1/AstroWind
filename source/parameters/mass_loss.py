import numpy as np
from parameters import *  

def calculate_mass_loss_rate(R_plane, M_dot_w, p, r_in, r_out):
    mask = (R_plane >= r_in) & (R_plane <= r_out)

    mass_loss_rate = np.zeros_like(R_plane)  
    if np.any(mask):
        effective_r_in = R_plane[mask].min()
        effective_r_out = R_plane[mask].max()
        k = ((p + 2) * M_dot_w) / (2 * np.pi * (effective_r_out**(p + 2) - effective_r_in**(p + 2)))
        mass_loss_rate[mask] = k * (R_plane[mask]**p)

    return mass_loss_rate
