import numpy as np

def coordinate_system():
    x_values = np.linspace(0.1, 64, 65)
    y_values = np.linspace(0.1, 64, 65)
    R_values = np.sqrt(np.add.outer(x_values**2, y_values**2))
    return R_values
