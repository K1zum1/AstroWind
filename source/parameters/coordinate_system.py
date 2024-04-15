import numpy as np
from astro_constants import AU

def coordinate_system():
    x_values = np.linspace(1, 65, 64) * AU  
    y_values = np.linspace(1, 65, 64) * AU
    z_values = np.linspace(1, 65, 64) * AU  

    X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing='ij')
    R_plane = np.sqrt(X**2 + Y**2)
    R_values = np.sqrt(X**2 + Y**2 + Z**2)

    return R_values, y_values, R_plane, z_values


