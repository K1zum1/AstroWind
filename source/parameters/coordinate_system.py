import numpy as np
from astro_constants import AU

def coordinate_system():
    x_values = np.linspace(0.1, 64, 64) * AU  # Adjusted to 64 points for a 64x64x64 grid
    y_values = np.linspace(0.1, 64, 64) * AU
    z_values = np.linspace(0.1, 64, 64) * AU  # Added z_values for the third dimension
    X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing='ij')
    R_values = np.sqrt(X**2 + Y**2 + Z**2)
    return R_values, y_values

R_values, y_values = coordinate_system()

def get_source_point(y_values):
    d = -5 * AU
    D = y_values + d
    return D
