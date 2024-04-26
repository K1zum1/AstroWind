import numpy as np
from parameters import *


def coordinate_system():
    d = -5 * AU
    x_values = np.linspace(1, 64, 64) * AU
    y_values = np.linspace(1, 64, 64) * AU
    z_values = np.linspace(1, 64, 64) * AU

    X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing="ij")
    R_plane = np.sqrt(X**2 + Y**2)
    R_values = np.sqrt(X**2 + Y**2 + Z**2)

    r_base = R_plane * np.abs(d) / (np.abs(d) + np.abs(z_values))

    return R_values, y_values, R_plane, z_values, r_base, X, Y, Z
