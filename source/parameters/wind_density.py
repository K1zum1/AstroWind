import numpy as np
from astro_constants import AU
from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle
from wind_velocity import calculate_wind_velocity
from coordinate_system import coordinate_system, get_source_point

R_values, y_values, R_plane, z_values = coordinate_system()
m_dot_wi = calculate_mass_loss_rate(R_values, R_plane)
vp_wi_l = calculate_wind_velocity(R_values)
delta = calculate_angle(R_plane, z_values)
d = -5 * AU
D_wi_l = get_source_point(y_values)

def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    rho_wi_l = (m_dot_wi / (vp_wi_l * np.abs(np.cos(delta)))) * (d / (D_wi_l * np.cos(delta)))**2
    return rho_wi_l

wind_density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)

wind_density_flat = wind_density.reshape(wind_density.shape[0], -1)
np.savetxt("wind_density_output.csv", wind_density_flat, delimiter=",")
