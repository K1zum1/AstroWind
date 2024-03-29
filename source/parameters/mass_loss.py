from coordinate_system import coordinate_system
import numpy as np

R_values, _, R_plane = coordinate_system()

def calculate_mass_loss_rate(R_values, R_plane):
    alpha = 0.76
    q = -1.15
    p = 4 * alpha * q
    M_dot_w = 1e17
    r_in = np.min(R_plane)
    r_out = np.max(R_values)
    k = ((p + 2) * M_dot_w) / (2 * np.pi * (r_out**(p + 2) - r_in**(p + 2)))
    mass_loss_rate = k * (R_values)**p

    return mass_loss_rate


mass_loss_rate = calculate_mass_loss_rate(R_values, R_plane)

