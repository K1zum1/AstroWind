import numpy as np
from coordinate_system import coordinate_system
from velocity_calculations import calculate_wind_velocity
from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle

R_values, y_values, R_plane, z_values = coordinate_system()
d = -5 * AU
vp_wi_l = calculate_wind_velocity(R_values, y_values, z_values)
m_dot_wi = calculate_mass_loss_rate(R_values, R_plane)
delta = calculate_angle(R_plane, z_values)
D_wi_l = get_source_point(y_values, z_values, d)

def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    return (m_dot_wi / (vp_wi_l * np.abs(np.cos(delta)))) * (d / (D_wi_l * np.cos(delta)))**2

density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)
density_flat = density.reshape(density.shape[0], -1)
np.savetxt("wind_density_output.csv", density_flat, delimiter=",")
