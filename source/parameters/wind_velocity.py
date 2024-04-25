import numpy as np
from parameters import *
from coordinate_system import *

R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system()

def get_source_point(R_plane, z_values, d):
    D = np.sqrt(R_plane**2 + (np.abs(z_values) + np.abs(d))**2)
    return D

import numpy as np

def calculate_vp(d, GM_star, lmbda, r_base):
    factor = 2 * lmbda - 3
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")

    vp = (np.sqrt(factor) * np.sqrt(GM_star)) / np.sqrt(r_base)
    return vp

vp = calculate_vp(d, GM_star, lmbda, r_base)

output_path = "./setup/wind_output.csv"



vp_flat = vp.flatten()
np.savetxt(output_path, vp_flat, delimiter=',', header='Velocity', comments='')


shape = r_base.shape

with open("./dataset/velocity_output.csv", "w") as file:
    file.write("X (AU), Y (AU), Z (AU), r_base (AU)\n")
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                x_in_au = X[i, j, k] / AU
                y_in_au = Y[i, j, k] / AU
                z_in_au = Z[i, j, k] / AU
                r_base_in_au = r_base[i, j, k] / AU
                file.write(f"{x_in_au},{y_in_au},{z_in_au},{r_base_in_au}\n")
