import numpy as np
from parameters import *
from coordinate_system import coordinate_system
from wind_velocity import calculate_vp, get_source_point
from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle

R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system()
vp_wi_l = calculate_vp(d, GM_star, lmbda, r_base)
m_dot_wi = calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k)
delta = calculate_angle(R_plane, z_values)
D_wi_l = get_source_point(R_plane, z_values, d)

def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    abs_cos_delta = np.abs(np.cos(delta))
    return (m_dot_wi / (vp_wi_l * abs_cos_delta)) * (np.abs(d) / (D_wi_l * abs_cos_delta))**2

density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)

density_flattened = density.flatten()

output_path_source = "./visualize/wind_density_output.csv"
output_path_setup = "./setup/wind_density_output.csv"

np.savetxt(output_path_source, density_flattened, delimiter=',', header='Density', comments='')
np.savetxt(output_path_setup, density_flattened, delimiter=',', header='Density', comments='')

shape = density.shape

with open("./dataset/check_density_values.csv", "w") as f:
    f.write("X (AU), Y (AU), Z (AU), Density (AU^-3)\n")  
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                x_in_au = X[i, j, k] / AU
                y_in_au = Y[i, j, k] / AU
                z_in_au = Z[i, j, k] / AU
                density_in_au3 = density[i, j, k] / AU
                f.write(f"{x_in_au},{y_in_au},{z_in_au},{density_in_au3}\n")
